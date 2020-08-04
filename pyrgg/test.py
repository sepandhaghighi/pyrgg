# -*- coding: utf-8 -*-
"""Test file."""
"""
>>> from pyrgg import *
>>> import random
>>> import os
>>> import json
>>> import yaml
>>> import pickle
>>> logger(2,2,2,2)
[Error] Logger Faild!
>>> result = input_filter({"file_name": "test","vertices": 5,"max_weight": 1000,"min_weight":455,"min_edge": -45,"max_edge": -11,"sign": 5,"output_format": 19,"direct": 2,"self_loop": 2,"multigraph":2})
>>> result == {'output_format': 1, 'min_weight': 455, 'min_edge': 5, 'max_edge': 5, 'file_name': 'test', 'vertices': 5, 'max_weight': 1000, 'sign': 2, "direct": 2, "self_loop": 2,"multigraph":2}
True
>>> result = input_filter({"file_name": "test2","vertices": 23,"max_weight": 2,"min_weight": 80,"min_edge": 23,"max_edge": 1,"sign": 1,"output_format": 1,"direct": 2,"self_loop": 10,"multigraph":10})
>>> result == {'min_weight': 2, 'vertices': 23, 'file_name': 'test2', 'max_edge': 23, 'min_edge': 1, 'max_weight': 80, 'output_format': 1, 'sign': 1,"direct": 2,"self_loop": 1,"multigraph":1}
True
>>> logger(100,50,'test','2min')
>>> convert_bytes(200)
'200.0 bytes'
>>> convert_bytes(6000)
'5.9 KB'
>>> convert_bytes(80000)
'78.1 KB'
>>> zero_insert('22')
'22'
>>> zero_insert('320')
'320'
>>> zero_insert('2')
'02'
>>> zero_insert(22)
Traceback (most recent call last):
        ...
TypeError: object of type 'int' has no len()
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
>>> all_vertices = list(range(1, 41))
>>> random.seed(2)
>>> branch_gen(1,10,1,20,1,1,1,1,all_vertices,used_vertices)
[[4, 25, 18, 3, 30, 34, 2, 26, 14, 11], [3, 10, 20, 14, -18, -2, -15, -14, 8, 6]]
>>> random.seed(20)
>>> branch_gen(1,4,1,20,2,1,1,1,all_vertices,used_vertices)
[[10, 7, 39, 2], [9, 11, 6, 14]]
>>> branch_gen(40,1,20,1)
Traceback (most recent call last):
        ...
TypeError: branch_gen() missing 6 required positional arguments: 'sign', 'direct', 'self_loop', 'multigraph', 'all_vertices', and 'used_vertices'
>>> random.seed(2)
>>> edge_gen(20,0,400,2,10,1,1,1,1)
[{1: [3, 7], 2: [20, 6, 14, 17, 1], 3: [13, 6, 9, 14, 16, 18, 11], 4: [12, 14, 19, 9, 15, 6, 16], 5: [20, 16, 18, 7], 6: [20, 1, 5, 3, 11, 13, 7], 7: [2, 13, 1, 5, 3, 7, 8, 17], 8: [2, 5, 18, 17], 9: [20, 8, 12, 17, 15, 6, 5, 10], 10: [5, 2, 8, 11, 12, 7, 6, 18, 16, 1], 11: [4, 5, 8, 10], 12: [15, 13, 7, 20, 2, 12, 16, 1, 9], 13: [10, 15, 11, 1, 18, 5, 7], 14: [3, 17, 13, 18, 14, 6], 15: [20, 13, 4], 16: [2, 13, 14, 20, 17, 6, 4, 8, 18], 17: [3, 19, 4], 18: [5, 9], 19: [17, 5, 12, 20], 20: [15, 12, 17, 14]}, {1: [184, -128], 2: [297, -326, -278, -18, -238], 3: [-269, 120, 90, 69, 228, -376, -303], 4: [-82, -335, 250, -256, -236, -249, 166], 5: [-395, -155, -159, -262], 6: [174, 381, 294, -302, 386, 136, 30], 7: [185, 127, 58, 20, -130, 376, 197, 126], 8: [176, -172, 157, 135], 9: [242, 338, 12, 265, -263, 174, -310, 358], 10: [129, 82, 232, 126, -37, 302, -131, -142, 77, -209], 11: [123, 10, 53, 266], 12: [-274, 350, -217, 297, -268, 48, -187, 312, -353], 13: [350, 53, 396, -30, -237, 2, 190], 14: [386, 59, -366, 385, -62, 62], 15: [-328, 354, 316], 16: [-148, -72, -247, -368, -348, -118, -305, -356, 299], 17: [-90, 213, 348], 18: [-199, -224], 19: [-57, -49, 366, -86], 20: [206, 238, 304, 201]}, 113]
>>> random.seed(11)
>>> edge_gen(20,0,100,2,10,2,1,1,1)
[{1: [18, 15, 19, 7, 20, 11, 2, 6, 3], 2: [20, 15], 3: [20, 17, 2, 8], 4: [15, 16], 5: [17, 10, 1, 4, 12], 6: [3, 10, 9, 13, 4, 18, 11, 7, 2, 20], 7: [7, 17, 14, 3, 9], 8: [11, 10, 1, 5, 12, 3], 9: [15, 6], 10: [7, 18, 5, 15, 16, 4, 8, 9, 6, 13], 11: [2, 8, 11], 12: [10, 3, 4, 11, 16, 14, 5], 13: [19, 13, 5, 9, 10, 4, 17, 14, 18], 14: [20, 14, 4, 2, 11, 16, 9, 10, 13], 15: [6, 3, 10, 4, 11, 17, 2, 13, 8, 1], 16: [12, 20, 3, 6, 14, 16], 17: [19, 20, 1, 13, 11, 2, 15, 10, 18, 8], 18: [3, 19, 2], 19: [11, 3, 18, 16], 20: [19, 13, 1, 4, 5, 3, 11, 10, 20]}, {1: [99, 57, 75, 23, 80, 23, 57, 18, 68], 2: [50, 83], 3: [1, 8, 4, 30], 4: [41, 75], 5: [29, 63, 84, 58, 52], 6: [90, 40, 65, 3, 72, 13, 13, 49, 2, 0], 7: [6, 48, 53, 72, 99], 8: [11, 42, 52, 17, 90, 1], 9: [62, 87], 10: [57, 24, 53, 14, 53, 0, 75, 2, 23, 77], 11: [18, 56, 1], 12: [49, 9, 26, 1, 47, 58, 75], 13: [17, 23, 39, 78, 92, 20, 80, 25, 49], 14: [10, 6, 13, 65, 30, 90, 32, 76, 37], 15: [92, 16, 61, 35, 26, 2, 34, 57, 7, 22], 16: [67, 16, 46, 57, 84, 88], 17: [17, 4, 60, 89, 4, 76, 9, 8, 39, 17], 18: [57, 47, 94], 19: [45, 87, 9, 3], 20: [1, 48, 77, 10, 81, 32, 93, 49, 88]}, 125]
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
a 5 4 148
a 5 3 -163
a 6 9 -139
a 7 9 -9
a 9 8 -97
a 10 9 143
<BLANKLINE>
>>> random.seed(4)
>>> dimacs_maker('testfile2',0,50,30,0,4,0,1,1,1)
41
>>> file=open('testfile2.gr','r')
>>> print(file.read())
c FILE                  :testfile2.gr
c No. of vertices       :30
c No. of edges          :41
c Max. weight           :50
c Min. weight           :0
c Min. edge             :0
c Max. edge             :4
p sp 30 41
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
a 10 15 -27
a 11 6 19
a 11 10 5
a 11 2 -40
a 12 17 -44
a 12 11 43
a 13 3 -12
a 14 9 22
a 14 15 -40
a 14 20 20
a 17 9 7
a 18 30 18
a 18 15 2
a 19 23 18
a 19 25 -1
a 20 10 -9
a 20 26 -39
a 22 20 28
a 22 10 16
a 23 20 21
a 23 19 23
a 23 2 -10
a 24 26 -18
a 24 19 28
a 25 14 7
a 29 20 38
<BLANKLINE>
>>> random.seed(20)
>>> dimacs_maker('testfile3',10,30,100,0,4,2,1,1,1)
197
>>> file=open('testfile3.gr','r')
>>> print(file.read())
c FILE                  :testfile3.gr
c No. of vertices       :100
c No. of edges          :197
c Max. weight           :30
c Min. weight           :10
c Min. edge             :0
c Max. edge             :4
p sp 100 197
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
a 18 80 11
a 18 69 16
a 19 23 15
a 19 11 13
a 19 40 10
a 20 87 22
a 20 59 26
a 22 16 24
a 23 43 10
a 23 10 28
a 23 98 13
a 23 13 20
a 24 83 12
a 24 86 19
a 27 29 26
a 28 90 10
a 28 21 10
a 28 87 26
a 28 18 19
a 29 54 18
a 31 13 16
a 31 32 16
a 31 30 13
a 32 17 27
a 32 51 14
a 34 63 10
a 34 23 16
a 34 84 19
a 35 13 19
a 35 28 21
a 35 82 19
a 36 87 13
a 38 8 22
a 38 49 19
a 39 60 13
a 39 9 28
a 39 63 16
a 41 9 27
a 41 81 20
a 41 94 10
a 41 24 18
a 42 78 13
a 42 1 11
a 43 96 16
a 44 52 29
a 44 11 28
a 44 48 19
a 44 60 11
a 45 80 22
a 46 51 22
a 46 33 10
a 46 61 12
a 46 78 25
a 47 30 16
a 47 39 24
a 48 49 16
a 48 81 11
a 49 18 12
a 49 97 21
a 52 31 27
a 52 19 19
a 52 96 10
a 53 88 21
a 54 68 14
a 54 3 17
a 55 68 24
a 55 32 22
a 55 51 27
a 56 65 29
a 56 85 19
a 57 98 12
a 57 84 25
a 57 35 21
a 57 97 14
a 58 85 17
a 58 63 14
a 58 46 20
a 59 19 30
a 59 97 27
a 59 99 13
a 59 98 18
a 61 25 21
a 61 52 16
a 61 72 26
a 61 94 19
a 62 81 15
a 62 18 14
a 62 37 10
a 63 86 12
a 63 22 20
a 63 37 17
a 63 88 20
a 65 34 18
a 67 39 12
a 68 6 26
a 68 7 25
a 68 63 22
a 69 95 13
a 69 84 14
a 69 92 19
a 69 65 27
a 70 22 24
a 70 58 26
a 70 64 14
a 71 25 16
a 72 16 16
a 72 59 22
a 73 9 19
a 73 83 27
a 73 16 16
a 74 94 19
a 75 65 19
a 76 61 13
a 76 47 26
a 76 32 15
a 77 74 21
a 77 38 14
a 77 2 20
a 77 51 14
a 78 66 14
a 78 67 12
a 79 77 26
a 80 5 13
a 80 37 23
a 80 75 12
a 80 71 16
a 81 88 24
a 81 57 23
a 81 94 11
a 81 95 15
a 82 13 25
a 83 73 30
a 83 39 15
a 83 32 18
a 83 30 13
a 85 89 27
a 85 76 24
a 85 56 20
a 85 31 27
a 86 66 11
a 87 12 26
a 87 4 19
a 87 5 18
a 88 34 19
a 88 70 22
a 90 2 11
a 90 75 15
a 91 30 30
a 93 54 11
a 93 1 29
a 93 99 16
a 94 70 27
a 94 60 12
a 94 37 24
a 95 38 20
a 95 14 24
a 95 26 14
a 95 83 30
a 98 24 16
a 98 25 17
a 99 1 13
a 99 8 17
a 100 65 30
a 100 79 22
a 100 88 18
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
41
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
197
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
[Error] Bad Input File
>>> json_to_pickle('testfile24')
[Error] Bad Input File
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
7
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
5     4     148
5     3     -163
6     9     -139
7     9     -9
9     8     -97
10    9     143
<BLANKLINE>
>>> random.seed(2)
>>> gl_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
7
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
9 8:-97
10 9:143
<BLANKLINE>
>>> file=open('testfile.csv','r')
>>> print(file.read())
4,3,-64
5,4,148
5,3,-163
6,9,-139
7,9,-9
9,8,-97
10,9,143
<BLANKLINE>
>>> random.seed(4)
>>> csv_maker('testfile2',0,50,30,0,4,0,1,1,1)
41
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
10,15,-27
11,6,19
11,10,5
11,2,-40
12,17,-44
12,11,43
13,3,-12
14,9,22
14,15,-40
14,20,20
17,9,7
18,30,18
18,15,2
19,23,18
19,25,-1
20,10,-9
20,26,-39
22,20,28
22,10,16
23,20,21
23,19,23
23,2,-10
24,26,-18
24,19,28
25,14,7
29,20,38
<BLANKLINE>
>>> random.seed(20)
>>> csv_maker('testfile3',10,30,100,0,4,2,1,1,1)
197
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
18,80,11
18,69,16
19,23,15
19,11,13
19,40,10
20,87,22
20,59,26
22,16,24
23,43,10
23,10,28
23,98,13
23,13,20
24,83,12
24,86,19
27,29,26
28,90,10
28,21,10
28,87,26
28,18,19
29,54,18
31,13,16
31,32,16
31,30,13
32,17,27
32,51,14
34,63,10
34,23,16
34,84,19
35,13,19
35,28,21
35,82,19
36,87,13
38,8,22
38,49,19
39,60,13
39,9,28
39,63,16
41,9,27
41,81,20
41,94,10
41,24,18
42,78,13
42,1,11
43,96,16
44,52,29
44,11,28
44,48,19
44,60,11
45,80,22
46,51,22
46,33,10
46,61,12
46,78,25
47,30,16
47,39,24
48,49,16
48,81,11
49,18,12
49,97,21
52,31,27
52,19,19
52,96,10
53,88,21
54,68,14
54,3,17
55,68,24
55,32,22
55,51,27
56,65,29
56,85,19
57,98,12
57,84,25
57,35,21
57,97,14
58,85,17
58,63,14
58,46,20
59,19,30
59,97,27
59,99,13
59,98,18
61,25,21
61,52,16
61,72,26
61,94,19
62,81,15
62,18,14
62,37,10
63,86,12
63,22,20
63,37,17
63,88,20
65,34,18
67,39,12
68,6,26
68,7,25
68,63,22
69,95,13
69,84,14
69,92,19
69,65,27
70,22,24
70,58,26
70,64,14
71,25,16
72,16,16
72,59,22
73,9,19
73,83,27
73,16,16
74,94,19
75,65,19
76,61,13
76,47,26
76,32,15
77,74,21
77,38,14
77,2,20
77,51,14
78,66,14
78,67,12
79,77,26
80,5,13
80,37,23
80,75,12
80,71,16
81,88,24
81,57,23
81,94,11
81,95,15
82,13,25
83,73,30
83,39,15
83,32,18
83,30,13
85,89,27
85,76,24
85,56,20
85,31,27
86,66,11
87,12,26
87,4,19
87,5,18
88,34,19
88,70,22
90,2,11
90,75,15
91,30,30
93,54,11
93,1,29
93,99,16
94,70,27
94,60,12
94,37,24
95,38,20
95,14,24
95,26,14
95,83,30
98,24,16
98,25,17
99,1,13
99,8,17
100,65,30
100,79,22
100,88,18
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
5 4 148
5 3 -163
6 9 -139
7 9 -9
9 8 -97
10 9 143
<BLANKLINE>
>>> random.seed(4)
>>> wel_maker('testfile2',0,50,30,0,4,0,1,1,1)
41
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
10 15 -27
11 6 19
11 10 5
11 2 -40
12 17 -44
12 11 43
13 3 -12
14 9 22
14 15 -40
14 20 20
17 9 7
18 30 18
18 15 2
19 23 18
19 25 -1
20 10 -9
20 26 -39
22 20 28
22 10 16
23 20 21
23 19 23
23 2 -10
24 26 -18
24 19 28
25 14 7
29 20 38
<BLANKLINE>
>>> random.seed(20)
>>> wel_maker('testfile3',10,30,100,0,4,2,1,1,1)
197
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
18 80 11
18 69 16
19 23 15
19 11 13
19 40 10
20 87 22
20 59 26
22 16 24
23 43 10
23 10 28
23 98 13
23 13 20
24 83 12
24 86 19
27 29 26
28 90 10
28 21 10
28 87 26
28 18 19
29 54 18
31 13 16
31 32 16
31 30 13
32 17 27
32 51 14
34 63 10
34 23 16
34 84 19
35 13 19
35 28 21
35 82 19
36 87 13
38 8 22
38 49 19
39 60 13
39 9 28
39 63 16
41 9 27
41 81 20
41 94 10
41 24 18
42 78 13
42 1 11
43 96 16
44 52 29
44 11 28
44 48 19
44 60 11
45 80 22
46 51 22
46 33 10
46 61 12
46 78 25
47 30 16
47 39 24
48 49 16
48 81 11
49 18 12
49 97 21
52 31 27
52 19 19
52 96 10
53 88 21
54 68 14
54 3 17
55 68 24
55 32 22
55 51 27
56 65 29
56 85 19
57 98 12
57 84 25
57 35 21
57 97 14
58 85 17
58 63 14
58 46 20
59 19 30
59 97 27
59 99 13
59 98 18
61 25 21
61 52 16
61 72 26
61 94 19
62 81 15
62 18 14
62 37 10
63 86 12
63 22 20
63 37 17
63 88 20
65 34 18
67 39 12
68 6 26
68 7 25
68 63 22
69 95 13
69 84 14
69 92 19
69 65 27
70 22 24
70 58 26
70 64 14
71 25 16
72 16 16
72 59 22
73 9 19
73 83 27
73 16 16
74 94 19
75 65 19
76 61 13
76 47 26
76 32 15
77 74 21
77 38 14
77 2 20
77 51 14
78 66 14
78 67 12
79 77 26
80 5 13
80 37 23
80 75 12
80 71 16
81 88 24
81 57 23
81 94 11
81 95 15
82 13 25
83 73 30
83 39 15
83 32 18
83 30 13
85 89 27
85 76 24
85 56 20
85 31 27
86 66 11
87 12 26
87 4 19
87 5 18
88 34 19
88 70 22
90 2 11
90 75 15
91 30 30
93 54 11
93 1 29
93 99 16
94 70 27
94 60 12
94 37 24
95 38 20
95 14 24
95 26 14
95 83 30
98 24 16
98 25 17
99 1 13
99 8 17
100 65 30
100 79 22
100 88 18
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
edge(5,4,148).
edge(5,3,-163).
edge(6,9,-139).
edge(7,9,-9).
edge(9,8,-97).
edge(10,9,143).
<BLANKLINE>
>>> random.seed(4)
>>> lp_maker('testfile2',0,50,30,0,4,0,1,1,1)
41
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
edge(10,15,-27).
edge(11,6,19).
edge(11,10,5).
edge(11,2,-40).
edge(12,17,-44).
edge(12,11,43).
edge(13,3,-12).
edge(14,9,22).
edge(14,15,-40).
edge(14,20,20).
edge(17,9,7).
edge(18,30,18).
edge(18,15,2).
edge(19,23,18).
edge(19,25,-1).
edge(20,10,-9).
edge(20,26,-39).
edge(22,20,28).
edge(22,10,16).
edge(23,20,21).
edge(23,19,23).
edge(23,2,-10).
edge(24,26,-18).
edge(24,19,28).
edge(25,14,7).
edge(29,20,38).
<BLANKLINE>
>>> input_dic=get_input(input_func=print_test)
>>> input_dic['sign']
2
>>> input_dic['vertices']
20
>>> input_dic['min_edge']
19
>>> input_dic['min_weight']
1
>>> input_dic['output_format']
1
>>> input_dic['max_weight']
1
>>> input_dic['file_name']
'14'
>>> input_dic['max_edge']
19
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
5 4 148
5 3 -163
6 9 -139
7 9 -9
9 8 -97
10 9 143
<BLANKLINE>
>>> random.seed(4)
>>> tgf_maker('testfile2',0,50,30,0,4,0,1,1,1)
41
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
10 15 -27
11 6 19
11 10 5
11 2 -40
12 17 -44
12 11 43
13 3 -12
14 9 22
14 15 -40
14 20 20
17 9 7
18 30 18
18 15 2
19 23 18
19 25 -1
20 10 -9
20 26 -39
22 20 28
22 10 16
23 20 21
23 19 23
23 2 -10
24 26 -18
24 19 28
25 14 7
29 20 38
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
5 4 148
5 3 -163
6 9 -139
7 9 -9
9 8 -97
10 9 143
<BLANKLINE>
>>> random.seed(4)
>>> dl_maker('testfile2',0,50,30,0,4,0,1,1,1)
41
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
10 15 -27
11 6 19
11 10 5
11 2 -40
12 17 -44
12 11 43
13 3 -12
14 9 22
14 15 -40
14 20 20
17 9 7
18 30 18
18 15 2
19 23 18
19 25 -1
20 10 -9
20 26 -39
22 20 28
22 10 16
23 20 21
23 19 23
23 2 -10
24 26 -18
24 19 28
25 14 7
29 20 38
<BLANKLINE>
>>> file.close()
>>> os.remove('testfile.csv')
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
>>> os.remove('testfile3.gr')
>>> os.remove('testfile3.json')
>>> os.remove('testfile3.p')
>>> os.remove('testfile3.wel')
>>> os.remove('testfile3.yaml')
>>> os.remove('logfile.log')

"""
