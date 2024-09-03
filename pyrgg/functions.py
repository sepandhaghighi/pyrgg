# -*- coding: utf-8 -*-
"""Pyrgg functions module."""
import os
from random import randint
from json import loads as json_loads
from json import dump as json_dump
from pickle import dump as pickle_dump
from yaml import safe_dump as yaml_dump
import pyrgg.params


def is_weighted(max_weight, min_weight, signed):
    """
    Check the graph is weighted or not.

    :param max_weight: maximum weight
    :type max_weight: int
    :param min_weight: minimum weight
    :type min_weight: int
    :param signed: weight sign flag
    :type signed: bool
    :return: result as bool
    """
    if max_weight == min_weight and min_weight == 0:
        return False
    if max_weight == min_weight and min_weight == 1 and not signed:
        return False
    return True


def get_min_max_weight(weight_dic):
    """
    Get minimum and maximum weight values.

    :param weight_dic: weight dictionary
    :type weight_dic: dict
    :return: minimum and maximum weight values
    """
    all_weights = [abs(w) for weights in weight_dic.values() for w in weights]
    return min(all_weights), max(all_weights)


def is_signed(weight_dic): # pragma: no cover
    """
    Check if the graph is signed.

    :param weight_dic: weight dictionary
    :type weight_dic: dict
    :return: signed flag
    """
    return any([any([w < 0 for w in weights]) for weights in weight_dic.values()])


def has_self_loop(edge_dic): # pragma: no cover
    """
    Check if the graph has self loops.
    
    :param edge_dic: edge dictionary
    :type edge_dic: dict
    :return: self looped flag
    """
    return any([v in edges for v, edges in edge_dic.items()])


def is_multigraph(edge_dic):
    """
    Check if the graph is a multigraph.

    :param edge_dic: edge dictionary
    :type edge_dic: dict
    :return: multigraph flag
    """
    return any([len(set(edges)) != len(edges) for edges in edge_dic.values()])


def get_precision(input_number):
    """
    Return precision of input number.

    :param input_number: input number
    :type input_number: float
    :return: precision as int
    """
    try:
        number_str = str(input_number)
        _, decimal_part = number_str.split(".")
        return len(decimal_part)
    except Exception:
        return 0


def threshold_calc(min_edge, max_edge, vertex_degree):
    """
    Calculate threshold for branch_gen_pyrgg function.

    :param min_edge: minimum number of edges (connected to each vertex)
    :type min_edge: int
    :param max_edge: maximum number of edges (connected to each vertex)
    :type max_edge: int
    :param vertex_degree: vertex degree
    :type vertex_degree: int
    :return: threshold as int
    """
    threshold = min_edge
    lower_limit = 0
    upper_limit = max_edge - vertex_degree
    if vertex_degree < min_edge:
        lower_limit = min_edge - vertex_degree
    if upper_limit > lower_limit:
        threshold = randint(lower_limit, upper_limit)
    return threshold


def is_float(input_number):
    """
    Check input for float conversion.

    :param input_number: input number
    :type input_number: float or int or str
    :return: result as bool
    """
    try:
        _, decimal_part = divmod(float(input_number), 1)
    except TypeError:
        return False
    else:
        return True if decimal_part else False


def handle_string(string):
    """
    Handle string and raise ValueError if it is empty.

    :param string: input string
    :type string: str
    :return: result as str
    """
    if string == "":
        raise ValueError
    return string


def handle_pos_int(input_number):
    """
    Handle input number and raise ValueError if it is negative.

    :param input_number: input number
    :type input_number: float or int or str
    :return: result as int
    """
    val = int(input_number)
    if val < 0:
        raise ValueError
    return val


def handle_str_to_number(string):
    """
    Convert string to float or int.

    :param string: input string
    :type string: str
    :return: result as float or int
    """
    return float(string) if is_float(string) else int(string)


def handle_str_prob(string):
    """
    Convert string to float and raise ValueError if string is invalid.

    :param string: input string
    :type string: str
    :return: result as float
    """
    val = handle_str_to_number(string)
    if val < 0:
        raise ValueError
    if val > 1:
        raise ValueError
    return val


def handle_str_to_bool(string):
    """
    Convert 0/1 string to bool and raise ValueError if string is invalid.

    :param string: input string
    :type string: str
    :return: result as bool
    """
    val = int(string)
    if val not in [0, 1]:
        raise ValueError
    return bool(val)


def handle_output_format(string):
    """
    Convert string to output format index.

    :param string: input string
    :type string: str
    :return: output format index as int
    """
    output_format = handle_pos_int(string)
    if output_format not in pyrgg.params.SUFFIX_MENU:
        raise ValueError
    return output_format


def handle_engine(string):
    """
    Convert string to engine index.

    :param string: input string
    :type string: str
    :return: engine index as int
    """
    engine = handle_pos_int(string)
    if engine not in pyrgg.params.ENGINE_MENU:
        raise ValueError
    return engine


ITEM_HANDLERS = {
    "file_name": handle_string,
    "output_format": handle_output_format,
    "weight": handle_str_to_bool,
    "engine": handle_engine,
    "vertices": handle_pos_int,
    "number_of_files": handle_pos_int,
    "max_weight": handle_str_to_number,
    "min_weight": handle_str_to_number,
    "min_edge": handle_pos_int,
    "max_edge": handle_pos_int,
    "sign": handle_str_to_bool,
    "direct": handle_str_to_bool,
    "self_loop": handle_str_to_bool,
    "multigraph": handle_str_to_bool,
    "config": handle_str_to_bool,
    "probability": handle_str_prob,
}


def description_print():
    """
    Print justified description for overview in console.

    :return: None
    """
    print(pyrgg.params.PYRGG_LINKS)
    line(40)
    print("\n")
    print(pyrgg.params.PYRGG_DESCRIPTION)
    print("\n")
    line(40)


def line(num=11, char="#"):
    """
    Print line of char.

    :param num: number of character in this line
    :type num : int
    :param char: character
    :type char: str
    :return: None
    """
    print(char * num)


def convert_bytes(num):
    """
    Convert num to idiomatic byte unit.

    :param num: the input number.
    :type num: int
    :return: result as str
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


def time_convert(input_time):
    """
    Convert input_time from sec to DD,HH,MM,SS format.

    :param input_time: input time in sec
    :type input_time: float
    :return: converted time as str
    """
    postfix_dict = {"s": "second", "d": "day", "h": "hour", "m": "minute"}
    value_dict = {"s": 0, "d": 0, "h": 0, "m": 0}
    value_dict["s"] = float(input_time)
    value_dict["d"], value_dict["s"] = divmod(value_dict["s"], 24 * 3600)
    value_dict["h"], value_dict["s"] = divmod(value_dict["s"], 3600)
    value_dict["m"], value_dict["s"] = divmod(value_dict["s"], 60)
    for i in postfix_dict:
        if value_dict[i] != 1:
            postfix_dict[i] += "s"
    return ", ".join([
        "{0:02.0f} {1}".format(value_dict["d"], postfix_dict["d"]),
        "{0:02.0f} {1}".format(value_dict["h"], postfix_dict["h"]),
        "{0:02.0f} {1}".format(value_dict["m"], postfix_dict["m"]),
        "{0:02.0f} {1}".format(value_dict["s"], postfix_dict["s"]),
    ])


def input_filter(input_dict):
    """
    Filter input data.

    :param input_dict: input dictionary
    :type input_dict: dict
    :return: filtered data as dict
    """
    filtered_dict = input_dict.copy()
    edge_upper_threshold = filtered_dict["vertices"]
    for key in ["min_edge", "max_edge", "vertices"]:
        if filtered_dict[key] < 0:
            filtered_dict[key] *= -1

    if filtered_dict["min_weight"] > filtered_dict["max_weight"]:
        filtered_dict["min_weight"], filtered_dict["max_weight"] = (
            filtered_dict["max_weight"], filtered_dict["min_weight"]
        )

    if filtered_dict["min_edge"] > filtered_dict["max_edge"]:
        filtered_dict["min_edge"], filtered_dict["max_edge"] = (
            filtered_dict["max_edge"], filtered_dict["min_edge"]
        )

    if not filtered_dict["self_loop"]:
        edge_upper_threshold -= 1

    if not filtered_dict["multigraph"]:
        for key in ["min_edge", "max_edge"]:
            filtered_dict[key] = min(filtered_dict[key], edge_upper_threshold)

    return filtered_dict


def get_input(input_func=input):
    """
    Get input from user and return as dictionary.

    :param input_func: input function
    :type input_func: function object
    :return: inputs as dict
    """
    result_dict = {
        "file_name": "",
        "number_of_files": 1,
        "vertices": 0,
        "max_weight": 1,
        "min_weight": 1,
        "min_edge": 0,
        "max_edge": 0,
        "sign": True,
        "output_format": 1,
        "weight": True,
        "engine": 1,
        "direct": True,
        "self_loop": True,
        "multigraph": False,
        "config": False,
        "probability": 0.5,
    }

    result_dict = _update_using_menu(result_dict, input_func)
    result_dict = _update_with_engine_params(
        result_dict, input_func, pyrgg.params.ENGINE_PARAM_MAP[result_dict['engine']])
    return input_filter(result_dict)


def _update_using_menu(result_dict, input_func):
    """
    Update result_dict using user input from the menu.

    :param result_dict: result data
    :type result_dict: dict
    :param input_func: input function
    :type input_func: function object
    :return: result_dict as dict
    """
    for index in sorted(pyrgg.params.MENU_ITEMS):
        item1, item2 = pyrgg.params.MENU_ITEMS[index]
        while True:
            try:
                result_dict[item1] = ITEM_HANDLERS[item1](
                    input_func(item2)
                )
            except Exception:
                print(pyrgg.params.PYRGG_INPUT_ERROR_MESSAGE)
            else:
                break
    return result_dict


def _update_with_engine_params(result_dict, input_func, engine_params):
    """
    Update result_dict using user input based on given engine requirements.

    :param result_dict: result data
    :type result_dict: dict
    :param input_func: input function
    :type input_func: function object
    :param engine_params: engine parameters
    :type engine_params: dict
    :return: result_dict as dict
    """
    for index in sorted(engine_params):
        item1, item2 = engine_params[index]
        if not result_dict["weight"] and item1 in ["max_weight", "min_weight"]:
            continue
        while True:
            try:
                result_dict[item1] = ITEM_HANDLERS[item1](
                    input_func(item2)
                )
            except Exception:
                print(pyrgg.params.PYRGG_INPUT_ERROR_MESSAGE)
            else:
                break
    return result_dict


def json_to_yaml(filename):
    """
    Convert json file to yaml file.

    :param filename: filename
    :type filename: str
    :return: None
    """
    try:
        with open(filename + ".json", "r") as json_file:
            json_data = json_loads(json_file.read())
            with open(filename + ".yaml", "w") as yaml_file:
                yaml_dump(json_data, yaml_file, default_flow_style=False)
    except FileNotFoundError:
        print(pyrgg.params.PYRGG_YAML_ERROR_MESSAGE)


def json_to_pickle(filename):
    """
    Convert json file to pickle file.

    :param filename: filename
    :type filename: str
    :return: None
    """
    try:
        with open(filename + ".json", "r") as json_file:
            json_data = json_loads(json_file.read())
            with open(filename + ".p", "wb") as pickle_file:
                pickle_dump(json_data, pickle_file)
    except FileNotFoundError:
        print(pyrgg.params.PYRGG_PICKLE_ERROR_MESSAGE)


def save_config(input_dict):
    """
    Save input_dict as the generation config.

    :param input_dict: input data
    :type input_dict: dict
    :return: path to file as str
    """
    try:
        input_dict_temp = input_dict.copy()
        input_dict_temp['engine'] = pyrgg.params.ENGINE_MENU[input_dict_temp['engine']]
        input_dict_temp['pyrgg_version'] = pyrgg.params.PYRGG_VERSION
        input_dict_temp['output_format'] = pyrgg.params.OUTPUT_FORMAT[input_dict_temp['output_format']]
        fname = pyrgg.params.CONFIG_FILE_FORMAT.format(
            input_dict_temp['file_name'])
        with open(fname, "w") as json_file:
            json_dump(input_dict_temp, json_file, indent=2)
        return os.path.abspath(fname)
    except BaseException:
        print(pyrgg.params.PYRGG_CONFIG_SAVE_ERROR_MESSAGE)


def load_config(path):
    """
    Load config based on given path.

    :param path: path to config file
    :type path: str
    :return: input data as dict
    """
    try:
        with open(path, "r") as json_file:
            config = json_loads(json_file.read())
            config['output_format'] = pyrgg.params.OUTPUT_FORMAT_INV[config['output_format']]
            config['engine'] = pyrgg.params.ENGINE_MENU_INV[config['engine']]
            return input_filter(config)
    except BaseException:
        print(pyrgg.params.PYRGG_CONFIG_LOAD_ERROR_MESSAGE)


def _print_select_config(configs, input_func=input):
    """
    Print configs in current directory and get input from user.

    :param configs: configs path
    :type configs: list
    :param input_func: input function
    :type input_func: function object
    :return: input data as dict
    """
    if len(configs) == 0:
        return None
    print(pyrgg.params.PYRGG_CONFIG_LIST_MESSAGE)
    for i, config in enumerate(configs):
        print("[{}] - {}".format(i + 1, config))
    key = input_func(pyrgg.params.PYRGG_CONFIG_LOAD_MESSAGE)
    try:
        return load_config(configs[int(key) - 1])
    except BaseException:
        return None


def check_for_config(input_func=input):
    """
    Check for config files in source directory.

    :param input_func: input function
    :type input_func: function object
    :return: input data as dict
    """
    configs = []
    for filename in os.listdir(pyrgg.params.SOURCE_DIR):
        file = os.path.join(pyrgg.params.SOURCE_DIR, filename)
        if os.path.isfile(file) and filename.endswith(
                pyrgg.params.CONFIG_FILE_FORMAT.format("")):
            configs.append(file)
    return _print_select_config(configs, input_func)
