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
>>> all_vertices = list(range(1, 41))
>>> random.seed(2)
>>> branch_gen(1,10,10,1,20,1,1,1,1,all_vertices,used_vertices,degree_dict)
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
TypeError: branch_gen() missing 8 required positional arguments: 'max_weight', 'sign', 'direct', 'self_loop', 'multigraph', 'all_vertices', 'used_vertices', and 'degree_dict'
>>> random.seed(2)
>>> edge_gen(20,0,400,2,10,1,1,1,1)
[{1: [3, 7], 2: [20, 6, 14, 17, 1], 3: [13, 6, 9, 14, 16, 18, 11], 4: [12, 14, 19, 9, 15, 6, 16], 5: [20, 16, 18, 7], 6: [20, 1, 5, 3, 11, 13, 7], 7: [2, 13, 1, 5, 3, 7, 8], 8: [8, 1], 9: [10, 1, 20], 10: [20, 8, 12, 17, 15, 9, 16, 1], 11: [9, 7], 12: [17, 8, 10, 9, 18], 13: [5, 15], 14: [9, 1, 11, 2, 8, 17, 20], 15: [1, 18, 17, 20, 13, 19, 2], 16: [7, 2, 19], 17: [11, 12, 19], 18: [13, 12, 9, 16, 18, 19], 19: [16, 5], 20: [17, 18, 8]}, {1: [184, -128], 2: [297, -326, -278, -18, -238], 3: [-269, 120, 90, 69, 228, -376, -303], 4: [-82, -335, 250, -256, -236, -249, 166], 5: [-395, -155, -159, -262], 6: [174, 381, 294, -302, 386, 136, 30], 7: [185, 127, 58, 20, -130, 376, 197], 8: [18, -315], 9: [-250, -229, 135], 10: [242, 338, 12, 265, -263, -134, -334, 343], 11: [67, 232], 12: [126, -37, 302, -131, -269], 13: [196, 56], 14: [51, 384, 111, -232, -108, 373, -217], 15: [214, 48, -9, 312, -353, -157, -51], 16: [231, -326, -106], 17: [190, 112, 59], 18: [-71, -62, 62, -108, 12, -397], 19: [-183, -137], 20: [-368, -202, 250]}, 92]
>>> random.seed(11)
>>> edge_gen(20,0,100,2,10,2,1,1,1)
[{1: [18, 15, 19, 7, 20, 11, 2, 6, 3], 2: [20, 15], 3: [20, 17, 2, 8], 4: [15, 16], 5: [17, 10, 1, 4, 12], 6: [3, 10, 9, 13, 4, 18, 11, 7, 2], 7: [7, 2], 8: [13, 3, 8, 11, 4, 9, 12, 2], 9: [4, 2, 18, 9, 10], 10: [14, 13, 15, 7], 11: [19, 7, 5, 4, 13, 2], 12: [10, 3, 4, 11, 16, 14, 5], 13: [19, 13, 5, 9, 10, 4], 14: [7, 14, 3, 2, 15, 9, 20, 16], 15: [10, 3, 20, 15, 14], 16: [7, 4, 17, 12, 18, 16], 17: [18, 5, 19, 20, 7, 13, 14], 18: [14, 13, 20, 15, 5], 19: [13, 19, 20], 20: [20, 14]}, {1: [99, 57, 75, 23, 80, 23, 57, 18, 68], 2: [50, 83], 3: [1, 8, 4, 30], 4: [41, 75], 5: [29, 63, 84, 58, 52], 6: [90, 40, 65, 3, 72, 13, 13, 49, 2], 7: [26, 60], 8: [53, 72, 99, 43, 39, 1, 97, 17], 9: [1, 59, 22, 57, 93], 10: [82, 14, 53, 0], 11: [38, 50, 5, 27, 33, 98], 12: [49, 9, 26, 1, 47, 58, 75], 13: [17, 23, 39, 78, 92, 20], 14: [87, 61, 53, 13, 32, 94, 50, 76], 15: [66, 16, 71, 78, 9], 16: [26, 34, 57, 47, 73, 17], 17: [74, 75, 39, 81, 61, 40, 57], 18: [45, 3, 1, 48, 10], 19: [49, 56, 69], 20: [14, 99]}, 105]
>>> edge_gen(0,400,2,10,1)
Traceback (most recent call last):
        ...
TypeError: edge_gen() missing 4 required positional arguments: 'sign', 'direct', 'self_loop', and 'multigraph'
>>> random.seed(2)
>>> dimacs_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
6
>>> file=open('testfile.gr','r')
>>> print(file.read())
c FILE                  :testfile.gr
c No. of vertices       :10
c No. of edges          :6
c Max. weight           :200
c Min. weight           :0
c Min. edge             :0
c Max. edge             :2
p sp 10 6
a 4 3 -64
a 5 4 148
a 5 3 -163
a 6 9 -139
a 7 9 -9
a 10 6 -108
<BLANKLINE>
>>> random.seed(4)
>>> dimacs_maker('testfile2',0,50,30,0,4,0,1,1,1)
40
>>> file=open('testfile2.gr','r')
>>> print(file.read())
c FILE                  :testfile2.gr
c No. of vertices       :30
c No. of edges          :40
c Max. weight           :50
c Min. weight           :0
c Min. edge             :0
c Max. edge             :4
p sp 30 40
a 1 10 46
a 2 16 5
a 2 3 25
a 2 20 -48
a 4 17 -17
a 5 27 16
a 6 30 41
a 7 26 -12
a 7 6 -18
a 8 3 -42
a 8 14 11
a 9 16 -5
a 10 27 0
a 10 10 -48
a 10 18 26
a 11 20 -27
a 11 15 14
a 11 10 -2
a 14 21 -33
a 14 18 -44
a 14 11 43
a 15 3 -12
a 16 9 22
a 16 15 -40
a 17 7 -6
a 17 28 45
a 17 9 -48
a 18 20 7
a 18 6 -29
a 21 23 18
a 21 25 -1
a 22 10 -9
a 22 26 -39
a 24 20 28
a 24 10 16
a 25 6 -36
a 25 1 -2
a 25 8 -50
a 26 10 28
a 26 7 -13
<BLANKLINE>
>>> random.seed(20)
>>> dimacs_maker('testfile3',10,30,100,0,4,2,1,1,1)
167
>>> file=open('testfile3.gr','r')
>>> print(file.read())
c FILE                  :testfile3.gr
c No. of vertices       :100
c No. of edges          :167
c Max. weight           :30
c Min. weight           :10
c Min. edge             :0
c Max. edge             :4
p sp 100 167
a 1 34 30
a 3 74 15
a 3 4 23
a 4 10 13
a 4 18 20
a 4 63 28
a 5 53 16
a 5 26 20
a 5 83 20
a 6 55 12
a 6 82 26
a 7 52 12
a 7 27 28
a 7 33 11
a 8 13 12
a 9 33 19
a 10 89 18
a 10 21 29
a 13 91 17
a 13 29 28
a 14 8 10
a 15 39 18
a 15 18 30
a 15 45 29
a 15 96 24
a 16 82 18
a 17 56 15
a 17 22 22
a 17 93 13
a 17 91 14
a 18 55 21
a 18 29 13
a 19 7 26
a 19 26 23
a 19 24 15
a 19 12 13
a 20 1 30
a 20 42 22
a 21 68 11
a 21 87 15
a 21 16 24
a 22 43 10
a 22 10 28
a 22 98 13
a 24 33 30
a 24 11 19
a 27 29 26
a 28 90 10
a 28 88 26
a 28 43 14
a 28 58 18
a 30 13 16
a 30 32 16
a 30 30 13
a 31 73 22
a 31 86 12
a 32 63 10
a 32 23 16
a 32 84 19
a 33 39 16
a 34 80 19
a 34 89 13
a 36 8 22
a 36 49 19
a 37 60 13
a 37 9 28
a 37 63 16
a 39 9 27
a 39 81 20
a 41 36 19
a 42 1 11
a 42 99 16
a 42 83 22
a 43 11 28
a 43 48 19
a 44 85 14
a 44 81 22
a 44 73 22
a 45 1 24
a 45 78 25
a 45 44 17
a 46 38 24
a 47 49 16
a 47 81 11
a 48 12 21
a 48 3 13
a 49 31 27
a 49 40 10
a 50 88 21
a 51 68 14
a 51 3 17
a 52 68 24
a 52 52 22
a 52 92 27
a 53 65 29
a 53 85 19
a 54 98 12
a 54 84 25
a 54 35 21
a 54 97 14
a 55 85 17
a 55 63 14
a 56 82 27
a 56 85 27
a 58 83 11
a 58 68 16
a 59 51 16
a 59 71 26
a 60 61 30
a 60 23 14
a 61 36 10
a 62 86 12
a 62 37 17
a 62 89 20
a 62 11 14
a 64 41 12
a 64 67 11
a 65 6 25
a 65 52 26
a 65 98 13
a 66 91 19
a 67 71 23
a 67 60 24
a 67 91 26
a 69 23 16
a 70 38 13
a 71 58 22
a 72 9 19
a 72 83 27
a 72 16 16
a 73 94 19
a 74 57 25
a 76 98 15
a 76 74 28
a 77 38 14
a 77 2 20
a 78 38 26
a 78 96 14
a 78 25 29
a 79 5 13
a 79 56 28
a 79 74 16
a 79 84 24
a 80 53 11
a 80 93 15
a 80 23 13
a 81 77 28
a 82 31 13
a 84 89 27
a 86 73 15
a 86 69 11
a 87 12 26
a 87 51 18
a 87 76 22
a 92 95 15
a 92 99 24
a 92 57 11
a 94 97 16
a 94 50 27
a 94 61 12
a 95 69 19
a 95 14 24
a 96 20 29
a 99 24 16
a 99 25 17
a 100 8 17
a 100 69 30
<BLANKLINE>
>>> dimacs_maker('testfile', 0, 200, 10, 0,0,1)
Traceback (most recent call last):
        ...
TypeError: dimacs_maker() missing 3 required positional arguments: 'direct', 'self_loop', and 'multigraph'
>>> random.seed(2)
>>> json_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
6
>>> file=open('testfile.json','r')
>>> testfile_1=json.load(file)
>>> testfile_1['graph']['nodes'][1]
{'id': '2'}
>>> testfile_1['graph']['edges'][1]['source']
'5'
>>> testfile_1['graph']['edges'][1]['target']
'4'
>>> testfile_1['graph']['edges'][1]['weight']
'148'
>>> json_to_yaml('testfile')
>>> file=open('testfile.yaml','r')
>>> testfile_1_yaml=yaml.load(file)
>>> testfile_1_yaml['graph']['edges'][1]['source']
'5'
>>> testfile_1_yaml['graph']['edges'][1]['target']
'4'
>>> testfile_1_yaml['graph']['edges'][1]['weight']
'148'
>>> json_to_pickle('testfile')
>>> testfile_1_p=pickle.load( open( 'testfile.p', 'rb' ) )
>>> testfile_1_p['graph']['edges'][1]['source']
'5'
>>> testfile_1_p['graph']['edges'][1]['target']
'4'
>>> testfile_1_p['graph']['edges'][1]['weight']
'148'
>>> random.seed(4)
>>> json_maker('testfile2',0,50,30,0,4,0,1,1,1)
40
>>> file=open('testfile2.json','r')
>>> testfile_2=json.load(file)
>>> testfile_2['graph']['nodes'][1]
{'id': '2'}
>>> testfile_2['graph']['edges'][1]['source']
'2'
>>> testfile_2['graph']['edges'][1]['target']
'16'
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
'16'
>>> testfile_2_yaml['graph']['edges'][1]['weight']
'5'
>>> json_to_pickle('testfile2')
>>> testfile_2_p=pickle.load( open( 'testfile2.p', 'rb' ) )
>>> testfile_2_p['graph']['edges'][1]['source']
'2'
>>> testfile_2_p['graph']['edges'][1]['target']
'16'
>>> testfile_2_p['graph']['edges'][1]['weight']
'5'
>>> random.seed(20)
>>> json_maker('testfile3',10,30,100,0,4,2,1,1,1)
167
>>> file=open('testfile3.json','r')
>>> testfile_3=json.load(file)
>>> testfile_3['graph']['nodes'][1]
{'id': '2'}
>>> testfile_3['graph']['edges'][1]['source']
'3'
>>> testfile_3['graph']['edges'][1]['target']
'74'
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
'74'
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
'74'
>>> testfile_3_p['graph']['edges'][1]['weight']
'15'
>>> random.seed(2)
>>> csv_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
6
>>> random.seed(2)
>>> gml_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
6
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
   target 4
   value 148
  ]
  edge
  [
   source 5
   target 3
   value -163
  ]
  edge
  [
   source 6
   target 9
   value -139
  ]
  edge
  [
   source 7
   target 9
   value -9
  ]
  edge
  [
   source 10
   target 6
   value -108
  ]
]
>>> random.seed(2)
>>> gexf_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
6
>>> file=open('testfile.gexf', 'r')
>>> random.seed(2)
>>> mtx_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
6
>>> random.seed(2)
>>> tsv_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
6
>>> file=open('testfile.mtx','r')
>>> print(file.read())
%%MatrixMarket matrix coordinate real general
10    10    6
4     3     -64
5     4     148
5     3     -163
6     9     -139
7     9     -9
10    6     -108
<BLANKLINE>
>>> random.seed(2)
>>> gdf_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
6
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
5,4,148
5,3,-163
6,9,-139
7,9,-9
10,6,-108
<BLANKLINE>
>>> random.seed(2)
>>> gl_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
6
>>> file=open('testfile.gl','r')
>>> print(file.read())
1
2
3
4 3:-64
5 4:148 3:-163
6 9:-139
7 9:-9
8
9
10 6:-108
<BLANKLINE>
>>> file=open('testfile.csv','r')
>>> print(file.read())
4,3,-64
5,4,148
5,3,-163
6,9,-139
7,9,-9
10,6,-108
<BLANKLINE>
>>> random.seed(4)
>>> csv_maker('testfile2',0,50,30,0,4,0,1,1,1)
40
>>> file=open('testfile2.csv','r')
>>> print(file.read())
1,10,46
2,16,5
2,3,25
2,20,-48
4,17,-17
5,27,16
6,30,41
7,26,-12
7,6,-18
8,3,-42
8,14,11
9,16,-5
10,27,0
10,10,-48
10,18,26
11,20,-27
11,15,14
11,10,-2
14,21,-33
14,18,-44
14,11,43
15,3,-12
16,9,22
16,15,-40
17,7,-6
17,28,45
17,9,-48
18,20,7
18,6,-29
21,23,18
21,25,-1
22,10,-9
22,26,-39
24,20,28
24,10,16
25,6,-36
25,1,-2
25,8,-50
26,10,28
26,7,-13
<BLANKLINE>
>>> random.seed(4)
>>> csv_maker('testfile4',0,50.2,30,0,4,0,1,1,1)
56
>>> file=open('testfile4.csv','r')
>>> print(file.read())
1,10,36.2
2,5,3.3
2,14,-40.2
2,27,11.1
3,12,-39.1
3,28,13.1
3,1,-40.2
3,8,15.6
4,29,-33.7
4,18,8.9
5,9,47.4
5,28,-0.4
5,11,-42.6
6,7,-21.3
6,11,-22.7
6,9,-13.0
6,29,4.1
7,21,-26.0
7,22,-35.2
7,25,3.3
8,21,-13.9
9,14,-31.8
9,12,42.1
10,26,6.1
11,10,-1.3
12,23,45.0
12,10,-0.9
13,11,38.9
13,15,14.7
14,29,-14.7
15,13,16.6
15,1,-2.2
16,27,-50.1
17,4,-49.3
17,15,5.7
17,2,37.0
17,23,30.4
18,16,16.1
18,30,-38.8
18,25,24.0
19,14,-1.9
20,8,-41.7
20,13,-12.2
20,23,-7.1
22,19,49.7
22,23,24.8
24,29,16.9
24,30,-40.9
24,19,32.9
25,26,2.2
25,25,38.5
26,22,43.7
26,24,-28.6
27,30,-11.0
27,1,46.3
30,4,-40.7
<BLANKLINE>
>>> random.seed(20)
>>> csv_maker('testfile3',10,30,100,0,4,2,1,1,1)
167
>>> file=open('testfile3.csv','r')
>>> print(file.read())
1,34,30
3,74,15
3,4,23
4,10,13
4,18,20
4,63,28
5,53,16
5,26,20
5,83,20
6,55,12
6,82,26
7,52,12
7,27,28
7,33,11
8,13,12
9,33,19
10,89,18
10,21,29
13,91,17
13,29,28
14,8,10
15,39,18
15,18,30
15,45,29
15,96,24
16,82,18
17,56,15
17,22,22
17,93,13
17,91,14
18,55,21
18,29,13
19,7,26
19,26,23
19,24,15
19,12,13
20,1,30
20,42,22
21,68,11
21,87,15
21,16,24
22,43,10
22,10,28
22,98,13
24,33,30
24,11,19
27,29,26
28,90,10
28,88,26
28,43,14
28,58,18
30,13,16
30,32,16
30,30,13
31,73,22
31,86,12
32,63,10
32,23,16
32,84,19
33,39,16
34,80,19
34,89,13
36,8,22
36,49,19
37,60,13
37,9,28
37,63,16
39,9,27
39,81,20
41,36,19
42,1,11
42,99,16
42,83,22
43,11,28
43,48,19
44,85,14
44,81,22
44,73,22
45,1,24
45,78,25
45,44,17
46,38,24
47,49,16
47,81,11
48,12,21
48,3,13
49,31,27
49,40,10
50,88,21
51,68,14
51,3,17
52,68,24
52,52,22
52,92,27
53,65,29
53,85,19
54,98,12
54,84,25
54,35,21
54,97,14
55,85,17
55,63,14
56,82,27
56,85,27
58,83,11
58,68,16
59,51,16
59,71,26
60,61,30
60,23,14
61,36,10
62,86,12
62,37,17
62,89,20
62,11,14
64,41,12
64,67,11
65,6,25
65,52,26
65,98,13
66,91,19
67,71,23
67,60,24
67,91,26
69,23,16
70,38,13
71,58,22
72,9,19
72,83,27
72,16,16
73,94,19
74,57,25
76,98,15
76,74,28
77,38,14
77,2,20
78,38,26
78,96,14
78,25,29
79,5,13
79,56,28
79,74,16
79,84,24
80,53,11
80,93,15
80,23,13
81,77,28
82,31,13
84,89,27
86,73,15
86,69,11
87,12,26
87,51,18
87,76,22
92,95,15
92,99,24
92,57,11
94,97,16
94,50,27
94,61,12
95,69,19
95,14,24
96,20,29
99,24,16
99,25,17
100,8,17
100,69,30
<BLANKLINE>
>>> csv_maker('testfile', 0, 200, 10, 0,0,1)
Traceback (most recent call last):
        ...
TypeError: csv_maker() missing 3 required positional arguments: 'direct', 'self_loop', and 'multigraph'
>>> random.seed(2)
>>> wel_maker('testfile', 0, 200, 10, 0, 2, 0,1,1,1)
6
>>> file=open('testfile.wel','r')
>>> print(file.read())
4 3 -64
5 4 148
5 3 -163
6 9 -139
7 9 -9
10 6 -108
<BLANKLINE>
>>> random.seed(4)
>>> wel_maker('testfile2',0,50,30,0,4,0,1,1,1)
40
>>> file=open('testfile2.wel','r')
>>> print(file.read())
1 10 46
2 16 5
2 3 25
2 20 -48
4 17 -17
5 27 16
6 30 41
7 26 -12
7 6 -18
8 3 -42
8 14 11
9 16 -5
10 27 0
10 10 -48
10 18 26
11 20 -27
11 15 14
11 10 -2
14 21 -33
14 18 -44
14 11 43
15 3 -12
16 9 22
16 15 -40
17 7 -6
17 28 45
17 9 -48
18 20 7
18 6 -29
21 23 18
21 25 -1
22 10 -9
22 26 -39
24 20 28
24 10 16
25 6 -36
25 1 -2
25 8 -50
26 10 28
26 7 -13
<BLANKLINE>
>>> random.seed(20)
>>> wel_maker('testfile3',10,30,100,0,4,2,1,1,1)
167
>>> file=open('testfile3.wel','r')
>>> print(file.read())
1 34 30
3 74 15
3 4 23
4 10 13
4 18 20
4 63 28
5 53 16
5 26 20
5 83 20
6 55 12
6 82 26
7 52 12
7 27 28
7 33 11
8 13 12
9 33 19
10 89 18
10 21 29
13 91 17
13 29 28
14 8 10
15 39 18
15 18 30
15 45 29
15 96 24
16 82 18
17 56 15
17 22 22
17 93 13
17 91 14
18 55 21
18 29 13
19 7 26
19 26 23
19 24 15
19 12 13
20 1 30
20 42 22
21 68 11
21 87 15
21 16 24
22 43 10
22 10 28
22 98 13
24 33 30
24 11 19
27 29 26
28 90 10
28 88 26
28 43 14
28 58 18
30 13 16
30 32 16
30 30 13
31 73 22
31 86 12
32 63 10
32 23 16
32 84 19
33 39 16
34 80 19
34 89 13
36 8 22
36 49 19
37 60 13
37 9 28
37 63 16
39 9 27
39 81 20
41 36 19
42 1 11
42 99 16
42 83 22
43 11 28
43 48 19
44 85 14
44 81 22
44 73 22
45 1 24
45 78 25
45 44 17
46 38 24
47 49 16
47 81 11
48 12 21
48 3 13
49 31 27
49 40 10
50 88 21
51 68 14
51 3 17
52 68 24
52 52 22
52 92 27
53 65 29
53 85 19
54 98 12
54 84 25
54 35 21
54 97 14
55 85 17
55 63 14
56 82 27
56 85 27
58 83 11
58 68 16
59 51 16
59 71 26
60 61 30
60 23 14
61 36 10
62 86 12
62 37 17
62 89 20
62 11 14
64 41 12
64 67 11
65 6 25
65 52 26
65 98 13
66 91 19
67 71 23
67 60 24
67 91 26
69 23 16
70 38 13
71 58 22
72 9 19
72 83 27
72 16 16
73 94 19
74 57 25
76 98 15
76 74 28
77 38 14
77 2 20
78 38 26
78 96 14
78 25 29
79 5 13
79 56 28
79 74 16
79 84 24
80 53 11
80 93 15
80 23 13
81 77 28
82 31 13
84 89 27
86 73 15
86 69 11
87 12 26
87 51 18
87 76 22
92 95 15
92 99 24
92 57 11
94 97 16
94 50 27
94 61 12
95 69 19
95 14 24
96 20 29
99 24 16
99 25 17
100 8 17
100 69 30
<BLANKLINE>
>>> wel_maker('testfile', 0, 200, 10, 0,0,1)
Traceback (most recent call last):
        ...
TypeError: wel_maker() missing 3 required positional arguments: 'direct', 'self_loop', and 'multigraph'
>>> random.seed(2)
>>> lp_maker('testfile', 0, 200, 10, 0, 2, 0,1,1,1)
6
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
edge(5,4,148).
edge(5,3,-163).
edge(6,9,-139).
edge(7,9,-9).
edge(10,6,-108).
<BLANKLINE>
>>> random.seed(4)
>>> lp_maker('testfile2',0,50,30,0,4,0,1,1,1)
40
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
edge(2,16,5).
edge(2,3,25).
edge(2,20,-48).
edge(4,17,-17).
edge(5,27,16).
edge(6,30,41).
edge(7,26,-12).
edge(7,6,-18).
edge(8,3,-42).
edge(8,14,11).
edge(9,16,-5).
edge(10,27,0).
edge(10,10,-48).
edge(10,18,26).
edge(11,20,-27).
edge(11,15,14).
edge(11,10,-2).
edge(14,21,-33).
edge(14,18,-44).
edge(14,11,43).
edge(15,3,-12).
edge(16,9,22).
edge(16,15,-40).
edge(17,7,-6).
edge(17,28,45).
edge(17,9,-48).
edge(18,20,7).
edge(18,6,-29).
edge(21,23,18).
edge(21,25,-1).
edge(22,10,-9).
edge(22,26,-39).
edge(24,20,28).
edge(24,10,16).
edge(25,6,-36).
edge(25,1,-2).
edge(25,8,-50).
edge(26,10,28).
edge(26,7,-13).
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
6
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
5 4 148
5 3 -163
6 9 -139
7 9 -9
10 6 -108
<BLANKLINE>
>>> random.seed(4)
>>> tgf_maker('testfile2',0,50,30,0,4,0,1,1,1)
40
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
2 16 5
2 3 25
2 20 -48
4 17 -17
5 27 16
6 30 41
7 26 -12
7 6 -18
8 3 -42
8 14 11
9 16 -5
10 27 0
10 10 -48
10 18 26
11 20 -27
11 15 14
11 10 -2
14 21 -33
14 18 -44
14 11 43
15 3 -12
16 9 22
16 15 -40
17 7 -6
17 28 45
17 9 -48
18 20 7
18 6 -29
21 23 18
21 25 -1
22 10 -9
22 26 -39
24 20 28
24 10 16
25 6 -36
25 1 -2
25 8 -50
26 10 28
26 7 -13
<BLANKLINE>
>>> random.seed(2)
>>> dl_maker('testfile', 0, 200, 10, 0, 2, 0,1,1,1)
6
>>> file=open('testfile.dl','r')
>>> print(file.read())
dl
format=edgelist1
n=10
data:
4 3 -64
5 4 148
5 3 -163
6 9 -139
7 9 -9
10 6 -108
<BLANKLINE>
>>> random.seed(4)
>>> dl_maker('testfile2',0,50,30,0,4,0,1,1,1)
40
>>> file=open('testfile2.dl','r')
>>> print(file.read())
dl
format=edgelist1
n=30
data:
1 10 46
2 16 5
2 3 25
2 20 -48
4 17 -17
5 27 16
6 30 41
7 26 -12
7 6 -18
8 3 -42
8 14 11
9 16 -5
10 27 0
10 10 -48
10 18 26
11 20 -27
11 15 14
11 10 -2
14 21 -33
14 18 -44
14 11 43
15 3 -12
16 9 22
16 15 -40
17 7 -6
17 28 45
17 9 -48
18 20 7
18 6 -29
21 23 18
21 25 -1
22 10 -9
22 26 -39
24 20 28
24 10 16
25 6 -36
25 1 -2
25 8 -50
26 10 28
26 7 -13
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
