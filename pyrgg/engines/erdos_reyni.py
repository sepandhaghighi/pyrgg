# -*- coding: utf-8 -*-
"""Erdős-Rényi Engine module."""
import datetime
from random import shuffle
from math import comb
from itertools import permutations
from pyrgg.params import ENGINE_MENU, PYRGG_LOGGER_ERROR_MESSAGE

LOGGER_TEMPLATE = """{0}
Filename : {1}
Vertices : {2}
Total Edges : {3}
Directed : {4}
Engine : {5} ({6})
Elapsed Time : {7}
-------------------------------
"""


def edge_gen(n, m, direct):
    """
    Generate each vertex connection number.

    :param n: number of vertices
    :type n: int
    :param m: number of edges
    :type m: int
    :param direct: directed graph flag
    :type direct: bool
    :return: list of dicts
    """
    edge_dic = {}
    weight_list = []
    edge_mold = []
    if direct:
        m = min(m, 2 * comb(n, 2))
        edge_mold = m * [1] + (2 * comb(n, 2) - m) * [0]
    else:
        m = min(m, comb(n, 2))
        edge_mold = m * [1] + (comb(n, 2) - m) * [0]
    shuffle(edge_mold)
    for i in range(1, n + 1):
        edge_dic[i] = []
        temp_list = []
        dest_list = range(i + 1, n + 1)
        if direct:
            dest_list = [*range(1, i), *dest_list]
        for j in dest_list:
            if edge_mold.pop() == 1:
                temp_list.append(1)
                edge_dic[i].append(j)
        weight_list.append(temp_list)
    return [edge_dic, dict(zip(range(1, n + 1), weight_list)), m]


def gen_using(
        gen_function,
        file_name,
        input_dict):
    """
    Generate graph using given function based on Erdos Renyi - G(n, m) model.

    Refer to (https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model).

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
        input_dict['edge_number'],
        input_dict['direct'])
    gen_function(
        edge_dic,
        weight_dic,
        {
            "file_name": file_name,
            "vertices_number": input_dict['vertices'],
            "edge_number": edge_number,
            "weighted": False,
            "max_weight": 1,
            "min_weight": 1,
            "direct": input_dict['direct'],
            "multigraph": False,
        })
    return edge_number


def logger(file, file_name, elapsed_time, input_dict):
    """
    Save generated graph logs for Erdős-Rényi engine.

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
                                          str(bool(input_dict["direct"])),
                                          input_dict["engine"],
                                          ENGINE_MENU[input_dict["engine"]],
                                          elapsed_time))
    except Exception:
        print(PYRGG_LOGGER_ERROR_MESSAGE)
