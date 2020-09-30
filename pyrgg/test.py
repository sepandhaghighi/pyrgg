# -*- coding: utf-8 -*-
"""Test file."""
"""
>>> from pyrgg import *
>>> import random
>>> import os
>>> import json
>>> import yaml
>>> import pickle
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
>>> logger(2,2,2,2)
[Error] Logger Failed!
>>> result = input_filter({"file_name": "test","vertices": 5,"max_weight": 1000,"min_weight":455,"min_edge": -45,"max_edge": -11,"sign": 5,"output_format": 19, "direct": 2,"self_loop": 1,"multigraph":1})
>>> result == {'output_format': 1, 'min_weight': 455, 'min_edge': 5, 'max_edge': 5, 'file_name': 'test', 'vertices': 5, 'max_weight': 1000, 'sign': 2, "direct": 2,"self_loop": 1,"multigraph":1}
True
>>> result = input_filter({"file_name": "test","vertices": 5,"max_weight": 1000,"min_weight":455,"min_edge": -45,"max_edge": -11,"sign": 5,"output_format": 19, "direct": 2,"self_loop": 2,"multigraph":1})
>>> result == {'output_format': 1, 'min_weight': 455, 'min_edge': 4, 'max_edge': 4, 'file_name': 'test', 'vertices': 5, 'max_weight': 1000, 'sign': 2, "direct": 2,"self_loop": 2,"multigraph":1}
True
>>> result = input_filter({"file_name": "test","vertices": -5,"max_weight": 1000,"min_weight":455,"min_edge": -45,"max_edge": -11,"sign": 5,"output_format": 19, "direct": 2,"self_loop": 2,"multigraph":2})
>>> result == {'output_format': 1, 'min_weight': 455, 'min_edge': 11, 'max_edge': 45, 'file_name': 'test', 'vertices': 5, 'max_weight': 1000, 'sign': 2, "direct": 2,"self_loop": 2,"multigraph":2}
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
>>> random.seed(2)
>>> sign_gen()
1
>>> random.seed(11)
>>> sign_gen()
-1
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
TypeError: branch_gen() missing 8 required positional arguments: 'max_weight', 'sign', 'direct', 'self_loop', 'multigraph', 'used_vertices', 'degree_dict', and 'degree_sort_dict'
>>> random.seed(2)
>>> edge_gen(20,0,400,2,10,1,1,1,1)
[{1: [3, 7], 2: [4, 17, 20, 9, 11], 3: [14, 8, 5, 12, 16, 19, 15], 4: [15, 17, 12, 8, 14, 13], 5: [16, 9, 7, 20, 19, 18, 13, 5], 6: [6, 10], 7: [18, 10, 11], 8: [], 9: [], 10: [12, 18, 8, 1, 14], 11: [9, 11], 12: [], 13: [], 14: [19, 16, 17, 20, 15], 15: [6, 1, 19], 16: [12, 13, 8, 9, 17], 17: [], 18: [9, 12, 17, 6, 20, 19, 1], 19: [13], 20: []}, {1: [184, -128], 2: [220, -278, -257, 14, -163], 3: [286, 118, 166, 261, -263, 228, -303], 4: [-82, -335, 250, -256, -338, -179], 5: [-337, -358, -395, -155, -159, 250, -350, -371], 6: [30, -302], 7: [386, -125, 216], 8: [], 9: [], 10: [127, 42, 12, 191, 80], 11: [-301, 77], 12: [], 13: [], 14: [146, -15, -282, 135, 242], 15: [-52, -65, -249], 16: [-132, -334, 343, -17, 87], 17: [], 18: [126, -37, 302, -131, -142, 77, -209], 19: [123], 20: []}, 61]
>>> random.seed(11)
>>> edge_gen(20,0,100,2,10,2,1,1,1)
[{1: [18, 15, 19, 7, 20, 11, 2, 6, 3], 2: [17], 3: [8, 4, 5, 9, 12, 10, 14, 16], 4: [20, 13, 4, 6], 5: [12, 7, 11, 10, 14], 6: [9], 7: [19], 8: [8, 18, 11, 2, 16, 17, 10], 9: [15, 12, 18], 10: [20, 14, 13, 15, 17, 16], 11: [19, 7, 20], 12: [13], 13: [2, 16, 13], 14: [18, 19, 6, 14, 17, 15], 15: [6, 7, 16], 16: [17, 20, 12, 18], 17: [19], 18: [7, 6, 9, 12, 20], 19: [19, 11, 4], 20: []}, {1: [99, 57, 75, 23, 80, 23, 57, 18, 68], 2: [50], 3: [79, 67, 7, 24, 76, 99, 41, 75], 4: [29, 63, 84, 58], 5: [70, 90, 40, 65, 3], 6: [51], 7: [37], 8: [2, 0, 26, 60, 90, 53, 72], 9: [43, 39, 1], 10: [15, 31, 1, 59, 22, 57], 11: [98, 53, 49], 12: [53], 13: [34, 2, 23], 14: [82, 12, 18, 56, 1, 37], 15: [9, 26, 1], 16: [47, 58, 75, 73], 17: [23], 18: [39, 78, 92, 20, 49], 19: [10, 6, 13], 20: []}, 74]
>>> edge_gen(0,400,2,10,1)
Traceback (most recent call last):
        ...
TypeError: edge_gen() missing 4 required positional arguments: 'sign', 'direct', 'self_loop', and 'multigraph'
>>> random.seed(2)
>>> dimacs_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
7
>>> file=open('testfile.gr','r')
>>> print(file.read())
c FILE                  :testfile.gr
c No. of vertices       :10
c No. of edges          :7
c Max. weight           :200
c Min. weight           :0
c Min. edge             :0
c Max. edge             :2
p sp 10 7
a 4 3 -64
a 5 6 148
a 5 9 110
a 6 10 -139
a 7 7 7
a 8 2 -97
a 9 1 60
<BLANKLINE>
>>> random.seed(4)
>>> dimacs_maker('testfile2',0,50,30,0,4,0,1,1,1)
35
>>> file=open('testfile2.gr','r')
>>> print(file.read())
c FILE                  :testfile2.gr
c No. of vertices       :30
c No. of edges          :35
c Max. weight           :50
c Min. weight           :0
c Min. edge             :0
c Max. edge             :4
p sp 30 35
a 1 10 46
a 2 18 5
a 2 4 25
a 2 22 -48
a 4 23 -17
a 5 7 -13
a 7 15 10
a 7 17 -40
a 8 8 -42
a 8 25 11
a 9 29 -5
a 10 3 -36
a 10 27 -48
a 11 13 -27
a 11 26 -27
a 11 21 14
a 11 16 -2
a 14 20 -44
a 14 14 43
a 14 12 26
a 15 28 -11
a 16 30 -40
a 16 24 20
a 19 19 7
a 20 12 -29
a 20 1 22
a 22 24 20
a 22 23 -9
a 23 18 18
a 23 27 28
a 24 6 -24
a 25 17 23
a 27 6 -50
a 28 21 28
a 28 13 -13
<BLANKLINE>
>>> random.seed(20)
>>> dimacs_maker('testfile3',10,30,100,0,4,2,1,1,1)
137
>>> file=open('testfile3.gr','r')
>>> print(file.read())
c FILE                  :testfile3.gr
c No. of vertices       :100
c No. of edges          :137
c Max. weight           :30
c Min. weight           :10
c Min. edge             :0
c Max. edge             :4
p sp 100 137
a 1 34 30
a 3 76 15
a 3 5 23
a 4 13 13
a 4 21 20
a 4 67 28
a 5 60 16
a 5 32 20
a 5 92 20
a 6 64 12
a 6 94 26
a 7 62 12
a 7 36 28
a 7 42 11
a 8 20 12
a 9 47 19
a 10 49 15
a 10 27 10
a 11 48 17
a 11 51 11
a 13 58 14
a 13 70 29
a 14 37 30
a 14 61 27
a 14 87 15
a 15 84 13
a 16 83 28
a 17 45 17
a 17 24 29
a 17 18 26
a 18 59 15
a 19 98 12
a 21 2 30
a 21 99 20
a 22 69 26
a 22 96 11
a 22 88 15
a 24 79 20
a 24 12 12
a 24 82 13
a 26 50 30
a 26 30 19
a 29 52 26
a 31 25 26
a 32 68 14
a 33 65 13
a 33 78 13
a 33 55 17
a 34 63 13
a 35 44 27
a 35 57 14
a 37 74 10
a 37 41 16
a 37 100 30
a 38 72 13
a 38 56 16
a 39 91 19
a 39 43 13
a 41 28 22
a 41 81 19
a 42 90 13
a 42 46 28
a 42 97 16
a 45 86 10
a 45 53 18
a 46 85 13
a 46 23 11
a 47 71 29
a 48 95 12
a 48 77 19
a 48 93 11
a 49 75 22
a 50 73 18
a 50 40 24
a 50 54 28
a 51 80 17
a 51 66 19
a 51 89 20
a 52 58 29
a 52 16 21
a 52 43 12
a 53 8 13
a 53 98 17
a 54 55 10
a 56 62 26
a 56 27 10
a 57 70 26
a 58 44 22
a 59 90 27
a 59 91 19
a 59 78 29
a 60 87 12
a 60 92 25
a 61 69 14
a 61 79 17
a 62 25 21
a 63 97 27
a 63 29 30
a 65 9 26
a 65 64 21
a 66 67 27
a 66 95 19
a 66 93 30
a 68 30 18
a 70 83 12
a 70 99 15
a 71 31 17
a 71 89 20
a 73 36 18
a 75 72 12
a 76 2 26
a 76 12 25
a 76 86 22
a 78 23 19
a 78 100 27
a 79 40 24
a 80 84 26
a 80 80 14
a 81 20 16
a 82 15 16
a 82 88 22
a 83 19 19
a 84 85 13
a 84 28 16
a 85 77 16
a 85 94 23
a 86 1 21
a 87 74 15
a 87 96 19
a 90 93 22
a 92 49 14
a 95 98 26
a 95 55 11
a 97 38 28
a 99 19 29
a 99 89 24
a 100 40 11
<BLANKLINE>
>>> dimacs_maker('testfile', 0, 200, 10, 0,0,1)
Traceback (most recent call last):
        ...
TypeError: dimacs_maker() missing 3 required positional arguments: 'direct', 'self_loop', and 'multigraph'
>>> random.seed(2)
>>> json_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
7
>>> file=open('testfile.json','r')
>>> testfile_1=json.load(file)
>>> testfile_1['graph']['nodes'][1]
{'id': '2'}
>>> testfile_1['graph']['edges'][1]['source']
'5'
>>> testfile_1['graph']['edges'][1]['target']
'6'
>>> testfile_1['graph']['edges'][1]['weight']
'148'
>>> json_to_yaml('testfile')
>>> file=open('testfile.yaml','r')
>>> testfile_1_yaml=yaml.load(file)
>>> testfile_1_yaml['graph']['edges'][1]['source']
'5'
>>> testfile_1_yaml['graph']['edges'][1]['target']
'6'
>>> testfile_1_yaml['graph']['edges'][1]['weight']
'148'
>>> json_to_pickle('testfile')
>>> testfile_1_p=pickle.load( open( 'testfile.p', 'rb' ) )
>>> testfile_1_p['graph']['edges'][1]['source']
'5'
>>> testfile_1_p['graph']['edges'][1]['target']
'6'
>>> testfile_1_p['graph']['edges'][1]['weight']
'148'
>>> random.seed(4)
>>> json_maker('testfile2',0,50,30,0,4,0,1,1,1)
35
>>> file=open('testfile2.json','r')
>>> testfile_2=json.load(file)
>>> testfile_2['graph']['nodes'][1]
{'id': '2'}
>>> testfile_2['graph']['edges'][1]['source']
'2'
>>> testfile_2['graph']['edges'][1]['target']
'18'
>>> testfile_2['graph']['edges'][1]['weight']
'5'
>>> json_to_yaml('testfile2')
>>> file=open('testfile2.yaml','r')
>>> testfile_2_yaml=yaml.load(file)
>>> testfile_2_yaml['graph']['nodes'][1]
{'id': '2'}
>>> testfile_2_yaml['graph']['edges'][1]['source']
'2'
>>> testfile_2_yaml['graph']['edges'][1]['target']
'18'
>>> testfile_2_yaml['graph']['edges'][1]['weight']
'5'
>>> json_to_pickle('testfile2')
>>> testfile_2_p=pickle.load( open( 'testfile2.p', 'rb' ) )
>>> testfile_2_p['graph']['edges'][1]['source']
'2'
>>> testfile_2_p['graph']['edges'][1]['target']
'18'
>>> testfile_2_p['graph']['edges'][1]['weight']
'5'
>>> random.seed(20)
>>> json_maker('testfile3',10,30,100,0,4,2,1,1,1)
137
>>> file=open('testfile3.json','r')
>>> testfile_3=json.load(file)
>>> testfile_3['graph']['nodes'][1]
{'id': '2'}
>>> testfile_3['graph']['edges'][1]['source']
'3'
>>> testfile_3['graph']['edges'][1]['target']
'76'
>>> testfile_3['graph']['edges'][1]['weight']
'15'
>>> json_to_yaml('testfile3')
>>> file=open('testfile3.yaml','r')
>>> testfile_3_yaml=yaml.load(file)
>>> testfile_3_yaml['graph']['nodes'][1]
{'id': '2'}
>>> testfile_3_yaml['graph']['edges'][1]['source']
'3'
>>> testfile_3_yaml['graph']['edges'][1]['target']
'76'
>>> testfile_3_yaml['graph']['edges'][1]['weight']
'15'
>>> json_to_yaml('testfile24')
[Error] Bad Input File!
>>> json_to_pickle('testfile24')
[Error] Bad Input File!
>>> json_maker('testfile', 0, 200, 10, 0, 0,1)
Traceback (most recent call last):
        ...
TypeError: json_maker() missing 3 required positional arguments: 'direct', 'self_loop', and 'multigraph'
>>> json_to_pickle('testfile3')
>>> testfile_3_p=pickle.load( open( 'testfile3.p', 'rb' ) )
>>> testfile_3_p['graph']['edges'][1]['source']
'3'
>>> testfile_3_p['graph']['edges'][1]['target']
'76'
>>> testfile_3_p['graph']['edges'][1]['weight']
'15'
>>> random.seed(2)
>>> csv_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
7
>>> random.seed(2)
>>> gml_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
7
>>> file=open('testfile.gml','r')
>>> print(file.read())
graph
[
  multigraph 0
  directed  1
  node
  [
   id 1
   label "Node 1"
  ]
  node
  [
   id 2
   label "Node 2"
  ]
  node
  [
   id 3
   label "Node 3"
  ]
  node
  [
   id 4
   label "Node 4"
  ]
  node
  [
   id 5
   label "Node 5"
  ]
  node
  [
   id 6
   label "Node 6"
  ]
  node
  [
   id 7
   label "Node 7"
  ]
  node
  [
   id 8
   label "Node 8"
  ]
  node
  [
   id 9
   label "Node 9"
  ]
  node
  [
   id 10
   label "Node 10"
  ]
  edge
  [
   source 4
   target 3
   value -64
  ]
  edge
  [
   source 5
   target 6
   value 148
  ]
  edge
  [
   source 5
   target 9
   value 110
  ]
  edge
  [
   source 6
   target 10
   value -139
  ]
  edge
  [
   source 7
   target 7
   value 7
  ]
  edge
  [
   source 8
   target 2
   value -97
  ]
  edge
  [
   source 9
   target 1
   value 60
  ]
]
>>> random.seed(2)
>>> gexf_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
7
>>> file=open('testfile.gexf', 'r')
>>> random.seed(2)
>>> mtx_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
7
>>> random.seed(2)
>>> tsv_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
7
>>> file=open('testfile.mtx','r')
>>> print(file.read())
%%MatrixMarket matrix coordinate real general
10    10    7
4     3     -64
5     6     148
5     9     110
6     10    -139
7     7     7
8     2     -97
9     1     60
<BLANKLINE>
>>> random.seed(2)
>>> gdf_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
7
>>> file=open('testfile.gdf','r')
>>> print(file.read())
nodedef>name VARCHAR,label VARCHAR
1,Node1
2,Node2
3,Node3
4,Node4
5,Node5
6,Node6
7,Node7
8,Node8
9,Node9
10,Node10
edgedef>node1 VARCHAR,node2 VARCHAR,weight DOUBLE
4,3,-64
5,6,148
5,9,110
6,10,-139
7,7,7
8,2,-97
9,1,60
<BLANKLINE>
>>> random.seed(2)
>>> gl_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
7
>>> file=open('testfile.gl','r')
>>> print(file.read())
4 3:-64
5 6:148 9:110
6 10:-139
7 7:7
8 2:-97
9 1:60
<BLANKLINE>
>>> file=open('testfile.csv','r')
>>> print(file.read())
4,3,-64
5,6,148
5,9,110
6,10,-139
7,7,7
8,2,-97
9,1,60
<BLANKLINE>
>>> random.seed(4)
>>> csv_maker('testfile2',0,50,30,0,4,0,1,1,1)
35
>>> file=open('testfile2.csv','r')
>>> print(file.read())
1,10,46
2,18,5
2,4,25
2,22,-48
4,23,-17
5,7,-13
7,15,10
7,17,-40
8,8,-42
8,25,11
9,29,-5
10,3,-36
10,27,-48
11,13,-27
11,26,-27
11,21,14
11,16,-2
14,20,-44
14,14,43
14,12,26
15,28,-11
16,30,-40
16,24,20
19,19,7
20,12,-29
20,1,22
22,24,20
22,23,-9
23,18,18
23,27,28
24,6,-24
25,17,23
27,6,-50
28,21,28
28,13,-13
<BLANKLINE>
>>> random.seed(4)
>>> csv_maker('testfile4',0,50.2,30,0,4,0,1,1,1)
41
>>> file=open('testfile4.csv','r')
>>> print(file.read())
1,10,36.2
2,6,3.3
2,16,-40.2
2,29,11.1
3,17,-39.1
3,7,-10.8
3,3,-40.2
4,12,-14.5
5,9,-33.7
5,28,8.9
6,21,47.4
6,27,-0.4
6,15,-42.6
7,20,-30.1
8,23,11.7
8,18,4.1
8,25,-26.0
9,24,50.1
9,13,20.7
9,14,-13.9
10,26,-31.8
10,19,-5.1
12,22,6.1
13,30,-1.3
14,11,-36.9
14,22,16.2
15,16,-43.2
15,11,-31.0
16,19,12.6
17,21,18.2
18,18,-39.3
18,25,-28.7
19,23,-46.0
24,20,27.4
25,4,-50.1
25,1,-38.8
26,27,-10.1
26,30,-24.7
26,29,-12.5
27,28,-9.4
29,20,26.4
<BLANKLINE>
>>> random.seed(20)
>>> csv_maker('testfile3',10,30,100,0,4,2,1,1,1)
137
>>> file=open('testfile3.csv','r')
>>> print(file.read())
1,34,30
3,76,15
3,5,23
4,13,13
4,21,20
4,67,28
5,60,16
5,32,20
5,92,20
6,64,12
6,94,26
7,62,12
7,36,28
7,42,11
8,20,12
9,47,19
10,49,15
10,27,10
11,48,17
11,51,11
13,58,14
13,70,29
14,37,30
14,61,27
14,87,15
15,84,13
16,83,28
17,45,17
17,24,29
17,18,26
18,59,15
19,98,12
21,2,30
21,99,20
22,69,26
22,96,11
22,88,15
24,79,20
24,12,12
24,82,13
26,50,30
26,30,19
29,52,26
31,25,26
32,68,14
33,65,13
33,78,13
33,55,17
34,63,13
35,44,27
35,57,14
37,74,10
37,41,16
37,100,30
38,72,13
38,56,16
39,91,19
39,43,13
41,28,22
41,81,19
42,90,13
42,46,28
42,97,16
45,86,10
45,53,18
46,85,13
46,23,11
47,71,29
48,95,12
48,77,19
48,93,11
49,75,22
50,73,18
50,40,24
50,54,28
51,80,17
51,66,19
51,89,20
52,58,29
52,16,21
52,43,12
53,8,13
53,98,17
54,55,10
56,62,26
56,27,10
57,70,26
58,44,22
59,90,27
59,91,19
59,78,29
60,87,12
60,92,25
61,69,14
61,79,17
62,25,21
63,97,27
63,29,30
65,9,26
65,64,21
66,67,27
66,95,19
66,93,30
68,30,18
70,83,12
70,99,15
71,31,17
71,89,20
73,36,18
75,72,12
76,2,26
76,12,25
76,86,22
78,23,19
78,100,27
79,40,24
80,84,26
80,80,14
81,20,16
82,15,16
82,88,22
83,19,19
84,85,13
84,28,16
85,77,16
85,94,23
86,1,21
87,74,15
87,96,19
90,93,22
92,49,14
95,98,26
95,55,11
97,38,28
99,19,29
99,89,24
100,40,11
<BLANKLINE>
>>> csv_maker('testfile', 0, 200, 10, 0,0,1)
Traceback (most recent call last):
        ...
TypeError: csv_maker() missing 3 required positional arguments: 'direct', 'self_loop', and 'multigraph'
>>> random.seed(2)
>>> wel_maker('testfile', 0, 200, 10, 0, 2, 0,1,1,1)
7
>>> file=open('testfile.wel','r')
>>> print(file.read())
4 3 -64
5 6 148
5 9 110
6 10 -139
7 7 7
8 2 -97
9 1 60
<BLANKLINE>
>>> random.seed(4)
>>> wel_maker('testfile2',0,50,30,0,4,0,1,1,1)
35
>>> file=open('testfile2.wel','r')
>>> print(file.read())
1 10 46
2 18 5
2 4 25
2 22 -48
4 23 -17
5 7 -13
7 15 10
7 17 -40
8 8 -42
8 25 11
9 29 -5
10 3 -36
10 27 -48
11 13 -27
11 26 -27
11 21 14
11 16 -2
14 20 -44
14 14 43
14 12 26
15 28 -11
16 30 -40
16 24 20
19 19 7
20 12 -29
20 1 22
22 24 20
22 23 -9
23 18 18
23 27 28
24 6 -24
25 17 23
27 6 -50
28 21 28
28 13 -13
<BLANKLINE>
>>> random.seed(20)
>>> wel_maker('testfile3',10,30,100,0,4,2,1,1,1)
137
>>> file=open('testfile3.wel','r')
>>> print(file.read())
1 34 30
3 76 15
3 5 23
4 13 13
4 21 20
4 67 28
5 60 16
5 32 20
5 92 20
6 64 12
6 94 26
7 62 12
7 36 28
7 42 11
8 20 12
9 47 19
10 49 15
10 27 10
11 48 17
11 51 11
13 58 14
13 70 29
14 37 30
14 61 27
14 87 15
15 84 13
16 83 28
17 45 17
17 24 29
17 18 26
18 59 15
19 98 12
21 2 30
21 99 20
22 69 26
22 96 11
22 88 15
24 79 20
24 12 12
24 82 13
26 50 30
26 30 19
29 52 26
31 25 26
32 68 14
33 65 13
33 78 13
33 55 17
34 63 13
35 44 27
35 57 14
37 74 10
37 41 16
37 100 30
38 72 13
38 56 16
39 91 19
39 43 13
41 28 22
41 81 19
42 90 13
42 46 28
42 97 16
45 86 10
45 53 18
46 85 13
46 23 11
47 71 29
48 95 12
48 77 19
48 93 11
49 75 22
50 73 18
50 40 24
50 54 28
51 80 17
51 66 19
51 89 20
52 58 29
52 16 21
52 43 12
53 8 13
53 98 17
54 55 10
56 62 26
56 27 10
57 70 26
58 44 22
59 90 27
59 91 19
59 78 29
60 87 12
60 92 25
61 69 14
61 79 17
62 25 21
63 97 27
63 29 30
65 9 26
65 64 21
66 67 27
66 95 19
66 93 30
68 30 18
70 83 12
70 99 15
71 31 17
71 89 20
73 36 18
75 72 12
76 2 26
76 12 25
76 86 22
78 23 19
78 100 27
79 40 24
80 84 26
80 80 14
81 20 16
82 15 16
82 88 22
83 19 19
84 85 13
84 28 16
85 77 16
85 94 23
86 1 21
87 74 15
87 96 19
90 93 22
92 49 14
95 98 26
95 55 11
97 38 28
99 19 29
99 89 24
100 40 11
<BLANKLINE>
>>> wel_maker('testfile', 0, 200, 10, 0,0,1)
Traceback (most recent call last):
        ...
TypeError: wel_maker() missing 3 required positional arguments: 'direct', 'self_loop', and 'multigraph'
>>> random.seed(2)
>>> lp_maker('testfile', 0, 200, 10, 0, 2, 0,1,1,1)
7
>>> file=open('testfile.lp','r')
>>> print(file.read())
node(1).
node(2).
node(3).
node(4).
node(5).
node(6).
node(7).
node(8).
node(9).
node(10).
edge(4,3,-64).
edge(5,6,148).
edge(5,9,110).
edge(6,10,-139).
edge(7,7,7).
edge(8,2,-97).
edge(9,1,60).
<BLANKLINE>
>>> random.seed(4)
>>> lp_maker('testfile2',0,50,30,0,4,0,1,1,1)
35
>>> file=open('testfile2.lp','r')
>>> print(file.read())
node(1).
node(2).
node(3).
node(4).
node(5).
node(6).
node(7).
node(8).
node(9).
node(10).
node(11).
node(12).
node(13).
node(14).
node(15).
node(16).
node(17).
node(18).
node(19).
node(20).
node(21).
node(22).
node(23).
node(24).
node(25).
node(26).
node(27).
node(28).
node(29).
node(30).
edge(1,10,46).
edge(2,18,5).
edge(2,4,25).
edge(2,22,-48).
edge(4,23,-17).
edge(5,7,-13).
edge(7,15,10).
edge(7,17,-40).
edge(8,8,-42).
edge(8,25,11).
edge(9,29,-5).
edge(10,3,-36).
edge(10,27,-48).
edge(11,13,-27).
edge(11,26,-27).
edge(11,21,14).
edge(11,16,-2).
edge(14,20,-44).
edge(14,14,43).
edge(14,12,26).
edge(15,28,-11).
edge(16,30,-40).
edge(16,24,20).
edge(19,19,7).
edge(20,12,-29).
edge(20,1,22).
edge(22,24,20).
edge(22,23,-9).
edge(23,18,18).
edge(23,27,28).
edge(24,6,-24).
edge(25,17,23).
edge(27,6,-50).
edge(28,21,28).
edge(28,13,-13).
<BLANKLINE>
>>> input_dic=get_input(input_func=lambda x: str(len(x)))
>>> input_dic['sign']
2
>>> input_dic['vertices']
20
>>> input_dic['min_edge']
20
>>> input_dic['min_weight']
1
>>> input_dic['output_format']
1
>>> input_dic['max_weight']
1
>>> input_dic['file_name']
'14'
>>> input_dic['max_edge']
20
>>> random.seed(2)
>>> tgf_maker('testfile', 0, 200, 10, 0, 2, 0, 1, 1,1)
7
>>> file=open('testfile.tgf','r')
>>> print(file.read())
1
2
3
4
5
6
7
8
9
10
#
4 3 -64
5 6 148
5 9 110
6 10 -139
7 7 7
8 2 -97
9 1 60
<BLANKLINE>
>>> random.seed(4)
>>> tgf_maker('testfile2',0,50,30,0,4,0,1,1,1)
35
>>> file=open('testfile2.tgf','r')
>>> print(file.read())
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
#
1 10 46
2 18 5
2 4 25
2 22 -48
4 23 -17
5 7 -13
7 15 10
7 17 -40
8 8 -42
8 25 11
9 29 -5
10 3 -36
10 27 -48
11 13 -27
11 26 -27
11 21 14
11 16 -2
14 20 -44
14 14 43
14 12 26
15 28 -11
16 30 -40
16 24 20
19 19 7
20 12 -29
20 1 22
22 24 20
22 23 -9
23 18 18
23 27 28
24 6 -24
25 17 23
27 6 -50
28 21 28
28 13 -13
<BLANKLINE>
>>> random.seed(2)
>>> dl_maker('testfile', 0, 200, 10, 0, 2, 0,1,1,1)
7
>>> file=open('testfile.dl','r')
>>> print(file.read())
dl
format=edgelist1
n=10
data:
4 3 -64
5 6 148
5 9 110
6 10 -139
7 7 7
8 2 -97
9 1 60
<BLANKLINE>
>>> random.seed(4)
>>> dl_maker('testfile2',0,50,30,0,4,0,1,1,1)
35
>>> file=open('testfile2.dl','r')
>>> print(file.read())
dl
format=edgelist1
n=30
data:
1 10 46
2 18 5
2 4 25
2 22 -48
4 23 -17
5 7 -13
7 15 10
7 17 -40
8 8 -42
8 25 11
9 29 -5
10 3 -36
10 27 -48
11 13 -27
11 26 -27
11 21 14
11 16 -2
14 20 -44
14 14 43
14 12 26
15 28 -11
16 30 -40
16 24 20
19 19 7
20 12 -29
20 1 22
22 24 20
22 23 -9
23 18 18
23 27 28
24 6 -24
25 17 23
27 6 -50
28 21 28
28 13 -13
<BLANKLINE>
>>> file.close()
>>> os.remove('testfile.csv')
>>> os.remove('testfile.gml')
>>> os.remove('testfile.gexf')
>>> os.remove('testfile.tsv')
>>> os.remove('testfile.dl')
>>> os.remove('testfile.gr')
>>> os.remove('testfile.json')
>>> os.remove('testfile.lp')
>>> os.remove('testfile.p')
>>> os.remove('testfile.tgf')
>>> os.remove('testfile.wel')
>>> os.remove('testfile.yaml')
>>> os.remove('testfile.mtx')
>>> os.remove('testfile.gdf')
>>> os.remove('testfile.gl')
>>> os.remove('testfile2.csv')
>>> os.remove('testfile2.dl')
>>> os.remove('testfile2.gr')
>>> os.remove('testfile2.json')
>>> os.remove('testfile2.lp')
>>> os.remove('testfile2.p')
>>> os.remove('testfile2.tgf')
>>> os.remove('testfile2.wel')
>>> os.remove('testfile2.yaml')
>>> os.remove('testfile3.csv')
>>> os.remove('testfile4.csv')
>>> os.remove('testfile3.gr')
>>> os.remove('testfile3.json')
>>> os.remove('testfile3.p')
>>> os.remove('testfile3.wel')
>>> os.remove('testfile3.yaml')
>>> os.remove('logfile.log')

"""
