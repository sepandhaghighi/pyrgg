# -*- coding: utf-8 -*-
"""Labeled Tree Generator Engine module."""
from typing import List, Dict, Callable, Any, IO, Tuple
from random import choice
from pyrgg.params import ENGINE_MENU, PYRGG_LOGGER_ERROR_MESSAGE
from pyrgg.functions import save_log


def generate_edges(n: int) -> Tuple[Dict[int, List[int]], Dict[int, List[float]], int]:
    """
    Generate each vertex connection number.

    :param n: number of vertices
    """
    prufer_seq = [choice(range(1, n + 1)) for _ in range(n - 2)]
    edge_number = 0
    _edge_dict = {x: [] for x in range(1, n + 1)}
    # degree initialization:
    degree_dict = {x: 1 for x in range(1, n + 1)}
    for i in prufer_seq:
        degree_dict[i] += 1
    # tree construction:
    for i in prufer_seq:
        for j in range(1, n + 1):
            if degree_dict[j] == 1:
                edge_number += 1
                _edge_dict[i].append(j)
                degree_dict[i] -= 1
                degree_dict[j] -= 1
                break
    # adding final edges:
    u, v = None, None
    for i in range(1, n + 1):
        if degree_dict[i] == 1:
            if u is None:
                u = i
            else:
                v = i
                break
    edge_number += 1
    _edge_dict[u].append(v)
    degree_dict[u] -= 1
    degree_dict[v] -= 1
    assert edge_number == n - 1
    # refine the graph
    edge_dict = {x: [] for x in range(1, n + 1)}
    weight_dict = {x: [] for x in range(1, n + 1)}
    for i in range(1, n + 1):
        for j in _edge_dict[i]:
            if i < j:
                edge_dict[i].append(j)
                weight_dict[i].append(1)
            else:
                edge_dict[j].append(i)
                weight_dict[j].append(1)
    edge_dict = {x: sorted(y) for x, y in edge_dict.items()}
    return [edge_dict, weight_dict, edge_number]


def generate_graph(
        gen_function: Callable,
        file_name: str,
        input_dict: Dict[str, Any]) -> int:
    """
    Generate a labeled tree using Prüfer sequence and return the number of edges.

    Refer to (https://en.wikipedia.org/wiki/Pr%C3%BCfer_sequence).

    :param gen_function: graph generator function
    :param file_name: file name
    :param input_dict: input data
    """
    edge_dict, weight_dict, edge_number = generate_edges(
        input_dict['vertices'])
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
            "multigraph": False,
        })
    return edge_number


def logger(file: IO, file_name: str, elapsed_time: str, input_dict: Dict[str, Any]) -> None:
    """
    Save generated tree logs.

    :param file: file to write log into
    :param file_name: file name
    :param elapsed_time: elapsed time
    :param input_dict: input data
    """
    try:
        text = "Vertices : {vertices}\n".format(vertices=input_dict['vertices'])
        text += "Total Edges : {edge_number}\n".format(edge_number=input_dict['edge_number'])
        text += "Engine : {engine_index} ({engine_name})\n".format(
            engine_index=input_dict['engine'], engine_name=ENGINE_MENU[input_dict['engine']])
        save_log(file, file_name, elapsed_time, text)
    except Exception:
        print(PYRGG_LOGGER_ERROR_MESSAGE)
