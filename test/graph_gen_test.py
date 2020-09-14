# -*- coding: utf-8 -*-
"""
>>> from pyrgg import *
>>> import random
>>> import os
>>> import json
>>> import yaml
>>> import pickle
>>> from scipy.io import mmread
>>> from networkx.readwrite.gml import read_gml
>>> from networkx.readwrite.gexf import read_gexf
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
>>> random.seed(20)
>>> dimacs_maker('testfile3',10,30,100,0,4,2,2,1,2)
170
>>> file=open('testfile3.gr','r')
>>> print(file.read())
c FILE                  :testfile3.gr
c No. of vertices       :100
c No. of edges          :170
c Max. weight           :30
c Min. weight           :10
c Min. edge             :0
c Max. edge             :4
p sp 100 170
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
a 18 100 28
a 19 45 17
a 19 79 11
a 19 68 16
a 20 23 15
a 20 11 13
a 20 38 10
a 21 87 22
a 21 59 26
a 23 16 24
a 24 43 10
a 24 10 28
a 24 96 13
a 24 12 20
a 25 83 12
a 25 85 19
a 28 29 26
a 29 90 10
a 29 21 10
a 30 18 19
a 30 55 18
a 30 14 22
a 30 13 16
a 31 26 17
a 33 73 22
a 33 19 30
a 35 63 10
a 35 23 16
a 35 82 19
a 36 39 16
a 36 48 29
a 36 40 14
a 39 8 22
a 39 48 19
a 40 60 13
a 40 9 28
a 40 61 16
a 42 9 27
a 42 80 20
a 42 92 10
a 42 23 18
a 43 78 13
a 43 1 11
a 44 96 16
a 45 52 29
a 45 11 28
a 45 47 19
a 46 7 30
a 46 18 29
a 46 49 27
a 47 51 18
a 47 1 24
a 47 12 28
a 48 41 17
a 48 100 16
a 49 58 20
a 49 49 16
a 50 46 14
a 50 98 21
a 50 3 13
a 50 64 17
a 51 96 10
a 51 91 21
a 51 72 14
a 53 56 26
a 54 32 22
a 54 90 27
a 54 91 19
a 55 78 30
a 55 92 19
a 56 98 12
a 56 84 25
a 57 96 14
a 57 61 17
a 58 84 27
a 58 20 30
a 58 99 27
a 60 83 11
a 60 68 16
a 61 28 27
a 62 62 30
a 62 79 12
a 62 26 20
a 62 36 20
a 64 34 18
a 66 66 11
a 67 6 25
a 67 94 26
a 67 97 13
a 67 86 14
a 68 65 27
a 68 54 15
a 69 57 26
a 69 62 14
a 69 26 16
a 70 16 16
a 70 52 24
a 72 82 27
a 72 95 16
a 73 27 26
a 73 37 23
a 74 69 17
a 74 98 15
a 74 74 28
a 75 38 14
a 75 2 20
a 76 38 26
a 76 95 14
a 76 9 15
a 77 65 26
a 77 5 13
a 77 75 12
a 77 71 16
a 78 88 24
a 78 57 23
a 80 66 29
a 81 81 19
a 81 33 18
a 82 16 13
a 83 89 27
a 83 76 24
a 84 31 27
a 84 95 15
a 85 8 24
a 85 12 26
a 85 38 10
a 86 99 21
a 86 34 19
a 87 52 30
a 87 87 12
a 87 2 11
a 88 95 15
a 88 31 30
a 88 59 23
a 92 71 27
a 93 12 19
a 93 98 24
a 93 90 26
a 94 14 24
a 94 25 14
a 99 31 19
>>> dimacs_maker('testfile', 0, 200, 10, 0,0,1)
Traceback (most recent call last):
        ...
TypeError: dimacs_maker() missing 1 required positional argument: 'sign'
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
TypeError: json_maker() missing 1 required positional argument: 'sign'
>>> json_to_pickle('testfile3')
>>> testfile_3_p=pickle.load( open( 'testfile3.p', 'rb' ) )
>>> testfile_3_p['graph']['edges'][1]['source']
'3'
>>> testfile_3_p['graph']['edges'][1]['target']
'74'
>>> testfile_3_p['graph']['edges'][1]['weight']
'15'
>>> random.seed(20)
>>> json_maker('testfile3',10,30,100,0,4,2,2,1,2)
170
>>> random.seed(2)
>>> csv_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
6
>>> file=open('testfile.csv','r')
>>> print(file.read())
4,3,-64
5,4,148
5,3,-163
6,9,-139
7,9,-9
10,6,-108
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
>>> gl_maker('testfile', 0, 200, 10, 1, 2, 0, 1,1,1)
10
>>> file=open('testfile.gl','r')
>>> print(file.read())
1 2:92
2 5:-155
3 10:148
4 7:-185
5 9:-128
6 1:93 9:-97
7 3:60
8 4:-44
9
10 10:114
>>> random.seed(2)
>>> mtx_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
6
>>> g = mmread("testfile.mtx")
>>> print(g)
  (3, 2)	-64.0
  (4, 3)	148.0
  (4, 2)	-163.0
  (5, 8)	-139.0
  (6, 8)	-9.0
  (9, 5)	-108.0
>>> random.seed(2)
>>> tsv_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
6
>>> file=open('testfile.tsv','r')
>>> print(file.read())
4	3	-64
5	4	148
5	3	-163
6	9	-139
7	9	-9
10	6	-108
<BLANKLINE>
>>> random.seed(4)
>>> gl_maker('testfile2',0,50,30,2,4,0,1,1,1)
60
>>> file=open('testfile2.gl','r')
>>> print(file.read())
1 10:46 14:-9
2 3:25 19:-48
3 8:-17 26:6
4 7:41 27:-17 8:19
5 21:-5 29:-42 13:11
6 16:-5 28:0
7 19:-48 17:26 14:-27
8 6:19 10:5
9 15:-33 19:-44
10 5:4 15:40
11 15:-11 12:-47 21:-40 20:20
12 27:45 28:7
13 30:18 15:2 12:18
14 22:-1 30:-39
15
16 21:28 17:21
17 1:-2 16:23
18 20:28 4:3 2:38
19 21:34
20 2:33 30:-41
21
22 9:-26 18:14 27:-13
23 3:-16 23:36 26:31
24 29:-41 26:41 24:-4
25 25:49 29:10 28:-36
26 30:13
27 1:-7
28 28:-14
29 9:23
30
>>> random.seed(4)
>>> csv_maker('testfile2',0,50,30,0,4,0,1,1,1)
40
>>> random.seed(4)
>>> gdf_maker('testfile2',0,50,30,0,4,0,1,1,1)
40
>>> random.seed(4)
>>> mtx_maker('testfile2',0,50,30,0,4,0,1,1,1)
40
>>> random.seed(4)
>>> tsv_maker('testfile2',0,50,30,0,4,0,1,1,1)
40
>>> g = mmread("testfile2.mtx")
>>> print(g)
  (0, 9)	46.0
  (1, 15)	5.0
  (1, 2)	25.0
  (1, 19)	-48.0
  (3, 16)	-17.0
  (4, 26)	16.0
  (5, 29)	41.0
  (6, 25)	-12.0
  (6, 5)	-18.0
  (7, 2)	-42.0
  (7, 13)	11.0
  (8, 15)	-5.0
  (9, 26)	0.0
  (9, 9)	-48.0
  (9, 17)	26.0
  (10, 19)	-27.0
  (10, 14)	14.0
  (10, 9)	-2.0
  (13, 20)	-33.0
  (13, 17)	-44.0
  (13, 10)	43.0
  (14, 2)	-12.0
  (15, 8)	22.0
  (15, 14)	-40.0
  (16, 6)	-6.0
  (16, 27)	45.0
  (16, 8)	-48.0
  (17, 19)	7.0
  (17, 5)	-29.0
  (20, 22)	18.0
  (20, 24)	-1.0
  (21, 9)	-9.0
  (21, 25)	-39.0
  (23, 19)	28.0
  (23, 9)	16.0
  (24, 5)	-36.0
  (24, 0)	-2.0
  (24, 7)	-50.0
  (25, 9)	28.0
  (25, 6)	-13.0
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
>>> random.seed(20)
>>> gl_maker('testfile3',10,30,100,3,4,2,1,1,1)
207
>>> file=open('testfile3.gl','r')
>>> print(file.read())
1 34:30 13:20 76:15
2 53:23 10:13 18:20
3 75:24 53:16 26:20 84:20
4 55:12 82:26 64:22 11:16
5 5:16 14:12 27:18
6 40:18 21:29 16:10 37:17
7 74:17 8:10 85:29
8 36:14 90:30 44:29
9 20:30 37:27 58:15 23:22
10 89:14 75:23 45:17
11 78:11 67:16 56:15
12 16:19 1:30 44:22
13 68:11 87:15 16:24
14 2:12 75:13 45:18
15 85:19 86:11 26:17
16 21:10
17 40:14 55:18 52:13
18 31:16 29:13 41:14
19 84:12 59:25 25:16 87:19
20 39:16 49:29 41:14
21 37:11 52:21
22 51:24 77:25 30:10 95:26
23 97:27 80:20 93:10
24 36:19 79:13 7:16
25 80:22 90:29 76:21
26 57:11 85:14
27 72:22 51:18 61:12
28 41:17 39:24 47:22 28:29
29 45:14 12:21 66:17
30 38:10 90:21 47:26
31 31:23 70:24 34:22
32 89:27 91:19 65:29 85:19
33 84:25 35:21 97:14
34 96:17 63:14
35 42:30 73:14 84:27
36 96:18 83:11
37 48:22
38 70:26 92:19 61:30
39 17:18 76:12
40 44:18 87:20
41 44:12
42 66:11 62:25 52:26
43 93:19 66:27 55:15
44
45 88:26
46 24:16 28:19 63:22 66:12
47 82:27 15:16
48 94:19 58:25 50:26
49 96:15 72:28 54:14
50 95:14 67:12 80:26
51 56:28 73:16
52 57:23
53 92:15 95:29
54 33:18 31:13 75:27
55 56:20
56 70:15
57 58:12 78:22
58 87:21
59 97:15 86:12 100:24
60 80:16 73:27 63:12 65:26
61 43:13 28:16
62 72:30 86:22 95:18
63 83:29
64 70:26 73:25 76:16
65 83:14 69:21
66
67 96:10 93:10
68 93:25 72:29 68:10
69 89:26 77:12 90:10
70
71 71:10 99:10 79:30
72
73
74 100:12 68:25 99:24
75
76
77 82:16 81:28
78 81:29 91:13
79 98:28 97:13
80
81 31:16 82:24
82
83 86:27
84
85
86
87
88 28:28 98:18 99:10
89 92:27
90
91 28:17 99:24
92 98:21
93
94 28:22 98:16 68:26
95
96
97
98
99
100 100:26 68:26
>>> random.seed(20)
>>> csv_maker('testfile3',10,30,100,0,4,2,1,1,1)
167
>>> random.seed(20)
>>> gdf_maker('testfile3',10,30,100,0,4,2,1,1,1)
167
>>> random.seed(20)
>>> mtx_maker('testfile3',10,30,100,0,4,2,1,1,1)
167
>>> random.seed(20)
>>> tsv_maker('testfile3',10,30,100,0,4,2,1,1,1)
167
>>> g = mmread("testfile3.mtx")
>>> print(g)
  (0, 33)	30.0
  (2, 73)	15.0
  (2, 3)	23.0
  (3, 9)	13.0
  (3, 17)	20.0
  (3, 62)	28.0
  (4, 52)	16.0
  (4, 25)	20.0
  (4, 82)	20.0
  (5, 54)	12.0
  (5, 81)	26.0
  (6, 51)	12.0
  (6, 26)	28.0
  (6, 32)	11.0
  (7, 12)	12.0
  (8, 32)	19.0
  (9, 88)	18.0
  (9, 20)	29.0
  (12, 90)	17.0
  (12, 28)	28.0
  (13, 7)	10.0
  (14, 38)	18.0
  (14, 17)	30.0
  (14, 44)	29.0
  (14, 95)	24.0
  :	:
  (78, 83)	24.0
  (79, 52)	11.0
  (79, 92)	15.0
  (79, 22)	13.0
  (80, 76)	28.0
  (81, 30)	13.0
  (83, 88)	27.0
  (85, 72)	15.0
  (85, 68)	11.0
  (86, 11)	26.0
  (86, 50)	18.0
  (86, 75)	22.0
  (91, 94)	15.0
  (91, 98)	24.0
  (91, 56)	11.0
  (93, 96)	16.0
  (93, 49)	27.0
  (93, 60)	12.0
  (94, 68)	19.0
  (94, 13)	24.0
  (95, 19)	29.0
  (98, 23)	16.0
  (98, 24)	17.0
  (99, 7)	17.0
  (99, 68)	30.0
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
>>> random.seed(20)
>>> csv_maker('testfile3',10,30,100,0,4,2,2,1,2)
170
>>> random.seed(20)
>>> gdf_maker('testfile3',10,30,100,0,4,2,2,1,2)
170
>>> random.seed(20)
>>> mtx_maker('testfile3',10,30,100,0,4,2,2,1,2)
170
>>> random.seed(20)
>>> tsv_maker('testfile3',10,30,100,0,4,2,2,1,2)
170
>>> gl_maker('testfile', 0, 200, 10, 0,0,1)
Traceback (most recent call last):
        ...
TypeError: gl_maker() missing 3 required positional arguments: 'direct', 'self_loop', and 'multigraph'
>>> csv_maker('testfile', 0, 200, 10, 0,0,1)
Traceback (most recent call last):
        ...
TypeError: csv_maker() missing 1 required positional argument: 'sign'
>>> gdf_maker('testfile', 0, 200, 10, 0,0,1)
Traceback (most recent call last):
        ...
TypeError: gdf_maker() missing 3 required positional arguments: 'direct', 'self_loop', and 'multigraph'
>>> mtx_maker('testfile', 0, 200, 10, 0,0,1)
Traceback (most recent call last):
        ...
TypeError: csv_maker() missing 1 required positional argument: 'sign'
>>> tsv_maker('testfile', 0, 200, 10, 0,0,1)
Traceback (most recent call last):
        ...
TypeError: tsv_maker() missing 2 required positional arguments: 'direct' and 'self_loop'
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
>>> random.seed(20)
>>> wel_maker('testfile3',10,30,100,0,4,2,2,1,2)
170
>>> wel_maker('testfile', 0, 200, 10, 0,0,1)
Traceback (most recent call last):
        ...
TypeError: wel_maker() missing 1 required positional argument: 'sign'
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
>>> random.seed(2)
>>> tgf_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
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
>>> random.seed(4)
>>> dimacs_maker('testfile4',0,50,30,0,4,0,1,2,1)
54
>>> file=open('testfile4.gr','r')
>>> print(file.read())
c FILE                  :testfile4.gr
c No. of vertices       :30
c No. of edges          :54
c Max. weight           :50
c Min. weight           :0
c Min. edge             :0
c Max. edge             :4
p sp 30 54
a 1 11 46
a 2 17 5
a 2 4 25
a 2 21 -48
a 4 18 -17
a 5 28 16
a 6 1 -17
a 7 6 -18
a 8 3 -42
a 8 15 11
a 9 17 -5
a 10 28 0
a 10 11 -48
a 10 19 26
a 10 16 -27
a 11 6 19
a 11 30 5
a 13 22 -33
a 13 19 -44
a 13 5 4
a 14 7 -17
a 14 6 -27
a 14 27 -40
a 15 7 -6
a 15 29 45
a 15 9 -48
a 16 21 7
a 16 12 -1
a 16 2 -44
a 18 25 -1
a 18 13 49
a 19 29 18
a 19 21 28
a 20 5 -24
a 20 22 21
a 21 1 -2
a 22 29 -18
a 22 4 -13
a 23 7 3
a 23 3 38
a 23 26 38
a 25 20 20
a 25 5 -49
a 25 17 30
a 26 8 -26
a 27 9 -28
a 27 24 -13
a 27 8 2
a 28 9 33
a 28 17 -9
a 29 12 36
a 30 14 27
a 30 26 21
a 30 12 -41
<BLANKLINE>
>>> random.seed(2)
>>> gml_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
6
>>> gml1 = read_gml("testfile.gml")
>>> type(gml1)
<class 'networkx.classes.digraph.DiGraph'>
>>> random.seed(4)
>>> gml_maker('testfile2',0,50,30,0,4,0,1,1,2)
43
>>> gml2 = read_gml("testfile2.gml")
>>> type(gml2)
<class 'networkx.classes.multidigraph.MultiDiGraph'>
>>> random.seed(20)
>>> gml_maker('testfile3',0,50,30,0,4,0,2,1,2)
40
>>> gml3 = read_gml("testfile3.gml")
>>> type(gml3)
<class 'networkx.classes.multigraph.MultiGraph'>
>>> random.seed(120)
>>> gml_maker('testfile4',0,50,30,0,4,0,2,1,1)
40
>>> gml4 = read_gml("testfile4.gml")
>>> type(gml4)
<class 'networkx.classes.graph.Graph'>
>>> random.seed(2)
>>> gexf_maker('testfile', 0, 200, 10, 0, 2, 0, 1,1,1)
6
>>> gexf1 = read_gexf("testfile.gexf")
>>> type(gexf1)
<class 'networkx.classes.digraph.DiGraph'>
>>> random.seed(8)
>>> gexf_maker('testfile2',0,50,30,0,4,0,1,1,2)
41
>>> gexf2 = read_gexf("testfile2.gexf")
>>> type(gexf2)
<class 'networkx.classes.multidigraph.MultiDiGraph'>
>>> random.seed(20)
>>> gexf_maker('testfile3',0,50,30,0,4,0,2,1,2)
40
>>> gexf3 = read_gexf("testfile3.gexf")
>>> type(gexf3)
<class 'networkx.classes.multigraph.MultiGraph'>
>>> random.seed(120)
>>> gexf_maker('testfile4',0,50,30,0,4,0,2,1,1)
40
>>> gexf4 = read_gexf("testfile4.gexf")
>>> type(gexf4)
<class 'networkx.classes.graph.Graph'>
>>> random.seed(120)
>>> gexf_maker('testfile5',0,50.2,30,0,4,0,2,1,1)
50
>>> gexf5 = read_gexf("testfile5.gexf")
>>> type(gexf5)
<class 'networkx.classes.graph.Graph'>
>>> random.seed(2)
>>> csv_maker('testfile4', 0.0, 200.22, 10, 0, 2, 0, 1,1,1)
6
>>> file = open("testfile4.csv")
>>> print(file.read())
4,3,-50.37
6,1,200.16
6,8,-108.96
7,9,-180.44
9,8,-181.75
10,3,47.28
<BLANKLINE>
>>> random.seed(2)
>>> csv_maker('testfile4', 0.0, 200.222, 10, 0, 2, 0, 1,1,1)
6
>>> file = open("testfile4.csv")
>>> print(file.read())
4,3,-50.373
6,1,200.166
6,8,-108.956
7,9,-180.442
9,8,-181.752
10,3,47.277
<BLANKLINE>
>>> file.close()
>>> os.remove('testfile.csv')
>>> os.remove('testfile.gml')
>>> os.remove('testfile.gexf')
>>> os.remove('testfile2.gexf')
>>> os.remove('testfile3.gexf')
>>> os.remove('testfile4.gexf')
>>> os.remove('testfile5.gexf')
>>> os.remove('testfile.gdf')
>>> os.remove('testfile.tsv')
>>> os.remove('testfile.mtx')
>>> os.remove('testfile.dl')
>>> os.remove('testfile.gl')
>>> os.remove('testfile.gr')
>>> os.remove('testfile.json')
>>> os.remove('testfile.lp')
>>> os.remove('testfile.p')
>>> os.remove('testfile.tgf')
>>> os.remove('testfile.wel')
>>> os.remove('testfile.yaml')
>>> os.remove('testfile2.csv')
>>> os.remove('testfile2.gml')
>>> os.remove('testfile2.gdf')
>>> os.remove('testfile2.mtx')
>>> os.remove('testfile2.tsv')
>>> os.remove('testfile2.dl')
>>> os.remove('testfile2.gl')
>>> os.remove('testfile2.gr')
>>> os.remove('testfile2.json')
>>> os.remove('testfile2.lp')
>>> os.remove('testfile2.p')
>>> os.remove('testfile2.tgf')
>>> os.remove('testfile2.wel')
>>> os.remove('testfile2.yaml')
>>> os.remove('testfile3.csv')
>>> os.remove('testfile4.csv')
>>> os.remove('testfile3.gml')
>>> os.remove('testfile3.gdf')
>>> os.remove('testfile3.mtx')
>>> os.remove('testfile3.tsv')
>>> os.remove('testfile3.gl')
>>> os.remove('testfile3.gr')
>>> os.remove('testfile4.gr')
>>> os.remove('testfile4.gml')
>>> os.remove('testfile3.json')
>>> os.remove('testfile3.p')
>>> os.remove('testfile3.wel')
>>> os.remove('testfile3.yaml')
>>> os.remove('logfile.log')

"""
