# -*- coding: utf-8 -*-
"""Pyrgg module."""
import random
import os
import datetime
import sys
import yaml
import json
import pickle
from pyrgg.params import *

# random_system=random.SystemRandom()
random_system = random


def left_justify(words, width):
    """
    Left justify words.

    :param words: list of words
    :type words : list
    :param width: width of each line
    :type width: int
    :return: left justified words as list
    """
    return ' '.join(words).ljust(width)


def justify(words, width):
    """
    Justify input words.

    :param words: list of words
    :type words : list
    :param width: width of each line
    :type width : int
    :return: list of justified words as list
    """
    line = []
    col = 0
    for word in words:
        if line and col + len(word) > width:
            if len(line) == 1:
                yield left_justify(line, width)
            else:
                # After n + 1 spaces are placed between each pair of
                # words, there are r spaces left over; these result in
                # wider spaces at the left.
                n, r = divmod(width - col + 1, len(line) - 1)
                narrow = ' ' * (n + 1)
                if r == 0:
                    yield narrow.join(line)
                else:
                    wide = ' ' * (n + 2)
                    yield wide.join(line[:r] + [narrow.join(line[r:])])
            line, col = [], 0
        line.append(word)
        col += len(word) + 1
    if line:
        yield left_justify(line, width)


def description_print():
    """
    Print justified description for overview in console.

    :return: None
    """
    print(PYRGG_LINKS)
    line(40)
    print("\n")
    print("\n".join(justify(PYRGG_DESCRIPTION.split(), 100)))
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
        file = open("logfile.log", "a")
        file.write(str(datetime.datetime.now()) + "\n")
        file.write("Filename : " + file_name + "\n")
        file.write("Vertices : " + str(vertices_number) + "\n")
        file.write("Edges : " + str(edge_number) + "\n")
        file.write("Elapsed Time : " + str(elapsed_time) + "\n")
        file.write("-------------------------------\n")
        file.close()
    except Exception:
        print("[Error] Logger Faild!")


def zero_insert(input_string):
    """
    Get a string as input if input is one digit add a zero.

    :param input_string: input digit az string
    :type input_string: str
    :return: modified output as str
    """
    if len(input_string) == 1:
        return "0" + input_string
    return input_string


def time_convert(input_string):
    """
    Convert input_string from sec to DD,HH,MM,SS format.

    :param input_string: input time string  in sec
    :type input_string: str
    :return: converted time as str
    """
    input_sec = float(input_string)
    input_minute = input_sec // 60
    input_sec = int(input_sec - input_minute * 60)
    input_hour = input_minute // 60
    input_minute = int(input_minute - input_hour * 60)
    input_day = int(input_hour // 24)
    input_hour = int(input_hour - input_day * 24)
    return zero_insert(str(input_day)) + " days, " + zero_insert(str(input_hour)) + " hour, " + \
        zero_insert(str(input_minute)) + " minutes, " + zero_insert(str(input_sec)) + " seconds"


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
    if filtered_dict["output_format"] not in list(range(1, 10)):
        filtered_dict["output_format"] = 1
    return filtered_dict


def get_input(input_func=input):
    """
    Get input from user and return as dictionary.

    :param input_func : input function
    :type input_func : function object
    :return: inputs as dict
    """
    try:
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
            "direct": 1}
        MENU_ITEMS_KEYS1 = sorted(list(MENU_ITEMS1.keys()))
        MENU_ITEMS_KEYS2 = sorted(list(MENU_ITEMS2.keys()))
        for item in MENU_ITEMS_KEYS1:
            exit_flag = False
            while not exit_flag:
                try:
                    if item != "file_name":
                        result_dict[item] = int(input_func(MENU_ITEMS1[item]))
                    else:
                        result_dict[item] = input_func(MENU_ITEMS1[item])
                    exit_flag = True
                except Exception:
                    print("[Error] Bad Input!")

        for item in MENU_ITEMS_KEYS2:
            exit_flag = False
            if result_dict["weight"] != 1 and (
                    item == "max_weight" or item == "min_weight"):
                continue
            while not exit_flag:
                try:
                    result_dict[item] = int(input_func(MENU_ITEMS2[item]))
                    exit_flag = True
                except Exception:
                    print("[Error] Bad Input!")
        result_dict = input_filter(result_dict)
        return result_dict
    except Exception:
        print("[Error] Bad Input!")
        sys.exit()


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
    :param all_vertices : all vertices list
    :type all_vertices : list
    :param used_vertices: used vertices dictionary
    :type used_vertices: dict
    :return: branch and weight list
    """
    index = 0
    branch_list = []
    weight_list = []
    reference_vertices = all_vertices
    if direct == 2 and (vertex_index in used_vertices.keys()):
        reference_vertices = list(
            set(reference_vertices) - set(used_vertices[vertex_index]))
    threhold = min(random_edge, len(reference_vertices))
    while (index < threhold):
        random_tail = random_system.choice(reference_vertices)
        if direct == 2:
            if random_tail in used_vertices.keys():
                used_vertices[random_tail].append(vertex_index)
            else:
                used_vertices[random_tail] = [vertex_index]
        if sign == 2:
            random_weight = random_system.randint(min_weight, max_weight)
        else:
            random_weight = sign_gen() * random_system.randint(min_weight, max_weight)
        if random_tail not in branch_list:
            branch_list.append(random_tail)
            weight_list.append(random_weight)
            index += 1
    return [branch_list, weight_list]


def edge_gen(
        vertices_number,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct):
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
            vertices_id,
            used_vertices)
        vertices_edge.append(temp_list[0])
        weight_list.append(temp_list[1])
        temp = temp + random_edge
    return [dict(zip(vertices_id, vertices_edge)),
            dict(zip(vertices_id, weight_list)), temp]


def dimacs_init(
        file,
        file_name,
        min_weight,
        max_weight,
        vertices,
        edge,
        min_edge,
        max_edge,
        direct):
    """
    Initialize dimacs output file.

    :param file: output file object
    :param file_name: file name
    :type file_name: str
    :type file: file_object
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: vertices number
    :type vertices: int
    :param edge:  edge number
    :type edge: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :return: None
    """
    file.write(
        DIMACS_FIX.format(
            file_name,
            str(vertices),
            str(edge),
            str(max_weight),
            str(min_weight),
            str(min_edge),
            str(max_edge)))


def dimacs_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct):
    """
    Create output file and fill in.

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :return: edge_number as int
    """
    file = open(file_name + ".gr", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    dimacs_init(
        file,
        file_name,
        min_weight,
        max_weight,
        vertices,
        edge_number,
        min_edge,
        max_edge,
        direct)
    for i in edge_dic.keys():
        for j, value in enumerate(edge_dic[i]):
            file.write("a " + str(i) + " " + str(value) +
                       " " + str(weight_dic[i][j]) + "\n")
    file.close()
    return edge_number


def json_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct):
    """
    Create output file in json format.

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :return: edge_number as int
    """
    file = open(file_name + ".json", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    nodes = '\t\t\t"nodes":[\n'
    edges = '\t\t\t"edges":[\n'
    for i in edge_dic.keys():
        nodes = nodes + '\t\t\t{\n\t\t\t\t' + \
            '"id": ' + '"' + str(i) + '"\n\t\t\t},\n'
        for j, value in enumerate(edge_dic[i]):
            edges = edges + '\t\t\t{\n\t\t\t\t"source": ' + '"' + str(i) + '",\n\t\t\t\t' + '"target": ' + '"' + str(
                value) + '",\n\t\t\t\t' + '"weight": ' + '"' + str(weight_dic[i][j]) + '"\n\t\t\t},\n'
    nodes = nodes[:-2] + "\n\t\t],\n"
    edges = edges[:-2] + "\n\t\t]\n\t}\n}"
    file.write('{\n\t"graph": {\n')
    file.write(nodes)
    file.write(edges)
    file.close()
    return edge_number


def csv_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct):
    """
    Create output file in csv format.

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :return: edge_number as int
    """
    file = open(file_name + ".csv", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    for i in edge_dic.keys():
        for j, value in enumerate(edge_dic[i]):
            file.write(str(i) + "," + str(value) + "," +
                       str(weight_dic[i][j]) + "\n")
    file.close()
    return edge_number


def json_to_yaml(filename):
    """
    Convert json file to yaml file.

    :param filename: filename
    :type filename: str
    :return: None
    """
    try:
        file = open(filename + ".json", "r")
        json_data = json.loads(file.read())
        yaml_file = open(filename + ".yaml", "w")
        yaml.safe_dump(json_data, yaml_file, default_flow_style=False)
        file.close()
        yaml_file.close()
    except FileNotFoundError:
        print("[Error] Bad Input File")


def json_to_pickle(filename):
    """
    Convert json file to yaml file.

    :param filename: filename
    :type filename: str
    :return: None
    """
    try:
        file = open(filename + ".json", "r")
        pickle_file = open(filename + ".p", "wb")
        json_data = json.loads(file.read())
        pickle.dump(json_data, pickle_file)
        pickle_file.close()
        file.close()
    except FileNotFoundError:
        print("[Error] Bad Input File")


def wel_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct):
    """
    Create output file in wel format.

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :return: edge_number as int
    """
    file = open(file_name + ".wel", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    for i in edge_dic.keys():
        for j, value in enumerate(edge_dic[i]):
            file.write(str(i) + " " + str(value) + " " +
                       str(weight_dic[i][j]) + "\n")
    file.close()
    return edge_number


def lp_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct):
    """
    Create output file in ASP format.

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :return: edge_number as int
    """
    file = open(file_name + ".lp", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    nodes = ''
    edges = ''
    for i in edge_dic.keys():
        nodes = nodes + 'node(' + str(i) + ").\n"
        for j, value in enumerate(edge_dic[i]):
            edges = edges + \
                'edge(' + str(i) + "," + str(value) + "," + str(weight_dic[i][j]) + ").\n"
    file.write(nodes)
    file.write(edges)
    file.close()
    return edge_number


def tgf_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct):
    """
    Create output file in Trivial Graph Format (TGF).

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :return: edge_number as int
    """
    file = open(file_name + ".tgf", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    nodes = ''
    edges = ''
    for i in edge_dic.keys():
        nodes = nodes + str(i) + "\n"
        for j, value in enumerate(edge_dic[i]):
            edges = edges + str(i) + " " + str(value) + \
                " " + str(weight_dic[i][j]) + "\n"
    file.write(nodes)
    file.write("#\n")
    file.write(edges)
    file.close()
    return edge_number


def dl_maker(
        file_name,
        min_weight,
        max_weight,
        vertices,
        min_edge,
        max_edge,
        sign,
        direct):
    """
    Create output file in UCINET DL Format.

    :param file_name: file name
    :type file_name: str
    :param min_weight: weight min range
    :type min_weight: int
    :param max_weight: weight max range
    :type max_weight: int
    :param vertices: number of vertices
    :type vertices: int
    :param min_edge : minimum edge number
    :type min_edge : int
    :param max_edge : maximum edge number
    :type max_edge : int
    :param sign: weight sign flag
    :type sign: int
    :param direct: directed and undirected graph flag
    :type direct: int
    :return: edge_number as int
    """
    file = open(file_name + ".dl", "w")
    dicts = edge_gen(
        vertices,
        min_weight,
        max_weight,
        min_edge,
        max_edge,
        sign,
        direct)
    edge_dic = dicts[0]
    weight_dic = dicts[1]
    edge_number = dicts[2]
    edges = ''
    for i in edge_dic.keys():
        for j, value in enumerate(edge_dic[i]):
            edges = edges + str(i) + " " + str(value) + \
                " " + str(weight_dic[i][j]) + "\n"
    file.write("dl\nformat=edgelist1\nn=" + str(vertices) + "\ndata:\n")
    file.write(edges)
    file.close()
    return edge_number


def print_test(a):
    """
    Added for get_input parameter injection testing.

    :param a: input
    :type a: int
    :return: len(a) as str
    """
    return str(len(a))
