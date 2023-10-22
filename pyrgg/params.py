# -*- coding: utf-8 -*-
"""Pyrgg params."""
from textwrap import dedent, fill
import os

MENU_ITEMS = {
    1: ["engine", dedent(
        """\
        - Select generation engine :
        1- Pyrgg engine
        """
        )],
    2: ["file_name", "- File Name (not empty) : "],
    3: ["number_of_files", "- Number of Files (>=0) : "],
    4: ["output_format", dedent(
        """\
        - Graph Formats :
        1- DIMACS(.gr)
        2- JSON(.json)
        3- CSV(.csv)
        4- YAML(.yaml)
        5- WEL(.wel)
        6- ASP(.lp)
        7- Pickle(.p)
        8- UCINET DL(.dl)
        9- TGF(.tgf)
        10- TSV(.tsv)
        11- Matrix Market(.mtx)
        12- Graph Line(.gl)
        13- GDF(.gdf)
        14- GML(.gml)
        15- GEXF(.gexf)
        16- DOT(.gv)
        """
        )],
    5: ["weight", "- Unweighted[0] or Weighted[1]"],
}

SUFFIX_MENU = {
    1: ".gr",
    2: ".json",
    3: ".csv",
    4: ".yaml",
    5: ".wel",
    6: ".lp",
    7: ".p",
    8: ".dl",
    9: ".tgf",
    10: ".tsv",
    11: ".mtx",
    12: ".gl",
    13: ".gdf",
    14: ".gml",
    15: ".gexf",
    16: ".gv"
}

PYRGG_ENGINE_PARAMS = {
    1: ["vertices", "- Vertices Number (>=0) : "],
    2: ["min_edge", "- Min Edge Number - Connected to Each Vertex (>=0) : "],
    3: ["max_edge", "- Max Edge Number - Connected to Each Vertex (>=0) : "],
    4: ["min_weight", "- Min Weight : "],
    5: ["max_weight", "- Max Weight : "],
    6: ["sign", "- Unsigned[0] or Signed[1]"],
    7: ["direct", "- Undirected[0] or Directed[1]"],
    8: ["self_loop", "- No Self Loop[0] or Self Loop[1]"],
    9: ["multigraph", "- Simple[0] or Multigraph[1]"],
    10: ["config", "- Save config[1] or not[0]"],
}

ENGINE_MENU = {
    1: "pyrgg",
}

ENGINE_MENU_INV = {v: k for k, v in ENGINE_MENU.items()}

ENGINE_PARAM_MAP = {
    1: PYRGG_ENGINE_PARAMS,
}

OUTPUT_FORMAT = {i: output_format[1:].upper()
                 for i, output_format in SUFFIX_MENU.items()}

OUTPUT_FORMAT_INV = {v: k for k, v in OUTPUT_FORMAT.items()}


PYRGG_VERSION = "1.4"

PYRGG_TEST_MODE = False

SOURCE_DIR = os.getcwd()

CONFIG_FILE_FORMAT = "{}.pyrgg.config.json"

PYRGG_LINKS = """
Webpage : https://www.pyrgg.ir
Repository : https://github.com/sepandhaghighi/pyrgg
Paper : https://doi.org/10.21105/joss.00331
* If you use Pyrgg in your research, please cite our paper
"""

_description = """\
Pyrgg is an easy-to-use synthetic random graph generator written in Python
which supports various graph file formats including DIMACS .gr files.
Pyrgg has the ability to generate graphs of different sizes
and is designed to provide input files
for broad range of graph-based research applications,
including but not limited to testing,
benchmarking and performance-analysis of graph processing frameworks.
Pyrgg target audiences are computer scientists
who study graph algorithms and graph processing frameworks.
"""

PYRGG_DESCRIPTION = fill(_description, width=70)

PYRGG_INPUT_ERROR_MESSAGE = "[Error] Bad input!"

PYRGG_FILE_ERROR_MESSAGE = "[Error] Bad input file!"

PYRGG_INVALID_ENGINE_ERROR_MESSAGE = "[Error] Invalid engine!"

PYRGG_YAML_ERROR_MESSAGE = "[Error] Failed to generate YAML file!"

PYRGG_PICKLE_ERROR_MESSAGE = "[Error] Failed to generate Pickle file!"

PYRGG_LOGGER_ERROR_MESSAGE = "[Error] Logger failed!"

PYRGG_CONFIG_LOAD_ERROR_MESSAGE = "[Error] Failed to load config file!"

PYRGG_CONFIG_SAVE_ERROR_MESSAGE = "[Error] Failed to save config file!"

PYRGG_LOGGER_TEMPLATE = """{0}
Filename : {1}
Vertices : {2}
Total Edges : {3}
Max Edge : {4}
Min Edge : {5}
Directed : {6}
Signed : {7}
Multigraph : {8}
Self Loop : {9}
Weighted : {10}
Max Weight : {11}
Min Weight : {12}
Engine : {13} ({14})
Elapsed Time : {15}
-------------------------------
"""

DIMACS_FIX = dedent(
    """\
    c FILE                  :{0}.gr
    c No. of vertices       :{1}
    c No. of edges          :{2}
    c Max. weight           :{3}
    c Min. weight           :{4}
    c Min. edge             :{5}
    c Max. edge             :{6}
    p sp {1} {2}
    """
)
