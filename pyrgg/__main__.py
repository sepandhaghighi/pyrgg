# -*- coding: utf-8 -*-
"""Pyrgg main."""
from pyrgg.graph_gen import *
from pyrgg.functions import *
from pyrgg.params import *
import time
import sys
import argparse
import doctest
from art import tprint
import pyrgg.engines.pyrgg as pyrgg_engine
import pyrgg.engines.erdos_reyni_gilbert as erg_engine

GENERATOR_MENU = {
    1: dimacs_maker,
    2: json_maker,
    3: csv_maker,
    4: json_maker,
    5: wel_maker,
    6: lp_maker,
    7: json_maker,
    8: dl_maker,
    9: tgf_maker,
    10: tsv_maker,
    11: mtx_maker,
    12: gl_maker,
    13: gdf_maker,
    14: gml_maker,
    15: gexf_maker,
    16: dot_maker,
}

ENGINE_GENERATOR = {
    1: pyrgg_engine.gen_using,
    2: erg_engine.gen_using,
}


def gen_graph(input_dict, file_name):
    """
    Generate a single graph.

    :param input_dict: input data
    :type input_dict: dict
    :param file_name: file name
    :type file_name: str
    :return: None
    """
    first_time = time.perf_counter()
    min_weight = input_dict["min_weight"]
    max_weight = input_dict["max_weight"]
    vertices_number = input_dict["vertices"]
    min_edge = input_dict["min_edge"]
    max_edge = input_dict["max_edge"]
    sign = input_dict["sign"]
    direct = input_dict["direct"]
    self_loop = input_dict["self_loop"]
    multigraph = input_dict["multigraph"]
    output_format = input_dict["output_format"]
    probability = input_dict["probability"]
    engine = input_dict["engine"]
    edge_number = ENGINE_GENERATOR[engine](
        GENERATOR_MENU[output_format],
        file_name=file_name,
        min_weight=min_weight,
        max_weight=max_weight,
        vertices_number=vertices_number,
        min_edge=min_edge,
        max_edge=max_edge,
        sign=sign,
        direct=direct,
        self_loop=self_loop,
        multigraph=multigraph,
        probability=probability)
    if output_format == 4:
        json_to_yaml(file_name)
    if output_format == 7:
        json_to_pickle(file_name)
    filesize(file_name + SUFFIX_MENU[output_format])
    second_time = time.perf_counter()
    elapsed_time = second_time - first_time
    elapsed_time_format = time_convert(elapsed_time)
    print("Total Number of Edges : " + str(edge_number))
    print("Graph Generated in " + elapsed_time_format)
    print("Where --> " + SOURCE_DIR)
    logger(
        file_name + SUFFIX_MENU[output_format],
        vertices_number,
        edge_number,
        max_edge,
        min_edge,
        direct,
        sign,
        multigraph,
        self_loop,
        max_weight,
        min_weight,
        engine,
        elapsed_time_format)


def run(input_dict=None):
    """
    Run proper converter.

    :param input_dict: input data
    :type input_dict: dict
    :return: None
    """
    if input_dict is None:
        input_dict = get_input()
        if input_dict["config"] is True:
            print("Config --> " + save_config(input_dict))
    file_name = input_dict["file_name"]
    number_of_files = input_dict["number_of_files"]
    line(40)
    for i in range(number_of_files):
        print("Generating {0} from {1}".format(i + 1, number_of_files))
        file_name_temp = file_name
        if number_of_files > 1:
            file_name_temp = file_name + "_" + str(i + 1)
        gen_graph(input_dict, file_name_temp)
        line(40)


def main():
    """
    CLI main function.

    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', help='version', nargs="?", const=1)
    parser.add_argument('--config', help='config')
    parser.add_argument('test', help='test', nargs="?", const=1)
    args = parser.parse_args()
    if args.version:
        print(PYRGG_VERSION)
    elif args.test:
        print("Testing ...")
        error_flag = doctest.testfile("test.py", verbose=False)[0]
        if error_flag == 0:
            print("Done!")
        sys.exit(error_flag)
    else:
        tprint("Pyrgg", "larry3d")
        tprint("v" + PYRGG_VERSION)
        description_print()
        EXIT_FLAG = False
        input_dict = None
        while not EXIT_FLAG:
            if args.config:
                input_dict = load_config(args.config)
            else:
                input_dict = check_for_config()
            run(input_dict)
            INPUTINDEX = str(
                input("Press [R] to restart Pyrgg or any other key to exit."))
            if INPUTINDEX.upper() != "R":
                EXIT_FLAG = True


if __name__ == "__main__":
    main()
