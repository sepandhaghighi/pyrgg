# -*- coding: utf-8 -*-
"""Erdős-Rényi-Gilbert Engine module."""
from random import random

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
        **kwargs):
    """
    Generate graph using given function based on Erdos Renyi Gilbert model.

    Refer to (https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model)

    :param gen_function: generation function
    :type gen_function: function object
    :param kwargs: input data as keyword arguments
    :type kwargs: dict
    :return: number of edges as int
    """
    edge_dic, edge_number = edge_gen(
        kwargs['vertices_number'],
        kwargs['probability'])
    weight_dic = {key: [1] * edge_number for key in range(1, kwargs['vertices_number'] + 1)}
    gen_function(
        edge_dic,
        weight_dic,
        {
            "file_name": kwargs['file_name'],
            "vertices_number": kwargs['vertices_number'],
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
