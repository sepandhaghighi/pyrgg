# -*- coding: utf-8 -*-
"""Random Geometric Graph Engine module."""
from typing import List, Dict, Callable, Any, IO, Tuple
from math import sqrt
from random import random
from pyrgg.params import ENGINE_MENU, PYRGG_LOGGER_ERROR_MESSAGE
from pyrgg.functions import is_weighted, get_min_max_weight, save_log


WEIGHT_DIGIT_PRECISION = 5


def generate_edges(n: int, d: int, r: float) -> Tuple[Dict[int, List[int]], Dict[int, List[float]], int]:
    """
    Generate each vertex connection number.

    :param n: number of vertices
    :param d: space dimension
    :param r: cutoff threshold for the existence of an edge
    """
    edge_dict = {}
    edge_number = 0
    weight_dict = {}
    points = [[random() for _ in range(d)] for _ in range(n)]
    for i in range(1, n + 1):
        edge_dict[i] = []
        weight_dict[i] = []
        for j in range(i + 1, n + 1):
            pi, pj = points[i - 1], points[j - 1]
            distance = sqrt(sum([(x - y)**2 for x, y in zip(pi, pj)]))
            if distance < r:
                edge_dict[i].append(j)
                weight_dict[i].append(round(distance, WEIGHT_DIGIT_PRECISION))
                edge_number += 1
    return edge_dict, weight_dict, edge_number


def generate_graph(
        gen_function: Callable,
        file_name: str,
        input_dict: Dict[str, Any]) -> int:
    """
    Generate graph using given function based on Random Geometric model and return the number of edges.

    Refer to (https://en.wikipedia.org/wiki/Random_geometric_graph).

    :param gen_function: generation function
    :param file_name: file name
    :param input_dict: input data
    """
    edge_dict, weight_dict, edge_number = generate_edges(
        input_dict['vertices'],
        input_dict['space_dimension'],
        input_dict['cutoff_threshold'])
    min_weight, max_weight = get_min_max_weight(weight_dict)
    weighted = is_weighted(max_weight, min_weight, False)
    gen_function(
        edge_dict,
        weight_dict,
        {
            "file_name": file_name,
            "vertices_number": input_dict['vertices'],
            "edge_number": edge_number,
            "weighted": weighted,
            "max_weight": max_weight,
            "min_weight": min_weight,
            "direct": False,
            "multigraph": False,
        })
    return edge_number


def logger(file: IO, file_name: str, elapsed_time: str, input_dict: Dict[str, Any]) -> None:
    """
    Save generated graph logs for Random Geometric Graph engine.

    :param file: file to write log into
    :param file_name: file name
    :param elapsed_time: elapsed time
    :param input_dict: input data
    """
    try:
        text = "Vertices : {0}\n".format(input_dict['vertices'])
        text += "Space Dimension : {0}\n".format(input_dict['space_dimension'])
        text += "Cutoff Threshold : {0}\n".format(input_dict['cutoff_threshold'])
        text += "Total Edges : {0}\n".format(input_dict['edge_number'])
        text += "Engine : {0} ({1})\n".format(input_dict['engine'], ENGINE_MENU[input_dict['engine']])
        save_log(file, file_name, elapsed_time, text)
    except Exception:
        print(PYRGG_LOGGER_ERROR_MESSAGE)
