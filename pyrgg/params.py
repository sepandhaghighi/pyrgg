# -*- coding: utf-8 -*-
"""Pyrgg params."""
import os

MENU_ITEMS1 = {
    "file_name": "- File Name : ",
    "output_format": "- Graph Formats : \n1- DIMACS(.gr)\n2- JSON(.json)\n3- CSV(.csv)\n4- YAML(.yaml)\n5- WEL(.wel)\n6- ASP(.lp)\n7- Pickle(.p)\n8- UCINET DL(.dl)\n9- TGF(.tgf)\n10- TSV("
                     ".tsv)\n11- Matrix Market(.mtx)\n12- Graph Line(.gl)\n",
    "weight": "- Weighted[1] or Unweighted[2]"}

MENU_ITEMS2 = {"vertices": "- Vertices Number : ",
               "max_weight": "- Max Weight : ",
               "min_weight": "- Min Weight : ",
               "min_edge": "- Min Edge Number :",
               "max_edge": "- Max Edge Number :",
               "sign": "- Signed[1] or Unsigned[2]",
               "direct": "- Directed[1] or Undirected[2]",
               "self_loop": "- Self Loop[1] or No Self Loop[2]",
               "multigraph": "- Simple[1] or Multigraph[2]"}


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
    12: ".gl"}


PYRGG_VERSION = "0.7"

SOURCE_DIR = os.getcwd()

PYRGG_LINKS = """
Webpage : https://www.pyrgg.ir
Repository : https://github.com/sepandhaghighi/pyrgg
Paper : https://doi.org/10.21105/joss.00331
* If you use Pyrgg in your research, please cite our paper
"""

PYRGG_DESCRIPTION = '''
Pyrgg is an easy-to-use synthetic random graph generator written in Python which supports various graph file formats
including DIMACS .gr files. Pyrgg has the ability to generate graphs of different sizes and is designed to provide input files
for broad range of graph-based research applications, including but not limited to testing, benchmarking and performance-analysis
of graph processing frameworks. Pyrgg target audiences are computer scientists who study graph algorithms and graph processing frameworks.
'''


DIMACS_FIX = """c FILE                  :{0}.gr
c No. of vertices       :{1}
c No. of edges          :{2}
c Max. weight           :{3}
c Min. weight           :{4}
c Min. edge             :{5}
c Max. edge             :{6}
p sp {1} {2}
"""
