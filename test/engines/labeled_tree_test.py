# -*- coding: utf-8 -*-
"""
>>> from pyrgg.functions import *
>>> from pyrgg.graph_gen import *
>>> import pyrgg.params
>>> import random
>>> import os
>>> import json
>>> import pyrgg.engines.labeled_tree as engine
>>> os.environ["PYRGG_TEST_MODE"] = "1"
>>> ######################################
>>> ## ========= logger function =========
>>> ######################################
>>> with open('logfile.log','a') as file:
...     engine.logger(file,'test','2min',{'vertices':100,'edge_number':99,'engine':8,'output_format':1})
>>> file = open('logfile.log','r')
>>> print("\\n".join(file.read().splitlines()[1:-1]))
Filename : test
Vertices : 100
Total Edges : 99
Engine : 8 (lt)
Elapsed Time : 2min
>>> class StrError:
...     def __init__(self):
...         pass
...     def __str__(self):
...         raise ValueError
>>> str_error_object = StrError()
>>> with open('logfile.log','a') as file:
...     engine.logger(file,'test','2min',{'vertices':str_error_object,'edge_number':99,'engine':8,'output_format':1})
[Error] Logger failed!
>>> ##########################################
>>> ## ========= generate_edges function =========
>>> ##########################################
>>> random.seed(2)
>>> edge_dict, weight_dict, edge_number = engine.generate_edges(20)
>>> edge_dict == {1: [2], 2: [16, 19], 3: [4, 5, 12], 4: [], 5: [], 6: [8, 14, 19], 7: [15, 20], 8: [], 9: [10, 20], 10: [11], 11: [], 12: [17, 18], 13: [14, 17], 14: [], 15: [], 16: [], 17: [], 18: [20], 19: [], 20: []}
True
>>> edge_number == 19
True
>>> random.seed(6)
>>> edge_dict, weight_dict, edge_number = engine.generate_edges(2)
>>> edge_dict == {1: [2], 2: []}
True
>>> edge_number == 1
True
>>> engine.generate_edges()
Traceback (most recent call last):
        ...
TypeError: generate_edges() missing 1 required positional argument: 'n'
>>> #########################################
>>> ## ========= generate_graph function =========
>>> #########################################
>>> #################### generate_dimacs_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_dimacs_file, 'testfile', {'vertices':10})
9
>>> file=open('testfile.gr','r')
>>> print(file.read())
c FILE                  :testfile.gr
c No. of vertices       :10
c No. of edges          :9
c Max. weight           :1
c Min. weight           :1
p sp 10 9
a 1 2 1
a 1 4 1
a 2 6 1
a 2 7 1
a 3 5 1
a 3 6 1
a 5 8 1
a 5 10 1
a 9 10 1
<BLANKLINE>
>>> #################### generate_json_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_json_file, 'testfile', {'vertices':10})
9
>>> file=open('testfile.json','r')
>>> testfile_1=json.load(file)
>>> testfile_1['graph']['nodes'][1]
{'id': 2}
>>> testfile_1['graph']['edges'][1]['source']
1
>>> testfile_1['graph']['edges'][1]['target']
4
>>> #################### generate_csv_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_csv_file, 'testfile', {'vertices':10})
9
>>> file=open('testfile.csv','r')
>>> print(file.read())
1,2,1
1,4,1
2,6,1
2,7,1
3,5,1
3,6,1
5,8,1
5,10,1
9,10,1
<BLANKLINE>
>>> #################### generate_gdf_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_gdf_file, 'testfile', {'vertices':10})
9
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
1,4,1
2,6,1
2,7,1
3,5,1
3,6,1
5,8,1
5,10,1
9,10,1
<BLANKLINE>
>>> #################### generate_gl_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_gl_file, 'testfile', {'vertices':10})
9
>>> file=open('testfile.gl','r')
>>> print(file.read())
1 2:1 4:1
2 6:1 7:1
3 5:1 6:1
5 8:1 10:1
9 10:1
<BLANKLINE>
>>> #################### generate_mtx_file ####################
>>> from scipy.io import mmread
>>> random.seed(2)
>>> engine.generate_graph(generate_mtx_file, 'testfile', {'vertices':10})
9
>>> g = mmread("testfile.mtx")
>>> print(g.data.tolist())
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
>>> #################### generate_tsv_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_tsv_file, 'testfile', {'vertices':10})
9
>>> file=open('testfile.tsv','r')
>>> print(file.read())
1	2	1
1	4	1
2	6	1
2	7	1
3	5	1
3	6	1
5	8	1
5	10	1
9	10	1
<BLANKLINE>
>>> #################### generate_wel_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_wel_file, 'testfile', {'vertices':10})
9
>>> file=open('testfile.wel','r')
>>> print(file.read())
1 2 1
1 4 1
2 6 1
2 7 1
3 5 1
3 6 1
5 8 1
5 10 1
9 10 1
<BLANKLINE>
>>> #################### generate_lp_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_lp_file, 'testfile', {'vertices':10})
9
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
edge(1,4,1).
edge(2,6,1).
edge(2,7,1).
edge(3,5,1).
edge(3,6,1).
edge(5,8,1).
edge(5,10,1).
edge(9,10,1).
<BLANKLINE>
>>> #################### generate_tgf_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_tgf_file, 'testfile', {'vertices':10})
9
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
1 4 1
2 6 1
2 7 1
3 5 1
3 6 1
5 8 1
5 10 1
9 10 1
<BLANKLINE>
>>> #################### generate_dl_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_dl_file, 'testfile', {'vertices':10})
9
>>> file=open('testfile.dl','r')
>>> print(file.read())
dl
format=edgelist1
n=10
data:
1 2 1
1 4 1
2 6 1
2 7 1
3 5 1
3 6 1
5 8 1
5 10 1
9 10 1
<BLANKLINE>
>>> #################### generate_gml_file ####################
>>> from networkx.readwrite.gml import read_gml
>>> random.seed(2)
>>> engine.generate_graph(generate_gml_file, 'testfile', {'vertices':10})
9
>>> gml1 = read_gml("testfile.gml")
>>> type(gml1)
<class 'networkx.classes.graph.Graph'>
>>> #################### generate_gexf_file ####################
>>> from networkx.readwrite.gexf import read_gexf
>>> random.seed(2)
>>> engine.generate_graph(generate_gexf_file, 'testfile', {'vertices':10})
9
>>> gexf1 = read_gexf("testfile.gexf")
>>> type(gexf1)
<class 'networkx.classes.graph.Graph'>
>>> #################### generate_dot_file ####################
>>> import pydot
>>> random.seed(2)
>>> engine.generate_graph(generate_dot_file, 'testfile', {'vertices':10})
9
>>> file=open('testfile.gv','r')
>>> g1 = pydot.graph_from_dot_data(file.read())
>>> g1[0].get_type()
'graph'
>>> len(g1[0].get_edge_list())
9
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
