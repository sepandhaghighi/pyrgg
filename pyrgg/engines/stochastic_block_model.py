# -*- coding: utf-8 -*-
"""Stochastic Block Model Engine module."""
from typing import List, Dict, Callable, Any, IO, Tuple
from random import random
from itertools import combinations
from pyrgg.params import ENGINE_MENU, PYRGG_LOGGER_ERROR_MESSAGE
from pyrgg.functions import save_log


def generate_edges(
        vertices: int,
        block_sizes: List[int],
        probability_matrix: List[List[float]],
        direct: bool,
        self_loop: bool) -> Tuple[Dict[int, List[int]], Dict[int, List[float]], int]:
    """
    Generate each vertex connection number.

    :param vertices: number of vertices
    :param block_sizes: block sizes
    :param probability_matrix: probability matrix
    :param direct: directed graph flag
    :param self_loop: self loop flag
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


def generate_graph(
        gen_function: Callable,
        file_name: str,
        input_dict: Dict[str, Any]) -> int:
    """
    Generate graph using given function based on Stochastic Block model and return the number of edges.

    Refer to (https://en.wikipedia.org/wiki/Stochastic_block_model).

    :param gen_function: generation function
    :param file_name: file name
    :param input_dict: input data
    """
    edge_dict, weight_dict, edge_number = generate_edges(
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


def logger(file: IO, file_name: str, elapsed_time: str, input_dict: Dict[str, Any]) -> None:
    """
    Save generated graph logs for Stochastic Block Model engine.

    :param file: file to write log into
    :param file_name: file name
    :param elapsed_time: elapsed time
    :param input_dict: input data
    """
    try:
        text = "Vertices : {vertices}\n".format(vertices=input_dict['vertices'])
        text += "Total Edges : {edge_number}\n".format(edge_number=input_dict['edge_number'])
        text += "Block Sizes : {block_sizes}\n".format(block_sizes=input_dict['block_sizes'])
        text += "Probability Matrix : {probability_matrix}\n".format(
            probability_matrix=input_dict['probability_matrix'])
        text += "Directed : {is_directed}\n".format(is_directed=bool(input_dict['direct']))
        text += "Self Loop : {has_self_loop}\n".format(has_self_loop=bool(input_dict['self_loop']))
        text += "Engine : {engine_index} ({engine_name})\n".format(
            engine_index=input_dict['engine'], engine_name=ENGINE_MENU[input_dict['engine']])
        save_log(file, file_name, elapsed_time, text)
    except Exception:
        print(PYRGG_LOGGER_ERROR_MESSAGE)
