# -*- coding: utf-8 -*-
"""Pyrgg graph generators module."""
import random
import datetime
from pyrgg.params import *
from pyrgg.functions import *

# random_system=random.SystemRandom()
random_system = random


def dimacs_maker(
        edge_dic,
        weight_dic,
        mdata):
    """
    Create output file and fill in.

    :param edge_dic: dictionary containing edges data
    :type edge_dic: dict
    :param weight_dic: dictionary containing weights data
    :type weight_dic: dict
    :param mdata: meta data
    :type mdata: dict
    :return: None
    """
    with open(mdata['file_name'] + ".gr", "w") as buf:
        buf.write(
            DIMACS_FIX.format(
                mdata['file_name'],
                str(mdata['vertices_number']),
                str(mdata['edge_number']),
                str(mdata['max_weight']),
                str(mdata['min_weight'])))
        _write_separated_file(
            buf, edge_dic, weight_dic, separator=' ', prefix='a',
        )


def json_maker(
        edge_dic,
        weight_dic,
        mdata):
    """
    Create output file in json format.

    :param edge_dic: dictionary containing edges data
    :type edge_dic: dict
    :param weight_dic: dictionary containing weights data
    :type weight_dic: dict
    :param mdata: meta data
    :type mdata: dict
    :return: None
    """
    with open(mdata['file_name'] + ".json", "w") as buf:
        _write_properties_to_json(
            buf,
            mdata['weighted'],
            mdata['direct'],
            mdata['multigraph'],)
        _write_data_to_json(
            buf,
            edge_dic,
            weight_dic,
        )


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
        weighted,
        direct,
        multigraph):
    """
    Write properties to json buffer.

    :param buf: output file object
    :type buf: file_object
    :param weighted: weighted graph flag
    :type weighted: bool
    :param direct: directed and undirected graph flag
    :type direct: bool
    :param multigraph: multigraph flag
    :type multigraph: bool
    :return: None
    """
    buf.write('{\n\t"properties": {\n')
    buf.write('\t\t"weighted": ' + str(weighted).lower() + ",\n")
    buf.write('\t\t"multigraph": ' + str(multigraph).lower() + ",\n")
    buf.write('\t\t"directed": ' + str(direct).lower() + "\n")
    buf.write("},\n")


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
        edge_dic,
        weight_dic,
        mdata):
    """
    Create output file in csv format.

    :param edge_dic: dictionary containing edges data
    :type edge_dic: dict
    :param weight_dic: dictionary containing weights data
    :type weight_dic: dict
    :param mdata: meta data
    :type mdata: dict
    :return: None
    """
    with open(mdata['file_name'] + ".csv", "w") as buf:
        _write_separated_file(buf, edge_dic, weight_dic, separator=',')


def tsv_maker(
        edge_dic,
        weight_dic,
        mdata):
    """
    Create output file in tsv format.

    :param edge_dic: dictionary containing edges data
    :type edge_dic: dict
    :param weight_dic: dictionary containing weights data
    :type weight_dic: dict
    :param mdata: meta data
    :type mdata: dict
    :return: None
    """
    with open(mdata['file_name'] + ".tsv", "w") as buf:
        _write_separated_file(buf, edge_dic, weight_dic, separator='\t')


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
        edge_dic,
        weight_dic,
        mdata):
    """
    Create output file in wel format.

    :param edge_dic: dictionary containing edges data
    :type edge_dic: dict
    :param weight_dic: dictionary containing weights data
    :type weight_dic: dict
    :param mdata: meta data
    :type mdata: dict
    :return: None
    """
    with open(mdata['file_name'] + ".wel", "w") as buf:
        _write_separated_file(buf, edge_dic, weight_dic, separator=' ')


def mtx_maker(
        edge_dic,
        weight_dic,
        mdata):
    """
    Create output file in Matrix Market format.

    :param edge_dic: dictionary containing edges data
    :type edge_dic: dict
    :param weight_dic: dictionary containing weights data
    :type weight_dic: dict
    :param mdata: meta data
    :type mdata: dict
    :return: None
    """
    max_edge_length = len(str(mdata['vertices_number']))
    with open(mdata['file_name'] + ".mtx", "w") as buf:
        buf.write("%%MatrixMarket matrix coordinate real general\n")
        buf.write(
            "{0}    {0}    {1}\n".format(str(mdata['vertices_number']), str(mdata['edge_number']))
        )
        for key, edge_val in edge_dic.items():
            for j, value in enumerate(edge_val):
                shift1 = (max_edge_length - len(str(key))) + 4
                shift2 = (max_edge_length - len(str(value))) + 4
                buf.write(str(key) + shift1 * " " + str(value) + shift2 * " " +
                          str(weight_dic[key][j]) + "\n")


def lp_maker(
        edge_dic,
        weight_dic,
        mdata):
    """
    Create output file in ASP format.

    :param edge_dic: dictionary containing edges data
    :type edge_dic: dict
    :param weight_dic: dictionary containing weights data
    :type weight_dic: dict
    :param mdata: meta data
    :type mdata: dict
    :return: None
    """
    with open(mdata['file_name'] + ".lp", "w") as buf:
        for key in edge_dic:
            buf.write('node(' + str(key) + ").\n")
        for key, edge_val in edge_dic.items():
            for j, value in enumerate(edge_val):
                buf.write('edge(' + str(key) + "," + str(value) +
                          "," + str(weight_dic[key][j]) + ").\n")


def tgf_maker(
        edge_dic,
        weight_dic,
        mdata):
    """
    Create output file in Trivial Graph Format (TGF).

    :param edge_dic: dictionary containing edges data
    :type edge_dic: dict
    :param weight_dic: dictionary containing weights data
    :type weight_dic: dict
    :param mdata: meta data
    :type mdata: dict
    :return: None
    """
    with open(mdata['file_name'] + ".tgf", "w") as buf:
        for key in edge_dic:
            buf.write(str(key) + "\n")
        buf.write("#\n")
        _write_separated_file(buf, edge_dic, weight_dic, separator=' ')


def gl_maker(
        edge_dic,
        weight_dic,
        mdata):
    """
    Create output file in Graph Line(GL).

    :param edge_dic: dictionary containing edges data
    :type edge_dic: dict
    :param weight_dic: dictionary containing weights data
    :type weight_dic: dict
    :param mdata: meta data
    :type mdata: dict
    :return: None
    """
    with open(mdata['file_name'] + ".gl", "w") as buf:
        for key, edge_val in edge_dic.items():
            line_data = str(key)
            write_flag = False
            for j, value in enumerate(edge_val):
                write_flag = True
                line_data += " " + str(value) + ":" + str(weight_dic[key][j])
            if write_flag:
                buf.write(line_data + "\n")


def dl_maker(
        edge_dic,
        weight_dic,
        mdata):
    """
    Create output file in UCINET DL Format.

    :param edge_dic: dictionary containing edges data
    :type edge_dic: dict
    :param weight_dic: dictionary containing weights data
    :type weight_dic: dict
    :param mdata: meta data
    :type mdata: dict
    :return: None
    """
    with open(mdata['file_name'] + ".dl", "w") as buf:
        buf.write("dl\nformat=edgelist1\nn=" + str(mdata['vertices_number']) + "\ndata:\n")
        _write_separated_file(buf, edge_dic, weight_dic, separator=' ')


def gdf_maker(
        edge_dic,
        weight_dic,
        mdata):
    """
    Create output file in GDF Format.

    :param edge_dic: dictionary containing edges data
    :type edge_dic: dict
    :param weight_dic: dictionary containing weights data
    :type weight_dic: dict
    :param mdata: meta data
    :type mdata: dict
    :return: None
    """
    with open(mdata['file_name'] + ".gdf", "w") as buf:
        buf.write("nodedef>name VARCHAR,label VARCHAR\n")
        for key in edge_dic:
            buf.write(str(key) + "," + "Node{0}".format(str(key)) + "\n")
        buf.write("edgedef>node1 VARCHAR,node2 VARCHAR,weight DOUBLE\n")
        _write_separated_file(buf, edge_dic, weight_dic, separator=',')


def gml_maker(
        edge_dic,
        weight_dic,
        mdata):
    """
    Create output file in GML Format.

    :param edge_dic: dictionary containing edges data
    :type edge_dic: dict
    :param weight_dic: dictionary containing weights data
    :type weight_dic: dict
    :param mdata: meta data
    :type mdata: dict
    :return: None
    """
    header = 'graph\n[\n  multigraph {0}\n  directed  {1}\n'.format(
        int(mdata['multigraph']), int(mdata['direct']))

    with open(mdata['file_name'] + ".gml", "w") as buf:
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


def gexf_maker(
        edge_dic,
        weight_dic,
        mdata):
    """
    Create output file in GEXF Format.

    :param edge_dic: dictionary containing edges data
    :type edge_dic: dict
    :param weight_dic: dictionary containing weights data
    :type weight_dic: dict
    :param mdata: meta data
    :type mdata: dict
    :return: None
    """
    header = '<?xml version="1.0" encoding="UTF-8"?>\n'
    header += '<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2">\n'
    date = datetime.datetime.now().date()
    meta = " " * 4 + '<meta lastmodifieddate="{0}">\n'.format(date)
    meta += " " * 8 + '<creator>PyRGG</creator>\n'
    meta += " " * 8 + '<description>{0}</description>\n'.format(mdata['file_name'])
    meta += " " * 4 + '</meta>\n'
    if mdata['direct']:
        defaultedgetype = "directed"
    else:
        defaultedgetype = "undirected"
    with open(mdata['file_name'] + ".gexf", "w") as buf:
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


def dot_maker(
        edge_dic,
        weight_dic,
        mdata):
    """
    Create output file in Dot Format.

    :param edge_dic: dictionary containing edges data
    :type edge_dic: dict
    :param weight_dic: dictionary containing weights data
    :type weight_dic: dict
    :param mdata: meta data
    :type mdata: dict
    :return: None
    """
    header = "{0} {1}"
    linker = "--"
    if mdata['direct']:
        header = header.format("digraph", mdata['file_name'])
        linker = "->"
    else:
        header = header.format("graph", mdata['file_name'])

    with open(mdata['file_name'] + ".gv", "w") as buf:
        buf.write(header + " {")
        for key, edge_val in edge_dic.items():
            for j, value in enumerate(edge_val):
                buf.write(
                    "\n" +
                    str(key) +
                    " " +
                    linker +
                    " " +
                    str(value) +
                    " [weight={}]".format(
                        weight_dic[key][j]) +
                    ";")
        buf.write("\n}")
