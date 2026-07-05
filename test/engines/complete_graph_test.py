# -*- coding: utf-8 -*-
"""
>>> from pyrgg.functions import *
>>> from pyrgg.graph_gen import *
>>> import pyrgg.params
>>> import random
>>> import os
>>> import json
>>> import networkx as nx
>>> import pyrgg.engines.complete_graph as engine
>>> os.environ["PYRGG_TEST_MODE"] = "1"
>>> ######################################
>>> ## ========= logger function =========
>>> ######################################
>>> with open('logfile.log','a') as file:
...     engine.logger(file,'test','2min',{'vertices':100,'edge_number':45,'direct':0,'max_weight':1,'min_weight':1,'engine':9,'output_format':1})
>>> file = open('logfile.log','r')
>>> print("\\n".join(file.read().splitlines()[1:-1]))
Filename : test
Vertices : 100
Total Edges : 45
Directed : False
Weighted : False
Max Weight : 1
Min Weight : 1
Engine : 9 (cg)
Elapsed Time : 2min
>>> class StrError:
...     def __init__(self):
...         pass
...     def __str__(self):
...         raise ValueError
>>> str_error_object = StrError()
>>> with open('logfile.log','a') as file:
...     engine.logger(file,'test','2min',{'vertices':str_error_object,'edge_number':45,'direct':0,'max_weight':1,'min_weight':1,'engine':9,'output_format':1})
[Error] Logger failed!
>>> ##########################################
>>> ## ========= generate_edges function =========
>>> ##########################################
>>> random.seed(2)
>>> edge_dict, weight_dict, edge_number = engine.generate_edges(10, 1, 1, False)
>>> edge_dict == {1: [], 2: [1], 3: [1, 2], 4: [1, 2, 3], 5: [1, 2, 3, 4], 6: [1, 2, 3, 4, 5], 7: [1, 2, 3, 4, 5, 6], 8: [1, 2, 3, 4, 5, 6, 7], 9: [1, 2, 3, 4, 5, 6, 7, 8], 10: [1, 2, 3, 4, 5, 6, 7, 8, 9]}
True
>>> weight_dict == {1: [], 2: [1], 3: [1, 1], 4: [1, 1, 1], 5: [1, 1, 1, 1], 6: [1, 1, 1, 1, 1], 7: [1, 1, 1, 1, 1, 1], 8: [1, 1, 1, 1, 1, 1, 1], 9: [1, 1, 1, 1, 1, 1, 1, 1], 10: [1, 1, 1, 1, 1, 1, 1, 1, 1]}
True
>>> edge_number == 45
True
>>> random.seed(11)
>>> edge_dict, weight_dict, edge_number = engine.generate_edges(10, 0, 200, True)
>>> edge_dict == {1: [2, 3, 4, 5, 6, 7, 8, 9, 10], 2: [1, 3, 4, 5, 6, 7, 8, 9, 10], 3: [1, 2, 4, 5, 6, 7, 8, 9, 10], 4: [1, 2, 3, 5, 6, 7, 8, 9, 10], 5: [1, 2, 3, 4, 6, 7, 8, 9, 10], 6: [1, 2, 3, 4, 5, 7, 8, 9, 10], 7: [1, 2, 3, 4, 5, 6, 8, 9, 10], 8: [1, 2, 3, 4, 5, 6, 7, 9, 10], 9: [1, 2, 3, 4, 5, 6, 7, 8, 10], 10: [1, 2, 3, 4, 5, 6, 7, 8, 9]}
True
>>> weight_dict == {1: [115, 143, 199, 119, 115, 130, 150, 48, 47], 2: [131, 121, 161, 157, 47, 24, 114, 77, 36], 3: [23, 137, 177, 162, 10, 152, 101, 115, 167], 4: [189, 157, 166, 40, 159, 3, 135, 16, 15], 5: [9, 48, 61, 153, 7, 199, 118, 83, 112], 6: [151, 50, 132, 59, 163, 75, 127, 1, 169], 7: [21, 117, 167, 71, 104, 141, 21, 181, 65], 8: [80, 194, 58, 131, 73, 7, 17, 144, 196], 9: [27, 102, 27, 74, 98, 17, 4, 175, 0], 10: [54, 53, 13, 120, 96, 181, 101, 107, 18]}
True
>>> edge_number == 90
True
>>> engine.generate_edges()
Traceback (most recent call last):
        ...
TypeError: generate_edges() missing 4 required positional arguments: 'n', 'min_weight', 'max_weight', and 'direct'
>>> #########################################
>>> ## ========= generate_graph function =========
>>> #########################################
>>> #################### generate_dimacs_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_dimacs_file, 'testfile', {'vertices':10, 'min_weight':1, 'max_weight':1, 'direct':0})
45
>>> file=open('testfile.gr','r')
>>> print(file.read())
c FILE                  :testfile.gr
c No. of vertices       :10
c No. of edges          :45
c Max. weight           :1
c Min. weight           :1
p sp 10 45
a 2 1 1
a 3 1 1
a 3 2 1
a 4 1 1
a 4 2 1
a 4 3 1
a 5 1 1
a 5 2 1
a 5 3 1
a 5 4 1
a 6 1 1
a 6 2 1
a 6 3 1
a 6 4 1
a 6 5 1
a 7 1 1
a 7 2 1
a 7 3 1
a 7 4 1
a 7 5 1
a 7 6 1
a 8 1 1
a 8 2 1
a 8 3 1
a 8 4 1
a 8 5 1
a 8 6 1
a 8 7 1
a 9 1 1
a 9 2 1
a 9 3 1
a 9 4 1
a 9 5 1
a 9 6 1
a 9 7 1
a 9 8 1
a 10 1 1
a 10 2 1
a 10 3 1
a 10 4 1
a 10 5 1
a 10 6 1
a 10 7 1
a 10 8 1
a 10 9 1
<BLANKLINE>
>>> random.seed(11)
>>> engine.generate_graph(generate_dimacs_file, 'testfile2', {'vertices':10, 'min_weight':0, 'max_weight':200, 'direct':1})
90
>>> file=open('testfile2.gr','r')
>>> print(file.read())
c FILE                  :testfile2.gr
c No. of vertices       :10
c No. of edges          :90
c Max. weight           :199
c Min. weight           :0
p sp 10 90
a 1 2 115
a 1 3 143
a 1 4 199
a 1 5 119
a 1 6 115
a 1 7 130
a 1 8 150
a 1 9 48
a 1 10 47
a 2 1 131
a 2 3 121
a 2 4 161
a 2 5 157
a 2 6 47
a 2 7 24
a 2 8 114
a 2 9 77
a 2 10 36
a 3 1 23
a 3 2 137
a 3 4 177
a 3 5 162
a 3 6 10
a 3 7 152
a 3 8 101
a 3 9 115
a 3 10 167
a 4 1 189
a 4 2 157
a 4 3 166
a 4 5 40
a 4 6 159
a 4 7 3
a 4 8 135
a 4 9 16
a 4 10 15
a 5 1 9
a 5 2 48
a 5 3 61
a 5 4 153
a 5 6 7
a 5 7 199
a 5 8 118
a 5 9 83
a 5 10 112
a 6 1 151
a 6 2 50
a 6 3 132
a 6 4 59
a 6 5 163
a 6 7 75
a 6 8 127
a 6 9 1
a 6 10 169
a 7 1 21
a 7 2 117
a 7 3 167
a 7 4 71
a 7 5 104
a 7 6 141
a 7 8 21
a 7 9 181
a 7 10 65
a 8 1 80
a 8 2 194
a 8 3 58
a 8 4 131
a 8 5 73
a 8 6 7
a 8 7 17
a 8 9 144
a 8 10 196
a 9 1 27
a 9 2 102
a 9 3 27
a 9 4 74
a 9 5 98
a 9 6 17
a 9 7 4
a 9 8 175
a 9 10 0
a 10 1 54
a 10 2 53
a 10 3 13
a 10 4 120
a 10 5 96
a 10 6 181
a 10 7 101
a 10 8 107
a 10 9 18
<BLANKLINE>
>>> #################### generate_json_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_json_file, 'testfile', {'vertices':10, 'min_weight':1, 'max_weight':1, 'direct':0})
45
>>> file=open('testfile.json','r')
>>> testfile_1=json.load(file)
>>> testfile_1['properties']['weighted']
False
>>> testfile_1['graph']['nodes'][1]
{'id': 2}
>>> testfile_1['graph']['edges'][1]['source']
3
>>> testfile_1['graph']['edges'][1]['target']
1
>>> random.seed(11)
>>> engine.generate_graph(generate_json_file, 'testfile2', {'vertices':10, 'min_weight':0, 'max_weight':200, 'direct':1})
90
>>> file=open('testfile2.json','r')
>>> testfile_2=json.load(file)
>>> testfile_2['properties']['weighted']
True
>>> testfile_2['graph']['nodes'][1]
{'id': 2}
>>> testfile_2['graph']['edges'][1]['source']
1
>>> testfile_2['graph']['edges'][1]['target']
3
>>> testfile_2['graph']['edges'][1]['weight']
143
>>> #################### generate_csv_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_csv_file, 'testfile', {'vertices':10, 'min_weight':1, 'max_weight':1, 'direct':0})
45
>>> file=open('testfile.csv','r')
>>> print(file.read())
2,1,1
3,1,1
3,2,1
4,1,1
4,2,1
4,3,1
5,1,1
5,2,1
5,3,1
5,4,1
6,1,1
6,2,1
6,3,1
6,4,1
6,5,1
7,1,1
7,2,1
7,3,1
7,4,1
7,5,1
7,6,1
8,1,1
8,2,1
8,3,1
8,4,1
8,5,1
8,6,1
8,7,1
9,1,1
9,2,1
9,3,1
9,4,1
9,5,1
9,6,1
9,7,1
9,8,1
10,1,1
10,2,1
10,3,1
10,4,1
10,5,1
10,6,1
10,7,1
10,8,1
10,9,1
<BLANKLINE>
>>> random.seed(11)
>>> engine.generate_graph(generate_csv_file, 'testfile2', {'vertices':10, 'min_weight':0, 'max_weight':200, 'direct':1})
90
>>> file=open('testfile2.csv','r')
>>> print(file.read())
1,2,115
1,3,143
1,4,199
1,5,119
1,6,115
1,7,130
1,8,150
1,9,48
1,10,47
2,1,131
2,3,121
2,4,161
2,5,157
2,6,47
2,7,24
2,8,114
2,9,77
2,10,36
3,1,23
3,2,137
3,4,177
3,5,162
3,6,10
3,7,152
3,8,101
3,9,115
3,10,167
4,1,189
4,2,157
4,3,166
4,5,40
4,6,159
4,7,3
4,8,135
4,9,16
4,10,15
5,1,9
5,2,48
5,3,61
5,4,153
5,6,7
5,7,199
5,8,118
5,9,83
5,10,112
6,1,151
6,2,50
6,3,132
6,4,59
6,5,163
6,7,75
6,8,127
6,9,1
6,10,169
7,1,21
7,2,117
7,3,167
7,4,71
7,5,104
7,6,141
7,8,21
7,9,181
7,10,65
8,1,80
8,2,194
8,3,58
8,4,131
8,5,73
8,6,7
8,7,17
8,9,144
8,10,196
9,1,27
9,2,102
9,3,27
9,4,74
9,5,98
9,6,17
9,7,4
9,8,175
9,10,0
10,1,54
10,2,53
10,3,13
10,4,120
10,5,96
10,6,181
10,7,101
10,8,107
10,9,18
<BLANKLINE>
>>> #################### generate_gdf_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_gdf_file, 'testfile', {'vertices':10, 'min_weight':1, 'max_weight':1, 'direct':0})
45
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
2,1,1
3,1,1
3,2,1
4,1,1
4,2,1
4,3,1
5,1,1
5,2,1
5,3,1
5,4,1
6,1,1
6,2,1
6,3,1
6,4,1
6,5,1
7,1,1
7,2,1
7,3,1
7,4,1
7,5,1
7,6,1
8,1,1
8,2,1
8,3,1
8,4,1
8,5,1
8,6,1
8,7,1
9,1,1
9,2,1
9,3,1
9,4,1
9,5,1
9,6,1
9,7,1
9,8,1
10,1,1
10,2,1
10,3,1
10,4,1
10,5,1
10,6,1
10,7,1
10,8,1
10,9,1
<BLANKLINE>
>>> random.seed(11)
>>> engine.generate_graph(generate_gdf_file, 'testfile2', {'vertices':10, 'min_weight':0, 'max_weight':200, 'direct':1})
90
>>> file=open('testfile2.gdf','r')
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
1,2,115
1,3,143
1,4,199
1,5,119
1,6,115
1,7,130
1,8,150
1,9,48
1,10,47
2,1,131
2,3,121
2,4,161
2,5,157
2,6,47
2,7,24
2,8,114
2,9,77
2,10,36
3,1,23
3,2,137
3,4,177
3,5,162
3,6,10
3,7,152
3,8,101
3,9,115
3,10,167
4,1,189
4,2,157
4,3,166
4,5,40
4,6,159
4,7,3
4,8,135
4,9,16
4,10,15
5,1,9
5,2,48
5,3,61
5,4,153
5,6,7
5,7,199
5,8,118
5,9,83
5,10,112
6,1,151
6,2,50
6,3,132
6,4,59
6,5,163
6,7,75
6,8,127
6,9,1
6,10,169
7,1,21
7,2,117
7,3,167
7,4,71
7,5,104
7,6,141
7,8,21
7,9,181
7,10,65
8,1,80
8,2,194
8,3,58
8,4,131
8,5,73
8,6,7
8,7,17
8,9,144
8,10,196
9,1,27
9,2,102
9,3,27
9,4,74
9,5,98
9,6,17
9,7,4
9,8,175
9,10,0
10,1,54
10,2,53
10,3,13
10,4,120
10,5,96
10,6,181
10,7,101
10,8,107
10,9,18
<BLANKLINE>
>>> #################### generate_gl_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_gl_file, 'testfile', {'vertices':10, 'min_weight':1, 'max_weight':1, 'direct':0})
45
>>> file=open('testfile.gl','r')
>>> print(file.read())
2 1:1
3 1:1 2:1
4 1:1 2:1 3:1
5 1:1 2:1 3:1 4:1
6 1:1 2:1 3:1 4:1 5:1
7 1:1 2:1 3:1 4:1 5:1 6:1
8 1:1 2:1 3:1 4:1 5:1 6:1 7:1
9 1:1 2:1 3:1 4:1 5:1 6:1 7:1 8:1
10 1:1 2:1 3:1 4:1 5:1 6:1 7:1 8:1 9:1
<BLANKLINE>
>>> random.seed(11)
>>> engine.generate_graph(generate_gl_file, 'testfile2', {'vertices':10, 'min_weight':0, 'max_weight':200, 'direct':1})
90
>>> file=open('testfile2.gl','r')
>>> print(file.read())
1 2:115 3:143 4:199 5:119 6:115 7:130 8:150 9:48 10:47
2 1:131 3:121 4:161 5:157 6:47 7:24 8:114 9:77 10:36
3 1:23 2:137 4:177 5:162 6:10 7:152 8:101 9:115 10:167
4 1:189 2:157 3:166 5:40 6:159 7:3 8:135 9:16 10:15
5 1:9 2:48 3:61 4:153 6:7 7:199 8:118 9:83 10:112
6 1:151 2:50 3:132 4:59 5:163 7:75 8:127 9:1 10:169
7 1:21 2:117 3:167 4:71 5:104 6:141 8:21 9:181 10:65
8 1:80 2:194 3:58 4:131 5:73 6:7 7:17 9:144 10:196
9 1:27 2:102 3:27 4:74 5:98 6:17 7:4 8:175 10:0
10 1:54 2:53 3:13 4:120 5:96 6:181 7:101 8:107 9:18
<BLANKLINE>
>>> #################### generate_mtx_file ####################
>>> from scipy.io import mmread
>>> random.seed(2)
>>> engine.generate_graph(generate_mtx_file, 'testfile', {'vertices':10, 'min_weight':1, 'max_weight':1, 'direct':0})
45
>>> g = mmread("testfile.mtx")
>>> print(g.data.tolist())
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
>>> random.seed(11)
>>> engine.generate_graph(generate_mtx_file, 'testfile2', {'vertices':10, 'min_weight':0, 'max_weight':200, 'direct':1})
90
>>> g = mmread("testfile2.mtx")
>>> print(g.data.tolist())
[115.0, 143.0, 199.0, 119.0, 115.0, 130.0, 150.0, 48.0, 47.0, 131.0, 121.0, 161.0, 157.0, 47.0, 24.0, 114.0, 77.0, 36.0, 23.0, 137.0, 177.0, 162.0, 10.0, 152.0, 101.0, 115.0, 167.0, 189.0, 157.0, 166.0, 40.0, 159.0, 3.0, 135.0, 16.0, 15.0, 9.0, 48.0, 61.0, 153.0, 7.0, 199.0, 118.0, 83.0, 112.0, 151.0, 50.0, 132.0, 59.0, 163.0, 75.0, 127.0, 1.0, 169.0, 21.0, 117.0, 167.0, 71.0, 104.0, 141.0, 21.0, 181.0, 65.0, 80.0, 194.0, 58.0, 131.0, 73.0, 7.0, 17.0, 144.0, 196.0, 27.0, 102.0, 27.0, 74.0, 98.0, 17.0, 4.0, 175.0, 0.0, 54.0, 53.0, 13.0, 120.0, 96.0, 181.0, 101.0, 107.0, 18.0]
>>> #################### generate_tsv_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_tsv_file, 'testfile', {'vertices':10, 'min_weight':1, 'max_weight':1, 'direct':0})
45
>>> file=open('testfile.tsv','r')
>>> print(file.read())
2	1	1
3	1	1
3	2	1
4	1	1
4	2	1
4	3	1
5	1	1
5	2	1
5	3	1
5	4	1
6	1	1
6	2	1
6	3	1
6	4	1
6	5	1
7	1	1
7	2	1
7	3	1
7	4	1
7	5	1
7	6	1
8	1	1
8	2	1
8	3	1
8	4	1
8	5	1
8	6	1
8	7	1
9	1	1
9	2	1
9	3	1
9	4	1
9	5	1
9	6	1
9	7	1
9	8	1
10	1	1
10	2	1
10	3	1
10	4	1
10	5	1
10	6	1
10	7	1
10	8	1
10	9	1
<BLANKLINE>
>>> random.seed(11)
>>> engine.generate_graph(generate_tsv_file, 'testfile2', {'vertices':10, 'min_weight':0, 'max_weight':200, 'direct':1})
90
>>> file=open('testfile2.tsv','r')
>>> print(file.read())
1	2	115
1	3	143
1	4	199
1	5	119
1	6	115
1	7	130
1	8	150
1	9	48
1	10	47
2	1	131
2	3	121
2	4	161
2	5	157
2	6	47
2	7	24
2	8	114
2	9	77
2	10	36
3	1	23
3	2	137
3	4	177
3	5	162
3	6	10
3	7	152
3	8	101
3	9	115
3	10	167
4	1	189
4	2	157
4	3	166
4	5	40
4	6	159
4	7	3
4	8	135
4	9	16
4	10	15
5	1	9
5	2	48
5	3	61
5	4	153
5	6	7
5	7	199
5	8	118
5	9	83
5	10	112
6	1	151
6	2	50
6	3	132
6	4	59
6	5	163
6	7	75
6	8	127
6	9	1
6	10	169
7	1	21
7	2	117
7	3	167
7	4	71
7	5	104
7	6	141
7	8	21
7	9	181
7	10	65
8	1	80
8	2	194
8	3	58
8	4	131
8	5	73
8	6	7
8	7	17
8	9	144
8	10	196
9	1	27
9	2	102
9	3	27
9	4	74
9	5	98
9	6	17
9	7	4
9	8	175
9	10	0
10	1	54
10	2	53
10	3	13
10	4	120
10	5	96
10	6	181
10	7	101
10	8	107
10	9	18
<BLANKLINE>
>>> #################### generate_wel_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_wel_file, 'testfile', {'vertices':10, 'min_weight':1, 'max_weight':1, 'direct':0})
45
>>> file=open('testfile.wel','r')
>>> print(file.read())
2 1 1
3 1 1
3 2 1
4 1 1
4 2 1
4 3 1
5 1 1
5 2 1
5 3 1
5 4 1
6 1 1
6 2 1
6 3 1
6 4 1
6 5 1
7 1 1
7 2 1
7 3 1
7 4 1
7 5 1
7 6 1
8 1 1
8 2 1
8 3 1
8 4 1
8 5 1
8 6 1
8 7 1
9 1 1
9 2 1
9 3 1
9 4 1
9 5 1
9 6 1
9 7 1
9 8 1
10 1 1
10 2 1
10 3 1
10 4 1
10 5 1
10 6 1
10 7 1
10 8 1
10 9 1
<BLANKLINE>
>>> random.seed(11)
>>> engine.generate_graph(generate_wel_file, 'testfile2', {'vertices':10, 'min_weight':0, 'max_weight':200, 'direct':1})
90
>>> file=open('testfile2.wel','r')
>>> print(file.read())
1 2 115
1 3 143
1 4 199
1 5 119
1 6 115
1 7 130
1 8 150
1 9 48
1 10 47
2 1 131
2 3 121
2 4 161
2 5 157
2 6 47
2 7 24
2 8 114
2 9 77
2 10 36
3 1 23
3 2 137
3 4 177
3 5 162
3 6 10
3 7 152
3 8 101
3 9 115
3 10 167
4 1 189
4 2 157
4 3 166
4 5 40
4 6 159
4 7 3
4 8 135
4 9 16
4 10 15
5 1 9
5 2 48
5 3 61
5 4 153
5 6 7
5 7 199
5 8 118
5 9 83
5 10 112
6 1 151
6 2 50
6 3 132
6 4 59
6 5 163
6 7 75
6 8 127
6 9 1
6 10 169
7 1 21
7 2 117
7 3 167
7 4 71
7 5 104
7 6 141
7 8 21
7 9 181
7 10 65
8 1 80
8 2 194
8 3 58
8 4 131
8 5 73
8 6 7
8 7 17
8 9 144
8 10 196
9 1 27
9 2 102
9 3 27
9 4 74
9 5 98
9 6 17
9 7 4
9 8 175
9 10 0
10 1 54
10 2 53
10 3 13
10 4 120
10 5 96
10 6 181
10 7 101
10 8 107
10 9 18
<BLANKLINE>
>>> #################### generate_lp_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_lp_file, 'testfile', {'vertices':10, 'min_weight':1, 'max_weight':1, 'direct':0})
45
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
edge(2,1,1).
edge(3,1,1).
edge(3,2,1).
edge(4,1,1).
edge(4,2,1).
edge(4,3,1).
edge(5,1,1).
edge(5,2,1).
edge(5,3,1).
edge(5,4,1).
edge(6,1,1).
edge(6,2,1).
edge(6,3,1).
edge(6,4,1).
edge(6,5,1).
edge(7,1,1).
edge(7,2,1).
edge(7,3,1).
edge(7,4,1).
edge(7,5,1).
edge(7,6,1).
edge(8,1,1).
edge(8,2,1).
edge(8,3,1).
edge(8,4,1).
edge(8,5,1).
edge(8,6,1).
edge(8,7,1).
edge(9,1,1).
edge(9,2,1).
edge(9,3,1).
edge(9,4,1).
edge(9,5,1).
edge(9,6,1).
edge(9,7,1).
edge(9,8,1).
edge(10,1,1).
edge(10,2,1).
edge(10,3,1).
edge(10,4,1).
edge(10,5,1).
edge(10,6,1).
edge(10,7,1).
edge(10,8,1).
edge(10,9,1).
<BLANKLINE>
>>> random.seed(11)
>>> engine.generate_graph(generate_lp_file, 'testfile2', {'vertices':10, 'min_weight':0, 'max_weight':200, 'direct':1})
90
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
edge(1,2,115).
edge(1,3,143).
edge(1,4,199).
edge(1,5,119).
edge(1,6,115).
edge(1,7,130).
edge(1,8,150).
edge(1,9,48).
edge(1,10,47).
edge(2,1,131).
edge(2,3,121).
edge(2,4,161).
edge(2,5,157).
edge(2,6,47).
edge(2,7,24).
edge(2,8,114).
edge(2,9,77).
edge(2,10,36).
edge(3,1,23).
edge(3,2,137).
edge(3,4,177).
edge(3,5,162).
edge(3,6,10).
edge(3,7,152).
edge(3,8,101).
edge(3,9,115).
edge(3,10,167).
edge(4,1,189).
edge(4,2,157).
edge(4,3,166).
edge(4,5,40).
edge(4,6,159).
edge(4,7,3).
edge(4,8,135).
edge(4,9,16).
edge(4,10,15).
edge(5,1,9).
edge(5,2,48).
edge(5,3,61).
edge(5,4,153).
edge(5,6,7).
edge(5,7,199).
edge(5,8,118).
edge(5,9,83).
edge(5,10,112).
edge(6,1,151).
edge(6,2,50).
edge(6,3,132).
edge(6,4,59).
edge(6,5,163).
edge(6,7,75).
edge(6,8,127).
edge(6,9,1).
edge(6,10,169).
edge(7,1,21).
edge(7,2,117).
edge(7,3,167).
edge(7,4,71).
edge(7,5,104).
edge(7,6,141).
edge(7,8,21).
edge(7,9,181).
edge(7,10,65).
edge(8,1,80).
edge(8,2,194).
edge(8,3,58).
edge(8,4,131).
edge(8,5,73).
edge(8,6,7).
edge(8,7,17).
edge(8,9,144).
edge(8,10,196).
edge(9,1,27).
edge(9,2,102).
edge(9,3,27).
edge(9,4,74).
edge(9,5,98).
edge(9,6,17).
edge(9,7,4).
edge(9,8,175).
edge(9,10,0).
edge(10,1,54).
edge(10,2,53).
edge(10,3,13).
edge(10,4,120).
edge(10,5,96).
edge(10,6,181).
edge(10,7,101).
edge(10,8,107).
edge(10,9,18).
<BLANKLINE>
>>> #################### generate_tgf_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_tgf_file, 'testfile', {'vertices':10, 'min_weight':1, 'max_weight':1, 'direct':0})
45
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
2 1 1
3 1 1
3 2 1
4 1 1
4 2 1
4 3 1
5 1 1
5 2 1
5 3 1
5 4 1
6 1 1
6 2 1
6 3 1
6 4 1
6 5 1
7 1 1
7 2 1
7 3 1
7 4 1
7 5 1
7 6 1
8 1 1
8 2 1
8 3 1
8 4 1
8 5 1
8 6 1
8 7 1
9 1 1
9 2 1
9 3 1
9 4 1
9 5 1
9 6 1
9 7 1
9 8 1
10 1 1
10 2 1
10 3 1
10 4 1
10 5 1
10 6 1
10 7 1
10 8 1
10 9 1
<BLANKLINE>
>>> random.seed(11)
>>> engine.generate_graph(generate_tgf_file, 'testfile2', {'vertices':10, 'min_weight':0, 'max_weight':200, 'direct':1})
90
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
#
1 2 115
1 3 143
1 4 199
1 5 119
1 6 115
1 7 130
1 8 150
1 9 48
1 10 47
2 1 131
2 3 121
2 4 161
2 5 157
2 6 47
2 7 24
2 8 114
2 9 77
2 10 36
3 1 23
3 2 137
3 4 177
3 5 162
3 6 10
3 7 152
3 8 101
3 9 115
3 10 167
4 1 189
4 2 157
4 3 166
4 5 40
4 6 159
4 7 3
4 8 135
4 9 16
4 10 15
5 1 9
5 2 48
5 3 61
5 4 153
5 6 7
5 7 199
5 8 118
5 9 83
5 10 112
6 1 151
6 2 50
6 3 132
6 4 59
6 5 163
6 7 75
6 8 127
6 9 1
6 10 169
7 1 21
7 2 117
7 3 167
7 4 71
7 5 104
7 6 141
7 8 21
7 9 181
7 10 65
8 1 80
8 2 194
8 3 58
8 4 131
8 5 73
8 6 7
8 7 17
8 9 144
8 10 196
9 1 27
9 2 102
9 3 27
9 4 74
9 5 98
9 6 17
9 7 4
9 8 175
9 10 0
10 1 54
10 2 53
10 3 13
10 4 120
10 5 96
10 6 181
10 7 101
10 8 107
10 9 18
<BLANKLINE>
>>> #################### generate_dl_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_dl_file, 'testfile', {'vertices':10, 'min_weight':1, 'max_weight':1, 'direct':0})
45
>>> file=open('testfile.dl','r')
>>> print(file.read())
dl
format=edgelist1
n=10
data:
2 1 1
3 1 1
3 2 1
4 1 1
4 2 1
4 3 1
5 1 1
5 2 1
5 3 1
5 4 1
6 1 1
6 2 1
6 3 1
6 4 1
6 5 1
7 1 1
7 2 1
7 3 1
7 4 1
7 5 1
7 6 1
8 1 1
8 2 1
8 3 1
8 4 1
8 5 1
8 6 1
8 7 1
9 1 1
9 2 1
9 3 1
9 4 1
9 5 1
9 6 1
9 7 1
9 8 1
10 1 1
10 2 1
10 3 1
10 4 1
10 5 1
10 6 1
10 7 1
10 8 1
10 9 1
<BLANKLINE>
>>> random.seed(11)
>>> engine.generate_graph(generate_dl_file, 'testfile2', {'vertices':10, 'min_weight':0, 'max_weight':200, 'direct':1})
90
>>> file=open('testfile2.dl','r')
>>> print(file.read())
dl
format=edgelist1
n=10
data:
1 2 115
1 3 143
1 4 199
1 5 119
1 6 115
1 7 130
1 8 150
1 9 48
1 10 47
2 1 131
2 3 121
2 4 161
2 5 157
2 6 47
2 7 24
2 8 114
2 9 77
2 10 36
3 1 23
3 2 137
3 4 177
3 5 162
3 6 10
3 7 152
3 8 101
3 9 115
3 10 167
4 1 189
4 2 157
4 3 166
4 5 40
4 6 159
4 7 3
4 8 135
4 9 16
4 10 15
5 1 9
5 2 48
5 3 61
5 4 153
5 6 7
5 7 199
5 8 118
5 9 83
5 10 112
6 1 151
6 2 50
6 3 132
6 4 59
6 5 163
6 7 75
6 8 127
6 9 1
6 10 169
7 1 21
7 2 117
7 3 167
7 4 71
7 5 104
7 6 141
7 8 21
7 9 181
7 10 65
8 1 80
8 2 194
8 3 58
8 4 131
8 5 73
8 6 7
8 7 17
8 9 144
8 10 196
9 1 27
9 2 102
9 3 27
9 4 74
9 5 98
9 6 17
9 7 4
9 8 175
9 10 0
10 1 54
10 2 53
10 3 13
10 4 120
10 5 96
10 6 181
10 7 101
10 8 107
10 9 18
<BLANKLINE>
>>> #################### generate_gml_file ####################
>>> from networkx.readwrite.gml import read_gml
>>> random.seed(2)
>>> engine.generate_graph(generate_gml_file, 'testfile', {'vertices':10, 'min_weight':1, 'max_weight':1, 'direct':0})
45
>>> gml1 = read_gml("testfile.gml")
>>> type(gml1)
<class 'networkx.classes.graph.Graph'>
>>> nx.is_isomorphic(gml1, nx.complete_graph(10))
True
>>> random.seed(11)
>>> engine.generate_graph(generate_gml_file, 'testfile2', {'vertices':10, 'min_weight':0, 'max_weight':200, 'direct':1})
90
>>> gml2 = read_gml("testfile2.gml")
>>> type(gml2)
<class 'networkx.classes.digraph.DiGraph'>
>>> nx.is_isomorphic(gml2, nx.complete_graph(10).to_directed())
True
>>> #################### generate_gexf_file ####################
>>> from networkx.readwrite.gexf import read_gexf
>>> random.seed(2)
>>> engine.generate_graph(generate_gexf_file, 'testfile', {'vertices':10, 'min_weight':1, 'max_weight':1, 'direct':0})
45
>>> gexf1 = read_gexf("testfile.gexf")
>>> type(gexf1)
<class 'networkx.classes.graph.Graph'>
>>> nx.is_isomorphic(gexf1, nx.complete_graph(10))
True
>>> random.seed(11)
>>> engine.generate_graph(generate_gexf_file, 'testfile2', {'vertices':10, 'min_weight':0, 'max_weight':200, 'direct':1})
90
>>> gexf2 = read_gexf("testfile2.gexf")
>>> type(gexf2)
<class 'networkx.classes.digraph.DiGraph'>
>>> nx.is_isomorphic(gexf2, nx.complete_graph(10).to_directed())
True
>>> #################### generate_dot_file ####################
>>> import pydot
>>> random.seed(2)
>>> engine.generate_graph(generate_dot_file, 'testfile', {'vertices':10, 'min_weight':1, 'max_weight':1, 'direct':0})
45
>>> file=open('testfile.gv','r')
>>> g1 = pydot.graph_from_dot_data(file.read())
>>> g1[0].get_type()
'graph'
>>> len(g1[0].get_edge_list())
45
>>> random.seed(11)
>>> engine.generate_graph(generate_dot_file, 'testfile2', {'vertices':10, 'min_weight':0, 'max_weight':200, 'direct':1})
90
>>> file=open('testfile2.gv','r')
>>> g2 = pydot.graph_from_dot_data(file.read())
>>> g2[0].get_type()
'digraph'
>>> len(g2[0].get_edge_list())
90
>>> file.close()
>>> os.remove('testfile.gr')
>>> os.remove('testfile2.gr')
>>> os.remove('testfile.json')
>>> os.remove('testfile2.json')
>>> os.remove('testfile.csv')
>>> os.remove('testfile2.csv')
>>> os.remove('testfile.gdf')
>>> os.remove('testfile2.gdf')
>>> os.remove('testfile.gl')
>>> os.remove('testfile2.gl')
>>> os.remove('testfile.mtx')
>>> os.remove('testfile2.mtx')
>>> os.remove('testfile.tsv')
>>> os.remove('testfile2.tsv')
>>> os.remove('testfile.wel')
>>> os.remove('testfile2.wel')
>>> os.remove('testfile.lp')
>>> os.remove('testfile2.lp')
>>> os.remove('testfile.tgf')
>>> os.remove('testfile2.tgf')
>>> os.remove('testfile.dl')
>>> os.remove('testfile2.dl')
>>> os.remove('testfile.gml')
>>> os.remove('testfile2.gml')
>>> os.remove('testfile.gexf')
>>> os.remove('testfile2.gexf')
>>> os.remove('testfile.gv')
>>> os.remove('testfile2.gv')
>>> os.remove('logfile.log')
"""
