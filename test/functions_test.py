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
>>> used_vertices = {k:[] for k in range(1,41)}
>>> degree_dict = {k:0 for k in range(1,41)}
>>> all_vertices = list(range(1, 41))
>>> random.seed(2)
>>> branch_gen(1,10,10,1,20,1,1,1,1,all_vertices ,used_vertices,degree_dict)
[[4, 25, 18, 3, 30, 34, 2, 26, 14, 11], [3, 10, 20, 14, -18, -2, -15, -14, 8, 6]]
>>> random.seed(20)
>>> branch_gen(1,10,4,1,20,2,1,1,1,all_vertices,used_vertices,degree_dict)
[[], []]
>>> used_vertices = {k:[] for k in range(1,41)}
>>> degree_dict = {k:0 for k in range(1,41)}
>>> branch_gen(1,10,4,1,20,2,1,1,1,all_vertices,used_vertices,degree_dict)
[[10, 7, 39, 2], [9, 11, 6, 14]]
>>> branch_gen(40,1,20,1)
Traceback (most recent call last):
        ...
TypeError: branch_gen() missing 1 required positional argument: 'sign'
>>> random.seed(2)
>>> edge_gen(20,0,400,2,10,1,1,1,1)
[{1: [3, 7], 2: [20, 6, 14, 17, 1], 3: [13, 6, 9, 14, 16, 18, 11], 4: [12, 14, 19, 9, 15, 6, 16], 5: [20, 16, 18, 7], 6: [20, 1, 5, 3, 11, 13, 7], 7: [2, 13, 1, 5, 3, 7, 8], 8: [8, 1], 9: [10, 1, 20], 10: [20, 8, 12, 17, 15, 9, 16, 1], 11: [9, 7], 12: [17, 8, 10, 9, 18], 13: [5, 15], 14: [9, 1, 11, 2, 8, 17, 20], 15: [1, 18, 17, 20, 13, 19, 2], 16: [7, 2, 19], 17: [11, 12, 19], 18: [13, 12, 9, 16, 18, 19], 19: [16, 5], 20: [17, 18, 8]}, {1: [184, -128], 2: [297, -326, -278, -18, -238], 3: [-269, 120, 90, 69, 228, -376, -303], 4: [-82, -335, 250, -256, -236, -249, 166], 5: [-395, -155, -159, -262], 6: [174, 381, 294, -302, 386, 136, 30], 7: [185, 127, 58, 20, -130, 376, 197], 8: [18, -315], 9: [-250, -229, 135], 10: [242, 338, 12, 265, -263, -134, -334, 343], 11: [67, 232], 12: [126, -37, 302, -131, -269], 13: [196, 56], 14: [51, 384, 111, -232, -108, 373, -217], 15: [214, 48, -9, 312, -353, -157, -51], 16: [231, -326, -106], 17: [190, 112, 59], 18: [-71, -62, 62, -108, 12, -397], 19: [-183, -137], 20: [-368, -202, 250]}, 92]
>>> random.seed(11)
>>> edge_gen(20,0,100,2,10,2,1,1,1)
[{1: [18, 15, 19, 7, 20, 11, 2, 6, 3], 2: [20, 15], 3: [20, 17, 2, 8], 4: [15, 16], 5: [17, 10, 1, 4, 12], 6: [3, 10, 9, 13, 4, 18, 11, 7, 2], 7: [7, 2], 8: [13, 3, 8, 11, 4, 9, 12, 2], 9: [4, 2, 18, 9, 10], 10: [14, 13, 15, 7], 11: [19, 7, 5, 4, 13, 2], 12: [10, 3, 4, 11, 16, 14, 5], 13: [19, 13, 5, 9, 10, 4], 14: [7, 14, 3, 2, 15, 9, 20, 16], 15: [10, 3, 20, 15, 14], 16: [7, 4, 17, 12, 18, 16], 17: [18, 5, 19, 20, 7, 13, 14], 18: [14, 13, 20, 15, 5], 19: [13, 19, 20], 20: [20, 14]}, {1: [99, 57, 75, 23, 80, 23, 57, 18, 68], 2: [50, 83], 3: [1, 8, 4, 30], 4: [41, 75], 5: [29, 63, 84, 58, 52], 6: [90, 40, 65, 3, 72, 13, 13, 49, 2], 7: [26, 60], 8: [53, 72, 99, 43, 39, 1, 97, 17], 9: [1, 59, 22, 57, 93], 10: [82, 14, 53, 0], 11: [38, 50, 5, 27, 33, 98], 12: [49, 9, 26, 1, 47, 58, 75], 13: [17, 23, 39, 78, 92, 20], 14: [87, 61, 53, 13, 32, 94, 50, 76], 15: [66, 16, 71, 78, 9], 16: [26, 34, 57, 47, 73, 17], 17: [74, 75, 39, 81, 61, 40, 57], 18: [45, 3, 1, 48, 10], 19: [49, 56, 69], 20: [14, 99]}, 105]
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
