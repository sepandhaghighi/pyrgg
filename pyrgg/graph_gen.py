# -*- coding: utf-8 -*-
"""Pyrgg graph generators module."""
import random
import datetime
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
    :type sign: bool
    :param direct: directed and undirected graph flag
    :type direct: bool
    :param self_loop: self loop flag
    :type self_loop: bool
    :param multigraph: multigraph flag
    :type multigraph: bool
    :return: edge_number as int
    """
    edge_dic, weight_dic, edge_number = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph,
    )

    with open(file_name + ".gr", "w") as buf:
        dimacs_init(
            buf,
            file_name,
            min_weight,
            max_weight,
            vertices,
            edge_number,
            min_edge,
            max_edge,
            direct,
        )
        _write_separated_file(
            buf, edge_dic, weight_dic, separator=' ', prefix='a',
        )
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
    :type sign: bool
    :param direct: directed and undirected graph flag
    :type direct: bool
    :param self_loop: self loop flag
    :type self_loop: bool
    :param multigraph: multigraph flag
    :type multigraph: bool
    :return: edge_number as int
    """
    edge_dic, weight_dic, edge_number = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph,
    )

    with open(file_name + ".json", "w") as buf:
        _write_properties_to_json(
            buf,
            min_weight,
            max_weight,
            sign,
            direct,
            self_loop,
            multigraph)
        _write_data_to_json(
            buf,
            edge_dic,
            weight_dic,
        )
    return edge_number


def _write_data_to_json(buf, edge_dic, weight_dic):
    """Write data to json buffer.

    :param buf: output file object
    :type buf: file_object
    :param edge_dic: dictionary containing edges data
    :type edge_dic: dict
    :param weight_dic: dictionary containing weights data
    :type weight_dic: dict
    :return: None
    """
    buf.write('\n\t"graph": {\n')
    _write_nodes_to_json(buf, edge_dic)
    buf.write("\n\t\t],\n")
    _write_edges_to_json(buf, edge_dic, weight_dic)
    buf.write("\n\t\t]\n\t}\n}")


def _write_properties_to_json(
        buf,
        min_weight,
        max_weight,
        sign,
        direct,
        self_loop,
        multigraph):
    """
    Write properties to json buffer.

    :param buf: output file object
    :type buf: file_object
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param sign: weight sign flag
    :type sign: bool
    :param direct: directed and undirected graph flag
    :type direct: bool
    :param self_loop: self loop flag
    :type self_loop: bool
    :param multigraph: multigraph flag
    :type multigraph: bool
    :return: None
    """
    buf.write('{\n\t"properties": {\n')
    buf.write('\t\t"directed": ' + str(direct).lower() + ",\n")
    buf.write('\t\t"signed": ' + str(sign).lower() + ",\n")
    buf.write('\t\t"multigraph": ' + str(multigraph).lower() + ",\n")
    buf.write('\t\t"weighted": ' +
              str(is_weighted(max_weight, min_weight, sign)).lower() + ",\n")
    buf.write('\t\t"self_loop": ' + str(self_loop).lower() + "\n\t},")


def _write_nodes_to_json(buf, edge_dic):
    """Write nodes to json.

    :param buf: output file object
    :type buf: file_object
    :param edge_dic: dictionary containing edges data
    :type edge_dic: dict
    :return: None
    """
    first_line = True
    nodes = '\t\t"nodes":[\n'
    buf.write(nodes)

    for key in edge_dic:
        nodes = ""
        if first_line:
            first_line = False
        else:
            nodes += ",\n"
        nodes = "".join([
            nodes,
            '\t\t{\n\t\t\t',
            '"id": ',
            str(key),
            '\n\t\t}'
        ])
        buf.write(nodes)


def _write_edges_to_json(buf, edge_dic, weight_dic):
    """Write edges to json.

    :param buf: output file object
    :type buf: file_object
    :param edge_dic: dictionary containing edges data
    :type edge_dic: dict
    :param weight_dic: dictionary containing weights data
    :type weight_dic: dict
    :return: None
    """
    edges = '\t\t"edges":[\n'

    first_line = True
    buf.write(edges)

    for key, edge_val in edge_dic.items():
        for j, value in enumerate(edge_val):
            edges = ""
            if first_line:
                first_line = False
            else:
                edges += ",\n"
            edges = "".join([
                edges,
                '\t\t{\n\t\t\t"source": ',
                str(key),
                ',\n\t\t\t',
                '"target": ',
                str(value),
                ',\n\t\t\t',
                '"weight": ',
                str(weight_dic[key][j]),
                '\n\t\t}'
            ])
            buf.write(edges)


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
    :type sign: bool
    :param direct: directed and undirected graph flag
    :type direct: bool
    :param self_loop: self loop flag
    :type self_loop: bool
    :param multigraph: multigraph flag
    :type multigraph: bool
    :return: edge_number as int
    """
    edge_dic, weight_dic, edge_number = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph,
    )
    with open(file_name + ".csv", "w") as buf:
        _write_separated_file(buf, edge_dic, weight_dic, separator=',')
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
    :type sign: bool
    :param direct: directed and undirected graph flag
    :type direct: bool
    :param self_loop: self loop flag
    :type self_loop: bool
    :param multigraph: multigraph flag
    :type multigraph: bool
    :return: edge_number as int
    """
    edge_dic, weight_dic, edge_number = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph,
    )
    with open(file_name + ".tsv", "w") as buf:
        _write_separated_file(buf, edge_dic, weight_dic, separator='\t')
    return edge_number


def _write_separated_file(buf, edge_dic, weight_dic, separator, prefix=''):
    r"""Write data to buffer separated with ``separator``.

    :param buf: output file object
    :type buf: file_object
    :param edge_dic: dictionary containing edges data
    :type edge_dic: dict
    :param weight_dic: dictionary containing weights data
    :type weight_dic: dict
    :param separator: separator in a separated file, like ',', '\t', ' ', etc.
    :type separator: str
    :param prefix: prefix to be added in front of each line
    :type prefix: str
    :return: None
    """
    dummy_prefix = object()
    prefix = prefix or dummy_prefix

    for key, edge_val in edge_dic.items():
        for j, value in enumerate(edge_val):
            elements = [
                prefix,
                str(key),
                str(value),
                str(weight_dic[key][j]) + "\n"
            ]
            string = separator.join(x for x in elements if x != dummy_prefix)
            buf.write(string)


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
    :type sign: bool
    :param direct: directed and undirected graph flag
    :type direct: bool
    :param self_loop: self loop flag
    :type self_loop: bool
    :param multigraph: multigraph flag
    :type multigraph: bool
    :return: edge_number as int
    """
    edge_dic, weight_dic, edge_number = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph,
    )
    with open(file_name + ".wel", "w") as buf:
        _write_separated_file(buf, edge_dic, weight_dic, separator=' ')
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
    :type sign: bool
    :param direct: directed and undirected graph flag
    :type direct: bool
    :param self_loop: self loop flag
    :type self_loop: bool
    :param multigraph: multigraph flag
    :type multigraph: bool
    :return: edge_number as int
    """
    edge_dic, weight_dic, edge_number = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph,
    )
    max_edge_length = len(str(vertices))
    with open(file_name + ".mtx", "w") as buf:
        buf.write("%%MatrixMarket matrix coordinate real general\n")
        buf.write(
            "{0}    {0}    {1}\n".format(str(vertices), str(edge_number))
        )
        for key, edge_val in edge_dic.items():
            for j, value in enumerate(edge_val):
                shift1 = (max_edge_length - len(str(key))) + 4
                shift2 = (max_edge_length - len(str(value))) + 4
                buf.write(str(key) + shift1 * " " + str(value) + shift2 * " " +
                          str(weight_dic[key][j]) + "\n")
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
    :type sign: bool
    :param direct: directed and undirected graph flag
    :type direct: bool
    :param self_loop: self loop flag
    :type self_loop: bool
    :param multigraph: multigraph flag
    :type multigraph: bool
    :return: edge_number as int
    """
    edge_dic, weight_dic, edge_number = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph,
    )
    with open(file_name + ".lp", "w") as buf:
        for key in edge_dic:
            buf.write('node(' + str(key) + ").\n")
        for key, edge_val in edge_dic.items():
            for j, value in enumerate(edge_val):
                buf.write('edge(' + str(key) + "," + str(value) +
                          "," + str(weight_dic[key][j]) + ").\n")
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
    :type sign: bool
    :param direct: directed and undirected graph flag
    :type direct: bool
    :param self_loop: self loop flag
    :type self_loop: bool
    :param multigraph: multigraph flag
    :type multigraph: bool
    :return: edge_number as int
    """
    edge_dic, weight_dic, edge_number = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph,
    )
    with open(file_name + ".tgf", "w") as buf:
        for key in edge_dic:
            buf.write(str(key) + "\n")
        buf.write("#\n")
        _write_separated_file(buf, edge_dic, weight_dic, separator=' ')
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
    :type sign: bool
    :param direct: directed and undirected graph flag
    :type direct: bool
    :param self_loop: self loop flag
    :type self_loop: bool
    :param multigraph: multigraph flag
    :type multigraph: bool
    :return: edge_number as int
    """
    edge_dic, weight_dic, edge_number = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph,
    )
    with open(file_name + ".gl", "w") as buf:
        for key, edge_val in edge_dic.items():
            line_data = str(key)
            write_flag = False
            for j, value in enumerate(edge_val):
                write_flag = True
                line_data += " " + str(value) + ":" + str(weight_dic[key][j])
            if write_flag:
                buf.write(line_data + "\n")
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
    :type sign: bool
    :param direct: directed and undirected graph flag
    :type direct: bool
    :param self_loop: self loop flag
    :type self_loop: bool
    :param multigraph: multigraph flag
    :type multigraph: bool
    :return: edge_number as int
    """
    edge_dic, weight_dic, edge_number = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph,
    )
    with open(file_name + ".dl", "w") as buf:
        buf.write("dl\nformat=edgelist1\nn=" + str(vertices) + "\ndata:\n")
        _write_separated_file(buf, edge_dic, weight_dic, separator=' ')
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
    :type sign: bool
    :param direct: directed and undirected graph flag
    :type direct: bool
    :param self_loop: self loop flag
    :type self_loop: bool
    :param multigraph: multigraph flag
    :type multigraph: bool
    :return: edge_number as int
    """
    edge_dic, weight_dic, edge_number = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph,
    )
    with open(file_name + ".gdf", "w") as buf:
        buf.write("nodedef>name VARCHAR,label VARCHAR\n")
        for key in edge_dic:
            buf.write(str(key) + "," + "Node{0}".format(str(key)) + "\n")
        buf.write("edgedef>node1 VARCHAR,node2 VARCHAR,weight DOUBLE\n")
        _write_separated_file(buf, edge_dic, weight_dic, separator=',')
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
    :type sign: bool
    :param direct: directed and undirected graph flag
    :type direct: bool
    :param self_loop: self loop flag
    :type self_loop: bool
    :param multigraph: multigraph flag
    :type multigraph: bool
    :return: edge_number as int
    """
    edge_dic, weight_dic, edge_number = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph,
    )

    header = 'graph\n[\n  multigraph {0}\n  directed  {1}\n'.format(
        int(multigraph), int(direct))

    with open(file_name + ".gml", "w") as buf:
        buf.write(header)
        for key in edge_dic:
            buf.write(
                "  node\n  [\n   id " +
                str(key) +
                "\n" +
                '   label "Node {0}"\n'.format(
                    str(key)) +
                "  ]\n")
        for key, edge_val in edge_dic.items():
            for j, value in enumerate(edge_val):
                buf.write("  edge\n  [\n   source " +
                          str(key) +
                          "\n" +
                          "   target " +
                          str(value) +
                          "\n" +
                          "   value " +
                          str(weight_dic[key][j]) +
                          "\n" +
                          "  ]\n")
        buf.write("]")
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
    :type sign: bool
    :param direct: directed and undirected graph flag
    :type direct: bool
    :param self_loop: self loop flag
    :type self_loop: bool
    :param multigraph: multigraph flag
    :type multigraph: bool
    :return: edge_number as int
    """
    edge_dic, weight_dic, edge_number = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph)
    header = '<?xml version="1.0" encoding="UTF-8"?>\n'
    header += '<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2">\n'
    date = datetime.datetime.now().date()
    meta = " " * 4 + '<meta lastmodifieddate="{0}">\n'.format(date)
    meta += " " * 8 + '<creator>PyRGG</creator>\n'
    meta += " " * 8 + '<description>{0}</description>\n'.format(file_name)
    meta += " " * 4 + '</meta>\n'
    if direct:
        defaultedgetype = "directed"
    else:
        defaultedgetype = "undirected"
    with open(file_name + ".gexf", "w") as buf:
        buf.write(header)
        buf.write(meta)

        buf.write(
            " " * 4 + '<graph defaultedgetype="' + defaultedgetype + '">\n'
        )
        buf.write(" " * 8 + "<nodes>\n")
        for key in edge_dic:
            buf.write(
                " " * 12 +
                '<node id="' +
                str(key) + '"' +
                ' label="Node {0}" />'.format(
                    str(key)) + "\n")
        buf.write(" " * 8 + "</nodes>\n")
        buf.write(" " * 8 + "<edges>\n")
        edge_id = 1
        for key, edge_val in edge_dic.items():
            for j, value in enumerate(edge_val):
                buf.write(
                    " " * 12 +
                    '<edge id="' +
                    str(edge_id) + '"' +
                    ' source="' +
                    str(key) + '"'
                    ' target="' +
                    str(value) + '"' +
                    ' weight="{0}" />'.format(
                        str(weight_dic[key][j])) + "\n")
                edge_id += 1
        buf.write(" " * 8 + "</edges>\n")
        buf.write(" " * 4 + "</graph>\n")
        buf.write("</gexf>")
    return edge_number
