# -*- coding: utf-8 -*-
"""Complete Graph Engine module."""
from typing import List, Dict, Callable, Any, IO, Tuple
from pyrgg.params import ENGINE_MENU, PYRGG_LOGGER_ERROR_MESSAGE
from pyrgg.functions import is_weighted, get_min_max_weight, save_log


def generate_edges(n: int) -> Tuple[Dict[int, List[int]], Dict[int, List[float]], int]:
    """
    Generate each vertex connection number.

    :param n: number of vertices
    """
    edge_dict = {i: list(range(1, i)) for i in range(1, n + 1)}
    edge_number = n * (n - 1) // 2
    weight_dict = {i: [1] * (i - 1) for i in range(1, n + 1)}
    return edge_dict, weight_dict, edge_number


def generate_graph(
        gen_function: Callable,
        file_name: str,
        input_dict: Dict[str, Any]) -> int:
    """
    Generate a complete graph using given function.

    Refer to (https://en.wikipedia.org/wiki/Complete_graph).

    :param gen_function: generation function
    :param file_name: file name
    :param input_dict: input data
    """
    edge_dict, weight_dict, edge_number = generate_edges(input_dict['vertices'])
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
    Save generated graph logs for the Complete Graph engine.

    :param file: file to write log into
    :param file_name: file name
    :param elapsed_time: elapsed time
    :param input_dict: input data
    """
    try:
        text = "Vertices : {0}\n".format(input_dict['vertices'])
        text += "Total Edges : {0}\n".format(input_dict['edge_number'])
        text += "Engine : {0} ({1})\n".format(input_dict['engine'], ENGINE_MENU[input_dict['engine']])
        save_log(file, file_name, elapsed_time, text)
    except Exception:
        print(PYRGG_LOGGER_ERROR_MESSAGE)
