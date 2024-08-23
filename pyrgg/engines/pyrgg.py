# -*- coding: utf-8 -*-
"""PyRGG Engine module."""
import datetime
import os
from random import randint, uniform, choice
from pyrgg.params import ENGINE_MENU, PYRGG_LOGGER_ERROR_MESSAGE
from pyrgg.functions import is_weighted, get_precision, threshold_calc
from pyrgg.functions import get_min_max_weight, is_multigraph

LOGGER_TEMPLATE = """{0}
Filename : {1}
Vertices : {2}
Total Edges : {3}
Max Edge : {4}
Min Edge : {5}
Directed : {6}
Signed : {7}
Multigraph : {8}
Self Loop : {9}
Weighted : {10}
Max Weight : {11}
Min Weight : {12}
Engine : {13} ({14})
Elapsed Time : {15}
-------------------------------
"""


def branch_gen(
        vertex_index,
        max_edge,
        min_edge,
        min_weight,
        max_weight,
        precision,
        sign,
        direct,
        self_loop,
        multigraph,
        used_vertices,
        degree_dict,
        degree_sort_dict):
    """
    Generate branch and weight vector of each vertex.

    :param vertex_index: origin vertex index
    :type vertex_index: int
    :param max_edge: maximum number of edges (connected to each vertex)
    :type max_edge: int
    :param min_edge: minimum number of edges (connected to each vertex)
    :type min_edge: int
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param precision: numbers precision
    :type precision: int
    :param sign: weight sign flag
    :type sign: bool
    :param direct: directed and undirected graph flag
    :type direct: bool
    :param self_loop: self loop flag
    :type self_loop: bool
    :param multigraph: multigraph flag
    :type multigraph: bool
    :param used_vertices: used vertices dictionary
    :type used_vertices: dict
    :param degree_dict: all vertices degree
    :type degree_dict: dict
    :param degree_sort_dict: degree to vertices list
    :type degree_sort_dict: dict
    :return: branch and weight list
    """
    index = 0
    branch_list = []
    weight_list = []
    reference_vertices = []
    random_unit = randint
    vertex_degree = degree_dict[vertex_index]
    if vertex_degree >= max_edge:
        return [branch_list, weight_list]
    threshold = threshold_calc(
        min_edge=min_edge,
        max_edge=max_edge,
        vertex_degree=vertex_degree)
    for i in range(max_edge + 1):
        reference_vertices.extend(list(degree_sort_dict[i].values()))
        if len(reference_vertices) >= threshold:
            break
    if precision > 0:
        random_unit = uniform
    if not direct and (
            vertex_index in used_vertices) and not multigraph:
        reference_vertices = list(
            set(reference_vertices) - set(used_vertices[vertex_index]))
    if not self_loop and vertex_index in reference_vertices:
        reference_vertices.remove(vertex_index)
    if int(os.environ.get("PYRGG_TEST_MODE", 0)):
        reference_vertices.sort()
    while (index < threshold):
        vertex_degree = degree_dict[vertex_index]
        if vertex_degree >= max_edge:
            break
        if len(reference_vertices) == 0:
            break
        random_tail_index = choice(
            range(len(reference_vertices)))
        random_tail = reference_vertices[random_tail_index]
        random_tail_degree = degree_dict[random_tail]
        if random_tail_degree >= max_edge or (
            random_tail == vertex_index and random_tail_degree >= (
                max_edge - 1)):
            reference_vertices.pop(random_tail_index)
            continue
        if not direct:
            try:
                used_vertices[random_tail].append(vertex_index)
            except KeyError:
                used_vertices[random_tail] = [vertex_index]
        weight_sign = 1
        if sign:
            weight_sign = choice([1, -1])
        random_weight = weight_sign * random_unit(min_weight, max_weight)
        random_weight = round(random_weight, precision)
        branch_list.append(random_tail)
        weight_list.append(random_weight)
        index += 1
        del degree_sort_dict[vertex_degree][vertex_index]
        degree_dict[random_tail] += 1
        degree_dict[vertex_index] += 1
        degree_sort_dict[degree_dict[vertex_index]
                         ][vertex_index] = vertex_index
        if random_tail != vertex_index:
            del degree_sort_dict[random_tail_degree][random_tail]
            degree_sort_dict[degree_dict[random_tail]
                             ][random_tail] = random_tail
        if not multigraph:
            reference_vertices.pop(random_tail_index)
    return [branch_list, weight_list]


def edge_gen(
        vertices_number,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph):
    """
    Generate each vertex connection number.

    :param vertices_number: number of vertices
    :type vertices_number: int
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param min_edge: minimum number of edges (connected to each vertex)
    :type min_edge: int
    :param max_edge: maximum number of edges (connected to each vertex)
    :type max_edge: int
    :param sign: weight sign flag
    :type sign: bool
    :param direct: directed and undirected graph flag
    :type direct: bool
    :param self_loop: self loop flag
    :type self_loop: bool
    :param multigraph: multigraph flag
    :type multigraph: bool
    :return: list of dicts
    """
    precision = max(
        get_precision(max_weight),
        get_precision(min_weight))
    temp = 0
    vertices_id = list(range(1, vertices_number + 1))
    vertices_edge = []
    weight_list = []
    used_vertices = {}
    degree_sort_dict = {i: {} for i in range(max_edge + 1)}
    degree_dict = {}
    for i in vertices_id:
        degree_dict[i] = 0
        degree_sort_dict[0][i] = i
    branch_gen_params = {
        "max_edge": max_edge,
        "min_edge": min_edge,
        "min_weight": min_weight,
        "max_weight": max_weight,
        "sign": sign,
        "direct": direct,
        "self_loop": self_loop,
        "multigraph": multigraph,
        "used_vertices": used_vertices,
        "degree_dict": degree_dict,
        "degree_sort_dict": degree_sort_dict,
        "precision": precision}
    for i in vertices_id:
        temp_list = branch_gen(vertex_index=i, **branch_gen_params)
        vertices_edge.append(temp_list[0])
        weight_list.append(temp_list[1])
        temp = temp + len(temp_list[0])
    return [dict(zip(vertices_id, vertices_edge)),
            dict(zip(vertices_id, weight_list)), temp]


def gen_using(
        gen_function,
        file_name,
        input_dict):
    """
    Generate graph using given function based on PyRGG model.

    :param gen_function: generation function
    :type gen_function: function object
    :param file_name: file name
    :type file_name: str
    :param input_dict: input data
    :type input_dict: dict
    :return: number of edges as int
    """
    edge_dic, weight_dic, edge_number = edge_gen(
        input_dict['vertices'],
        input_dict['min_weight'],
        input_dict['max_weight'],
        input_dict['min_edge'],
        input_dict['max_edge'],
        input_dict['sign'],
        input_dict['direct'],
        input_dict['self_loop'],
        input_dict['multigraph'])
    min_weight, max_weight = get_min_max_weight(weight_dic)
    weighted = is_weighted(max_weight, min_weight, bool(input_dict['sign']))
    gen_function(
        edge_dic,
        weight_dic,
        {
            "file_name": file_name,
            "vertices_number": input_dict['vertices'],
            "weighted": weighted,
            "edge_number": edge_number,
            "min_weight": min_weight,
            "max_weight": max_weight,
            "direct": input_dict['direct'],
            "multigraph": is_multigraph(edge_dic),
        })
    return edge_number


def logger(file, file_name, elapsed_time, input_dict):
    """
    Save generated graph logs for PyRGG engine.

    :param file: file to write log into
    :type file: file object
    :param file_name: file name
    :type file_name: str
    :param elapsed_time: elapsed time
    :type elapsed_time: str
    :param input_dict: input data
    :type input_dict: dict
    :return: None
    """
    try:
        file.write(LOGGER_TEMPLATE.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                          file_name,
                                          str(input_dict["vertices"]),
                                          str(input_dict["edge_number"]),
                                          str(input_dict["max_edge"]),
                                          str(input_dict["min_edge"]),
                                          str(bool(input_dict["direct"])),
                                          str(bool(input_dict["sign"])),
                                          str(bool(input_dict["multigraph"])),
                                          str(bool(input_dict["self_loop"])),
                                          str(is_weighted(input_dict["max_weight"],
                                                          input_dict["min_weight"],
                                                          bool(input_dict["sign"]))),
                                          str(input_dict["max_weight"]),
                                          str(input_dict["min_weight"]),
                                          input_dict["engine"],
                                          ENGINE_MENU[input_dict["engine"]],
                                          elapsed_time))
    except Exception:
        print(PYRGG_LOGGER_ERROR_MESSAGE)
