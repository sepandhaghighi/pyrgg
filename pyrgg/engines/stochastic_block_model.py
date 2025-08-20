# -*- coding: utf-8 -*-
"""Stochastic Block Model Engine module."""
from random import random
from itertools import combinations
from pyrgg.params import ENGINE_MENU, PYRGG_LOGGER_ERROR_MESSAGE
from pyrgg.functions import save_log


def edge_gen(
        vertices,
        block_sizes,
        probability_matrix,
        direct,
        self_loop):
    """
    Generate each vertex connection number.

    :param vertices: number of vertices
    :type vertices: int
    :param block_sizes: block sizes
    :type block_sizes: list
    :param probability_matrix: probability matrix
    :type probability_matrix: list
    :param direct: directed graph flag
    :type direct: bool
    :param self_loop: self loop flag
    :type self_loop: bool
    :return: list of dicts
    """
    edge_number = 0
    edge_dict = {x: [] for x in range(1, vertices + 1)}
    weight_dict = {x: [] for x in range(1, vertices + 1)}
    vertices2blocks = {}
    for c, r in enumerate(block_sizes):
        n0 = len(vertices2blocks)
        vertices2blocks.update({i: c for i in range(n0 + 1, n0 + r + 1)})
    
    vertices_pairs = list(combinations(range(1, vertices + 1), 2))
    if direct:
        vertices_pairs += [(j, i) for i, j in vertices_pairs]
    if self_loop:
        vertices_pairs += [(i, i) for i in range(1, vertices + 1)]
    for v1, v2 in sorted(vertices_pairs):
        c1 = vertices2blocks[v1]
        c2 = vertices2blocks[v2]
        if random() < probability_matrix[c1][c2]:
            edge_dict[v1].append(v2)
            weight_dict[v1].append(1)
            edge_number += 1
    return [edge_dict, weight_dict, edge_number]
 

def gen_using(
        gen_function,
        file_name,
        input_dict):
    """
    Generate graph using given function based on Stochastic Block model.

    Refer to (https://en.wikipedia.org/wiki/Stochastic_block_model).

    :param gen_function: generation function
    :type gen_function: function object
    :param file_name: file name
    :type file_name: str
    :param input_dict: input data
    :type input_dict: dict
    :return: number of edges as int
    """
    edge_dict, weight_dict, edge_number = edge_gen(
        input_dict['vertices'],
        input_dict['block_sizes'],
        input_dict['probability_matrix'],
        input_dict['direct'],
        input_dict['self_loop'])
    gen_function(
        edge_dict,
        weight_dict,
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
    Save generated graph logs for Stochastic Block Model engine.

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
        text = "Vertices : {0}\n".format(input_dict['vertices'])
        text += "Total Edges : {0}\n".format(input_dict['edge_number'])
        text += "Block Sizes : {0}\n".format(input_dict['block_sizes'])
        text += "Probability Matrix : {0}\n".format(input_dict['probability_matrix'])
        text += "Directed : {0}\n".format(bool(input_dict['direct']))
        text += "Self Loop : {0}\n".format(bool(input_dict['self_loop']))
        text += "Engine : {0} ({1})\n".format(input_dict['engine'], ENGINE_MENU[input_dict['engine']])
        save_log(file, file_name, elapsed_time, text)
    except Exception:
        print(PYRGG_LOGGER_ERROR_MESSAGE)
