# -*- coding: utf-8 -*-
"""Pyrgg main."""
from pyrgg.pyrgg import *
import time
import sys
import doctest
from art import tprint


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
    print("Generating . . . ")
    if input_dict["output_format"] == 1:
        edge_number = dimacs_maker(
            file_name,
            min_weight,
            max_weight,
            vertices_number,
            min_edge,
            max_edge,
            sign)
        filesize(file_name + ".gr")
    elif input_dict["output_format"] == 2:
        edge_number = json_maker(
            file_name,
            min_weight,
            max_weight,
            vertices_number,
            min_edge,
            max_edge,
            sign)
        filesize(file_name + ".json")
    elif input_dict["output_format"] == 3:
        edge_number = csv_maker(
            file_name,
            min_weight,
            max_weight,
            vertices_number,
            min_edge,
            max_edge,
            sign)
        filesize(file_name + ".csv")
    elif input_dict["output_format"] == 4:
        edge_number = json_maker(
            file_name,
            min_weight,
            max_weight,
            vertices_number,
            min_edge,
            max_edge,
            sign)
        json_to_yaml(file_name)
        filesize(file_name + ".yaml")
    elif input_dict["output_format"] == 5:
        edge_number = wel_maker(
            file_name,
            min_weight,
            max_weight,
            vertices_number,
            min_edge,
            max_edge,
            sign)
        filesize(file_name + ".wel")
    elif input_dict["output_format"] == 6:
        edge_number = lp_maker(
            file_name,
            min_weight,
            max_weight,
            vertices_number,
            min_edge,
            max_edge,
            sign)
        filesize(file_name + ".lp")
    elif input_dict["output_format"] == 7:
        edge_number = json_maker(
            file_name,
            min_weight,
            max_weight,
            vertices_number,
            min_edge,
            max_edge,
            sign)
        json_to_pickle(file_name)
        filesize(file_name + ".p")
    elif input_dict["output_format"] == 8:
        edge_number = dl_maker(
            file_name,
            min_weight,
            max_weight,
            vertices_number,
            min_edge,
            max_edge,
            sign)
        filesize(file_name + ".dl")
    else:
        edge_number = tgf_maker(
            file_name,
            min_weight,
            max_weight,
            vertices_number,
            min_edge,
            max_edge,
            sign)
        filesize(file_name + ".tgf")
    second_time = time.perf_counter()
    elapsed_time = second_time - first_time
    elapsed_time_format = time_convert(str(elapsed_time))
    print("Graph Generated In " + elapsed_time_format)
    print("Where --> " + Source_dir)
    logger(
        vertices_number,
        edge_number,
        file_name + ".gr",
        elapsed_time_format)


if __name__ == "__main__":
    tprint("Pyrgg", "larry3d")
    tprint("v" + PYRGG_VERSION)
    line(50)
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
