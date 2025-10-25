# -*- coding: utf-8 -*-
"""Watts-Strogatz Engine module."""
from random import random, choice
from pyrgg.params import ENGINE_MENU, PYRGG_LOGGER_ERROR_MESSAGE
from pyrgg.functions import save_log


def _rot_idx(i, n):
    """
    Wrap around indices in a ring.

    :param i: node index
    :param n: total number of nodes
    :return: wrapped index
    """
    return (i - 1) % n + 1


def _get_neighbors(i, k, n):
    """
    Return k neighbors of node i in a ring lattice.

    :param i: node index
    :param k: number of neighbors in each side
    :param n: total number of nodes
    :return: list of neighbor indices
    """
    return [_rot_idx(i + j, n) for j in range(-k // 2, k // 2 + 1) if j != 0]


def edge_gen(n, k, beta):
    """
    Generate each vertex connection number.

    :param n: number of vertices
    :type n: int
    :param k: mean degree (should be a positive even number)
    :type k: int
    :param beta: rewiring probability (0 <= beta <= 1)
    :type beta: float
    :return: list of dicts
    """
    if n <= k:
        return {i: [j for j in range(i + 1, n + 1)] for i in range(1, n + 1)}, \
               {i: [1] * (n - i) for i in range(1, n + 1)}, \
                n * (n - 1) // 2

    lattice_edge_dict = {i: [] for i in range(1, n + 1)}
    weight_dict = {i: [] for i in range(1, n + 1)}
    edge_number = 0

    # Create ring lattice (n, k)
    for i in range(1, n + 1):
        neighbors = [j for j in _get_neighbors(i, k, n) if i not in lattice_edge_dict[j]]
        lattice_edge_dict[i].extend(neighbors)
        weight_dict[i].extend([1] * len(neighbors))
        edge_number += len(neighbors)

    # Rewire edges
    edge_dict = {i: [] for i in range(1, n + 1)}
    for i in range(1, n + 1):
        for j in lattice_edge_dict[i]:
            node_to = j
            if i < j <= _rot_idx(i + k // 2, n) and random() < beta:
                candidates = [x for x in range(1, n + 1)
                              if x != i and # no self-loops
                              x not in edge_dict[i] and i not in edge_dict[x] and # no duplicate edges
                              x not in [y for y in lattice_edge_dict[i] if j <= y]] # no original neighbors
                node_to = choice(candidates)
            edge_dict[i].append(node_to)
    return edge_dict, weight_dict, edge_number


def gen_using(
        gen_function,
        file_name,
        input_dict):
    """
    Generate a graph using Watts-Strogatz model.

    Refer to (https://en.wikipedia.org/wiki/Watts%E2%80%93Strogatz_model).

    :param gen_function: graph generator function
    :type gen_function: function
    :param file_name: file name
    :type file_name: str
    :param input_dict: input data
    :type input_dict: dict
    :return: number of edges
    """
    edge_dict, weight_dict, edge_number = edge_gen(
        input_dict['vertices'],
        input_dict['mean_degree'],
        input_dict['rewiring_probability'])
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


def logger(file, file_name, elapsed_time, input_dict):
    """
    Save generated graph logs for Watts-Strogatz engine.

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
        text += "Mean Degree : {0}\n".format(input_dict['mean_degree'])
        text += "Rewiring Probability : {0}\n".format(input_dict['rewiring_probability'])
        text += "Total Edges : {0}\n".format(input_dict['edge_number'])
        text += "Engine : {0} ({1})\n".format(input_dict['engine'], ENGINE_MENU[input_dict['engine']])
        save_log(file, file_name, elapsed_time, text)
    except Exception:
        print(PYRGG_LOGGER_ERROR_MESSAGE)
