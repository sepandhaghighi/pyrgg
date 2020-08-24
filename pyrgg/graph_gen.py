# -*- coding: utf-8 -*-
"""Pyrgg graph generators module."""
import random
import os
import datetime
import sys
from pyrgg.params import *
from pyrgg.functions import *

# random_system=random.SystemRandom()
random_system = random


def dimacs_init(
        file,
        file_name,
        min_weight,
        max_weight,
        vertices,
        edge,
        min_edge,
        max_edge,
        direct):
    """
    Initialize dimacs output file.

    :param file: output file object
    :param file_name: file name
    :type file_name: str
    :type file: file_object
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: vertices number
    :type vertices: int
    :param edge:  edge number
    :type edge: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :return: None
    """
    file.write(
        DIMACS_FIX.format(
            file_name,
            str(vertices),
            str(edge),
            str(max_weight),
            str(min_weight),
            str(min_edge),
            str(max_edge)))


def dimacs_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph):
    """
    Create output file and fill in.

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :param self_loop: self loop flag
    :type self_loop: int
    :param multigraph: multigraph flag
    :type multigraph: int
    :return: edge_number as int
    """
    file = open(file_name + ".gr", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    dimacs_init(
        file,
        file_name,
        min_weight,
        max_weight,
        vertices,
        edge_number,
        min_edge,
        max_edge,
        direct)
    for i in edge_dic.keys():
        for j, value in enumerate(edge_dic[i]):
            file.write("a " + str(i) + " " + str(value) +
                       " " + str(weight_dic[i][j]) + "\n")
    file.close()
    return edge_number


def json_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph):
    """
    Create output file in json format.

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :param self_loop: self loop flag
    :type self_loop: int
    :param multigraph: multigraph flag
    :type multigraph: int
    :return: edge_number as int
    """
    file = open(file_name + ".json", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    first_line = True
    nodes = '\t\t\t"nodes":[\n'
    edges = '\t\t\t"edges":[\n'
    file.write('{\n\t"graph": {\n')
    file.write(nodes)
    for i in edge_dic.keys():
        nodes = ""
        if first_line:
            first_line = False
        else:
            nodes += ",\n"
        nodes = nodes + '\t\t\t{\n\t\t\t\t' + \
            '"id": ' + '"' + str(i) + '"\n\t\t\t}'
        file.write(nodes)
    file.write("\n\t\t],\n")
    first_line = True
    file.write(edges)
    for i in edge_dic.keys():
        for j, value in enumerate(edge_dic[i]):
            edges = ""
            if first_line:
                first_line = False
            else:
                edges += ",\n"
            edges = edges + '\t\t\t{\n\t\t\t\t"source": ' + '"' + str(i) + '",\n\t\t\t\t' + '"target": ' + '"' + str(
                value) + '",\n\t\t\t\t' + '"weight": ' + '"' + str(weight_dic[i][j]) + '"\n\t\t\t}'
            file.write(edges)
    file.write("\n\t\t]\n\t}\n}")
    file.close()
    return edge_number


def csv_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph):
    """
    Create output file in csv format.

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :param self_loop: self loop flag
    :type self_loop: int
    :param multigraph: multigraph flag
    :type multigraph: int
    :return: edge_number as int
    """
    file = open(file_name + ".csv", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    for i in edge_dic.keys():
        for j, value in enumerate(edge_dic[i]):
            file.write(str(i) + "," + str(value) + "," +
                       str(weight_dic[i][j]) + "\n")
    file.close()
    return edge_number


def tsv_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph):
    """
    Create output file in tsv format.

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :param self_loop: self loop flag
    :type self_loop: int
    :param multigraph: multigraph flag
    :type multigraph: int
    :return: edge_number as int
    """
    file = open(file_name + ".tsv", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    for i in edge_dic.keys():
        for j, value in enumerate(edge_dic[i]):
            file.write(str(i) + "\t" + str(value) + "\t" +
                       str(weight_dic[i][j]) + "\n")
    file.close()
    return edge_number


def wel_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph):
    """
    Create output file in wel format.

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :param self_loop: self loop flag
    :type self_loop: int
    :param multigraph: multigraph flag
    :type multigraph: int
    :return: edge_number as int
    """
    file = open(file_name + ".wel", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    for i in edge_dic.keys():
        for j, value in enumerate(edge_dic[i]):
            file.write(str(i) + " " + str(value) + " " +
                       str(weight_dic[i][j]) + "\n")
    file.close()
    return edge_number


def mtx_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph):
    """
    Create output file in Matrix Market format.

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :param self_loop: self loop flag
    :type self_loop: int
    :param multigraph: multigraph flag
    :type multigraph: int
    :return: edge_number as int
    """
    file = open(file_name + ".mtx", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    max_edge_length = len(str(vertices))
    file.write("%%MatrixMarket matrix coordinate real general\n")
    file.write("{0}    {0}    {1}\n".format(str(vertices), str(edge_number)))
    for i in edge_dic.keys():
        for j, value in enumerate(edge_dic[i]):
            shift1 = (max_edge_length - len(str(i))) + 4
            shift2 = (max_edge_length - len(str(value))) + 4
            file.write(str(i) + shift1 * " " + str(value) + shift2 * " " +
                       str(weight_dic[i][j]) + "\n")
    file.close()
    return edge_number


def lp_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph):
    """
    Create output file in ASP format.

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :param self_loop: self loop flag
    :type self_loop: int
    :param multigraph: multigraph flag
    :type multigraph: int
    :return: edge_number as int
    """
    file = open(file_name + ".lp", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    for i in edge_dic.keys():
        file.write('node(' + str(i) + ").\n")
    for i in edge_dic.keys():
        for j, value in enumerate(edge_dic[i]):
            file.write('edge(' + str(i) + "," + str(value) +
                       "," + str(weight_dic[i][j]) + ").\n")
    file.close()
    return edge_number


def tgf_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph):
    """
    Create output file in Trivial Graph Format (TGF).

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :param self_loop: self loop flag
    :type self_loop: int
    :param multigraph: multigraph flag
    :type multigraph: int
    :return: edge_number as int
    """
    file = open(file_name + ".tgf", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    for i in edge_dic.keys():
        file.write(str(i) + "\n")
    file.write("#\n")
    for i in edge_dic.keys():
        for j, value in enumerate(edge_dic[i]):
            file.write(str(i) + " " + str(value) + " " +
                       str(weight_dic[i][j]) + "\n")
    file.close()
    return edge_number


def gl_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph):
    """
    Create output file in Graph Line(GL).

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :param self_loop: self loop flag
    :type self_loop: int
    :param multigraph: multigraph flag
    :type multigraph: int
    :return: edge_number as int
    """
    file = open(file_name + ".gl", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    for i in edge_dic.keys():
        line_data = str(i)
        for j, value in enumerate(edge_dic[i]):
            line_data += " " + str(value) + ":" + str(weight_dic[i][j])
        file.write(line_data + "\n")
    file.close()
    return edge_number


def dl_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph):
    """
    Create output file in UCINET DL Format.

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :param self_loop: self loop flag
    :type self_loop: int
    :param multigraph: multigraph flag
    :type multigraph: int
    :return: edge_number as int
    """
    file = open(file_name + ".dl", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    file.write("dl\nformat=edgelist1\nn=" + str(vertices) + "\ndata:\n")
    for i in edge_dic.keys():
        for j, value in enumerate(edge_dic[i]):
            file.write(str(i) + " " + str(value) + " " +
                       str(weight_dic[i][j]) + "\n")
    file.close()
    return edge_number


def gdf_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph):
    """
    Create output file in GDF Format.

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :param self_loop: self loop flag
    :type self_loop: int
    :param multigraph: multigraph flag
    :type multigraph: int
    :return: edge_number as int
    """
    file = open(file_name + ".gdf", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    file.write("nodedef>name VARCHAR,label VARCHAR\n")
    for i in edge_dic.keys():
        file.write(str(i) + "," + "Node{0}".format(str(i)) + "\n")
    file.write("edgedef>node1 VARCHAR,node2 VARCHAR,weight DOUBLE\n")
    for i in edge_dic.keys():
        for j, value in enumerate(edge_dic[i]):
            file.write(str(i) + "," + str(value) + "," +
                       str(weight_dic[i][j]) + "\n")
    file.close()
    return edge_number


def gml_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph):
    """
    Create output file in GML Format.

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :param self_loop: self loop flag
    :type self_loop: int
    :param multigraph: multigraph flag
    :type multigraph: int
    :return: edge_number as int
    """
    file = open(file_name + ".gml", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    header = 'graph\n[\n  multigraph {0}\n  directed  {1}\n'
    multigraph_flag = str(int(abs((1 - multigraph))))
    directed_flag = str(int(2 - direct))
    header = header.format(multigraph_flag, directed_flag)
    file.write(header)
    for i in edge_dic.keys():
        file.write(
            "  node\n  [\n   id " +
            str(i) +
            "\n" +
            '   label "Node {0}"\n'.format(
                str(i)) +
            "  ]\n")
    for i in edge_dic.keys():
        for j, value in enumerate(edge_dic[i]):
            file.write("  edge\n  [\n   source " +
                       str(i) +
                       "\n" +
                       "   target " +
                       str(value) +
                       "\n" +
                       "   value " +
                       str(weight_dic[i][j]) +
                       "\n" +
                       "  ]\n")
    file.write("]")
    file.close()
    return edge_number


def gexf_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph):
    """
    Create output file in GEXF Format.

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :param self_loop: self loop flag
    :type self_loop: int
    :param multigraph: multigraph flag
    :type multigraph: int
    :return: edge_number as int
    """
    file = open(file_name + ".gexf", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    header = '<?xml version="1.0" encoding="UTF-8"?>\n'
    header += '<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2">\n'
    date = datetime.datetime.now().date()
    meta = " " * 4 + '<meta lastmodifieddate="{0}">\n'.format(date)
    meta += " " * 8 + '<creator>PyRGG</creator>\n'
    meta += " " * 8 + '<description>{0}</description>\n'.format(file_name)
    meta += " " * 4 + '</meta>\n'
    file.write(header)
    file.write(meta)
    if direct == 1:
        defaultedgetype = "directed"
    else:
        defaultedgetype = "undirected"
    file.write(
        " " * 4 + '<graph defaultedgetype="' + defaultedgetype + '">\n'
    )
    file.write(" " * 8 + "<nodes>\n")
    for i in edge_dic.keys():
        file.write(
            " " * 12 +
            '<node id="' +
            str(i) + '"' +
            ' label="Node {0}" />'.format(
                str(i)) + "\n")
    file.write(" " * 8 + "</nodes>\n")
    file.write(" " * 8 + "<edges>\n")
    edge_id = 1
    for i in edge_dic.keys():
        for j, value in enumerate(edge_dic[i]):
            file.write(
                " " * 12 +
                '<edge id="' +
                str(edge_id) + '"' +
                ' source="' +
                str(i) + '"'
                ' target="' +
                str(value) + '"' +
                ' weight="{0}" />'.format(
                    str(weight_dic[i][j])) + "\n")
            edge_id += 1
    file.write(" " * 8 + "</edges>\n")
    file.write(" " * 4 + "</graph>\n")
    file.write("</gexf>")
    file.close()
    return edge_number
