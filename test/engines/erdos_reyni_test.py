# -*- coding: utf-8 -*-
"""
>>> from pyrgg.functions import *
>>> from pyrgg.graph_gen import *
>>> import pyrgg.params
>>> import random
>>> import os
>>> import json
>>> import pyrgg.engines.erdos_reyni as engine
>>> os.environ["PYRGG_TEST_MODE"] = "1"
>>> ######################################
>>> ## ========= logger function =========
>>> ######################################
>>> with open('logfile.log','a') as file:
...     engine.logger(file,'test','2min',{'vertices':100,'edge_number':50,'direct':0,'engine':3,'output_format':1})
>>> file = open('logfile.log','r')
>>> print("\\n".join(file.read().splitlines()[1:-1]))
Filename : test
Vertices : 100
Total Edges : 50
Directed : False
Engine : 3 (er)
Elapsed Time : 2min
>>> class StrError:
...     def __init__(self):
...         pass
...     def __str__(self):
...         raise ValueError
>>> str_error_object = StrError()
>>> with open('logfile.log','a') as file:
...     engine.logger(file,'test','2min',{'vertices':str_error_object,'edge_number':50,'direct':0,'engine':3,'output_format':1})
[Error] Logger failed!
>>> ##########################################
>>> ## ========= edge_gen function =========
>>> ##########################################
>>> random.seed(2)
>>> edge_dic, weight_dic, edge_number = engine.edge_gen(20, 10, False)
>>> edge_dic == {1: [13], 2: [9], 3: [4], 4: [], 5: [], 6: [], 7: [16], 8: [], 9: [10, 18], 10: [12, 17], 11: [13], 12: [], 13: [], 14: [], 15: [], 16: [], 17: [], 18: [20], 19: [], 20: []}
True
>>> edge_number == 10
True
>>> random.seed(11)
>>> edge_dic, weight_dic, edge_number = engine.edge_gen(20, 100, True)
>>> edge_dic == {1: [8, 9, 14, 15, 18, 19], 2: [4, 11, 13, 15, 16, 17], 3: [1, 13, 14, 19], 4: [7, 9, 14, 15, 16, 19], 5: [4, 10, 15, 16, 18, 19], 6: [3, 4, 9, 12, 19], 7: [5, 10, 13, 15, 16, 17, 20], 8: [1, 18, 19, 20], 9: [3, 6, 11, 13, 16, 18, 20], 10: [1, 3, 4, 13, 17], 11: [6, 7, 8, 17, 18], 12: [3, 5, 8, 17], 13: [5, 15], 14: [7, 12, 17, 19], 15: [1, 4, 7, 9, 14, 19, 20], 16: [3, 7, 8, 9, 12, 20], 17: [3, 5, 8, 14, 16], 18: [2, 9, 10, 11, 14], 19: [4, 9, 12], 20: [1, 12, 13]}
True
>>> edge_number == 100
True
>>> engine.edge_gen(0)
Traceback (most recent call last):
        ...
TypeError: edge_gen() missing 2 required positional arguments: 'm' and 'direct'
>>> #########################################
>>> ## ========= gen_using function =========
>>> #########################################
>>> #################### dimacs_maker ####################
>>> random.seed(2)
>>> engine.gen_using(dimacs_maker, 'testfile', {'vertices':10, 'edge_number':5, 'direct':0})
5
>>> file=open('testfile.gr','r')
>>> print(file.read())
c FILE                  :testfile.gr
c No. of vertices       :10
c No. of edges          :5
c Max. weight           :1
c Min. weight           :1
p sp 10 5
a 1 2 1
a 1 10 1
a 3 6 1
a 3 7 1
a 6 10 1
<BLANKLINE>
>>> random.seed(4)
>>> engine.gen_using(dimacs_maker, 'testfile2', {'vertices':10, 'edge_number':8, 'direct':1})
8
>>> file=open('testfile2.gr','r')
>>> print(file.read())
c FILE                  :testfile2.gr
c No. of vertices       :10
c No. of edges          :8
c Max. weight           :1
c Min. weight           :1
p sp 10 8
a 1 10 1
a 2 5 1
a 3 6 1
a 4 10 1
a 6 5 1
a 8 3 1
a 9 8 1
a 10 2 1
<BLANKLINE>
>>> #################### json_maker ####################
>>> random.seed(2)
>>> engine.gen_using(json_maker, 'testfile', {'vertices':10, 'edge_number':5, 'direct':0})
5
>>> file=open('testfile.json','r')
>>> testfile_1=json.load(file)
>>> testfile_1['graph']['nodes'][1]
{'id': 2}
>>> testfile_1['graph']['edges'][1]['source']
1
>>> testfile_1['graph']['edges'][1]['target']
10
>>> random.seed(4)
>>> engine.gen_using(json_maker, 'testfile2', {'vertices':10, 'edge_number':8, 'direct':1})
8
>>> file=open('testfile2.json','r')
>>> testfile_2=json.load(file)
>>> testfile_2['graph']['nodes'][1]
{'id': 2}
>>> testfile_2['graph']['edges'][1]['source']
2
>>> testfile_2['graph']['edges'][1]['target']
5
>>> #################### csv_maker ####################
>>> random.seed(2)
>>> engine.gen_using(csv_maker, 'testfile', {'vertices':10, 'edge_number':5, 'direct':0})
5
>>> file=open('testfile.csv','r')
>>> print(file.read())
1,2,1
1,10,1
3,6,1
3,7,1
6,10,1
<BLANKLINE>
>>> random.seed(4)
>>> engine.gen_using(csv_maker, 'testfile2', {'vertices':10, 'edge_number':8, 'direct':1})
8
>>> file=open('testfile2.csv','r')
>>> print(file.read())
1,10,1
2,5,1
3,6,1
4,10,1
6,5,1
8,3,1
9,8,1
10,2,1
<BLANKLINE>
>>> #################### gdf_maker ####################
>>> random.seed(2)
>>> engine.gen_using(gdf_maker, 'testfile', {'vertices':10, 'edge_number':5, 'direct':0})
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
1,2,1
1,10,1
3,6,1
3,7,1
6,10,1
<BLANKLINE>
>>> random.seed(4)
>>> engine.gen_using(gdf_maker, 'testfile2', {'vertices':10, 'edge_number':8, 'direct':1})
8
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
1,10,1
2,5,1
3,6,1
4,10,1
6,5,1
8,3,1
9,8,1
10,2,1
<BLANKLINE>
>>> #################### gl_maker ####################
>>> random.seed(2)
>>> engine.gen_using(gl_maker, 'testfile', {'vertices':10, 'edge_number':5, 'direct':0})
5
>>> file=open('testfile.gl','r')
>>> print(file.read())
1 2:1 10:1
3 6:1 7:1
6 10:1
>>> random.seed(4)
>>> engine.gen_using(gl_maker, 'testfile2', {'vertices':10, 'edge_number':8, 'direct':1})
8
>>> file=open('testfile2.gl','r')
>>> print(file.read())
1 10:1
2 5:1
3 6:1
4 10:1
6 5:1
8 3:1
9 8:1
10 2:1
>>> #################### mtx_maker ####################
>>> from scipy.io import mmread
>>> random.seed(2)
>>> engine.gen_using(mtx_maker, 'testfile', {'vertices':10, 'edge_number':5, 'direct':0})
5
>>> g = mmread("testfile.mtx")
>>> print(g.data.tolist())
[1.0, 1.0, 1.0, 1.0, 1.0]
>>> random.seed(4)
>>> engine.gen_using(mtx_maker, 'testfile2', {'vertices':10, 'edge_number':8, 'direct':1})
8
>>> g = mmread("testfile2.mtx")
>>> print(g.data.tolist())
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
>>> #################### tsv_maker ####################
>>> random.seed(2)
>>> engine.gen_using(tsv_maker, 'testfile', {'vertices':10, 'edge_number':5, 'direct':0})
5
>>> file=open('testfile.tsv','r')
>>> print(file.read())
1	2	1
1	10	1
3	6	1
3	7	1
6	10	1
<BLANKLINE>
>>> random.seed(4)
>>> engine.gen_using(tsv_maker, 'testfile2', {'vertices':10, 'edge_number':8, 'direct':1})
8
>>> file=open('testfile2.tsv','r')
>>> print(file.read())
1	10	1
2	5	1
3	6	1
4	10	1
6	5	1
8	3	1
9	8	1
10	2	1
<BLANKLINE>
>>> #################### wel_maker ####################
>>> random.seed(2)
>>> engine.gen_using(wel_maker, 'testfile', {'vertices':10, 'edge_number':5, 'direct':0})
5
>>> file=open('testfile.wel','r')
>>> print(file.read())
1 2 1
1 10 1
3 6 1
3 7 1
6 10 1
<BLANKLINE>
>>> random.seed(4)
>>> engine.gen_using(wel_maker, 'testfile2', {'vertices':10, 'edge_number':8, 'direct':1})
8
>>> file=open('testfile2.wel','r')
>>> print(file.read())
1 10 1
2 5 1
3 6 1
4 10 1
6 5 1
8 3 1
9 8 1
10 2 1
<BLANKLINE>
>>> #################### lp_maker ####################
>>> random.seed(2)
>>> engine.gen_using(lp_maker, 'testfile', {'vertices':10, 'edge_number':5, 'direct':0})
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
edge(1,2,1).
edge(1,10,1).
edge(3,6,1).
edge(3,7,1).
edge(6,10,1).
<BLANKLINE>
>>> random.seed(4)
>>> engine.gen_using(lp_maker, 'testfile2', {'vertices':10, 'edge_number':8, 'direct':1})
8
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
edge(1,10,1).
edge(2,5,1).
edge(3,6,1).
edge(4,10,1).
edge(6,5,1).
edge(8,3,1).
edge(9,8,1).
edge(10,2,1).
<BLANKLINE>
>>> #################### tgf_maker ####################
>>> random.seed(2)
>>> engine.gen_using(tgf_maker, 'testfile', {'vertices':10, 'edge_number':5, 'direct':0})
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
1 2 1
1 10 1
3 6 1
3 7 1
6 10 1
<BLANKLINE>
>>> random.seed(4)
>>> engine.gen_using(tgf_maker, 'testfile2', {'vertices':10, 'edge_number':8, 'direct':1})
8
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
1 10 1
2 5 1
3 6 1
4 10 1
6 5 1
8 3 1
9 8 1
10 2 1
<BLANKLINE>
>>> #################### dl_maker ####################
>>> random.seed(2)
>>> engine.gen_using(dl_maker, 'testfile', {'vertices':10, 'edge_number':5, 'direct':0})
5
>>> file=open('testfile.dl','r')
>>> print(file.read())
dl
format=edgelist1
n=10
data:
1 2 1
1 10 1
3 6 1
3 7 1
6 10 1
<BLANKLINE>
>>> random.seed(4)
>>> engine.gen_using(dl_maker, 'testfile2', {'vertices':10, 'edge_number':8, 'direct':1})
8
>>> file=open('testfile2.dl','r')
>>> print(file.read())
dl
format=edgelist1
n=10
data:
1 10 1
2 5 1
3 6 1
4 10 1
6 5 1
8 3 1
9 8 1
10 2 1
<BLANKLINE>
>>> #################### gml_maker ####################
>>> from networkx.readwrite.gml import read_gml
>>> random.seed(2)
>>> engine.gen_using(gml_maker, 'testfile', {'vertices':10, 'edge_number':5, 'direct':0})
5
>>> gml1 = read_gml("testfile.gml")
>>> type(gml1)
<class 'networkx.classes.graph.Graph'>
>>> random.seed(4)
>>> engine.gen_using(gml_maker, 'testfile2', {'vertices':10, 'edge_number':8, 'direct':1})
8
>>> gml2 = read_gml("testfile2.gml")
>>> type(gml2)
<class 'networkx.classes.digraph.DiGraph'>
>>> #################### gexf_maker ####################
>>> from networkx.readwrite.gexf import read_gexf
>>> random.seed(2)
>>> engine.gen_using(gexf_maker, 'testfile', {'vertices':10, 'edge_number':5, 'direct':0})
5
>>> gexf1 = read_gexf("testfile.gexf")
>>> type(gexf1)
<class 'networkx.classes.graph.Graph'>
>>> random.seed(4)
>>> engine.gen_using(gexf_maker, 'testfile2', {'vertices':10, 'edge_number':8, 'direct':1})
8
>>> gexf2 = read_gexf("testfile2.gexf")
>>> type(gexf2)
<class 'networkx.classes.digraph.DiGraph'>
>>> #################### dot_maker ####################
>>> import pydot
>>> random.seed(2)
>>> engine.gen_using(dot_maker, 'testfile', {'vertices':10, 'edge_number':5, 'direct':0})
5
>>> file=open('testfile.gv','r')
>>> g1 = pydot.graph_from_dot_data(file.read())
>>> g1[0].get_type()
'graph'
>>> len(g1[0].get_edge_list())
5
>>> random.seed(4)
>>> engine.gen_using(dot_maker, 'testfile2', {'vertices':10, 'edge_number':8, 'direct':1})
8
>>> file=open('testfile2.gv','r')
>>> g2 = pydot.graph_from_dot_data(file.read())
>>> g2[0].get_type()
'digraph'
>>> len(g2[0].get_edge_list())
8
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
