# -*- coding: utf-8 -*-
"""
>>> from pyrgg.functions import *
>>> import pyrgg.params
>>> import random
>>> import os
>>> os.environ["PYRGG_TEST_MODE"] = "1"
>>> description_print()
<BLANKLINE>
Webpage : https://www.pyrgg.site
Repository : https://github.com/sepandhaghighi/pyrgg
Paper : https://doi.org/10.21105/joss.00331
* If you use Pyrgg in your research, please cite our paper
<BLANKLINE>
########################################
<BLANKLINE>
<BLANKLINE>
PyRGG is a user-friendly synthetic random graph generator that is written in Python and supports multiple graph
file formats, such as DIMACS-Graph files. It can generate graphs of various sizes and is specifically designed to
create input files for a wide range of graph-based research applications, including testing, benchmarking, and
performance analysis of graph processing frameworks. PyRGG is aimed at computer scientists who are studying graph
algorithms and graph processing frameworks.
<BLANKLINE>
<BLANKLINE>
########################################
>>> result = input_filter({"file_name": "test","vertices": 5,"max_weight": 1000,"min_weight":455,"min_edge": -45,"max_edge": -11,"sign": False,"output_format": 1, "direct": False,"self_loop": True,"multigraph":False,"number_of_files":2,"engine":1})
>>> result == {'output_format': 1, 'min_weight': 455, 'min_edge': 5, 'max_edge': 5, 'file_name': 'test', 'vertices': 5, 'max_weight': 1000, 'sign': False, "direct": False,"self_loop": True,"multigraph":False,"number_of_files":2,"engine":1}
True
>>> result = input_filter({"file_name": "test","vertices": 5,"max_weight": 1000,"min_weight":455,"min_edge": -45,"max_edge": -11,"sign": False,"output_format": 1, "direct": False,"self_loop": False,"multigraph":False,"number_of_files":10,"engine":1})
>>> result == {'output_format': 1, 'min_weight': 455, 'min_edge': 4, 'max_edge': 4, 'file_name': 'test', 'vertices': 5, 'max_weight': 1000, 'sign': False, "direct": False,"self_loop": False,"multigraph":False,"number_of_files":10,"engine":1}
True
>>> result = input_filter({"file_name": "test","vertices": -5,"max_weight": 1000,"min_weight":455,"min_edge": -45,"max_edge": -11,"sign": False,"output_format": 1, "direct": False,"self_loop": False,"multigraph":True,"number_of_files":1,"engine":1})
>>> result == {'output_format': 1, 'min_weight': 455, 'min_edge': 11, 'max_edge': 45, 'file_name': 'test', 'vertices': 5, 'max_weight': 1000, 'sign': False, "direct": False,"self_loop": False,"multigraph":True,"number_of_files":1,"engine":1}
True
>>> result = input_filter({"file_name": "test","vertices": -5,"max_weight": 1000,"min_weight":455,"min_edge": -45,"max_edge": -11,"sign": False,"output_format": 1, "direct": False,"self_loop": False,"multigraph":True,"number_of_files":1,"engine":1})
>>> result == {'output_format': 1, 'min_weight': 455, 'min_edge': 11, 'max_edge': 45, 'file_name': 'test', 'vertices': 5, 'max_weight': 1000, 'sign': False, "direct": False,"self_loop": False,"multigraph":True,"number_of_files":1,"engine":1}
True
>>> result = input_filter({"file_name": "test2","vertices": 23,"max_weight": 2,"min_weight": 80,"min_edge": 23,"max_edge": 1,"sign": True,"output_format": 1, "direct": False,"self_loop": True,"multigraph":False,"number_of_files":2,"engine":1})
>>> result == {'min_weight': 2, 'vertices': 23, 'file_name': 'test2', 'max_edge': 23, 'min_edge': 1, 'max_weight': 80, 'output_format': 1, 'sign': True, "direct": False,"self_loop": True,"multigraph":False,"number_of_files":2,"engine":1}
True
>>> convert_bytes(200)
'200.0 bytes'
>>> convert_bytes(6000)
'5.9 KB'
>>> convert_bytes(80000)
'78.1 KB'
>>> time_convert(33)
'00 days, 00 hours, 00 minutes, 33 seconds'
>>> time_convert(15000)
'00 days, 04 hours, 10 minutes, 00 seconds'
>>> time_convert(1)
'00 days, 00 hours, 00 minutes, 01 second'
>>> time_convert(60)
'00 days, 00 hours, 01 minute, 00 seconds'
>>> time_convert(60*60)
'00 days, 01 hour, 00 minutes, 00 seconds'
>>> time_convert(60*60*24)
'01 day, 00 hours, 00 minutes, 00 seconds'
>>> time_convert(60*60*24 + 60*60 + 60 + 1)
'01 day, 01 hour, 01 minute, 01 second'
>>> time_convert(0)
'00 days, 00 hours, 00 minutes, 00 seconds'
>>> time_convert('sadasdasd')
Traceback (most recent call last):
        ...
ValueError: could not convert string to float: 'sadasdasd'
>>> line(12,"*")
************
>>> is_weighted(0,0,False)
False
>>> is_weighted(0,0,True)
False
>>> is_weighted(20,20,False)
True
>>> is_weighted(1,1,False)
False
>>> is_weighted(1,1,True)
True
>>> get_precision(2)
0
>>> get_precision(2.2)
1
>>> get_precision(2.22)
2
>>> get_precision(2.223)
3
>>> handle_str_to_number("20")
20
>>> handle_str_to_number("20.2")
20.2
>>> handle_str_to_bool("1")
True
>>> handle_str_to_bool("3")
Traceback (most recent call last):
        ...
ValueError
>>> handle_str_to_bool("0")
False
>>> handle_str_prob("0.2")
0.2
>>> handle_str_prob("-0.2")
Traceback (most recent call last):
        ...
ValueError
>>> handle_str_prob("1.2")
Traceback (most recent call last):
        ...
ValueError
>>> is_float(10)
False
>>> is_float(10.2)
True
>>> is_float(None)
False
>>> prev_item = ""
>>> input_func_dict = {"vertices":"120","max_weight":"110","min_weight":"0","min_edge":"1","max_edge":"1000","sign":"1","direct":"1","self_loop":"1","multigraph":"0","file_name":"File 1","output_format":"2","weight":"1","error":"120","number_of_files":"3","config":"0","engine":"1"}
>>> def input_func_test(input_data):
...    global prev_item
...    for index in pyrgg.params.MENU_ITEMS:
...        item1, item2 = pyrgg.params.MENU_ITEMS[index]
...        if input_data == item2:
...            if item1 != prev_item:
...                prev_item = item1
...                return input_func_dict[item1]
...            else:
...                return input_func_dict["error"]
...    for index in pyrgg.params.PYRGG_ENGINE_PARAMS:
...        item1, item2 = pyrgg.params.PYRGG_ENGINE_PARAMS[index]
...        if input_data == item2:
...            if item1 != prev_item :
...                prev_item = item1
...                return input_func_dict[item1]
...            else:
...                return input_func_dict["error"]
...    for index in pyrgg.params.ERG_ENGINE_PARAMS:
...        item1, item2 = pyrgg.params.ERG_ENGINE_PARAMS[index]
...        if input_data == item2:
...            if item1 != prev_item :
...                prev_item = item1
...                return input_func_dict[item1]
...            else:
...                return input_func_dict["error"]
...    for index in pyrgg.params.ER_ENGINE_PARAMS:
...        item1, item2 = pyrgg.params.ER_ENGINE_PARAMS[index]
...        if input_data == item2:
...            if item1 != prev_item :
...                prev_item = item1
...                return input_func_dict[item1]
...            else:
...                return input_func_dict["error"]
>>> def input_func_conf_test1(input_data):
...     return "1"
>>> def input_func_conf_test2(input_data):
...     return "2"
>>> input_data = get_input(input_func_test)
>>> input_data["vertices"]
120
>>> input_data["max_weight"]
110
>>> input_data["min_weight"]
0
>>> input_data["min_edge"]
1
>>> input_data["max_edge"]
120
>>> input_data["number_of_files"]
3
>>> input_data["sign"]
True
>>> input_data["weight"]
True
>>> input_data["engine"]
1
>>> prev_item = ""
>>> input_func_dict = {"vertices":"120","max_weight":"110","min_weight":"1.2","min_edge":"10000","max_edge":"2","sign":"1","direct":"1","self_loop":"1","multigraph":"0","file_name":"File 1","output_format":"2","weight":"1","error":"120","number_of_files":"1","config":"1","engine":"1"}
>>> input_data = get_input(input_func_test)
>>> input_data["vertices"]
120
>>> input_data["max_weight"]
110
>>> input_data["number_of_files"]
1
>>> input_data["min_weight"]
1.2
>>> input_data["min_edge"]
2
>>> input_data["max_edge"]
120
>>> input_data["sign"]
True
>>> input_data["weight"]
True
>>> input_data["engine"]
1
>>> loaded_config = check_for_config(input_func_conf_test1)
>>> input_data["config"]
True
>>> input_data_ = input_data.copy()
>>> config_path = save_config(input_data)
>>> loaded_config = load_config(config_path)
>>> loaded_config["vertices"] == input_data_["vertices"]
True
>>> loaded_config["number_of_files"] == input_data_["number_of_files"]
True
>>> loaded_config["output_format"] == input_data_["output_format"]
True
>>> save_config("test")
[Error] Failed to save config file!
>>> load_config("test123456789")
[Error] Failed to load config file!
>>> loaded_config = check_for_config(input_func_conf_test1)
Config files detected in the current directory are listed below:
[1] - ...
>>> loaded_config["vertices"] == input_data_["vertices"]
True
>>> loaded_config["number_of_files"] == input_data_["number_of_files"]
True
>>> loaded_config["output_format"] == input_data_["output_format"]
True
>>> loaded_config = check_for_config(input_func_conf_test2)
Config files detected in the current directory are listed below:
[1] - ...
>>> loaded_config == None
True
>>> input_func_dict = {"vertices":"120","max_weight":"110.45","min_weight":"test","min_edge":"10000","max_edge":"2","sign":"1","direct":"1","self_loop":"0","multigraph":"0","file_name":"File 2","output_format":"1","weight":"0","number_of_files":"1","error":"120","config":"0","engine":"1"}
>>> input_data = get_input(input_func_test)
>>> input_data["vertices"]
120
>>> input_data["min_weight"]
1
>>> input_data["max_edge"]
119
>>> input_data["max_weight"]
1
>>> input_data["weight"]
False
>>> input_data["sign"]
True
>>> input_data["direct"]
True
>>> input_data["multigraph"]
False
>>> prev_item = ""
>>> input_func_dict = {"vertices":"wrong vertices","max_weight":"110.45","min_weight":"2","min_edge":"10000","max_edge":"2","sign":"1","direct":"1","self_loop":"1","multigraph":"1","file_name":"File 2","output_format":"1","weight":"1","error":"1200","number_of_files":"2","config":"0","engine":"1"}
>>> input_data = get_input(input_func_test)
[Error] Bad input!
>>> input_data["vertices"]
1200
>>> prev_item = ""
>>> input_func_dict = {"vertices":"1200","max_weight":"wrong max_weight","min_weight":"2","min_edge":"10000","max_edge":"2","sign":"1","direct":"1","self_loop":"1","multigraph":"1","file_name":"File 2","output_format":"1","weight":"1","error":"400","number_of_files":"2","config":"0","engine":"1"}
>>> input_data = get_input(input_func_test)
[Error] Bad input!
>>> input_data["max_weight"]
400
>>> prev_item = ""
>>> input_func_dict = {"vertices":"1200","max_weight":"400","min_weight":"wrong min_weight","min_edge":"10000","max_edge":"2","sign":"1","direct":"1","self_loop":"1","multigraph":"1","file_name":"File 2","output_format":"1","weight":"1","error":"2","number_of_files":"2","config":"0","engine":"1"}
>>> input_data = get_input(input_func_test)
[Error] Bad input!
>>> input_data["min_weight"]
2
>>> prev_item = ""
>>> input_func_dict = {"vertices":"1200","max_weight":"400","min_weight":"2","min_edge":"wrong min_edge","max_edge":"2","sign":"1","direct":"1","self_loop":"1","multigraph":"1","file_name":"File 2","output_format":"1","weight":"1","error":"0","number_of_files":"2","config":"0","engine":"1"}
>>> input_data = get_input(input_func_test)
[Error] Bad input!
>>> input_data["min_edge"]
0
>>> prev_item = ""
>>> input_func_dict = {"vertices":"1200","max_weight":"400","min_weight":"2","min_edge":"0","max_edge":"wrong max_edge","sign":"1","direct":"1","self_loop":"1","multigraph":"1","file_name":"File 2","output_format":"1","weight":"1","error":"2000","number_of_files":"2","config":"0","engine":"1"}
>>> input_data = get_input(input_func_test)
[Error] Bad input!
>>> input_data["max_edge"]
2000
>>> prev_item = ""
>>> input_func_dict = {"vertices":"1200","max_weight":"400","min_weight":"2","min_edge":"0","max_edge":"2000","sign":"400","direct":"1","self_loop":"1","multigraph":"1","file_name":"File 2","output_format":"1","weight":"1","error":"1","number_of_files":"2","config":"0","engine":"1"}
>>> input_data = get_input(input_func_test)
[Error] Bad input!
>>> input_data["sign"]
True
>>> prev_item = ""
>>> input_func_dict = {"vertices":"1200","max_weight":"400","min_weight":"2","min_edge":"0","max_edge":"2000","sign":"1","direct":"4000","self_loop":"1","multigraph":"1","file_name":"File 2","output_format":"1","weight":"1","error":"1","number_of_files":"2","config":"0","engine":"1"}
>>> input_data = get_input(input_func_test)
[Error] Bad input!
>>> input_data["direct"]
True
>>> prev_item = ""
>>> input_func_dict = {"vertices":"1200","max_weight":"400","min_weight":"2","min_edge":"0","max_edge":"2000","sign":"1","direct":"1","self_loop":"4000","multigraph":"1","file_name":"File 2","output_format":"1","weight":"1","error":"0","number_of_files":"2","config":"0","engine":"1"}
>>> input_data = get_input(input_func_test)
[Error] Bad input!
>>> input_data["self_loop"]
False
>>> prev_item = ""
>>> input_func_dict = {"vertices":"1200","max_weight":"400","min_weight":"2","min_edge":"0","max_edge":"2000","sign":"1","direct":"1","self_loop":"0","multigraph":"40000","file_name":"File 2","output_format":"1","weight":"1","error":"0","number_of_files":"2","config":"0","engine":"1"}
>>> input_data = get_input(input_func_test)
[Error] Bad input!
>>> input_data["multigraph"]
False
>>> prev_item = ""
>>> input_func_dict = {"vertices":"1200","max_weight":"400","min_weight":"2","min_edge":"0","max_edge":"2000","sign":"1","direct":"1","self_loop":"0","multigraph":"0","file_name":"","output_format":"1","weight":"1","error":"file1","number_of_files":"2","config":"0","engine":"1"}
>>> input_data = get_input(input_func_test)
[Error] Bad input!
>>> input_data["file_name"]
'file1'
>>> prev_item = ""
>>> input_func_dict = {"vertices":"1200","max_weight":"400","min_weight":"2","min_edge":"0","max_edge":"2000","sign":"1","direct":"1","self_loop":"0","multigraph":"0","file_name":"file1","output_format":"4000","weight":"1","error":"1","number_of_files":"2","config":"0","engine":"1"}
>>> input_data = get_input(input_func_test)
[Error] Bad input!
>>> input_data["output_format"]
1
>>> prev_item = ""
>>> input_func_dict = {"vertices":"1200","max_weight":"400","min_weight":"2","min_edge":"0","max_edge":"2000","sign":"1","direct":"1","self_loop":"0","multigraph":"0","file_name":"file1","output_format":"1","weight":"4000","error":"0","number_of_files":"2","config":"0","engine":"1"}
>>> input_data = get_input(input_func_test)
[Error] Bad input!
>>> input_data["weight"]
False
>>> prev_item = ""
>>> input_func_dict = {"vertices":"1200","max_weight":"400","min_weight":"2","min_edge":"0","max_edge":"2000","sign":"1","direct":"1","self_loop":"0","multigraph":"0","file_name":"file1","output_format":"1","weight":"0","error":"1","number_of_files":"-5","config":"0","engine":"1"}
>>> input_data = get_input(input_func_test)
[Error] Bad input!
>>> input_data["number_of_files"]
1
>>> prev_item = ""
>>> input_func_dict = {"vertices":"1200","max_weight":"400","min_weight":"2","min_edge":"0","max_edge":"2000","sign":"1","direct":"1","self_loop":"0","multigraph":"0","file_name":"file1","output_format":"1","weight":"0","error":"0","number_of_files":"1","config":"4000","engine":"1"}
>>> input_data = get_input(input_func_test)
[Error] Bad input!
>>> input_data["config"]
False
>>> prev_item = ""
>>> input_func_dict = {"vertices":"1200","max_weight":"400","min_weight":"2","min_edge":"0","max_edge":"2000","sign":"1","direct":"1","self_loop":"0","multigraph":"0","file_name":"file1","output_format":"1","weight":"0","error":"1","number_of_files":"1","config":"0","engine":"100000"}
>>> input_data = get_input(input_func_test)
[Error] Bad input!
>>> input_data["engine"]
1
>>> handle_string("2")
'2'
>>> handle_string("")
Traceback (most recent call last):
    ...
ValueError
>>> handle_pos_int(1)
1
>>> handle_pos_int(-1)
Traceback (most recent call last):
    ...
ValueError
>>> handle_output_format("1")
1
>>> handle_output_format("-14")
Traceback (most recent call last):
    ...
ValueError
>>> handle_output_format("10000000000")
Traceback (most recent call last):
    ...
ValueError
>>> handle_engine("1")
1
>>> handle_engine(-4)
Traceback (most recent call last):
    ...
ValueError
>>> handle_engine("10000000000")
Traceback (most recent call last):
    ...
ValueError
>>> os.remove('File 1.pyrgg.config.json')
"""
