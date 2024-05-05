# -*- coding: utf-8 -*-
"""
>>> from pyrgg.functions import *
>>> from pyrgg.graph_gen import *
>>> import pyrgg.params
>>> import random
>>> import os
>>> import json
>>> import pyrgg.engines.erdos_reyni_gilbert as engine
>>> os.environ["PYRGG_TEST_MODE"] = "1"
>>> ######################################
>>> ## ========= logger function =========
>>> ######################################
>>> with open('logfile.log','a') as file:
...     engine.logger(file,'test','2min',{'vertices':100,'edge_number':50,'direct':0,'engine':1,'probability':0.5,'output_format':1})
>>> file = open('logfile.log','r')
>>> print("\\n".join(file.read().splitlines()[1:-1]))
Filename : test
Probability : 0.5
Vertices : 100
Total Edges : 50
Directed : False
Engine : 1 (pyrgg)
Elapsed Time : 2min
>>> class StrError:
...     def __init__(self):
...         pass
...     def __str__(self):
...         raise ValueError
>>> str_error_object = StrError()
>>> with open('logfile.log','a') as file:
...     engine.logger(file,'test','2min',{'vertices':str_error_object,'edge_number':50,'direct':0,'engine':1,'probability':0.5,'output_format':1})
[Error] Logger failed!
>>> ##########################################
>>> ## ========= edge_gen function =========
>>> ##########################################
>>> random.seed(2)
>>> edge_dic, weight_dic, edge_number = engine.edge_gen(20, 0.5, False)
>>> edge_dic == {1: [4, 5, 9, 13, 14, 15, 20], 2: [3, 4, 5, 6, 7, 8, 12, 13, 14, 15, 19], 3: [9, 12, 15, 17], 4: [5, 8, 12, 13, 14, 16, 18, 20], 5: [12, 13, 17], 6: [7, 9, 11, 12, 14, 17, 18, 20],7: [9, 10, 11, 13, 15, 17, 18, 20], 8: [9, 11, 12, 14, 15, 16, 19, 20], 9: [10, 11, 18, 19], 10: [11, 12, 13, 15, 17, 19], 11: [12, 14, 15, 17, 18, 19, 20], 12: [13, 19, 20], 13: [14, 19, 20], 14: [16, 17, 18, 19], 15: [16, 17, 18, 19, 20], 16: [18, 19], 17: [18], 18: [20], 19: [], 20: []}
True
>>> edge_number == 93
True
>>> random.seed(11)
>>> edge_dic, weight_dic, edge_number = engine.edge_gen(20, 0.1, True)
>>> edge_dic == {1: [12, 14, 17], 2: [4, 6, 9], 3: [7, 14, 20], 4: [5, 12], 5: [], 6: [1, 2], 7: [8, 18], 8: [6, 10], 9: [2, 3, 7, 14], 10: [15], 11: [5, 7, 17], 12: [], 13: [16, 17, 19], 14: [4, 7, 11], 15: [3, 17], 16: [], 17: [7, 12, 14], 18: [9], 19: [12], 20: [1, 19]}
True
>>> edge_number == 40
True
>>> engine.edge_gen(0)
Traceback (most recent call last):
        ...
TypeError: edge_gen() missing 2 required positional arguments: 'p' and 'direct'
>>> #########################################
>>> ## ========= gen_using function =========
>>> #########################################
>>> #################### dimacs_maker ####################
>>> random.seed(2)
>>> engine.gen_using(dimacs_maker, 'testfile', {'vertices':10, 'probability':0.1, 'direct':0})
5
>>> file=open('testfile.gr','r')
>>> print(file.read())
c FILE                  :testfile.gr
c No. of vertices       :10
c No. of edges          :5
c Max. weight           :1
c Min. weight           :1
c Min. edge             :5
c Max. edge             :5
p sp 10 5
a 1 4 1
a 1 5 1
a 3 7 1
a 3 8 1
a 4 10 1
<BLANKLINE>
>>> random.seed(4)
>>> engine.gen_using(dimacs_maker, 'testfile2', {'vertices':10, 'probability':0.1, 'direct':1})
8
>>> file=open('testfile2.gr','r')
>>> print(file.read())
c FILE                  :testfile2.gr
c No. of vertices       :10
c No. of edges          :8
c Max. weight           :1
c Min. weight           :1
c Min. edge             :8
c Max. edge             :8
p sp 10 8
a 1 6 1
a 3 9 1
a 4 6 1
a 6 3 1
a 6 4 1
a 8 4 1
a 9 3 1
a 9 10 1
<BLANKLINE>
>>> #################### json_maker ####################
>>> random.seed(2)
>>> engine.gen_using(json_maker, 'testfile', {'vertices':10, 'probability':0.1})
5
>>> file=open('testfile.json','r')
>>> testfile_1=json.load(file)
>>> testfile_1['graph']['nodes'][1]
{'id': 2}
>>> testfile_1['graph']['edges'][1]['source']
1
>>> testfile_1['graph']['edges'][1]['target']
5
>>> #################### csv_maker ####################
>>> random.seed(2)
>>> engine.gen_using(csv_maker, 'testfile', {'vertices':10, 'probability':0.1})
5
>>> file=open('testfile.csv','r')
>>> print(file.read())
1,4,1
1,5,1
3,7,1
3,8,1
4,10,1
<BLANKLINE>
>>> #################### gdf_maker ####################
>>> random.seed(2)
>>> engine.gen_using(gdf_maker, 'testfile', {'vertices':10, 'probability':0.1})
5
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
1,4,1
1,5,1
3,7,1
3,8,1
4,10,1
<BLANKLINE>
>>> #################### gl_maker ####################
>>> random.seed(2)
>>> engine.gen_using(gl_maker, 'testfile', {'vertices':10, 'probability':0.1})
5
>>> file=open('testfile.gl','r')
>>> print(file.read())
1 4:1 5:1
3 7:1 8:1
4 10:1
>>> #################### mtx_maker ####################
>>> from scipy.io import mmread
>>> random.seed(2)
>>> engine.gen_using(mtx_maker, 'testfile', {'vertices':10, 'probability':0.1})
5
>>> g = mmread("testfile.mtx")
>>> print(g)
  (0, 3)	1.0
  (0, 4)	1.0
  (2, 6)	1.0
  (2, 7)	1.0
  (3, 9)	1.0
>>> #################### tsv_maker ####################
>>> random.seed(2)
>>> engine.gen_using(tsv_maker, 'testfile', {'vertices':10, 'probability':0.1})
5
>>> file=open('testfile.tsv','r')
>>> print(file.read())
1	4	1
1	5	1
3	7	1
3	8	1
4	10	1
<BLANKLINE>
>>> #################### wel_maker ####################
>>> random.seed(2)
>>> engine.gen_using(wel_maker, 'testfile', {'vertices':10, 'probability':0.1})
5
>>> file=open('testfile.wel','r')
>>> print(file.read())
1 4 1
1 5 1
3 7 1
3 8 1
4 10 1
<BLANKLINE>
>>> #################### lp_maker ####################
>>> random.seed(2)
>>> engine.gen_using(lp_maker, 'testfile', {'vertices':10, 'probability':0.1})
5
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
edge(1,4,1).
edge(1,5,1).
edge(3,7,1).
edge(3,8,1).
edge(4,10,1).
<BLANKLINE>
>>> #################### tgf_maker ####################
>>> random.seed(2)
>>> engine.gen_using(tgf_maker, 'testfile', {'vertices':10, 'probability':0.1})
5
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
1 4 1
1 5 1
3 7 1
3 8 1
4 10 1
<BLANKLINE>
>>> #################### dl_maker ####################
>>> random.seed(2)
>>> engine.gen_using(dl_maker, 'testfile', {'vertices':10, 'probability':0.1})
5
>>> file=open('testfile.dl','r')
>>> print(file.read())
dl
format=edgelist1
n=10
data:
1 4 1
1 5 1
3 7 1
3 8 1
4 10 1
<BLANKLINE>
>>> #################### gml_maker ####################
>>> from networkx.readwrite.gml import read_gml
>>> random.seed(2)
>>> engine.gen_using(gml_maker, 'testfile', {'vertices':10, 'probability':0.1})
5
>>> gml1 = read_gml("testfile.gml")
>>> type(gml1)
<class 'networkx.classes.graph.Graph'>
>>> #################### gexf_maker ####################
>>> from networkx.readwrite.gexf import read_gexf
>>> random.seed(2)
>>> engine.gen_using(gexf_maker, 'testfile', {'vertices':10, 'probability':0.1})
5
>>> gexf1 = read_gexf("testfile.gexf")
>>> type(gexf1)
<class 'networkx.classes.graph.Graph'>
>>> #################### dot_maker ####################
>>> import pydot
>>> random.seed(2)
>>> engine.gen_using(dot_maker, 'testfile', {'vertices':10, 'probability':0.1})
5
>>> file=open('testfile.gv','r')
>>> g1 = pydot.graph_from_dot_data(file.read())
>>> g1[0].get_type()
'graph'
>>> len(g1[0].get_edge_list())
5
>>> file.close()
>>> os.remove('testfile.gr')
>>> os.remove('testfile.json')
>>> os.remove('testfile.csv')
>>> os.remove('testfile.gdf')
>>> os.remove('testfile.gl')
>>> os.remove('testfile.mtx')
>>> os.remove('testfile.tsv')
>>> os.remove('testfile.wel')
>>> os.remove('testfile.lp')
>>> os.remove('testfile.tgf')
>>> os.remove('testfile.dl')
>>> os.remove('testfile.gml')
>>> os.remove('testfile.gexf')
>>> os.remove('testfile.gv')
>>> os.remove('logfile.log')
"""
