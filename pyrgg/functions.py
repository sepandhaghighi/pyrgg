# -*- coding: utf-8 -*-
"""Pyrgg functions module."""
import random
import os
import textwrap
import datetime
import yaml
import json
import pickle
from pyrgg.params import *

# random_system=random.SystemRandom()
random_system = random


def get_precision(input_number):
    """
    Return precision of input number.

    :param input_number: input number
    :type input_number: float
    :return: precision as int
    """
    try:
        number_str = str(input_number)
        intpart, decimalpart = number_str.split(".")
        return len(decimalpart)
    except Exception:
        return 0


def is_float(input_number):
    """
    Check input for float conversion.

    :param input_number: input number
    :type input_number: float or int
    :return: result as bool
    """
    try:
        _ = float(input_number)
        number_splitted = str(input_number).split(".")
        if len(number_splitted) == 2:
            return True
        return False
    except Exception:
        return False


def weight_str_to_number(weight):
    """
    Convert weight string to float or int.

    :param weight: input weight
    :type weight: str
    :return: weight as float or int
    """
    weight_splitted = weight.split(".")
    if len(weight_splitted) == 2:
        return float(weight)
    return int(weight)


def description_print():
    """
    Print justified description for overview in console.

    :return: None
    """
    print(PYRGG_LINKS)
    line(40)
    print("\n")
    print(textwrap.fill(PYRGG_DESCRIPTION, width=100))
    print("\n")
    line(40)


def line(num=11, char="#"):
    """
    Print line of char.

    :param num: number of character in this line
    :type num : int
    :param char: character
    :type char : str
    :return: None
    """
    print(char * num)


def convert_bytes(num):
    """
    Convert num to idiomatic byte unit.

    :param num: the input number.
    :type num: int
    :return: str
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def filesize(fileaddr):  # pragma: no cover
    """
    Calculate output file size.

    :param fileaddr: file addresses
    :type fileaddr: str
    :return: file size for print as string
    """
    file_info = os.stat(fileaddr)
    file_size = file_info.st_size
    print("Graph File Size : " + convert_bytes(file_size))


def logger(vertices_number, edge_number, file_name, elapsed_time):
    """
    Save generated graphs log.

    :param vertices_number: number of vertices
    :type vertices_number:int
    :param edge_number: number of edges
    :type edge_number: int
    :param file_name: file name
    :type file_name: str
    :param elapsed_time: elapsed time
    :type elapsed_time : str
    :return:  None
    """
    try:
        with open("logfile.log", "a") as file:
            file.write(str(datetime.datetime.now()) + "\n")
            file.write("Filename : " + file_name + "\n")
            file.write("Vertices : " + str(vertices_number) + "\n")
            file.write("Edges : " + str(edge_number) + "\n")
            file.write("Elapsed Time : " + str(elapsed_time) + "\n")
            file.write("-------------------------------\n")
    except Exception:
        print(PYRGG_LOGGER_ERROR_MESSAGE)


def time_convert(input_string):
    """
    Convert input_string from sec to DD,HH,MM,SS format.

    :param input_string: input time string in sec
    :type input_string: str
    :return: converted time as str
    """
    sec = float(input_string)
    days, sec = divmod(sec, 24 * 3600)
    hours, sec = divmod(sec, 3600)
    minutes, sec = divmod(sec, 60)
    return ", ".join([
        "{:02.0f} days".format(days),
        "{:02.0f} hour".format(hours),
        "{:02.0f} minutes".format(minutes),
        "{:02.0f} seconds".format(sec),
    ])


def input_filter(input_dict):
    """
    Filter input data.

    :param input_dict: input dictionary
    :type input_dict: dict
    :return: filtered data as dict
    """
    filtered_dict = input_dict.copy()
    if filtered_dict["min_edge"] < 0:
        filtered_dict["min_edge"] = -1 * filtered_dict["min_edge"]
    if filtered_dict["max_edge"] < 0:
        filtered_dict["max_edge"] = -1 * filtered_dict["max_edge"]
    if filtered_dict["min_weight"] > filtered_dict["max_weight"]:
        temp = filtered_dict["min_weight"]
        filtered_dict["min_weight"] = filtered_dict["max_weight"]
        filtered_dict["max_weight"] = temp
    if filtered_dict["min_edge"] > filtered_dict["max_edge"]:
        temp = filtered_dict["min_edge"]
        filtered_dict["min_edge"] = filtered_dict["max_edge"]
        filtered_dict["max_edge"] = temp
    filtered_dict["max_edge"] = min(
        filtered_dict["max_edge"],
        filtered_dict["vertices"])
    filtered_dict["min_edge"] = min(
        filtered_dict["min_edge"],
        filtered_dict["vertices"])
    if filtered_dict["sign"] not in [1, 2]:
        filtered_dict["sign"] = 2
    if filtered_dict["direct"] not in [1, 2]:
        filtered_dict["direct"] = 1
    if filtered_dict["self_loop"] not in [1, 2]:
        filtered_dict["self_loop"] = 1
    if filtered_dict["multigraph"] not in [1, 2]:
        filtered_dict["multigraph"] = 1
    if filtered_dict["output_format"] not in list(
            range(1, len(SUFFIX_MENU) + 1)):
        filtered_dict["output_format"] = 1
    return filtered_dict


def get_input(input_func=input):
    """
    Get input from user and return as dictionary.

    :param input_func : input function
    :type input_func : function object
    :return: inputs as dict
    """
    result_dict = {
        "file_name": "",
        "vertices": 0,
        "max_weight": 1,
        "min_weight": 1,
        "min_edge": 0,
        "max_edge": 0,
        "sign": 1,
        "output_format": 1,
        "weight": 1,
        "direct": 1,
        "self_loop": 1,
        "multigraph": 1,
    }

    result_dict = _update_using_first_menu(result_dict, input_func)
    result_dict = _update_using_second_menu(result_dict, input_func)
    return input_filter(result_dict)


def _update_using_first_menu(result_dict, input_func):
    """
    Update result_dict using user input from the first menu.

    :param result_dict: result data
    :type result_dict: dict
    :param input_func : input function
    :type input_func : function object
    :return: result_dict as dict
    """
    MENU_ITEMS_KEYS1 = sorted(list(MENU_ITEMS1.keys()))
    for item in MENU_ITEMS_KEYS1:
        while True:
            try:
                if item != "file_name":
                    result_dict[item] = int(input_func(MENU_ITEMS1[item]))
                else:
                    result_dict[item] = input_func(MENU_ITEMS1[item])
            except Exception:
                print(PYRGG_INPUT_ERROR_MESSAGE)
            else:
                break
    return result_dict


def _update_using_second_menu(result_dict, input_func):
    """
    Update result_dict using user input from the second menu.

    :param result_dict: result data
    :type result_dict: dict
    :param input_func : input function
    :type input_func : function object
    :return: result_dict as dict
    """
    MENU_ITEMS_KEYS2 = sorted(list(MENU_ITEMS2.keys()))
    for item in MENU_ITEMS_KEYS2:
        if result_dict["weight"] != 1 and item in ["max_weight", "min_weight"]:
            continue
        while True:
            try:
                user_input = input_func(MENU_ITEMS2[item])
                if item in ["max_weight", "min_weight"]:
                    result_dict[item] = weight_str_to_number(user_input)
                else:
                    result_dict[item] = int(user_input)
            except Exception:
                print(PYRGG_INPUT_ERROR_MESSAGE)
            else:
                break
    return result_dict


def sign_gen():
    """
    Return random sign.

    :return: 1 or -1
    """
    flag = random_system.randint(0, 1)
    if flag == 0:
        return 1
    return -1


def branch_gen(
        vertex_index,
        random_edge,
        min_weight,
        max_weight,
        sign,
        direct,
        self_loop,
        multigraph,
        all_vertices,
        used_vertices):
    """
    Generate branch and weight vector of each vertex.

    :param vertex_index: origin vertex index
    :type vertex_index: int
    :param random_edge: number of vertex edges
    :type random_edge: int
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :param self_loop: self loop flag
    :type self_loop: int
    :param multigraph: multigraph flag
    :type multigraph: int
    :param all_vertices : all vertices list
    :type all_vertices : list
    :param used_vertices: used vertices dictionary
    :type used_vertices: dict
    :return: branch and weight list
    """
    index = 0
    branch_list = []
    weight_list = []
    reference_vertices = all_vertices[:]
    max_weight_flag = is_float(max_weight)
    min_weight_flag = is_float(min_weight)
    weight_float_flag = min_weight_flag or max_weight_flag
    random_unit = random_system.randint
    weight_precision = max(
        get_precision(max_weight),
        get_precision(min_weight))
    if weight_float_flag:
        random_unit = random_system.uniform
    if direct == 2 and (
            vertex_index in used_vertices.keys()) and multigraph == 1:
        reference_vertices = list(
            set(reference_vertices) - set(used_vertices[vertex_index]))
    if self_loop == 2 and vertex_index in reference_vertices:
        reference_vertices.remove(vertex_index)
    threhold = min(random_edge, len(reference_vertices))
    while (index < threhold):
        random_tail = random_system.choice(reference_vertices)
        if direct == 2:
            if random_tail in used_vertices.keys():
                used_vertices[random_tail].append(vertex_index)
            else:
                used_vertices[random_tail] = [vertex_index]
        if sign == 2:
            random_weight = random_unit(min_weight, max_weight)
        else:
            random_weight = sign_gen() * random_unit(min_weight, max_weight)
        if weight_float_flag:
            random_weight = round(random_weight, weight_precision)
        branch_list.append(random_tail)
        weight_list.append(random_weight)
        index += 1
        if multigraph == 1:
            reference_vertices.remove(random_tail)
    return [branch_list, weight_list]


def edge_gen(
        vertices_number,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct,
        self_loop,
        multigraph):
    """
    Generate each vertex connection number.

    :param vertices_number: number of vertices
    :type vertices_number: int
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :param self_loop: self loop flag
    :type self_loop: int
    :param multigraph: multigraph flag
    :type multigraph: int
    :return: list of dicts
    """
    temp = 0
    vertices_id = list(range(1, vertices_number + 1))
    vertices_edge = []
    weight_list = []
    used_vertices = {}
    random_edge = min_edge
    for i in vertices_id:
        if min_edge != max_edge:
            random_edge = random_system.randint(min_edge, max_edge)
        temp_list = branch_gen(
            i,
            random_edge,
            min_weight,
            max_weight,
            sign,
            direct,
            self_loop,
            multigraph,
            vertices_id,
            used_vertices)
        vertices_edge.append(temp_list[0])
        weight_list.append(temp_list[1])
        temp = temp + random_edge
    return [dict(zip(vertices_id, vertices_edge)),
            dict(zip(vertices_id, weight_list)), temp]


def json_to_yaml(filename):
    """
    Convert json file to yaml file.

    :param filename: filename
    :type filename: str
    :return: None
    """
    try:
        with open(filename + ".json", "r") as json_file:
            json_data = json.loads(json_file.read())
            with open(filename + ".yaml", "w") as yaml_file:
                yaml.safe_dump(json_data, yaml_file, default_flow_style=False)
    except FileNotFoundError:
        print(PYRGG_FILE_ERROR_MESSAGE)


def json_to_pickle(filename):
    """
    Convert json file to pickle file.

    :param filename: filename
    :type filename: str
    :return: None
    """
    try:
        with open(filename + ".json", "r") as json_file:
            json_data = json.loads(json_file.read())
            with open(filename + ".p", "wb") as pickle_file:
                pickle.dump(json_data, pickle_file)
    except FileNotFoundError:
        print(PYRGG_FILE_ERROR_MESSAGE)
