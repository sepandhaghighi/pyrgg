# -*- coding: utf-8 -*-
"""Pyrgg utility module."""


def get_min_weight(weight_dic):
    """
    Get minimum weight value.

    :param edge_dic: edge dictionary
    :type edge_dic: dict
    :param weighted: weighted flag
    :type weighted: bool
    :return: minimum weight value
    """
    return min([abs(w) for weights in weight_dic.values() for w in weights])


def get_max_weight(weight_dic):
    """
    Get maximum weight value.

    :param edge_dic: edge dictionary
    :type edge_dic: dict
    :param weighted: weighted flag
    :type weighted: bool
    :return: maximum weight value
    """
    return max([abs(w) for weights in weight_dic.values() for w in weights])


def is_signed(weight_dic):
    """
    Check if the graph is signed.

    :param weight_dic: weight dictionary
    :type weight_dic: dict
    :return: signed flag
    """
    return any([any([w < 0 for w in weights]) for weights in weight_dic.values()])


def has_self_loop(edge_dic):
    """
    Check if the graph has self loops.
    
    :param edge_dic: edge dictionary
    :type edge_dic: dict
    :return: self looped flag
    """
    return any([v in edges for v, edges in edge_dic.items()])


def is_multigraph(edge_dic):
    """
    Check if the graph is a multigraph.

    :param edge_dic: edge dictionary
    :type edge_dic: dict
    :return: multigraph flag
    """
    return any([len(set(edges)) != len(edges) for edges in edge_dic.values()])
