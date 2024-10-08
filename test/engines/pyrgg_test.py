# -*- coding: utf-8 -*-
"""
>>> from pyrgg.functions import *
>>> from pyrgg.graph_gen import *
>>> import pyrgg.params
>>> import random
>>> import os
>>> import json
>>> import pyrgg.engines.pyrgg as engine
>>> os.environ["PYRGG_TEST_MODE"] = "1"
>>> ######################################
>>> ## ========= logger function =========
>>> ######################################
>>> with open('logfile.log','a') as file:
...     engine.logger(file,'test','2min',{'vertices':100,'edge_number':50,'max_edge':1000,'min_edge':10,'direct':1,'sign':0,'multigraph':0,'self_loop':1,'max_weight':20,'min_weight':1,'engine':1,'output_format':1})
>>> file = open('logfile.log','r')
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
Engine : 1 (pyrgg)
Elapsed Time : 2min
>>> class StrError:
...     def __init__(self):
...         pass
...     def __str__(self):
...         raise ValueError
>>> str_error_object = StrError()
>>> with open('logfile.log','a') as file:
...     engine.logger(file,'test','2min',{'vertices':str_error_object,'edge_number':50,'max_edge':1000,'min_edge':10,'direct':1,'sign':0,'multigraph':0,'self_loop':1,'max_weight':20,'min_weight':1,'engine':1,'output_format':1})
[Error] Logger failed!
>>> ##########################################
>>> ## ========= branch_gen function =========
>>> ##########################################
>>> used_vertices = {k:[] for k in range(1,6)}
>>> degree_dict = {1:2,2:3,3:3,4:3,5:3}
>>> degree_dict_sort = {0:{},1:{},2:{1:1},3:{2:2,3:3,4:4,5:5},4:{},5:{}}
>>> all_vertices = list(range(1, 6))
>>> engine.branch_gen(1,3,3,300,3000,0,True,False,False,False,used_vertices,degree_dict,degree_dict_sort)
[[], []]
>>> used_vertices = {k:[] for k in range(1,41)}
>>> degree_dict = {k:0 for k in range(1,41)}
>>> degree_dict_sort = {k:{} for k in range(41)}
>>> degree_dict_sort[0] = {i:i for i in range(1,41)}
>>> all_vertices = list(range(1, 41))
>>> random.seed(2)
>>> engine.branch_gen(1,10,10,1,20,0,True,True,True,False,used_vertices,degree_dict,degree_dict_sort)
[[4, 25, 18, 3, 30, 34, 2, 26, 14, 11], [3, 10, 20, 14, -18, -2, -15, -14, 8, 6]]
>>> random.seed(20)
>>> engine.branch_gen(1,10,4,1,20,0,False,True,True,False,used_vertices,degree_dict,degree_dict_sort)
[[], []]
>>> used_vertices = {k:[] for k in range(1,41)}
>>> degree_dict = {k:0 for k in range(1,41)}
>>> degree_dict_sort = {k:{} for k in range(41)}
>>> degree_dict_sort[0] = {i:i for i in range(1,41)}
>>> engine.branch_gen(1,10,4,1,20,0,False,True,True,False,used_vertices,degree_dict,degree_dict_sort)
[[10, 7, 39, 2, 30, 9, 25, 35, 18], [9, 11, 6, 14, 3, 5, 16, 14, 7]]
>>> engine.branch_gen(40,1,20,1)
Traceback (most recent call last):
        ...
TypeError: branch_gen() missing 9 required positional arguments: 'max_weight', 'precision', 'sign', 'direct', 'self_loop', 'multigraph', 'used_vertices', 'degree_dict', and 'degree_sort_dict'
>>> ##########################################
>>> ## ========= edge_gen function =========
>>> ##########################################
>>> random.seed(2)
>>> engine.edge_gen(20,0,400,2,10,True,True,True,False)
[{1: [3, 7], 2: [4, 17, 20, 9, 11], 3: [14, 8, 5, 12, 16, 19, 15], 4: [15, 17, 12, 8, 14, 13], 5: [16, 9, 7, 20, 19, 18, 13, 5], 6: [6, 10], 7: [18, 10, 11], 8: [], 9: [], 10: [12, 18, 8, 1, 14], 11: [9, 11], 12: [], 13: [], 14: [19, 16, 17, 20, 15], 15: [6, 1, 19], 16: [12, 13, 8, 9, 17], 17: [], 18: [9, 12, 17, 6, 20, 19, 1], 19: [13], 20: []}, {1: [184, -128], 2: [220, -278, -257, 14, -163], 3: [286, 118, 166, 261, -263, 228, -303], 4: [-82, -335, 250, -256, -338, -179], 5: [-337, -358, -395, -155, -159, 250, -350, -371], 6: [30, -302], 7: [386, -125, 216], 8: [], 9: [], 10: [127, 42, 12, 191, 80], 11: [-301, 77], 12: [], 13: [], 14: [146, -15, -282, 135, 242], 15: [-52, -65, -249], 16: [-132, -334, 343, -17, 87], 17: [], 18: [126, -37, 302, -131, -142, 77, -209], 19: [123], 20: []}, 61]
>>> random.seed(11)
>>> engine.edge_gen(20,0,100,2,10,False,True,True,False)
[{1: [18, 15, 19, 7, 20, 11, 2, 6, 3], 2: [17], 3: [8, 4, 5, 9, 12, 10, 14, 16], 4: [20, 13, 4, 6], 5: [12, 7, 11, 10, 14], 6: [9], 7: [19], 8: [8, 18, 11, 2, 16, 17, 10], 9: [15, 12, 18], 10: [20, 14, 13, 15, 17, 16], 11: [19, 7, 20], 12: [13], 13: [2, 16, 13], 14: [18, 19, 6, 14, 17, 15], 15: [6, 7, 16], 16: [17, 20, 12, 18], 17: [19], 18: [7, 6, 9, 12, 20], 19: [19, 11, 4], 20: []}, {1: [99, 57, 75, 23, 80, 23, 57, 18, 68], 2: [50], 3: [79, 67, 7, 24, 76, 99, 41, 75], 4: [29, 63, 84, 58], 5: [70, 90, 40, 65, 3], 6: [51], 7: [37], 8: [2, 0, 26, 60, 90, 53, 72], 9: [43, 39, 1], 10: [15, 31, 1, 59, 22, 57], 11: [98, 53, 49], 12: [53], 13: [34, 2, 23], 14: [82, 12, 18, 56, 1, 37], 15: [9, 26, 1], 16: [47, 58, 75, 73], 17: [23], 18: [39, 78, 92, 20, 49], 19: [10, 6, 13], 20: []}, 74]
>>> engine.edge_gen(0,400,2,10,1)
Traceback (most recent call last):
        ...
TypeError: edge_gen() missing 4 required positional arguments: 'sign', 'direct', 'self_loop', and 'multigraph'
>>> #########################################
>>> ## ========= gen_using function =========
>>> #########################################
>>> #################### dimacs_maker ####################
>>> random.seed(2)
>>> engine.gen_using(dimacs_maker, 'testfile', {'min_weight':0, 'max_weight':200, 'vertices':10, 'min_edge':0, 'max_edge':2, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
7
>>> file=open('testfile.gr','r')
>>> print(file.read())
c FILE                  :testfile.gr
c No. of vertices       :10
c No. of edges          :7
c Max. weight           :148
c Min. weight           :7
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
>>> engine.gen_using(dimacs_maker, 'testfile2', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
35
>>> file=open('testfile2.gr','r')
>>> print(file.read())
c FILE                  :testfile2.gr
c No. of vertices       :30
c No. of edges          :35
c Max. weight           :50
c Min. weight           :2
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
>>> engine.gen_using(dimacs_maker, 'testfile3', {'min_weight':10, 'max_weight':30, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':0, 'direct':1, 'self_loop':1, 'multigraph':0})
137
>>> file=open('testfile3.gr','r')
>>> print(file.read())
c FILE                  :testfile3.gr
c No. of vertices       :100
c No. of edges          :137
c Max. weight           :30
c Min. weight           :10
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
>>> random.seed(20)
>>> engine.gen_using(dimacs_maker, 'testfile3', {'min_weight':10, 'max_weight':30, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':0, 'direct':0, 'self_loop':1, 'multigraph':1})
131
>>> file=open('testfile3.gr','r')
>>> print(file.read())
c FILE                  :testfile3.gr
c No. of vertices       :100
c No. of edges          :131
c Max. weight           :30
c Min. weight           :10
p sp 100 131
a 1 34 30
a 3 76 15
a 3 5 23
a 4 13 13
a 4 20 20
a 4 65 28
a 5 60 16
a 5 32 20
a 5 90 20
a 6 64 12
a 6 93 26
a 7 62 12
a 7 36 28
a 7 41 11
a 8 21 12
a 9 47 19
a 10 49 15
a 10 27 10
a 11 48 17
a 11 100 17
a 14 61 18
a 14 33 30
a 14 68 29
a 14 84 14
a 15 87 15
a 15 42 22
a 17 82 28
a 18 46 17
a 18 24 29
a 18 18 26
a 19 57 15
a 20 97 12
a 22 2 30
a 22 95 20
a 23 69 26
a 23 94 11
a 23 85 15
a 25 78 20
a 25 12 12
a 25 79 13
a 27 52 30
a 27 31 19
a 30 51 26
a 32 26 26
a 33 66 14
a 34 59 13
a 34 74 13
a 34 54 17
a 35 56 13
a 36 44 27
a 36 83 14
a 38 70 10
a 38 39 16
a 38 91 30
a 39 67 13
a 39 99 19
a 40 63 29
a 41 43 13
a 41 16 18
a 43 75 19
a 43 77 24
a 43 45 12
a 44 58 10
a 44 96 12
a 44 98 29
a 45 86 10
a 45 37 18
a 46 81 13
a 46 28 11
a 47 55 29
a 48 92 12
a 48 92 21
a 48 72 24
a 50 88 27
a 51 73 18
a 51 29 24
a 51 29 28
a 52 80 17
a 52 71 19
a 52 89 20
a 53 58 29
a 53 16 21
a 53 40 12
a 54 8 13
a 54 98 17
a 55 55 10
a 56 82 21
a 57 73 14
a 57 2 17
a 58 76 24
a 59 67 22
a 60 78 29
a 60 88 19
a 62 61 21
a 62 99 14
a 62 75 17
a 63 26 21
a 63 66 30
a 63 87 14
a 65 12 26
a 65 37 21
a 66 50 27
a 67 74 25
a 67 42 14
a 68 72 10
a 70 84 18
a 71 91 20
a 74 30 13
a 76 13 25
a 78 9 25
a 78 81 22
a 80 96 19
a 81 90 23
a 81 28 24
a 82 93 25
a 83 31 16
a 85 21 16
a 85 94 22
a 86 17 19
a 86 86 27
a 89 97 19
a 91 49 23
a 91 77 13
a 92 100 17
a 93 24 27
a 93 69 19
a 96 64 14
a 97 95 14
a 98 1 15
a 98 1 13
a 99 35 28
>>> random.seed(4)
>>> engine.gen_using(dimacs_maker, 'testfile4', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':1, 'direct':1, 'self_loop':0, 'multigraph':0})
37
>>> file=open('testfile4.gr','r')
>>> print(file.read())
c FILE                  :testfile4.gr
c No. of vertices       :30
c No. of edges          :37
c Max. weight           :50
c Min. weight           :0
p sp 30 37
a 1 11 46
a 2 19 5
a 2 5 25
a 2 23 -48
a 4 24 -17
a 5 8 -13
a 7 16 10
a 7 18 -40
a 8 9 -42
a 8 26 11
a 9 30 -5
a 10 29 0
a 10 14 -48
a 10 22 26
a 10 20 -27
a 11 12 19
a 11 17 5
a 11 3 -40
a 12 25 -44
a 12 15 43
a 13 6 -12
a 14 27 22
a 14 28 -40
a 14 21 -6
a 16 19 7
a 17 15 -29
a 17 1 22
a 19 25 20
a 20 21 49
a 20 28 -39
a 21 4 -39
a 21 18 -18
a 22 24 -38
a 23 13 23
a 25 6 -50
a 26 29 28
a 26 3 -13
<BLANKLINE>
>>> #################### json_maker ####################
>>> random.seed(2)
>>> engine.gen_using(json_maker, 'testfile', {'min_weight':0, 'max_weight':200, 'vertices':10, 'min_edge':0, 'max_edge':2, 'sign':True, 'direct':True, 'self_loop':True, 'multigraph':False})
7
>>> file=open('testfile.json','r')
>>> testfile_1=json.load(file)
>>> testfile_1['graph']['nodes'][1]
{'id': 2}
>>> testfile_1['graph']['edges'][1]['source']
5
>>> testfile_1['graph']['edges'][1]['target']
6
>>> testfile_1['graph']['edges'][1]['weight']
148
>>> testfile_1['properties']['directed']
True
>>> testfile_1['properties']['multigraph']
False
>>> testfile_1['properties']['weighted']
True
>>> random.seed(4)
>>> engine.gen_using(json_maker, 'testfile2', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':True, 'direct':True, 'self_loop':True, 'multigraph':False})
35
>>> file=open('testfile2.json','r')
>>> testfile_2=json.load(file)
>>> testfile_2['graph']['nodes'][1]
{'id': 2}
>>> testfile_2['graph']['edges'][1]['source']
2
>>> testfile_2['graph']['edges'][1]['target']
18
>>> testfile_2['graph']['edges'][1]['weight']
5
>>> testfile_2['properties']['multigraph']
False
>>> testfile_2['properties']['directed']
True
>>> testfile_2['properties']['weighted']
True
>>> random.seed(20)
>>> engine.gen_using(json_maker, 'testfile3', {'min_weight':10, 'max_weight':30, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':False, 'direct':True, 'self_loop':True, 'multigraph':False})
137
>>> file=open('testfile3.json','r')
>>> testfile_3=json.load(file)
>>> testfile_3['graph']['nodes'][1]
{'id': 2}
>>> testfile_3['graph']['edges'][1]['source']
3
>>> testfile_3['graph']['edges'][1]['target']
76
>>> testfile_3['graph']['edges'][1]['weight']
15
>>> testfile_3['properties']['directed']
True
>>> testfile_3['properties']['multigraph']
False
>>> testfile_3['properties']['weighted']
True
>>> random.seed(20)
>>> engine.gen_using(json_maker, 'testfile3', {'min_weight':10, 'max_weight':30, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':False, 'direct':False, 'self_loop':True, 'multigraph':True})
131
>>> file=open('testfile3.json','r')
>>> testfile_3=json.load(file)
>>> testfile_3['properties']['directed']
False
>>> testfile_3['properties']['multigraph']
True
>>> testfile_3['properties']['weighted']
True
>>> random.seed(21)
>>> engine.gen_using(json_maker, 'testfile3', {'min_weight':1, 'max_weight':1, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':False, 'direct':False, 'self_loop':True, 'multigraph':True})
136
>>> file=open('testfile3.json','r')
>>> testfile_3=json.load(file)
>>> testfile_3['properties']['weighted']
False
>>> random.seed(21)
>>> engine.gen_using(json_maker, 'testfile3', {'min_weight':1, 'max_weight':1, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':True, 'direct':False, 'self_loop':True, 'multigraph':True})
158
>>> file=open('testfile3.json','r')
>>> testfile_3=json.load(file)
>>> testfile_3['properties']['weighted']
True
>>> #################### csv_maker ####################
>>> random.seed(2)
>>> engine.gen_using(csv_maker, 'testfile', {'min_weight':0, 'max_weight':200, 'vertices':10, 'min_edge':0, 'max_edge':2, 'sign':True, 'direct':True, 'self_loop':True, 'multigraph':False})
7
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
>>> engine.gen_using(csv_maker, 'testfile2', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':True, 'direct':True, 'self_loop':True, 'multigraph':False})
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
>>> random.seed(20)
>>> engine.gen_using(csv_maker, 'testfile3', {'min_weight':10, 'max_weight':30, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':False, 'direct':True, 'self_loop':True, 'multigraph':False})
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
>>> random.seed(20)
>>> engine.gen_using(csv_maker, 'testfile3', {'min_weight':10, 'max_weight':30, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':0, 'direct':0, 'self_loop':1, 'multigraph':1})
131
>>> random.seed(2)
>>> engine.gen_using(csv_maker, 'testfile4', {'min_weight':0.0, 'max_weight':200.22, 'vertices':10, 'min_edge':0, 'max_edge':2, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
5
>>> file = open("testfile4.csv")
>>> print(file.read())
4,3,-50.37
6,1,200.16
6,9,-160.91
7,7,-100.52
10,10,-181.75
<BLANKLINE>
>>> random.seed(2)
>>> engine.gen_using(csv_maker, 'testfile4', {'min_weight':0.0, 'max_weight':200.222, 'vertices':10, 'min_edge':0, 'max_edge':2, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
5
>>> file = open("testfile4.csv")
>>> print(file.read())
4,3,-50.373
6,1,200.166
6,9,-160.912
7,7,-100.525
10,10,-181.752
<BLANKLINE>
>>> #################### gdf_maker ####################
>>> random.seed(2)
>>> engine.gen_using(gdf_maker, 'testfile', {'min_weight':0, 'max_weight':200, 'vertices':10, 'min_edge':0, 'max_edge':2, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
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
>>> random.seed(4)
>>> engine.gen_using(gdf_maker, 'testfile2', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
35
>>> random.seed(20)
>>> engine.gen_using(gdf_maker, 'testfile3', {'min_weight':10, 'max_weight':30, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':0, 'direct':1, 'self_loop':1, 'multigraph':0})
137
>>> random.seed(20)
>>> engine.gen_using(gdf_maker, 'testfile3', {'min_weight':10, 'max_weight':30, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':0, 'direct':0, 'self_loop':1, 'multigraph':1})
131
>>> #################### gl_maker ####################
>>> random.seed(2)
>>> engine.gen_using(gl_maker, 'testfile', {'min_weight':0, 'max_weight':200, 'vertices':10, 'min_edge':1, 'max_edge':2, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
7
>>> file=open('testfile.gl','r')
>>> print(file.read())
1 2:92
3 7:155 9:110
4 10:-139 8:-9
5 6:-81
6 9:143
>>> random.seed(4)
>>> engine.gen_using(gl_maker, 'testfile2', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':2, 'max_edge':4, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
44
>>> file=open('testfile2.gl','r')
>>> print(file.read())
1 10:46 14:-9
2 4:25 22:-48
3 12:-17 9:16
4 5:-17
5 15:-18
6 23:38 21:-32 18:15 30:-5
7 29:0 16:-48 25:26 20:-27
8 13:19 24:5 8:-40
9 27:-44 19:43
10 11:-12
11 28:-17 17:-27 26:20
12 13:17
13 21:21 19:-29
14 14:-44
15 20:-1
16 23:-9 30:-39
17 18:-39 25:-18 22:-24
18 26:-36 24:-2
19 27:-50
20 29:28
22 28:3
25 10:38 2:-37
27 1:33
28 23:30
>>> random.seed(20)
>>> engine.gen_using(gl_maker, 'testfile3', {'min_weight':10, 'max_weight':30, 'vertices':100, 'min_edge':3, 'max_edge':4, 'sign':0, 'direct':1, 'self_loop':1, 'multigraph':0})
178
>>> file=open('testfile3.gl','r')
>>> print(file.read())
1 34:30 13:20 76:15
2 56:23 11:13 20:20
3 83:24 60:16 31:20 92:20
4 65:12 95:26 74:22 16:16
5 9:16 22:12 37:18
6 54:18 33:29 27:10 51:17
7 48:11 8:30 62:18
8 69:29 88:14
9 86:15 41:22 32:14
10 75:17 21:29 15:26 30:23
11 35:12 25:19
12 94:30 96:20 82:22
13 70:11 85:15 28:24
14 14:12 79:13 26:20
15 91:12 97:19 98:11
16 44:17 77:26
17 42:10 81:14 57:14
18 55:13 68:13 49:17 47:17
19 66:14 80:14 71:12
20 61:10 39:16 100:30
21 58:13 50:16 59:29
22 38:13 23:18 29:22
23 64:22 87:13 40:28
24 53:10 43:27 78:20 90:10
25 63:19 93:13
26 36:16 67:29
27 46:28 99:21 72:24
28 52:29 89:27
29 73:18 45:24 84:28
30 70:17 55:19 89:20
31 58:29 37:21 49:12
32 33:13 67:17 73:14
33 91:10 43:21
34 75:14 35:17 68:26
35 54:22 66:27
36 80:29 92:19 88:12
37 60:21 47:24
38 83:14 71:20
39 99:27 48:18
40 94:16 78:22
41 98:26 74:25
42 56:14 76:10
43 97:15
44 59:17 93:20 46:14
45 63:13 53:19 51:25
46 87:11
47 86:22 95:13
48 77:26
49 64:24 96:26
50 90:14 57:16 62:19
51 69:24
52 84:12 79:30 61:16
53 100:19
54 85:19
55 82:13 72:26
56 65:27
57 75:14 80:22
58 81:26
59 93:12
60 95:26
61 68:18
62 67:27 77:29
63 82:23 100:11
64 98:15
65 86:29
66 73:17 79:17
69 89:20 81:27
70 97:11
71 74:26 84:10
72 99:21 85:19
73 78:21
76 87:17
78 91:11
81 94:27
82 83:19
83 92:20
85 88:14
88 90:16
91 96:13
94 68:30
95 89:18
96 87:29
98 7:10
100 28:14
>>> #################### mtx_maker ####################
>>> from scipy.io import mmread
>>> random.seed(2)
>>> engine.gen_using(mtx_maker, 'testfile', {'min_weight':0, 'max_weight':200, 'vertices':10, 'min_edge':0, 'max_edge':2, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
7
>>> g = mmread("testfile.mtx")
>>> print(g.data.tolist())
[-64.0, 148.0, 110.0, -139.0, 7.0, -97.0, 60.0]
>>> random.seed(4)
>>> engine.gen_using(mtx_maker, 'testfile2', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
35
>>> g = mmread("testfile2.mtx")
>>> print(int(sum(g.data.tolist())))
-179
>>> random.seed(20)
>>> engine.gen_using(mtx_maker, 'testfile3', {'min_weight':10, 'max_weight':30, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':0, 'direct':1, 'self_loop':1, 'multigraph':0})
137
>>> g = mmread("testfile3.mtx")
>>> print(int(sum(g.data.tolist())))
2644
>>> random.seed(20)
>>> engine.gen_using(mtx_maker, 'testfile3', {'min_weight':10, 'max_weight':30, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':0, 'direct':0, 'self_loop':1, 'multigraph':1})
131
>>> #################### tsv_maker ####################
>>> random.seed(2)
>>> engine.gen_using(tsv_maker, 'testfile', {'min_weight':0, 'max_weight':200, 'vertices':10, 'min_edge':0, 'max_edge':2, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
7
>>> file=open('testfile.tsv','r')
>>> print(file.read())
4	3	-64
5	6	148
5	9	110
6	10	-139
7	7	7
8	2	-97
9	1	60
<BLANKLINE>
>>> random.seed(4)
>>> engine.gen_using(tsv_maker, 'testfile2', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
35
>>> random.seed(20)
>>> engine.gen_using(tsv_maker, 'testfile3', {'min_weight':10, 'max_weight':30, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':0, 'direct':1, 'self_loop':1, 'multigraph':0})
137
>>> random.seed(20)
>>> engine.gen_using(tsv_maker, 'testfile3', {'min_weight':10, 'max_weight':30, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':0, 'direct':0, 'self_loop':1, 'multigraph':1})
131
>>> #################### wel_maker ####################
>>> random.seed(2)
>>> engine.gen_using(wel_maker, 'testfile', {'min_weight':0, 'max_weight':200, 'vertices':10, 'min_edge':0, 'max_edge':2, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
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
>>> engine.gen_using(wel_maker, 'testfile2', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
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
>>> engine.gen_using(wel_maker, 'testfile3', {'min_weight':10, 'max_weight':30, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':0, 'direct':1, 'self_loop':1, 'multigraph':0})
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
>>> random.seed(20)
>>> engine.gen_using(wel_maker, 'testfile3', {'min_weight':10, 'max_weight':30, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':0, 'direct':0, 'self_loop':1, 'multigraph':1})
131
>>> #################### lp_maker ####################
>>> random.seed(2)
>>> engine.gen_using(lp_maker, 'testfile', {'min_weight':0, 'max_weight':200, 'vertices':10, 'min_edge':0, 'max_edge':2, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
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
>>> engine.gen_using(lp_maker, 'testfile2', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
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
>>> #################### tgf_maker ####################
>>> random.seed(2)
>>> engine.gen_using(tgf_maker, 'testfile', {'min_weight':0, 'max_weight':200, 'vertices':10, 'min_edge':0, 'max_edge':2, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
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
>>> engine.gen_using(tgf_maker, 'testfile2', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
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
>>> #################### dl_maker ####################
>>> random.seed(2)
>>> engine.gen_using(dl_maker, 'testfile', {'min_weight':0, 'max_weight':200, 'vertices':10, 'min_edge':0, 'max_edge':2, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
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
>>> engine.gen_using(dl_maker, 'testfile2', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
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
>>> #################### gml_maker ####################
>>> from networkx.readwrite.gml import read_gml
>>> random.seed(2)
>>> engine.gen_using(gml_maker, 'testfile', {'min_weight':0, 'max_weight':200, 'vertices':10, 'min_edge':0, 'max_edge':2, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
7
>>> gml1 = read_gml("testfile.gml")
>>> type(gml1)
<class 'networkx.classes.digraph.DiGraph'>
>>> random.seed(4)
>>> engine.gen_using(gml_maker, 'testfile2', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':1})
38
>>> gml2 = read_gml("testfile2.gml")
>>> type(gml2)
<class 'networkx.classes.digraph.DiGraph'>
>>> random.seed(20)
>>> engine.gen_using(gml_maker, 'testfile3', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':1, 'direct':0, 'self_loop':1, 'multigraph':1})
35
>>> gml3 = read_gml("testfile3.gml")
>>> type(gml3)
<class 'networkx.classes.multigraph.MultiGraph'>
>>> random.seed(120)
>>> engine.gen_using(gml_maker, 'testfile4', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':1, 'direct':0, 'self_loop':1, 'multigraph':0})
35
>>> gml4 = read_gml("testfile4.gml")
>>> type(gml4)
<class 'networkx.classes.graph.Graph'>
>>> #################### gexf_maker ####################
>>> from networkx.readwrite.gexf import read_gexf
>>> random.seed(2)
>>> engine.gen_using(gexf_maker, 'testfile', {'min_weight':0, 'max_weight':200, 'vertices':10, 'min_edge':0, 'max_edge':2, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
7
>>> gexf1 = read_gexf("testfile.gexf")
>>> type(gexf1)
<class 'networkx.classes.digraph.DiGraph'>
>>> random.seed(8)
>>> engine.gen_using(gexf_maker, 'testfile2', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':1})
35
>>> gexf2 = read_gexf("testfile2.gexf")
>>> type(gexf2)
<class 'networkx.classes.multidigraph.MultiDiGraph'>
>>> random.seed(20)
>>> engine.gen_using(gexf_maker, 'testfile3', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':1, 'direct':0, 'self_loop':1, 'multigraph':1})
35
>>> gexf3 = read_gexf("testfile3.gexf")
>>> type(gexf3)
<class 'networkx.classes.multigraph.MultiGraph'>
>>> random.seed(120)
>>> engine.gen_using(gexf_maker, 'testfile4', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':1, 'direct':0, 'self_loop':1, 'multigraph':0})
35
>>> gexf4 = read_gexf("testfile4.gexf")
>>> type(gexf4)
<class 'networkx.classes.graph.Graph'>
>>> random.seed(120)
>>> engine.gen_using(gexf_maker, 'testfile5', {'min_weight':0, 'max_weight':50.2, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':1, 'direct':0, 'self_loop':1, 'multigraph':0})
40
>>> gexf5 = read_gexf("testfile5.gexf")
>>> type(gexf5)
<class 'networkx.classes.graph.Graph'>
>>> #################### dot_maker ####################
>>> import pydot
>>> random.seed(2)
>>> engine.gen_using(dot_maker, 'testfile', {'min_weight':0, 'max_weight':200, 'vertices':10, 'min_edge':0, 'max_edge':2, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
7
>>> file=open('testfile.gv','r')
>>> g1 = pydot.graph_from_dot_data(file.read())
>>> g1[0].get_type()
'digraph'
>>> len(g1[0].get_edge_list())
7
>>> random.seed(4)
>>> engine.gen_using(dot_maker, 'testfile2', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
35
>>> file=open('testfile2.gv','r')
>>> g2 = pydot.graph_from_dot_data(file.read())
>>> g2[0].get_type()
'digraph'
>>> len(g2[0].get_edge_list())
35
>>> random.seed(20)
>>> engine.gen_using(dot_maker, 'testfile3', {'min_weight':10, 'max_weight':30, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':0, 'direct':0, 'self_loop':1, 'multigraph':1})
131
>>> file=open('testfile3.gv','r')
>>> g3 = pydot.graph_from_dot_data(file.read())
>>> g3[0].get_type()
'graph'
>>> len(g3[0].get_edge_list())
131
>>> file.close()
>>> os.remove('testfile.gr')
>>> os.remove('testfile2.gr')
>>> os.remove('testfile3.gr')
>>> os.remove('testfile4.gr')
>>> os.remove('testfile.json')
>>> os.remove('testfile2.json')
>>> os.remove('testfile3.json')
>>> os.remove('testfile.csv')
>>> os.remove('testfile2.csv')
>>> os.remove('testfile3.csv')
>>> os.remove('testfile4.csv')
>>> os.remove('testfile.gdf')
>>> os.remove('testfile2.gdf')
>>> os.remove('testfile3.gdf')
>>> os.remove('testfile.gl')
>>> os.remove('testfile2.gl')
>>> os.remove('testfile3.gl')
>>> os.remove('testfile.mtx')
>>> os.remove('testfile2.mtx')
>>> os.remove('testfile3.mtx')
>>> os.remove('testfile.tsv')
>>> os.remove('testfile2.tsv')
>>> os.remove('testfile3.tsv')
>>> os.remove('testfile.wel')
>>> os.remove('testfile2.wel')
>>> os.remove('testfile3.wel')
>>> os.remove('testfile.lp')
>>> os.remove('testfile2.lp')
>>> os.remove('testfile.tgf')
>>> os.remove('testfile2.tgf')
>>> os.remove('testfile.dl')
>>> os.remove('testfile2.dl')
>>> os.remove('testfile.gml')
>>> os.remove('testfile2.gml')
>>> os.remove('testfile3.gml')
>>> os.remove('testfile4.gml')
>>> os.remove('testfile.gexf')
>>> os.remove('testfile2.gexf')
>>> os.remove('testfile3.gexf')
>>> os.remove('testfile4.gexf')
>>> os.remove('testfile5.gexf')
>>> os.remove('testfile.gv')
>>> os.remove('testfile2.gv')
>>> os.remove('testfile3.gv')
>>> os.remove('logfile.log')
"""
