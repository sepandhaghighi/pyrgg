# -*- coding: utf-8 -*-
"""PyRGG graph generators module."""
from typing import List, Dict, Callable, Any, IO
import random
import datetime
from pyrgg.params import *
from pyrgg.functions import *

# random_system=random.SystemRandom()
random_system = random


def generate_dimacs_file(
        edge_dict: Dict[int, List[int]],
        weight_dict: Dict[int, List[float]],
        mdata: Dict[str, Any]) -> None:
    """
    Create output file and fill in.

    :param edge_dict: dictionary containing edges data
    :param weight_dict: dictionary containing weights data
    :param mdata: meta data
    """
    with open(mdata['file_name'] + ".gr", "w") as buf:
        buf.write(
            DIMACS_FIX.format(
                file_name=mdata['file_name'],
                vertices_number=str(mdata['vertices_number']),
                edge_number=str(mdata['edge_number']),
                max_weight=str(mdata['max_weight']),
                min_weight=str(mdata['min_weight'])))
        _write_separated_file(
            buf, edge_dict, weight_dict, separator=' ', prefix='a',
        )


def generate_json_file(
        edge_dict: Dict[int, List[int]],
        weight_dict: Dict[int, List[float]],
        mdata: Dict[str, Any]) -> None:
    """
    Create output file in json format.

    :param edge_dict: dictionary containing edges data
    :param weight_dict: dictionary containing weights data
    :param mdata: meta data
    """
    with open(mdata['file_name'] + ".json", "w") as buf:
        _write_properties_to_json(
            buf,
            mdata['weighted'],
            mdata['direct'],
            mdata['multigraph'],)
        _write_data_to_json(
            buf,
            edge_dict,
            weight_dict,
        )


def _write_data_to_json(buf: IO, edge_dict: Dict[int, List[int]], weight_dict: Dict[int, List[float]]) -> None:
    """
    Write data to json buffer.

    :param buf: output file object
    :param edge_dict: dictionary containing edges data
    :param weight_dict: dictionary containing weights data
    """
    buf.write('\n\t"graph": {\n')
    _write_nodes_to_json(buf, edge_dict)
    buf.write("\n\t\t],\n")
    _write_edges_to_json(buf, edge_dict, weight_dict)
    buf.write("\n\t\t]\n\t}\n}")


def _write_properties_to_json(
        buf: IO,
        weighted: bool,
        direct: bool,
        multigraph: bool) -> None:
    """
    Write properties to json buffer.

    :param buf: output file object
    :param weighted: weighted graph flag
    :param direct: directed and undirected graph flag
    :param multigraph: multigraph flag
    """
    buf.write('{\n\t"properties": {\n')
    buf.write('\t\t"weighted": ' + str(weighted).lower() + ",\n")
    buf.write('\t\t"multigraph": ' + str(multigraph).lower() + ",\n")
    buf.write('\t\t"directed": ' + str(direct).lower() + "\n")
    buf.write("},\n")


def _write_nodes_to_json(buf: IO, edge_dict: Dict[int, List[int]]) -> None:
    """
    Write nodes to json.

    :param buf: output file object
    :param edge_dict: dictionary containing edges data
    """
    first_line = True
    nodes = '\t\t"nodes":[\n'
    buf.write(nodes)

    for key in edge_dict:
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


def _write_edges_to_json(buf: IO, edge_dict: Dict[int, List[int]], weight_dict: Dict[int, List[float]]) -> None:
    """
    Write edges to json.

    :param buf: output file object
    :param edge_dict: dictionary containing edges data
    :param weight_dict: dictionary containing weights data
    """
    edges = '\t\t"edges":[\n'

    first_line = True
    buf.write(edges)

    for key, edge_val in edge_dict.items():
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
                str(weight_dict[key][j]),
                '\n\t\t}'
            ])
            buf.write(edges)


def generate_csv_file(
        edge_dict: Dict[int, List[int]],
        weight_dict: Dict[int, List[float]],
        mdata: Dict[str, Any]) -> None:
    """
    Create output file in csv format.

    :param edge_dict: dictionary containing edges data
    :param weight_dict: dictionary containing weights data
    :param mdata: meta data
    """
    with open(mdata['file_name'] + ".csv", "w") as buf:
        _write_separated_file(buf, edge_dict, weight_dict, separator=',')


def generate_tsv_file(
        edge_dict: Dict[int, List[int]],
        weight_dict: Dict[int, List[float]],
        mdata: Dict[str, Any]) -> None:
    """
    Create output file in tsv format.

    :param edge_dict: dictionary containing edges data
    :param weight_dict: dictionary containing weights data
    :param mdata: meta data
    """
    with open(mdata['file_name'] + ".tsv", "w") as buf:
        _write_separated_file(buf, edge_dict, weight_dict, separator='\t')


def _write_separated_file(buf: IO,
                          edge_dict: Dict[int,
                                          List[int]],
                          weight_dict: Dict[int,
                                            List[float]],
                          separator: str,
                          prefix: str = '') -> None:
    r"""
    Write data to buffer separated with ``separator``.

    :param buf: output file object
    :param edge_dict: dictionary containing edges data
    :param weight_dict: dictionary containing weights data
    :param separator: separator in a separated file, like ',', '\t', ' ', etc.
    :param prefix: prefix to be added in front of each line
    """
    dummy_prefix = object()
    prefix = prefix or dummy_prefix

    for key, edge_val in edge_dict.items():
        for j, value in enumerate(edge_val):
            elements = [
                prefix,
                str(key),
                str(value),
                str(weight_dict[key][j]) + "\n"
            ]
            string = separator.join(x for x in elements if x != dummy_prefix)
            buf.write(string)


def generate_wel_file(
        edge_dict: Dict[int, List[int]],
        weight_dict: Dict[int, List[float]],
        mdata: Dict[str, Any]) -> None:
    """
    Create output file in wel format.

    :param edge_dict: dictionary containing edges data
    :param weight_dict: dictionary containing weights data
    :param mdata: meta data
    """
    with open(mdata['file_name'] + ".wel", "w") as buf:
        _write_separated_file(buf, edge_dict, weight_dict, separator=' ')


def mtx_maker(
        edge_dict: Dict[int, List[int]],
        weight_dict: Dict[int, List[float]],
        mdata: Dict[str, Any]) -> None:
    """
    Create output file in Matrix Market format.

    :param edge_dict: dictionary containing edges data
    :param weight_dict: dictionary containing weights data
    :param mdata: meta data
    """
    max_edges_length = len(str(mdata['vertices_number']))
    with open(mdata['file_name'] + ".mtx", "w") as buf:
        buf.write("%%MatrixMarket matrix coordinate real general\n")
        buf.write("{vertices_number}    {vertices_number}    {edge_number}\n".format(
            vertices_number=str(mdata['vertices_number']), edge_number=str(mdata['edge_number'])))
        for key, edge_vals in edge_dict.items():
            for j, value in enumerate(edge_vals):
                shift1 = (max_edges_length - len(str(key))) + 4
                shift2 = (max_edges_length - len(str(value))) + 4
                buf.write(str(key) + shift1 * " " + str(value) + shift2 * " " +
                          str(weight_dict[key][j]) + "\n")


def lp_maker(
        edge_dict: Dict[int, List[int]],
        weight_dict: Dict[int, List[float]],
        mdata: Dict[str, Any]) -> None:
    """
    Create output file in ASP format.

    :param edge_dict: dictionary containing edges data
    :param weight_dict: dictionary containing weights data
    :param mdata: meta data
    """
    with open(mdata['file_name'] + ".lp", "w") as buf:
        for key in edge_dict:
            buf.write('node(' + str(key) + ").\n")
        for key, edge_val in edge_dict.items():
            for j, value in enumerate(edge_val):
                buf.write('edge(' + str(key) + "," + str(value) +
                          "," + str(weight_dict[key][j]) + ").\n")


def tgf_maker(
        edge_dict: Dict[int, List[int]],
        weight_dict: Dict[int, List[float]],
        mdata: Dict[str, Any]) -> None:
    """
    Create output file in Trivial Graph Format (TGF).

    :param edge_dict: dictionary containing edges data
    :param weight_dict: dictionary containing weights data
    :param mdata: meta data
    """
    with open(mdata['file_name'] + ".tgf", "w") as buf:
        for key in edge_dict:
            buf.write(str(key) + "\n")
        buf.write("#\n")
        _write_separated_file(buf, edge_dict, weight_dict, separator=' ')


def gl_maker(
        edge_dict: Dict[int, List[int]],
        weight_dict: Dict[int, List[float]],
        mdata: Dict[str, Any]) -> None:
    """
    Create output file in Graph Line(GL).

    :param edge_dict: dictionary containing edges data
    :param weight_dict: dictionary containing weights data
    :param mdata: meta data
    """
    with open(mdata['file_name'] + ".gl", "w") as buf:
        for key, edge_val in edge_dict.items():
            line_data = str(key)
            write_flag = False
            for j, value in enumerate(edge_val):
                write_flag = True
                line_data += " " + str(value) + ":" + str(weight_dict[key][j])
            if write_flag:
                buf.write(line_data + "\n")


def dl_maker(
        edge_dict: Dict[int, List[int]],
        weight_dict: Dict[int, List[float]],
        mdata: Dict[str, Any]) -> None:
    """
    Create output file in UCINET DL Format.

    :param edge_dict: dictionary containing edges data
    :param weight_dict: dictionary containing weights data
    :param mdata: meta data
    """
    with open(mdata['file_name'] + ".dl", "w") as buf:
        buf.write("dl\nformat=edgelist1\nn=" + str(mdata['vertices_number']) + "\ndata:\n")
        _write_separated_file(buf, edge_dict, weight_dict, separator=' ')


def gdf_maker(
        edge_dict: Dict[int, List[int]],
        weight_dict: Dict[int, List[float]],
        mdata: Dict[str, Any]) -> None:
    """
    Create output file in GDF Format.

    :param edge_dict: dictionary containing edges data
    :param weight_dict: dictionary containing weights data
    :param mdata: meta data
    """
    with open(mdata['file_name'] + ".gdf", "w") as buf:
        buf.write("nodedef>name VARCHAR,label VARCHAR\n")
        for key in edge_dict:
            buf.write(str(key) + "," + "Node{index}".format(index=str(key)) + "\n")
        buf.write("edgedef>node1 VARCHAR,node2 VARCHAR,weight DOUBLE\n")
        _write_separated_file(buf, edge_dict, weight_dict, separator=',')


def gml_maker(
        edge_dict: Dict[int, List[int]],
        weight_dict: Dict[int, List[float]],
        mdata: Dict[str, Any]) -> None:
    """
    Create output file in GML Format.

    :param edge_dict: dictionary containing edges data
    :param weight_dict: dictionary containing weights data
    :param mdata: meta data
    """
    header = 'graph\n[\n  multigraph {is_multigraph}\n  directed  {is_directed}\n'.format(
        is_multigraph=int(mdata['multigraph']), is_directed=int(mdata['direct']))

    with open(mdata['file_name'] + ".gml", "w") as buf:
        buf.write(header)
        for key in edge_dict:
            buf.write(
                "  node\n  [\n   id " +
                str(key) +
                "\n" +
                '   label "Node {index}"\n'.format(
                    index=str(key)) +
                "  ]\n")
        for key, edge_vals in edge_dict.items():
            for j, value in enumerate(edge_vals):
                buf.write("  edge\n  [\n   source " +
                          str(key) +
                          "\n" +
                          "   target " +
                          str(value) +
                          "\n" +
                          "   value " +
                          str(weight_dict[key][j]) +
                          "\n" +
                          "  ]\n")
        buf.write("]")


def gexf_maker(
        edge_dict: Dict[int, List[int]],
        weight_dict: Dict[int, List[float]],
        mdata: Dict[str, Any]) -> None:
    """
    Create output file in GEXF Format.

    :param edge_dict: dictionary containing edges data
    :param weight_dict: dictionary containing weights data
    :param mdata: meta data
    """
    header = '<?xml version="1.0" encoding="UTF-8"?>\n'
    header += '<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2">\n'
    date = datetime.datetime.now().date()
    meta = " " * 4 + '<meta lastmodifieddate="{date}">\n'.format(date=date)
    meta += " " * 8 + '<creator>PyRGG</creator>\n'
    meta += " " * 8 + '<description>{file_name}</description>\n'.format(file_name=mdata['file_name'])
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
        for key in edge_dict:
            buf.write(
                " " * 12 +
                '<node id="' +
                str(key) + '"' +
                ' label="Node {index}" />'.format(
                    index=str(key)) + "\n")
        buf.write(" " * 8 + "</nodes>\n")
        buf.write(" " * 8 + "<edges>\n")
        edge_id = 1
        for key, edge_vals in edge_dict.items():
            for j, value in enumerate(edge_vals):
                buf.write(
                    " " * 12 +
                    '<edge id="' +
                    str(edge_id) + '"' +
                    ' source="' +
                    str(key) + '"'
                    ' target="' +
                    str(value) + '"' +
                    ' weight="{weight}" />'.format(
                        weight=str(weight_dict[key][j])) + "\n")
                edge_id += 1
        buf.write(" " * 8 + "</edges>\n")
        buf.write(" " * 4 + "</graph>\n")
        buf.write("</gexf>")


def dot_maker(
        edge_dict: Dict[int, List[int]],
        weight_dict: Dict[int, List[float]],
        mdata: Dict[str, Any]) -> None:
    """
    Create output file in Dot Format.

    :param edge_dict: dictionary containing edges data
    :param weight_dict: dictionary containing weights data
    :param mdata: meta data
    """
    header = "{graph_type} {file_name}"
    linker = "--"
    if mdata['direct']:
        header = header.format(graph_type="digraph", file_name=mdata['file_name'])
        linker = "->"
    else:
        header = header.format(graph_type="graph", file_name=mdata['file_name'])

    with open(mdata['file_name'] + ".gv", "w") as buf:
        buf.write(header + " {")
        for key, edge_val in edge_dict.items():
            for j, value in enumerate(edge_val):
                buf.write(
                    "\n" +
                    str(key) +
                    " " +
                    linker +
                    " " +
                    str(value) +
                    " [weight={weight}]".format(
                        weight=weight_dict[key][j]) +
                    ";")
        buf.write("\n}")
