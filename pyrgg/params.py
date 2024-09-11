# -*- coding: utf-8 -*-
"""Pyrgg params."""
from textwrap import dedent, fill
import os

os.environ["PYRGG_TEST_MODE"] = "0"

MENU_ITEMS = {
    1: ["engine", dedent(
        """\
        - Select generation engine :
        1- Pyrgg engine
        2- Erdos-Renyi-Gilbert - G(n, p)
        """
    )],
    2: ["file_name", "- File Name (Not Empty) : "],
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
    5: ["config", "- Save Config[1] or Not[0]"],
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

ENGINE_MENU = {
    1: "pyrgg",
    2: "erg",
}

ENGINE_MENU_INV = {v: k for k, v in ENGINE_MENU.items()}

ERG_ENGINE_PARAMS = {
    1: ["vertices", "- Vertices Number (>=0) : "],
    2: ["probability", "- Probability (0 <= p <= 1) : "],
    3: ["direct", "- Undirected[0] or Directed[1]"],
}

PYRGG_ENGINE_PARAMS = {
    1: ["vertices", "- Vertices Number (>=0) : "],
    2: ["min_edge", "- Min Edge Number - Connected to Each Vertex (>=0) : "],
    3: ["max_edge", "- Max Edge Number - Connected to Each Vertex (>=0) : "],
    4: ["weight", "- Unweighted[0] or Weighted[1]"],
    5: ["min_weight", "- Min Weight : "],
    6: ["max_weight", "- Max Weight : "],
    7: ["sign", "- Unsigned[0] or Signed[1]"],
    8: ["direct", "- Undirected[0] or Directed[1]"],
    9: ["self_loop", "- No Self Loop[0] or Self Loop[1]"],
    10: ["multigraph", "- Simple[0] or Multigraph[1]"],
}

ENGINE_PARAM_MAP = {
    1: PYRGG_ENGINE_PARAMS,
    2: ERG_ENGINE_PARAMS,
}

OUTPUT_FORMAT = {i: output_format[1:].upper()
                 for i, output_format in SUFFIX_MENU.items()}

OUTPUT_FORMAT_INV = {v: k for k, v in OUTPUT_FORMAT.items()}


PYRGG_VERSION = "1.5"

SOURCE_DIR = os.getcwd()

CONFIG_FILE_FORMAT = "{}.pyrgg.config.json"

PYRGG_LINKS = """
Webpage : https://www.pyrgg.site
Repository : https://github.com/sepandhaghighi/pyrgg
Paper : https://doi.org/10.21105/joss.00331
* If you use Pyrgg in your research, please cite our paper
"""

_description = """\
PyRGG is a user-friendly synthetic random graph generator that is written in Python and supports multiple graph file formats, such as DIMACS-Graph files.
It can generate graphs of various sizes and is specifically designed to create input files for a wide range of graph-based research applications, including testing,
benchmarking, and performance analysis of graph processing frameworks.
PyRGG is aimed at computer scientists who are studying graph algorithms and graph processing frameworks.
"""

PYRGG_DESCRIPTION = fill(_description, width=113)

PYRGG_INPUT_ERROR_MESSAGE = "[Error] Bad input!"

PYRGG_FILE_ERROR_MESSAGE = "[Error] Bad input file!"

PYRGG_INVALID_ENGINE_ERROR_MESSAGE = "[Error] Invalid engine!"

PYRGG_YAML_ERROR_MESSAGE = "[Error] Failed to generate YAML file!"

PYRGG_PICKLE_ERROR_MESSAGE = "[Error] Failed to generate Pickle file!"

PYRGG_LOGGER_ERROR_MESSAGE = "[Error] Logger failed!"

PYRGG_CONFIG_LOAD_ERROR_MESSAGE = "[Error] Failed to load config file!"

PYRGG_CONFIG_SAVE_ERROR_MESSAGE = "[Error] Failed to save config file!"

PYRGG_CONFIG_LIST_MESSAGE = "Config files detected in the current directory are listed below:"

PYRGG_CONFIG_LOAD_MESSAGE = "Press the config index to load or any other keys to start with the new one:"

DIMACS_FIX = dedent(
    """\
    c FILE                  :{0}.gr
    c No. of vertices       :{1}
    c No. of edges          :{2}
    c Max. weight           :{3}
    c Min. weight           :{4}
    p sp {1} {2}
    """
)
