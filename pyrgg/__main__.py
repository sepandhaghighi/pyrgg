# -*- coding: utf-8 -*-
"""PyRGG main."""
from typing import Dict, Any, Optional
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
import pyrgg.engines.erdos_reyni as er_engine
import pyrgg.engines.stochastic_block_model as sbm_engine
import pyrgg.engines.barabasi_albert as ba_engine
import pyrgg.engines.watts_strogatz as ws_engine
import pyrgg.engines.geometric_graph as gg_engine

GENERATOR_MENU = {
    1: generate_dimacs_file,
    2: generate_json_file,
    3: generate_csv_file,
    4: generate_json_file,
    5: generate_wel_file,
    6: generate_lp_file,
    7: generate_json_file,
    8: dl_maker,
    9: generate_tgf_file,
    10: generate_tsv_file,
    11: generate_mtx_file,
    12: generate_gl_file,
    13: gdf_maker,
    14: gml_maker,
    15: gexf_maker,
    16: dot_maker,
}

ENGINE_MAPPER = {
    1: pyrgg_engine,
    2: erg_engine,
    3: er_engine,
    4: sbm_engine,
    5: ba_engine,
    6: ws_engine,
    7: gg_engine,
}


def gen_graph(input_dict: Dict[str, Any], file_name: str) -> None:
    """
    Generate a single graph.

    :param input_dict: input data
    :param file_name: file name
    """
    first_time = time.perf_counter()
    output_format = input_dict["output_format"]
    engine = input_dict["engine"]
    input_dict["edge_number"] = ENGINE_MAPPER[engine].generate_graph(
        GENERATOR_MENU[output_format],
        file_name,
        input_dict)
    if output_format == 4:
        json_to_yaml(file_name)
    if output_format == 7:
        json_to_pickle(file_name)
    print("Graph File Size : " + get_file_size(file_name + SUFFIX_MENU[output_format]))
    second_time = time.perf_counter()
    elapsed_time = second_time - first_time
    elapsed_time_format = convert_time(elapsed_time)
    print("Total Number of Edges : " + str(input_dict["edge_number"]))
    print("Graph Generated in " + elapsed_time_format)
    print("Where --> " + SOURCE_DIR)
    with open("logfile.log", "a") as file:
        ENGINE_MAPPER[engine].logger(file,
                                     file_name + SUFFIX_MENU[output_format],
                                     elapsed_time_format,
                                     input_dict)


def run(input_dict: Optional[Dict[str, Any]] = None) -> None:
    """
    Run proper converter.

    :param input_dict: input data
    """
    if input_dict is None:
        input_dict = get_input()
        if input_dict["config"] is True:
            print("Config --> " + save_config(input_dict))
    file_name = input_dict["file_name"]
    number_of_files = input_dict["number_of_files"]
    print_line(40)
    for i in range(number_of_files):
        print("Generating {index} from {number_of_files}".format(index=i + 1, number_of_files=number_of_files))
        file_name_temp = file_name
        if number_of_files > 1:
            file_name_temp = file_name + "_" + str(i + 1)
        gen_graph(input_dict, file_name_temp)
        print_line(40)


def main() -> None:
    """CLI main function."""
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
        tprint("PyRGG", "larry3d")
        tprint("v" + PYRGG_VERSION)
        print_description()
        EXIT_FLAG = False
        input_dict = None
        while not EXIT_FLAG:
            if args.config:
                input_dict = load_config(args.config)
            else:
                input_dict = check_for_config()
            run(input_dict)
            INPUTINDEX = str(
                input("Press [R] to restart PyRGG or any other key to exit."))
            if INPUTINDEX.upper() != "R":
                EXIT_FLAG = True


if __name__ == "__main__":
    main()
