# -*- coding: utf-8 -*-
"""
>>> from pyrgg.functions import *
>>> import pyrgg.params
>>> import random
>>> pyrgg.params.PYRGG_TEST_MODE = True
>>> description_print()
Webpage : https://www.pyrgg.ir
Repository : https://github.com/sepandhaghighi/pyrgg
Paper : https://doi.org/10.21105/joss.00331
* If you use Pyrgg in your research, please cite our paper
<BLANKLINE>
########################################
<BLANKLINE>
<BLANKLINE>
Pyrgg  is  an  easy-to-use synthetic random graph generator written in Python which supports various
graph file formats including DIMACS .gr files. Pyrgg has the ability to generate graphs of different
sizes  and  is designed to provide input files for broad range of graph-based research applications,
including  but  not  limited  to  testing, benchmarking and performance-analysis of graph processing
frameworks.  Pyrgg  target  audiences  are  computer scientists who study graph algorithms and graph
processing frameworks.
<BLANKLINE>
<BLANKLINE>
########################################
>>> result = input_filter({"file_name": "test","vertices": 5,"max_weight": 1000,"min_weight":455,"min_edge": -45,"max_edge": -11,"sign": False,"output_format": 19, "direct": False,"self_loop": True,"multigraph":False,"number_of_files":2})
>>> result == {'output_format': 1, 'min_weight': 455, 'min_edge': 5, 'max_edge': 5, 'file_name': 'test', 'vertices': 5, 'max_weight': 1000, 'sign': False, "direct": False,"self_loop": True,"multigraph":False,"number_of_files":2}
True
>>> result = input_filter({"file_name": "test","vertices": 5,"max_weight": 1000,"min_weight":455,"min_edge": -45,"max_edge": -11,"sign": False,"output_format": 19, "direct": False,"self_loop": False,"multigraph":False,"number_of_files":10})
>>> result == {'output_format': 1, 'min_weight': 455, 'min_edge': 4, 'max_edge': 4, 'file_name': 'test', 'vertices': 5, 'max_weight': 1000, 'sign': False, "direct": False,"self_loop": False,"multigraph":False,"number_of_files":10}
True
>>> result = input_filter({"file_name": "test","vertices": -5,"max_weight": 1000,"min_weight":455,"min_edge": -45,"max_edge": -11,"sign": False,"output_format": 19, "direct": False,"self_loop": False,"multigraph":True,"number_of_files":-1})
>>> result == {'output_format': 1, 'min_weight': 455, 'min_edge': 11, 'max_edge': 45, 'file_name': 'test', 'vertices': 5, 'max_weight': 1000, 'sign': False, "direct": False,"self_loop": False,"multigraph":True,"number_of_files":1}
True
>>> result = input_filter({"file_name": "test","vertices": -5,"max_weight": 1000,"min_weight":455,"min_edge": -45,"max_edge": -11,"sign": False,"output_format": 19, "direct": False,"self_loop": False,"multigraph":True,"number_of_files":-1})
>>> result == {'output_format': 1, 'min_weight': 455, 'min_edge': 11, 'max_edge': 45, 'file_name': 'test', 'vertices': 5, 'max_weight': 1000, 'sign': False, "direct": False,"self_loop": False,"multigraph":True,"number_of_files":1}
True
>>> result = input_filter({"file_name": "test2","vertices": 23,"max_weight": 2,"min_weight": 80,"min_edge": 23,"max_edge": 1,"sign": True,"output_format": 1, "direct": False,"self_loop": True,"multigraph":False,"number_of_files":2})
>>> result == {'min_weight': 2, 'vertices': 23, 'file_name': 'test2', 'max_edge': 23, 'min_edge': 1, 'max_weight': 80, 'output_format': 1, 'sign': True, "direct": False,"self_loop": True,"multigraph":False,"number_of_files":2}
True
>>> logger('test',100,50,1000,10,1,0,0,1,20,1,'2min')
>>> file=open('logfile.log','r')
>>> print("\\n".join(file.read().splitlines()[1:-1]))
Filename : test
Vertices : 100
Total Edges : 50
Max Edge : 1000
Min Edge : 10
Directed : True
Signed : False
Multigraph : False
Self Loop : True
Weighted : True
Max Weight : 20
Min Weight : 1
Elapsed Time : 2min
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
>>> convert_str_to_number("20")
20
>>> convert_str_to_number("20.2")
20.2
>>> convert_str_to_bool("1")
True
>>> convert_str_to_bool("3")
True
>>> convert_str_to_bool("0")
False
>>> is_float(10)
False
>>> is_float(10.2)
True
>>> is_float(None)
False
>>> used_vertices = {k:[] for k in range(1,6)}
>>> degree_dict = {1:2,2:3,3:3,4:3,5:3}
>>> degree_dict_sort = {0:{},1:{},2:{1:1},3:{2:2,3:3,4:4,5:5},4:{},5:{}}
>>> all_vertices = list(range(1, 6))
>>> branch_gen(1,3,3,300,3000,0,True,False,False,False,used_vertices,degree_dict,degree_dict_sort)
[[], []]
>>> used_vertices = {k:[] for k in range(1,41)}
>>> degree_dict = {k:0 for k in range(1,41)}
>>> degree_dict_sort = {k:{} for k in range(41)}
>>> degree_dict_sort[0] = {i:i for i in range(1,41)}
>>> all_vertices = list(range(1, 41))
>>> random.seed(2)
>>> branch_gen(1,10,10,1,20,0,True,True,True,False,used_vertices,degree_dict,degree_dict_sort)
[[4, 25, 18, 3, 30, 34, 2, 26, 14, 11], [3, 10, 20, 14, -18, -2, -15, -14, 8, 6]]
>>> random.seed(20)
>>> branch_gen(1,10,4,1,20,0,False,True,True,False,used_vertices,degree_dict,degree_dict_sort)
[[], []]
>>> used_vertices = {k:[] for k in range(1,41)}
>>> degree_dict = {k:0 for k in range(1,41)}
>>> degree_dict_sort = {k:{} for k in range(41)}
>>> degree_dict_sort[0] = {i:i for i in range(1,41)}
>>> branch_gen(1,10,4,1,20,0,False,True,True,False,used_vertices,degree_dict,degree_dict_sort)
[[10, 7, 39, 2, 30, 9, 25, 35, 18], [9, 11, 6, 14, 3, 5, 16, 14, 7]]
>>> branch_gen(40,1,20,1)
Traceback (most recent call last):
        ...
TypeError: branch_gen() missing 1 required positional argument: 'sign'
>>> random.seed(2)
>>> edge_gen(20,0,400,2,10,True,True,True,False)
[{1: [3, 7], 2: [4, 17, 20, 9, 11], 3: [14, 8, 5, 12, 16, 19, 15], 4: [15, 17, 12, 8, 14, 13], 5: [16, 9, 7, 20, 19, 18, 13, 5], 6: [6, 10], 7: [18, 10, 11], 8: [], 9: [], 10: [12, 18, 8, 1, 14], 11: [9, 11], 12: [], 13: [], 14: [19, 16, 17, 20, 15], 15: [6, 1, 19], 16: [12, 13, 8, 9, 17], 17: [], 18: [9, 12, 17, 6, 20, 19, 1], 19: [13], 20: []}, {1: [184, -128], 2: [220, -278, -257, 14, -163], 3: [286, 118, 166, 261, -263, 228, -303], 4: [-82, -335, 250, -256, -338, -179], 5: [-337, -358, -395, -155, -159, 250, -350, -371], 6: [30, -302], 7: [386, -125, 216], 8: [], 9: [], 10: [127, 42, 12, 191, 80], 11: [-301, 77], 12: [], 13: [], 14: [146, -15, -282, 135, 242], 15: [-52, -65, -249], 16: [-132, -334, 343, -17, 87], 17: [], 18: [126, -37, 302, -131, -142, 77, -209], 19: [123], 20: []}, 61]
>>> random.seed(11)
>>> edge_gen(20,0,100,2,10,False,True,True,False)
[{1: [18, 15, 19, 7, 20, 11, 2, 6, 3], 2: [17], 3: [8, 4, 5, 9, 12, 10, 14, 16], 4: [20, 13, 4, 6], 5: [12, 7, 11, 10, 14], 6: [9], 7: [19], 8: [8, 18, 11, 2, 16, 17, 10], 9: [15, 12, 18], 10: [20, 14, 13, 15, 17, 16], 11: [19, 7, 20], 12: [13], 13: [2, 16, 13], 14: [18, 19, 6, 14, 17, 15], 15: [6, 7, 16], 16: [17, 20, 12, 18], 17: [19], 18: [7, 6, 9, 12, 20], 19: [19, 11, 4], 20: []}, {1: [99, 57, 75, 23, 80, 23, 57, 18, 68], 2: [50], 3: [79, 67, 7, 24, 76, 99, 41, 75], 4: [29, 63, 84, 58], 5: [70, 90, 40, 65, 3], 6: [51], 7: [37], 8: [2, 0, 26, 60, 90, 53, 72], 9: [43, 39, 1], 10: [15, 31, 1, 59, 22, 57], 11: [98, 53, 49], 12: [53], 13: [34, 2, 23], 14: [82, 12, 18, 56, 1, 37], 15: [9, 26, 1], 16: [47, 58, 75, 73], 17: [23], 18: [39, 78, 92, 20, 49], 19: [10, 6, 13], 20: []}, 74]
>>> edge_gen(0,400,2,10,1)
Traceback (most recent call last):
        ...
TypeError: edge_gen() missing 1 required positional argument: 'sign'
>>> prev_item = ""
>>> input_func_dict = {"vertices":"120","max_weight":"110","min_weight":"0","min_edge":"1","max_edge":"1000","sign":"1","direct":"1","self_loop":"1","multigraph":"0","file_name":"File 1","output_format":"2","weight":"1","error":"120","number_of_files":3}
>>> def input_func_test(input_data):
...    menu = dict(pyrgg.params.MENU_ITEMS1,**pyrgg.params.MENU_ITEMS2)
...    global prev_item
...    for item in menu:
...        if input_data == menu[item]:
...            if item != prev_item :
...                prev_item = item
...                return input_func_dict[item]
...            else:
...                return input_func_dict["error"]
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
>>> prev_item = ""
>>> input_func_dict = {"vertices":"120","max_weight":"110","min_weight":"1.2","min_edge":"10000","max_edge":"2","sign":"1","direct":"1","self_loop":"1","multigraph":"0","file_name":"File 1","output_format":"2","weight":"1","error":"120","number_of_files":-1}
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
>>> prev_item = ""
>>> input_func_dict = {"vertices":"120","max_weight":"110.45","min_weight":"test","min_edge":"10000","max_edge":"2","sign":"1","direct":"-2","self_loop":"0","multigraph":"0","file_name":"File 2","output_format":"200","weight":"0","number_of_files":-1,"error":"120"}
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
>>> input_func_dict = {"vertices":"120","max_weight":"110.45","min_weight":"test","min_edge":"10000","max_edge":"2","sign":"1","direct":"-2","self_loop":"2","multigraph":"400","file_name":"File 2","output_format":"200","weight":"1","error":"120","number_of_files":2}
>>> input_data = get_input(input_func_test)
[Error] Bad Input!
>>> input_data["min_weight"]
110.45
>>> input_data["max_weight"]
120
>>> input_func_dict = {"vertices":"120","max_weight":"110","min_weight":"0","min_edge":"1","max_edge":"1000","sign":"1","direct":"1","self_loop":"1","multigraph":"1","file_name":"File 1","output_format":"2","weight":"test","error":"2","number_of_files":2}
>>> input_data = get_input(input_func_test)
[Error] Bad Input!
>>> input_data["weight"]
True

"""
