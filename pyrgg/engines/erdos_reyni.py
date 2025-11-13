# -*- coding: utf-8 -*-
"""Erdős-Rényi Engine module."""
from typing import List, Dict, Callable, Any, IO, Tuple
from random import shuffle
from pyrgg.params import ENGINE_MENU, PYRGG_LOGGER_ERROR_MESSAGE
from pyrgg.functions import save_log


def edge_gen(n: int, m: int, direct: bool) -> Tuple[Dict[int, List[int]], Dict[int, List[float]], int]:
    """
    Generate each vertex connection number.

    :param n: number of vertices
    :param m: number of edges
    :param direct: directed graph flag
    """
    edge_dict = {}
    weight_list = []
    edge_mold = []
    max_edges = (n * (n - 1)) // 2
    if direct:
        max_edges *= 2
    m = min(m, max_edges)
    edge_mold = m * [1] + (max_edges - m) * [0]
    shuffle(edge_mold)
    for i in range(1, n + 1):
        edge_dict[i] = []
        temp_list = []
        dest_list = range(i + 1, n + 1)
        if direct:
            dest_list = [*range(1, i), *dest_list]
        for j in dest_list:
            if edge_mold.pop() == 1:
                temp_list.append(1)
                edge_dict[i].append(j)
        weight_list.append(temp_list)
    return [edge_dict, dict(zip(range(1, n + 1), weight_list)), m]


def gen_using(
        gen_function: Callable,
        file_name: str,
        input_dict: Dict[str, Any]) -> int:
    """
    Generate graph using given function based on Erdos Renyi - G(n, m) model and return the number of edges.

    Refer to (https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model).

    :param gen_function: generation function
    :param file_name: file name
    :param input_dict: input data
    """
    edge_dict, weight_dict, edge_number = edge_gen(
        input_dict['vertices'],
        input_dict['edge_number'],
        input_dict['direct'])
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
    Save generated graph logs for Erdős-Rényi engine.

    :param file: file to write log into
    :param file_name: file name
    :param elapsed_time: elapsed time
    :param input_dict: input data
    """
    try:
        text = "Vertices : {vertices}\n".format(vertices=input_dict['vertices'])
        text += "Total Edges : {edge_number}\n".format(edge_number=input_dict['edge_number'])
        text += "Directed : {is_directed}\n".format(is_directed=bool(input_dict['direct']))
        text += "Engine : {engine_index} ({engine_name})\n".format(
            engine_index=input_dict['engine'], engine_name=ENGINE_MENU[input_dict['engine']])
        save_log(file, file_name, elapsed_time, text)
    except Exception:
        print(PYRGG_LOGGER_ERROR_MESSAGE)
