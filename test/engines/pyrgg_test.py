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
>>> random.seed(2)
>>> engine.gen_using(dimacs_maker, 'testfile', {'min_weight':0, 'max_weight':200, 'vertices':10, 'min_edge':0, 'max_edge':2, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
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
>>> engine.gen_using(dimacs_maker, 'testfile2', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
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
>>> engine.gen_using(dimacs_maker, 'testfile3', {'min_weight':10, 'max_weight':30, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':0, 'direct':1, 'self_loop':1, 'multigraph':0})
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
c Min. edge             :0
c Max. edge             :4
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
>>> testfile_1['properties']['signed']
True
>>> testfile_1['properties']['directed']
True
>>> testfile_1['properties']['self_loop']
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
>>> testfile_2['properties']['signed']
True
>>> testfile_2['properties']['directed']
True
>>> testfile_2['properties']['self_loop']
True
>>> testfile_2['properties']['multigraph']
False
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
>>> testfile_3['properties']['signed']
False
>>> testfile_3['properties']['directed']
True
>>> testfile_3['properties']['self_loop']
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
>>> testfile_3['properties']['signed']
False
>>> testfile_3['properties']['directed']
False
>>> testfile_3['properties']['self_loop']
True
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
>>> os.remove('testfile.gr')
>>> os.remove('testfile2.gr')
>>> os.remove('testfile3.gr')
>>> os.remove('testfile.json')
>>> os.remove('testfile2.json')
>>> os.remove('testfile3.json')
>>> os.remove('testfile.csv')
>>> os.remove('testfile.gdf')
>>> os.remove('testfile.gl')
>>> os.remove('logfile.log')
"""