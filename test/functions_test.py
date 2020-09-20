# -*- coding: utf-8 -*-
"""
>>> from pyrgg.functions import *
>>> import random
>>> logger(2,2,2,2)
[Error] Logger Failed!
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
>>> result = input_filter({"file_name": "test","vertices": 5,"max_weight": 1000,"min_weight":455,"min_edge": -45,"max_edge": -11,"sign": 5,"output_format": 19, "direct": 2,"self_loop": 1,"multigraph":1})
>>> result == {'output_format': 1, 'min_weight': 455, 'min_edge': 5, 'max_edge': 5, 'file_name': 'test', 'vertices': 5, 'max_weight': 1000, 'sign': 2, "direct": 2,"self_loop": 1,"multigraph":1}
True
>>> result = input_filter({"file_name": "test","vertices": 5,"max_weight": 1000,"min_weight":455,"min_edge": -45,"max_edge": -11,"sign": 5,"output_format": 19, "direct": 2,"self_loop": 2,"multigraph":1})
>>> result == {'output_format': 1, 'min_weight': 455, 'min_edge': 4, 'max_edge': 4, 'file_name': 'test', 'vertices': 5, 'max_weight': 1000, 'sign': 2, "direct": 2,"self_loop": 2,"multigraph":1}
True
>>> result = input_filter({"file_name": "test","vertices": -5,"max_weight": 1000,"min_weight":455,"min_edge": -45,"max_edge": -11,"sign": 5,"output_format": 19, "direct": 2,"self_loop": 2,"multigraph":2})
>>> result == {'output_format': 1, 'min_weight': 455, 'min_edge': 11, 'max_edge': 45, 'file_name': 'test', 'vertices': 5, 'max_weight': 1000, 'sign': 2, "direct": 2,"self_loop": 2,"multigraph":2}
True
>>> result = input_filter({"file_name": "test","vertices": -5,"max_weight": 1000,"min_weight":455,"min_edge": -45,"max_edge": -11,"sign": 5,"output_format": 19, "direct": 2,"self_loop": 1,"multigraph":2})
>>> result == {'output_format': 1, 'min_weight': 455, 'min_edge': 11, 'max_edge': 45, 'file_name': 'test', 'vertices': 5, 'max_weight': 1000, 'sign': 2, "direct": 2,"self_loop": 1,"multigraph":2}
True
>>> result = input_filter({"file_name": "test2","vertices": 23,"max_weight": 2,"min_weight": 80,"min_edge": 23,"max_edge": 1,"sign": 1,"output_format": 1, "direct": 2,"self_loop": 10,"multigraph":10})
>>> result == {'min_weight': 2, 'vertices': 23, 'file_name': 'test2', 'max_edge': 23, 'min_edge': 1, 'max_weight': 80, 'output_format': 1, 'sign': 1, "direct": 2,"self_loop": 1,"multigraph":1}
True
>>> logger(100,50,'test','2min')
>>> convert_bytes(200)
'200.0 bytes'
>>> convert_bytes(6000)
'5.9 KB'
>>> convert_bytes(80000)
'78.1 KB'
>>> time_convert('33')
'00 days, 00 hour, 00 minutes, 33 seconds'
>>> time_convert('15000')
'00 days, 04 hour, 10 minutes, 00 seconds'
>>> time_convert('sadasdasd')
Traceback (most recent call last):
        ...
ValueError: could not convert string to float: 'sadasdasd'
>>> line(12,"*")
************
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
>>> is_float(10)
False
>>> is_float(10.2)
True
>>> is_float(None)
False
>>> random.seed(2)
>>> sign_gen()
1
>>> random.seed(11)
>>> sign_gen()
-1
>>> used_vertices = {k:[] for k in range(1,5)}
>>> used_vertices = {k:[] for k in range(1,6)}
>>> degree_dict = {1:2,2:3,3:3,4:3,5:3}
>>> degree_dict_sort = {0:{},1:{},2:{1:1},3:{2:2,3:3,4:4,5:5},4:{},5:{}}
>>> all_vertices = list(range(1, 6))
>>> branch_gen(1,3,3,300,3000,1,2,2,1,used_vertices,degree_dict,degree_dict_sort)
[[], []]
>>> used_vertices = {k:[] for k in range(1,41)}
>>> degree_dict = {k:0 for k in range(1,41)}
>>> degree_dict_sort = {k:{} for k in range(41)}
>>> degree_dict_sort[0] = {i:i for i in range(1,41)}
>>> all_vertices = list(range(1, 41))
>>> random.seed(2)
>>> branch_gen(1,10,10,1,20,1,1,1,1,used_vertices,degree_dict,degree_dict_sort)
[[4, 25, 18, 3, 30, 34, 2, 26, 14, 11], [3, 10, 20, 14, -18, -2, -15, -14, 8, 6]]
>>> random.seed(20)
>>> branch_gen(1,10,4,1,20,2,1,1,1,used_vertices,degree_dict,degree_dict_sort)
[[], []]
>>> used_vertices = {k:[] for k in range(1,41)}
>>> degree_dict = {k:0 for k in range(1,41)}
>>> degree_dict_sort = {k:{} for k in range(41)}
>>> degree_dict_sort[0] = {i:i for i in range(1,41)}
>>> branch_gen(1,10,4,1,20,2,1,1,1,used_vertices,degree_dict,degree_dict_sort)
[[10, 7, 39, 2], [9, 11, 6, 14]]
>>> branch_gen(40,1,20,1)
Traceback (most recent call last):
        ...
TypeError: branch_gen() missing 1 required positional argument: 'sign'
>>> random.seed(2)
>>> edge_gen(20,0,400,2,10,1,1,1,1)
[{1: [3, 7], 2: [4, 17, 20, 9, 11], 3: [14, 8, 5, 12, 16, 19, 15], 4: [14, 16, 9, 4, 12, 11], 5: [15, 18, 13, 20, 19, 17, 8, 6, 10], 6: [6, 10], 7: [18, 20, 11, 10, 8, 13, 7, 15], 8: [19, 1], 9: [], 10: [], 11: [16, 13, 14, 9, 17], 12: [18, 12, 14], 13: [10, 16, 1, 9, 15], 14: [], 15: [18, 17, 20], 16: [19], 17: [14, 1, 9], 18: [6, 10, 18, 19, 20], 19: [8, 20, 1, 14, 10], 20: [2, 16, 6, 9]}, {1: [184, -128], 2: [220, -278, -257, 14, -163], 3: [286, 118, 166, 261, -263, 228, -303], 4: [-82, -335, 250, -256, -338, -179], 5: [-337, -358, -395, -155, -159, 250, -350, -371, 381], 6: [139, 386], 7: [-125, 30, 29, -88, 42, 12, 191, 80], 8: [197, 77], 9: [], 10: [], 11: [146, -15, -282, -386, 242], 12: [-52, -65, -249], 13: [-132, -334, 343, -17, 87], 14: [], 15: [126, -37, 302], 16: [-350], 17: [77, -209, 262], 18: [52, 93, 111, -232, -108], 19: [-217, 297, -268, 48, -9], 20: [-148, -157, -51, -101]}, 75]
>>> random.seed(11)
>>> edge_gen(20,0,100,2,10,2,1,1,1)
[{1: [18, 15, 19, 7, 20, 11, 2, 6, 3], 2: [17], 3: [8, 4, 5, 9, 12, 10, 14, 16], 4: [20, 12, 13, 5], 5: [13, 7, 11, 10], 6: [6, 9, 8, 17, 14], 7: [], 8: [16, 18, 19], 9: [15], 10: [13, 12, 2, 10], 11: [11, 7, 20], 12: [19, 15], 13: [16, 18, 14], 14: [19, 7, 9, 16, 18, 15], 15: [], 16: [17], 17: [17, 7, 18, 2], 18: [], 19: [20], 20: [9, 15, 2, 20]}, {1: [99, 57, 75, 23, 80, 23, 57, 18, 68], 2: [50], 3: [79, 67, 7, 24, 76, 99, 41, 75], 4: [29, 63, 84, 58], 5: [70, 90, 40, 65], 6: [8, 51, 37, 8, 87], 7: [], 8: [6, 48, 53], 9: [99], 10: [11, 42, 52, 17], 11: [1, 59, 62], 12: [71, 57], 13: [53, 49, 50], 14: [0, 75, 2, 23, 77, 12], 15: [], 16: [56], 17: [98, 42, 49, 9], 18: [], 19: [1], 20: [47, 58, 75, 73]}, 63]
>>> edge_gen(0,400,2,10,1)
Traceback (most recent call last):
        ...
TypeError: edge_gen() missing 1 required positional argument: 'sign'
>>> prev_item = ""
>>> input_func_dict = {"vertices":"120","max_weight":"110","min_weight":"0","min_edge":"1","max_edge":"1000","sign":"1","direct":"1","self_loop":"1","multigraph":"1","file_name":"File 1","output_format":"2","weight":"1","error":"120"}
>>> def input_func_test(input_data):
...    menu = dict(MENU_ITEMS1,**MENU_ITEMS2)
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
>>> input_data["sign"]
1
>>> input_data["weight"]
1
>>> prev_item = ""
>>> input_func_dict = {"vertices":"120","max_weight":"110","min_weight":"1.2","min_edge":"10000","max_edge":"2","sign":"1","direct":"1","self_loop":"1","multigraph":"1","file_name":"File 1","output_format":"2","weight":"1","error":"120"}
>>> input_data = get_input(input_func_test)
>>> input_data["vertices"]
120
>>> input_data["max_weight"]
110
>>> input_data["min_weight"]
1.2
>>> input_data["min_edge"]
2
>>> input_data["max_edge"]
120
>>> input_data["sign"]
1
>>> input_data["weight"]
1
>>> prev_item = ""
>>> input_func_dict = {"vertices":"120","max_weight":"110.45","min_weight":"test","min_edge":"10000","max_edge":"2","sign":"1","direct":"-2","self_loop":"2","multigraph":"400","file_name":"File 2","output_format":"200","weight":"100","error":"120"}
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
100
>>> input_data["sign"]
1
>>> input_data["direct"]
1
>>> input_data["multigraph"]
1
>>> input_func_dict = {"vertices":"120","max_weight":"110.45","min_weight":"test","min_edge":"10000","max_edge":"2","sign":"1","direct":"-2","self_loop":"2","multigraph":"400","file_name":"File 2","output_format":"200","weight":"1","error":"120"}
>>> input_data = get_input(input_func_test)
[Error] Bad Input!
>>> input_data["min_weight"]
110.45
>>> input_data["max_weight"]
120
>>> input_func_dict = {"vertices":"120","max_weight":"110","min_weight":"0","min_edge":"1","max_edge":"1000","sign":"1","direct":"1","self_loop":"1","multigraph":"1","file_name":"File 1","output_format":"2","weight":"test","error":"2"}
>>> input_data = get_input(input_func_test)
[Error] Bad Input!
>>> input_data["weight"]
2

"""
