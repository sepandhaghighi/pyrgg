# -*- coding: utf-8 -*-
"""Erdős-Rényi-Gilbert Engine module."""
import datetime
from random import random
from pyrgg.params import ENGINE_MENU, PYRGG_LOGGER_ERROR_MESSAGE

LOGGER_TEMPLATE = """{0}
Filename : {1}
Probability : {2}
Vertices : {3}
Total Edges : {4}
Directed : {5}
Engine : {6} ({7})
Elapsed Time : {8}
-------------------------------
"""


def edge_gen(n, p, direct):
    """
    Generate each vertex connection number.

    :param n: number of vertices
    :type n: int
    :param p: probability
    :type p: float
    :param direct: directed graph flag
    :type direct: bool
    :return: list of dicts
    """
    edge_dic = {}
    edge_number = 0
    weight_list = []
    for i in range(1, n + 1):
        edge_dic[i] = []
        temp_list = []
        dest_list = range(i + 1, n + 1)
        if direct:
            dest_list = [*range(1, i), *dest_list]
        for j in dest_list:
            temp_list.append(1)
            if random() < p:
                edge_dic[i].append(j)
                edge_number += 1
        weight_list.append(temp_list)
    return [edge_dic, dict(zip(range(1, n + 1), weight_list)), edge_number]


def gen_using(
        gen_function,
        file_name,
        input_dict):
    """
    Generate graph using given function based on Erdos Renyi Gilbert model.

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
        input_dict['probability'],
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
    Save generated graph logs for Erdős-Rényi-Gilbert engine.

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
                                          str(input_dict["probability"]),
                                          str(input_dict["vertices"]),
                                          str(input_dict["edge_number"]),
                                          str(bool(input_dict["direct"])),
                                          input_dict["engine"],
                                          ENGINE_MENU[input_dict["engine"]],
                                          elapsed_time))
    except Exception:
        print(PYRGG_LOGGER_ERROR_MESSAGE)
