# -*- coding: utf-8 -*-
"""Barabási-Albert Engine module."""
from random import sample
from pyrgg.params import ENGINE_MENU, PYRGG_LOGGER_ERROR_MESSAGE
from pyrgg.functions import save_log


def edge_gen(n, m_):
    """
    Generate each vertex connection number.

    :param n: number of vertices
    :type n: int
    :param m_: number of edges to be attached to a new node
    :type m_: int
    :return: list of dicts
    """
    edge_dic = {i: [] for i in range(1, m_ + 1)}
    weight_dict = {i: [] for i in range(1, m_ + 1)}
    node_from = m_ + 1
    node_to = list(range(1, m_ + 1))
    nodes_history = []
    while node_from <= n:
        edge_dic[node_from] = [i for i in node_to]
        weight_dict[node_from] = [1] * m_
        nodes_history.extend(node_to)
        nodes_history.extend([node_from] * m_)
        node_to = sample(nodes_history, m_)
        node_from += 1
    
    return [edge_dic, weight_dict, (n - m_) * m_]


def gen_using(
        gen_function,
        file_name,
        input_dict):
    """
    Generate graph using given function based on Barabási-Albert model.

    Refer to (https://en.wikipedia.org/wiki/Barab%C3%A1si%E2%80%93Albert_model).
    We assume that m0 is the same as m_ and m_ is the number of edges to attach to a new node.

    :param gen_function: generation function
    :type gen_function: function object
    :param file_name: file name
    :type file_name: str
    :param input_dict: input data
    :type input_dict: dict
    :return: number of edges as int
    """
    edge_dic, weight_dic, edge_number = edge_gen(
        input_dict['vertices'],
        input_dict['attaching_edge_number'])
    gen_function(
        edge_dic,
        weight_dic,
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


def logger(file, file_name, elapsed_time, input_dict):
    """
    Save generated graph logs for Barabási-Albert engine.

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
        text += "Engine : {0} ({1})\n".format(input_dict['engine'], ENGINE_MENU[input_dict['engine']])
        save_log(file, file_name, elapsed_time, text)
    except Exception:
        print(PYRGG_LOGGER_ERROR_MESSAGE)
