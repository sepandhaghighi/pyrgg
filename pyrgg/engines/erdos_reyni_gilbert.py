# -*- coding: utf-8 -*-
"""Erdős-Rényi-Gilbert Engine module."""
import datetime
from random import random
from pyrgg.params import ENGINE_MENU

LOGGER_TEMPLATE = """{0}
Filename : {1}
Probability : {2}
Vertices : {3}
Total Edges : {4}
Engine : {5} ({6})
Elapsed Time : {7}
-------------------------------
"""


def edge_gen(n, p):
    """
    Generate each vertex connection number.

    :param n: number of vertices
    :type n: int
    :param p: probability
    :type p: float
    :return: list of dicts
    """
    edge_dic = {}
    edge_number = 0
    for i in range(1, n + 1):
        edge_dic[i] = []
        for j in range(i + 1, n + 1):
            if random() < p:
                edge_dic[i].append(j)
                edge_number += 1
    return edge_dic, edge_number


def gen_using(
        gen_function,
        file_name,
        input_dict):
    """
    Generate graph using given function based on Erdos Renyi Gilbert model.

    Refer to (https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model)

    :param gen_function: generation function
    :type gen_function: function object
    :param file_name: file name
    :type file_name: str
    :param input_dict: input data
    :type input_dict: dict
    :return: number of edges as int
    """
    edge_dic, edge_number = edge_gen(
        input_dict['vertices'],
        input_dict['probability'])
    weight_dic = {key: [1] * edge_number for key in range(1, input_dict['vertices'] + 1)}
    gen_function(
        edge_dic,
        weight_dic,
        {
            "file_name": file_name,
            "vertices_number": input_dict['vertices'],
            "max_weight": 1,
            "min_weight": 1,
            "min_edge": edge_number,
            "max_edge": edge_number,
            "sign": False,
            "direct": False,
            "self_loop": False,
            "multigraph": False,
            "edge_number": edge_number,
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
    file.write(LOGGER_TEMPLATE.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                      file_name,
                                      str(input_dict["probability"]),
                                      str(input_dict["vertices"]),
                                      str(input_dict["edge_number"]),
                                      input_dict["engine"],
                                      ENGINE_MENU[input_dict["engine"]],
                                      elapsed_time))
