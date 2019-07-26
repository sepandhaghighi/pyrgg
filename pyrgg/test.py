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
>>> result = input_filter({"file_name": "test","vertices": 5,"max_weight": 1000,"min_weight":455,"min_edge": -45,"max_edge": -11,"sign": 5,"output_format": 19,"direct": 2})
>>> result == {'output_format': 1, 'min_weight': 455, 'min_edge': 5, 'max_edge': 5, 'file_name': 'test', 'vertices': 5, 'max_weight': 1000, 'sign': 2, "direct": 2}
True
>>> result = input_filter({"file_name": "test2","vertices": 23,"max_weight": 2,"min_weight": 80,"min_edge": 23,"max_edge": 1,"sign": 1,"output_format": 1,"direct": 2})
>>> result == {'min_weight': 2, 'vertices': 23, 'file_name': 'test2', 'max_edge': 23, 'min_edge': 1, 'max_weight': 80, 'output_format': 1, 'sign': 1,"direct": 2}
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
>>> branch_gen(1,10,1,20,1,1,all_vertices,used_vertices)
[[4, 24, 17, 3, 26, 29, 2, 21, 34, 12], [3, 10, 20, 14, -18, -2, -15, -14, 18, 8]]
>>> random.seed(20)
>>> branch_gen(1,4,1,20,2,1,all_vertices,used_vertices)
[[10, 7, 37, 2], [9, 11, 6, 14]]
>>> branch_gen(40,1,20,1)
Traceback (most recent call last):
        ...
TypeError: branch_gen() missing 4 required positional arguments: 'sign', 'direct', 'all_vertices', and 'used_vertices'
>>> random.seed(2)
>>> edge_gen(20,0,400,2,10,1,1)
[{1: [3, 6], 2: [20, 6, 13, 15, 1], 3: [13, 6, 8, 11, 17, 18, 14], 4: [12, 13, 17, 9, 15, 19, 8], 5: [20, 16, 17, 7], 6: [20, 1, 4, 2, 8, 17, 14], 7: [12, 1, 3, 5, 6, 19, 11], 8: [15, 13, 8, 11, 19, 17], 9: [9, 14, 18, 2, 5, 4, 8], 10: [15, 3, 20, 14, 1], 11: [14, 17, 4, 6, 7, 15, 18, 19], 12: [19, 16, 17, 12, 14, 10, 1, 7, 15, 9], 13: [20, 13, 4], 14: [2, 12, 17, 14, 10, 6, 9, 3, 5], 15: [2, 13, 11], 16: [10, 18, 11, 17, 6, 8, 19, 15, 13, 9], 17: [16, 11, 8, 13, 15, 6, 19, 4], 18: [9, 20, 7, 1, 3], 19: [15, 20, 13, 5, 16, 10, 12], 20: [19, 10, 5, 18, 9, 11, 13, 7]}, {1: [184, -128], 2: [297, -326, -278, -18, -238], 3: [-269, 120, 90, 69, -263, 228, -303], 4: [-82, -335, 250, -256, -179, -249, -358], 5: [-395, -155, -159, -262], 6: [174, 381, 294, -302, 386, 136, 29], 7: [127, 58, 20, 376, 197, 126, -15], 8: [135, 242, 338, 12, -249, -73], 9: [-310, 358, 343, -17, 87, -325, 126], 10: [128, 319, -131, -269, 18], 11: [56, 123, 10, 53, 266, -158, -108, 214], 12: [48, -9, 312, -353, 53, 396, -30, 2, 385, 62], 13: [-328, 354, 316], 14: [-148, -72, -368, -348, -118, -305, -356, 36, -34], 15: [151, 362, -88], 16: [79, -49, 366, -86, -360, -183, 238, 304, 201, -129], 17: [-280, 389, 206, 160, -332, 8, -110, -285], 18: [250, 4, 179, -272, -345], 19: [-257, -88, -345, 83, -237, 5, 275], 20: [-104, -332, -353, -39, -155, -334, 260, -305]}, 128]
>>> random.seed(11)
>>> edge_gen(20,0,100,2,10,2,1)
[{1: [18, 15, 17, 7, 20, 4, 10, 3, 2], 2: [15, 20, 6, 1, 3, 2, 8, 7], 3: [10, 1, 3, 9, 18], 4: [11, 8, 10, 3, 4, 13], 5: [1, 7], 6: [13, 3, 7, 9, 11, 14, 4, 8, 2], 7: [6, 18, 15, 7, 5, 13, 9, 10, 19], 8: [5, 15], 9: [20, 10], 10: [3, 7, 8], 11: [12, 15, 19, 13, 5, 8, 7], 12: [7, 13, 20, 14, 4, 2, 9, 16, 17, 3], 13: [16, 20, 3, 7, 1], 14: [14, 8, 2, 10, 17, 5], 15: [5, 11, 17, 2, 16, 10, 1], 16: [16, 10, 5], 17: [15, 12, 2], 18: [11, 3, 16, 14], 19: [19, 20, 13, 3, 4, 14, 11, 15, 18], 20: [17, 10, 3, 1, 4, 20, 16, 11, 15, 8]}, {1: [99, 57, 75, 23, 23, 57, 18, 68, 76], 2: [83, 83, 79, 67, 7, 24, 76, 66], 3: [63, 84, 58, 52, 10], 4: [97, 65, 3, 72, 51, 8], 5: [27, 6], 6: [90, 72, 99, 43, 1, 97, 17, 90, 59], 7: [87, 24, 65, 93, 53, 14, 75, 2, 12], 8: [27, 33], 9: [42, 49], 10: [11, 74, 1], 11: [79, 16, 61, 23, 39, 78, 20], 12: [87, 61, 10, 6, 13, 65, 30, 37, 22, 16], 13: [71, 78, 35, 26, 8], 14: [57, 7, 22, 47, 73, 11], 15: [57, 84, 74, 2, 45, 4, 76], 16: [8, 40, 9], 17: [69, 94, 94], 18: [45, 87, 9, 3], 19: [1, 84, 48, 11, 32, 93, 49, 59, 10], 20: [3, 76, 61, 29, 63, 84, 32, 84, 63, 41]}, 119]
>>> edge_gen(0,400,2,10,1)
Traceback (most recent call last):
        ...
TypeError: edge_gen() missing 2 required positional arguments: 'sign' and 'direct'
>>> random.seed(2)
>>> dimacs_maker('testfile', 0, 200, 10, 0, 2, 0, 1)
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
>>> dimacs_maker('testfile2',0,50,30,0,4,0,1)
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
a 2 18 -48
a 4 17 -17
a 5 27 16
a 6 30 41
a 7 26 -12
a 7 6 -18
a 8 3 -42
a 8 13 11
a 9 16 -5
a 10 27 0
a 10 30 -36
a 10 23 -48
a 10 17 26
a 11 20 -27
a 11 15 14
a 11 10 -2
a 14 21 -33
a 14 18 -44
a 14 11 43
a 15 3 -12
a 16 9 22
a 16 14 -40
a 16 18 20
a 19 9 7
a 20 30 18
a 20 15 2
a 21 23 18
a 21 24 -1
a 22 10 -9
a 22 25 -39
a 24 20 28
a 24 10 16
a 25 20 21
a 25 19 23
a 25 2 -10
a 26 26 -18
a 26 19 28
a 27 14 7
<BLANKLINE>
>>> random.seed(20)
>>> dimacs_maker('testfile3',10,30,100,0,4,2,1)
189
>>> file=open('testfile3.gr','r')
>>> print(file.read())
c FILE                  :testfile3.gr
c No. of vertices       :100
c No. of edges          :189
c Max. weight           :30
c Min. weight           :10
c Min. edge             :0
c Max. edge             :4
p sp 100 189
a 1 34 30
a 3 74 15
a 3 4 23
a 4 10 13
a 4 17 20
a 4 61 28
a 5 53 16
a 5 26 20
a 5 81 20
a 6 55 12
a 6 81 26
a 7 52 12
a 7 27 28
a 7 32 11
a 8 13 12
a 9 33 19
a 10 89 18
a 10 21 29
a 13 91 17
a 13 29 28
a 14 8 10
a 15 39 18
a 15 18 30
a 15 43 29
a 15 93 24
a 16 82 18
a 17 56 15
a 17 22 22
a 17 91 13
a 17 89 14
a 18 55 21
a 18 29 13
a 18 78 11
a 18 67 16
a 19 23 15
a 19 11 13
a 19 38 10
a 20 87 22
a 20 59 26
a 22 16 24
a 23 43 10
a 23 10 28
a 23 96 13
a 23 12 20
a 24 83 12
a 24 85 19
a 27 29 26
a 28 90 10
a 28 21 10
a 28 86 26
a 28 18 19
a 29 54 18
a 31 13 16
a 31 31 16
a 31 29 13
a 32 17 27
a 32 50 14
a 34 63 10
a 34 23 16
a 34 82 19
a 35 13 19
a 35 27 21
a 35 80 19
a 36 87 13
a 38 8 22
a 38 48 19
a 39 60 13
a 39 9 28
a 39 61 16
a 41 9 27
a 41 80 20
a 41 92 10
a 41 23 18
a 42 78 13
a 42 1 11
a 43 96 16
a 44 52 29
a 44 11 28
a 44 47 19
a 44 57 11
a 45 80 22
a 46 51 22
a 46 33 10
a 46 100 24
a 46 12 28
a 47 41 17
a 47 100 16
a 47 38 24
a 48 49 16
a 48 80 11
a 49 18 12
a 49 96 21
a 52 31 27
a 52 19 19
a 52 100 10
a 53 88 21
a 54 68 14
a 54 3 17
a 55 68 24
a 55 32 22
a 55 50 27
a 56 65 29
a 56 84 19
a 57 98 12
a 57 84 25
a 57 35 21
a 57 95 14
a 58 85 17
a 58 63 14
a 58 46 20
a 59 19 30
a 59 96 27
a 59 97 13
a 59 83 11
a 60 25 21
a 60 51 16
a 60 70 26
a 60 91 19
a 61 81 15
a 61 18 14
a 61 36 10
a 62 86 12
a 62 100 15
a 62 44 18
a 62 32 20
a 64 34 18
a 66 39 12
a 67 6 26
a 67 61 22
a 67 92 26
a 69 91 19
a 70 71 23
a 70 22 24
a 70 57 26
a 70 62 14
a 71 25 16
a 72 16 16
a 72 58 22
a 73 9 19
a 73 82 27
a 73 15 16
a 74 94 19
a 75 65 19
a 76 61 13
a 76 47 26
a 76 32 15
a 77 74 21
a 77 38 14
a 77 2 20
a 77 49 14
a 78 66 14
a 78 23 29
a 79 67 11
a 79 15 18
a 79 54 28
a 79 12 27
a 80 78 24
a 81 53 11
a 81 92 15
a 81 23 13
a 82 91 29
a 82 73 30
a 82 39 15
a 83 36 17
a 86 89 27
a 86 76 24
a 86 56 20
a 86 31 27
a 87 66 11
a 88 12 26
a 88 4 19
a 88 99 21
a 89 40 27
a 89 52 30
a 91 2 11
a 91 74 15
a 92 30 30
a 94 54 11
a 94 1 29
a 94 97 16
a 95 70 27
a 95 60 12
a 95 37 24
a 96 38 20
a 96 14 24
a 96 25 14
a 96 80 30
a 99 24 16
a 99 38 10
<BLANKLINE>
>>> dimacs_maker('testfile', 0, 200, 10, 0,0)
Traceback (most recent call last):
        ...
TypeError: dimacs_maker() missing 2 required positional arguments: 'sign' and 'direct'
>>> random.seed(2)
>>> json_maker('testfile', 0, 200, 10, 0, 2, 0, 1)
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
>>> json_maker('testfile2',0,50,30,0,4,0,1)
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
>>> json_maker('testfile3',10,30,100,0,4,2,1)
189
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
>>> json_maker('testfile', 0, 200, 10, 0, 0)
Traceback (most recent call last):
        ...
TypeError: json_maker() missing 2 required positional arguments: 'sign' and 'direct'
>>> json_to_pickle('testfile3')
>>> testfile_3_p=pickle.load( open( 'testfile3.p', 'rb' ) )
>>> testfile_3_p['graph']['edges'][1]['source']
'3'
>>> testfile_3_p['graph']['edges'][1]['target']
'74'
>>> testfile_3_p['graph']['edges'][1]['weight']
'15'
>>> random.seed(2)
>>> csv_maker('testfile', 0, 200, 10, 0, 2, 0, 1)
7
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
>>> csv_maker('testfile2',0,50,30,0,4,0,1)
41
>>> file=open('testfile2.csv','r')
>>> print(file.read())
1,10,46
2,16,5
2,3,25
2,18,-48
4,17,-17
5,27,16
6,30,41
7,26,-12
7,6,-18
8,3,-42
8,13,11
9,16,-5
10,27,0
10,30,-36
10,23,-48
10,17,26
11,20,-27
11,15,14
11,10,-2
14,21,-33
14,18,-44
14,11,43
15,3,-12
16,9,22
16,14,-40
16,18,20
19,9,7
20,30,18
20,15,2
21,23,18
21,24,-1
22,10,-9
22,25,-39
24,20,28
24,10,16
25,20,21
25,19,23
25,2,-10
26,26,-18
26,19,28
27,14,7
<BLANKLINE>
>>> random.seed(20)
>>> csv_maker('testfile3',10,30,100,0,4,2,1)
189
>>> file=open('testfile3.csv','r')
>>> print(file.read())
1,34,30
3,74,15
3,4,23
4,10,13
4,17,20
4,61,28
5,53,16
5,26,20
5,81,20
6,55,12
6,81,26
7,52,12
7,27,28
7,32,11
8,13,12
9,33,19
10,89,18
10,21,29
13,91,17
13,29,28
14,8,10
15,39,18
15,18,30
15,43,29
15,93,24
16,82,18
17,56,15
17,22,22
17,91,13
17,89,14
18,55,21
18,29,13
18,78,11
18,67,16
19,23,15
19,11,13
19,38,10
20,87,22
20,59,26
22,16,24
23,43,10
23,10,28
23,96,13
23,12,20
24,83,12
24,85,19
27,29,26
28,90,10
28,21,10
28,86,26
28,18,19
29,54,18
31,13,16
31,31,16
31,29,13
32,17,27
32,50,14
34,63,10
34,23,16
34,82,19
35,13,19
35,27,21
35,80,19
36,87,13
38,8,22
38,48,19
39,60,13
39,9,28
39,61,16
41,9,27
41,80,20
41,92,10
41,23,18
42,78,13
42,1,11
43,96,16
44,52,29
44,11,28
44,47,19
44,57,11
45,80,22
46,51,22
46,33,10
46,100,24
46,12,28
47,41,17
47,100,16
47,38,24
48,49,16
48,80,11
49,18,12
49,96,21
52,31,27
52,19,19
52,100,10
53,88,21
54,68,14
54,3,17
55,68,24
55,32,22
55,50,27
56,65,29
56,84,19
57,98,12
57,84,25
57,35,21
57,95,14
58,85,17
58,63,14
58,46,20
59,19,30
59,96,27
59,97,13
59,83,11
60,25,21
60,51,16
60,70,26
60,91,19
61,81,15
61,18,14
61,36,10
62,86,12
62,100,15
62,44,18
62,32,20
64,34,18
66,39,12
67,6,26
67,61,22
67,92,26
69,91,19
70,71,23
70,22,24
70,57,26
70,62,14
71,25,16
72,16,16
72,58,22
73,9,19
73,82,27
73,15,16
74,94,19
75,65,19
76,61,13
76,47,26
76,32,15
77,74,21
77,38,14
77,2,20
77,49,14
78,66,14
78,23,29
79,67,11
79,15,18
79,54,28
79,12,27
80,78,24
81,53,11
81,92,15
81,23,13
82,91,29
82,73,30
82,39,15
83,36,17
86,89,27
86,76,24
86,56,20
86,31,27
87,66,11
88,12,26
88,4,19
88,99,21
89,40,27
89,52,30
91,2,11
91,74,15
92,30,30
94,54,11
94,1,29
94,97,16
95,70,27
95,60,12
95,37,24
96,38,20
96,14,24
96,25,14
96,80,30
99,24,16
99,38,10
<BLANKLINE>
>>> csv_maker('testfile', 0, 200, 10, 0,0)
Traceback (most recent call last):
        ...
TypeError: csv_maker() missing 2 required positional arguments: 'sign' and 'direct'
>>> random.seed(2)
>>> wel_maker('testfile', 0, 200, 10, 0, 2, 0,1)
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
>>> wel_maker('testfile2',0,50,30,0,4,0,1)
41
>>> file=open('testfile2.wel','r')
>>> print(file.read())
1 10 46
2 16 5
2 3 25
2 18 -48
4 17 -17
5 27 16
6 30 41
7 26 -12
7 6 -18
8 3 -42
8 13 11
9 16 -5
10 27 0
10 30 -36
10 23 -48
10 17 26
11 20 -27
11 15 14
11 10 -2
14 21 -33
14 18 -44
14 11 43
15 3 -12
16 9 22
16 14 -40
16 18 20
19 9 7
20 30 18
20 15 2
21 23 18
21 24 -1
22 10 -9
22 25 -39
24 20 28
24 10 16
25 20 21
25 19 23
25 2 -10
26 26 -18
26 19 28
27 14 7
<BLANKLINE>
>>> random.seed(20)
>>> wel_maker('testfile3',10,30,100,0,4,2,1)
189
>>> file=open('testfile3.wel','r')
>>> print(file.read())
1 34 30
3 74 15
3 4 23
4 10 13
4 17 20
4 61 28
5 53 16
5 26 20
5 81 20
6 55 12
6 81 26
7 52 12
7 27 28
7 32 11
8 13 12
9 33 19
10 89 18
10 21 29
13 91 17
13 29 28
14 8 10
15 39 18
15 18 30
15 43 29
15 93 24
16 82 18
17 56 15
17 22 22
17 91 13
17 89 14
18 55 21
18 29 13
18 78 11
18 67 16
19 23 15
19 11 13
19 38 10
20 87 22
20 59 26
22 16 24
23 43 10
23 10 28
23 96 13
23 12 20
24 83 12
24 85 19
27 29 26
28 90 10
28 21 10
28 86 26
28 18 19
29 54 18
31 13 16
31 31 16
31 29 13
32 17 27
32 50 14
34 63 10
34 23 16
34 82 19
35 13 19
35 27 21
35 80 19
36 87 13
38 8 22
38 48 19
39 60 13
39 9 28
39 61 16
41 9 27
41 80 20
41 92 10
41 23 18
42 78 13
42 1 11
43 96 16
44 52 29
44 11 28
44 47 19
44 57 11
45 80 22
46 51 22
46 33 10
46 100 24
46 12 28
47 41 17
47 100 16
47 38 24
48 49 16
48 80 11
49 18 12
49 96 21
52 31 27
52 19 19
52 100 10
53 88 21
54 68 14
54 3 17
55 68 24
55 32 22
55 50 27
56 65 29
56 84 19
57 98 12
57 84 25
57 35 21
57 95 14
58 85 17
58 63 14
58 46 20
59 19 30
59 96 27
59 97 13
59 83 11
60 25 21
60 51 16
60 70 26
60 91 19
61 81 15
61 18 14
61 36 10
62 86 12
62 100 15
62 44 18
62 32 20
64 34 18
66 39 12
67 6 26
67 61 22
67 92 26
69 91 19
70 71 23
70 22 24
70 57 26
70 62 14
71 25 16
72 16 16
72 58 22
73 9 19
73 82 27
73 15 16
74 94 19
75 65 19
76 61 13
76 47 26
76 32 15
77 74 21
77 38 14
77 2 20
77 49 14
78 66 14
78 23 29
79 67 11
79 15 18
79 54 28
79 12 27
80 78 24
81 53 11
81 92 15
81 23 13
82 91 29
82 73 30
82 39 15
83 36 17
86 89 27
86 76 24
86 56 20
86 31 27
87 66 11
88 12 26
88 4 19
88 99 21
89 40 27
89 52 30
91 2 11
91 74 15
92 30 30
94 54 11
94 1 29
94 97 16
95 70 27
95 60 12
95 37 24
96 38 20
96 14 24
96 25 14
96 80 30
99 24 16
99 38 10
<BLANKLINE>
>>> wel_maker('testfile', 0, 200, 10, 0,0)
Traceback (most recent call last):
        ...
TypeError: wel_maker() missing 2 required positional arguments: 'sign' and 'direct'
>>> random.seed(2)
>>> lp_maker('testfile', 0, 200, 10, 0, 2, 0,1)
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
>>> lp_maker('testfile2',0,50,30,0,4,0,1)
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
edge(2,18,-48).
edge(4,17,-17).
edge(5,27,16).
edge(6,30,41).
edge(7,26,-12).
edge(7,6,-18).
edge(8,3,-42).
edge(8,13,11).
edge(9,16,-5).
edge(10,27,0).
edge(10,30,-36).
edge(10,23,-48).
edge(10,17,26).
edge(11,20,-27).
edge(11,15,14).
edge(11,10,-2).
edge(14,21,-33).
edge(14,18,-44).
edge(14,11,43).
edge(15,3,-12).
edge(16,9,22).
edge(16,14,-40).
edge(16,18,20).
edge(19,9,7).
edge(20,30,18).
edge(20,15,2).
edge(21,23,18).
edge(21,24,-1).
edge(22,10,-9).
edge(22,25,-39).
edge(24,20,28).
edge(24,10,16).
edge(25,20,21).
edge(25,19,23).
edge(25,2,-10).
edge(26,26,-18).
edge(26,19,28).
edge(27,14,7).
<BLANKLINE>
>>> input_dic=get_input(input_func=print_test)
>>> input_dic['sign']
2
>>> input_dic['vertices']
18
>>> input_dic['min_edge']
17
>>> input_dic['min_weight']
1
>>> input_dic['output_format']
1
>>> input_dic['max_weight']
1
>>> input_dic['file_name']
'12'
>>> input_dic['max_edge']
17
>>> random.seed(2)
>>> tgf_maker('testfile', 0, 200, 10, 0, 2, 0, 1)
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
>>> tgf_maker('testfile2',0,50,30,0,4,0,1)
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
2 18 -48
4 17 -17
5 27 16
6 30 41
7 26 -12
7 6 -18
8 3 -42
8 13 11
9 16 -5
10 27 0
10 30 -36
10 23 -48
10 17 26
11 20 -27
11 15 14
11 10 -2
14 21 -33
14 18 -44
14 11 43
15 3 -12
16 9 22
16 14 -40
16 18 20
19 9 7
20 30 18
20 15 2
21 23 18
21 24 -1
22 10 -9
22 25 -39
24 20 28
24 10 16
25 20 21
25 19 23
25 2 -10
26 26 -18
26 19 28
27 14 7
<BLANKLINE>
>>> random.seed(2)
>>> dl_maker('testfile', 0, 200, 10, 0, 2, 0,1)
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
>>> dl_maker('testfile2',0,50,30,0,4,0,1)
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
2 18 -48
4 17 -17
5 27 16
6 30 41
7 26 -12
7 6 -18
8 3 -42
8 13 11
9 16 -5
10 27 0
10 30 -36
10 23 -48
10 17 26
11 20 -27
11 15 14
11 10 -2
14 21 -33
14 18 -44
14 11 43
15 3 -12
16 9 22
16 14 -40
16 18 20
19 9 7
20 30 18
20 15 2
21 23 18
21 24 -1
22 10 -9
22 25 -39
24 20 28
24 10 16
25 20 21
25 19 23
25 2 -10
26 26 -18
26 19 28
27 14 7
<BLANKLINE>
>>> file.close()
>>> os.remove('testfile.csv')
>>> os.remove('testfile.dl')
>>> os.remove('testfile.gr')
>>> os.remove('testfile.json')
>>> os.remove('testfile.lp')
>>> os.remove('testfile.p')
>>> os.remove('testfile.tgf')
>>> os.remove('testfile.wel')
>>> os.remove('testfile.yaml')
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
