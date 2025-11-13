# -*- coding: utf-8 -*-
"""PyRGG Engine module."""
from typing import List, Dict, Callable, Any, IO, Tuple
import os
from random import randint, uniform, choice
from pyrgg.params import ENGINE_MENU, PYRGG_LOGGER_ERROR_MESSAGE
from pyrgg.functions import is_weighted, get_precision, calculate_threshold
from pyrgg.functions import get_min_max_weight, is_multigraph
from pyrgg.functions import save_log


def branch_gen(
        vertex_index: int,
        max_edges: int,
        min_edges: int,
        min_weight: float,
        max_weight: float,
        precision: int,
        sign: bool,
        direct: bool,
        self_loop: bool,
        multigraph: bool,
        used_vertices: Dict[int, List[int]],
        degree_dict: Dict[int, int],
        degree_sort_dict: Dict[int, List[int]]) -> Tuple[List[int], List[float]]:
    """
    Generate branch and weight vector of each vertex.

    :param vertex_index: origin vertex index
    :param max_edges: maximum number of edges (connected to each vertex)
    :param min_edges: minimum number of edges (connected to each vertex)
    :param min_weight: weight min range
    :param max_weight: weight max range
    :param precision: numbers precision
    :param sign: weight sign flag
    :param direct: directed and undirected graph flag
    :param self_loop: self loop flag
    :param multigraph: multigraph flag
    :param used_vertices: used vertices dictionary
    :param degree_dict: all vertices degree
    :param degree_sort_dict: degree to vertices list
    """
    index = 0
    branch_list = []
    weight_list = []
    reference_vertices = []
    random_unit = randint
    vertex_degree = degree_dict[vertex_index]
    if vertex_degree >= max_edges:
        return [branch_list, weight_list]
    threshold = calculate_threshold(
        min_edges=min_edges,
        max_edges=max_edges,
        vertex_degree=vertex_degree)
    for i in range(max_edges + 1):
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
        if vertex_degree >= max_edges:
            break
        if len(reference_vertices) == 0:
            break
        random_tail_index = choice(
            range(len(reference_vertices)))
        random_tail = reference_vertices[random_tail_index]
        random_tail_degree = degree_dict[random_tail]
        if random_tail_degree >= max_edges or (
            random_tail == vertex_index and random_tail_degree >= (
                max_edges - 1)):
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
        vertices_number: int,
        min_weight: float,
        max_weight: float,
        min_edges: int,
        max_edges: int,
        sign: bool,
        direct: bool,
        self_loop: bool,
        multigraph: bool) -> Tuple[Dict[int, List[int]], Dict[int, List[float]], int]:
    """
    Generate each vertex connection number.

    :param vertices_number: number of vertices
    :param min_weight: weight min range
    :param max_weight: weight max range
    :param min_edges: minimum number of edges (connected to each vertex)
    :param max_edges: maximum number of edges (connected to each vertex)
    :param sign: weight sign flag
    :param direct: directed and undirected graph flag
    :param self_loop: self loop flag
    :param multigraph: multigraph flag
    """
    precision = max(
        get_precision(max_weight),
        get_precision(min_weight))
    temp = 0
    vertices_id = list(range(1, vertices_number + 1))
    vertices_edge = []
    weight_list = []
    used_vertices = {}
    degree_sort_dict = {i: {} for i in range(max_edges + 1)}
    degree_dict = {}
    for i in vertices_id:
        degree_dict[i] = 0
        degree_sort_dict[0][i] = i
    branch_gen_params = {
        "max_edges": max_edges,
        "min_edges": min_edges,
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
        gen_function: Callable,
        file_name: str,
        input_dict: Dict[str, Any]) -> int:
    """
    Generate graph using given function based on PyRGG model and return the number of edges.

    :param gen_function: generation function
    :param file_name: file name
    :param input_dict: input data
    """
    edge_dict, weight_dict, edge_number = edge_gen(
        input_dict['vertices'],
        input_dict['min_weight'],
        input_dict['max_weight'],
        input_dict['min_edges'],
        input_dict['max_edges'],
        input_dict['sign'],
        input_dict['direct'],
        input_dict['self_loop'],
        input_dict['multigraph'])
    min_weight, max_weight = get_min_max_weight(weight_dict)
    weighted = is_weighted(max_weight, min_weight, bool(input_dict['sign']))
    gen_function(
        edge_dict,
        weight_dict,
        {
            "file_name": file_name,
            "vertices_number": input_dict['vertices'],
            "weighted": weighted,
            "edge_number": edge_number,
            "min_weight": min_weight,
            "max_weight": max_weight,
            "direct": input_dict['direct'],
            "multigraph": is_multigraph(edge_dict),
        })
    return edge_number


def logger(file: IO, file_name: str, elapsed_time: str, input_dict: Dict[str, Any]) -> None:
    """
    Save generated graph logs for PyRGG engine.

    :param file: file to write log into
    :param file_name: file name
    :param elapsed_time: elapsed time
    :param input_dict: input data
    """
    try:
        text = "Vertices : {vertices}\n".format(vertices=input_dict['vertices'])
        text += "Total Edges : {edge_number}\n".format(edge_number=input_dict['edge_number'])
        text += "Max Edges : {max_edges}\n".format(max_edges=input_dict['max_edges'])
        text += "Min Edges : {min_edges}\n".format(min_edges=input_dict['min_edges'])
        text += "Directed : {is_directed}\n".format(is_directed=bool(input_dict['direct']))
        text += "Signed : {is_signed}\n".format(is_signed=bool(input_dict['sign']))
        text += "Multigraph : {is_multigraph}\n".format(is_multigraph=bool(input_dict['multigraph']))
        text += "Self Loop : {has_self_loop}\n".format(has_self_loop=bool(input_dict['self_loop']))
        text += "Weighted : {is_weighted}\n".format(
            is_weighted=is_weighted(input_dict['max_weight'], input_dict['min_weight'], bool(input_dict['sign'])))
        text += "Max Weight : {max_weight}\n".format(max_weight=input_dict['max_weight'])
        text += "Min Weight : {min_weight}\n".format(min_weight=input_dict['min_weight'])
        text += "Engine : {engine_index} ({engine_name})\n".format(
            engine_index=input_dict['engine'], engine_name=ENGINE_MENU[input_dict['engine']])
        save_log(file, file_name, elapsed_time, text)
    except Exception:
        print(PYRGG_LOGGER_ERROR_MESSAGE)
