# -*- coding: utf-8 -*-
"""Pyrgg main."""
from pyrgg.pyrgg import *
from pyrgg.params import *
import time
import sys
import doctest
from art import tprint

GENERATOR_MENU = {
    1: dimacs_maker,
    2: json_maker,
    3: csv_maker,
    4: json_maker,
    5: wel_maker,
    6: lp_maker,
    7: json_maker,
    8: dl_maker,
    9: tgf_maker}


def run():
    """
    Run proper converter.

    :return: None
    """
    first_time = time.perf_counter()
    input_dict = get_input()
    file_name = input_dict["file_name"]
    min_weight = input_dict["min_weight"]
    max_weight = input_dict["max_weight"]
    vertices_number = input_dict["vertices"]
    min_edge = input_dict["min_edge"]
    max_edge = input_dict["max_edge"]
    sign = input_dict["sign"]
    direct = input_dict["direct"]
    print("Generating . . . ")
    edge_number = GENERATOR_MENU[input_dict["output_format"]](
        file_name,
        min_weight,
        max_weight,
        vertices_number,
        min_edge,
        max_edge,
        sign,
        direct)
    if input_dict["output_format"] == 4:
        json_to_yaml(file_name)
    if input_dict["output_format"] == 7:
        json_to_pickle(file_name)
    filesize(file_name + SUFFIX_MENU[input_dict["output_format"]])
    second_time = time.perf_counter()
    elapsed_time = second_time - first_time
    elapsed_time_format = time_convert(str(elapsed_time))
    print("Graph Generated In " + elapsed_time_format)
    print("Where --> " + SOURCE_DIR)
    logger(
        vertices_number,
        edge_number,
        file_name + ".gr",
        elapsed_time_format)


if __name__ == "__main__":
    tprint("Pyrgg", "larry3d")
    tprint("v" + PYRGG_VERSION)
    description_print()
    args = sys.argv
    if len(args) > 1:
        if args[1].upper() == "TEST":
            error_flag = doctest.testfile("test.py", verbose=False)[0]
            sys.exit(error_flag)
        else:
            print("Bad Input!")
            print("Test (Run doctest)")
            print("Without arg --> Normal Run")
    else:
        EXIT_FLAG = False
        while not EXIT_FLAG:
            run()
            INPUTINDEX = str(
                input("Press [R] to restart Pyrgg or any other key to exit."))
            if INPUTINDEX.upper() != "R":
                EXITFLAG = True
