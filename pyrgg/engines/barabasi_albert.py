# -*- coding: utf-8 -*-
"""Barabási-Albert Engine module."""
from typing import List, Dict, Callable, Any, IO, Tuple
from random import sample
from pyrgg.params import ENGINE_MENU, PYRGG_LOGGER_ERROR_MESSAGE
from pyrgg.functions import save_log


def edge_gen(n: int, k: int) -> Tuple[Dict[int, List[int]], Dict[int, List[float]], int]:
    """
    Generate each vertex connection number.

    :param n: number of vertices
    :param k: number of edges to attach to a new node in each iteration, m in the Barabási-Albert model
    """
    # We assume m0 is the same as k, similar to the original paper examples
    edge_dict = {i: [] for i in range(1, k + 1)}
    weight_dict = {i: [] for i in range(1, k + 1)}
    node_from = k + 1
    node_to = list(range(1, k + 1))
    nodes_history = []
    while node_from <= n:
        edge_dict[node_from] = [i for i in node_to]
        weight_dict[node_from] = [1] * k
        nodes_history.extend(node_to)
        nodes_history.extend([node_from] * k)
        node_to = sample(nodes_history, k)
        node_from += 1

    return [edge_dict, weight_dict, (n - k) * k]


def gen_using(
        gen_function: Callable,
        file_name: str,
        input_dict: Dict[str, Any]) -> int:
    """
    Generate graph using given function based on Barabási-Albert model and return number of edges.

    Refer to (https://en.wikipedia.org/wiki/Barab%C3%A1si%E2%80%93Albert_model).
    We assume that m0 is the same as k and k is the number of edges to attach to a new node.

    :param gen_function: generation function
    :param file_name: file name
    :param input_dict: input data
    """
    edge_dict, weight_dict, edge_number = edge_gen(
        input_dict['vertices'],
        input_dict['attaching_edge_number'])
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
            "direct": False,
            "multigraph": True,
        })
    return edge_number


def logger(file: IO, file_name: str, elapsed_time: str, input_dict: Dict[str, Any]) -> None:
    """
    Save generated graph logs for Barabási-Albert engine.

    :param file: file to write log into
    :param file_name: file name
    :param elapsed_time: elapsed time
    :param input_dict: input data
    """
    try:
        text = "Vertices : {vertices}\n".format(vertices=input_dict['vertices'])
        text += "Edges to Attach to a New Node : {attaching_edge_number}\n".format(
            attaching_edge_number=input_dict['attaching_edge_number'])
        text += "Total Edges : {edge_number}\n".format(edge_number=input_dict['edge_number'])
        text += "Engine : {engine_index} ({engine_name})\n".format(
            engine_index=input_dict['engine'], engine_name=ENGINE_MENU[input_dict['engine']])
        save_log(file, file_name, elapsed_time, text)
    except Exception:
        print(PYRGG_LOGGER_ERROR_MESSAGE)
