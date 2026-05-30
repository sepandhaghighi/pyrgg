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
...     engine.logger(file,'test','2min',{'vertices':10,'edge_number':45,'engine':9,'output_format':1})
>>> file = open('logfile.log','r')
>>> print("\\n".join(file.read().splitlines()[1:-1]))
Filename : test
Vertices : 10
Total Edges : 45
Engine : 9 (cg)
Elapsed Time : 2min
>>> class StrError:
...     def __init__(self):
...         pass
...     def __str__(self):
...         raise ValueError
>>> str_error_object = StrError()
>>> with open('logfile.log','a') as file:
...     engine.logger(file,'test','2min',{'vertices':str_error_object,'edge_number':45,'engine':9,'output_format':1})
[Error] Logger failed!
>>> ##########################################
>>> ## ========= generate_edges function =========
>>> ##########################################
>>> edge_dict, weight_dict, edge_number = engine.generate_edges(5)
>>> edge_dict == {1: [], 2: [1], 3: [1, 2], 4: [1, 2, 3], 5: [1, 2, 3, 4]}
True
>>> weight_dict == {1: [], 2: [1], 3: [1, 1], 4: [1, 1, 1], 5: [1, 1, 1, 1]}
True
>>> edge_number == 10
True
>>> engine.generate_edges()
Traceback (most recent call last):
        ...
TypeError: generate_edges() missing 1 required positional argument: 'n'
>>> #########################################
>>> ## ========= generate_graph function =========
>>> #########################################
>>> #################### generate_dimacs_file ####################
>>> engine.generate_graph(generate_dimacs_file, 'testfile', {'vertices':5})
10
>>> file=open('testfile.gr','r')
>>> print(file.read())
c FILE                  :testfile.gr
c No. of vertices       :5
c No. of edges          :10
c Max. weight           :1
c Min. weight           :1
p sp 5 10
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
<BLANKLINE>
>>> #################### generate_json_file ####################
>>> engine.generate_graph(generate_json_file, 'testfile', {'vertices':5})
10
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
>>> #################### generate_csv_file ####################
>>> engine.generate_graph(generate_csv_file, 'testfile', {'vertices':5})
10
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
<BLANKLINE>
>>> #################### generate_gdf_file ####################
>>> engine.generate_graph(generate_gdf_file, 'testfile', {'vertices':5})
10
>>> file=open('testfile.gdf','r')
>>> print(file.read())
nodedef>name VARCHAR,label VARCHAR
1,Node1
2,Node2
3,Node3
4,Node4
5,Node5
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
<BLANKLINE>
>>> #################### generate_gl_file ####################
>>> engine.generate_graph(generate_gl_file, 'testfile', {'vertices':5})
10
>>> file=open('testfile.gl','r')
>>> print(file.read())
2 1:1
3 1:1 2:1
4 1:1 2:1 3:1
5 1:1 2:1 3:1 4:1
<BLANKLINE>
>>> #################### generate_mtx_file ####################
>>> from scipy.io import mmread
>>> engine.generate_graph(generate_mtx_file, 'testfile', {'vertices':5})
10
>>> g = mmread("testfile.mtx")
>>> print(g.data.tolist())
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
>>> #################### generate_tsv_file ####################
>>> engine.generate_graph(generate_tsv_file, 'testfile', {'vertices':5})
10
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
<BLANKLINE>
>>> #################### generate_wel_file ####################
>>> engine.generate_graph(generate_wel_file, 'testfile', {'vertices':5})
10
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
<BLANKLINE>
>>> #################### generate_lp_file ####################
>>> engine.generate_graph(generate_lp_file, 'testfile', {'vertices':5})
10
>>> file=open('testfile.lp','r')
>>> print(file.read())
node(1).
node(2).
node(3).
node(4).
node(5).
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
<BLANKLINE>
>>> #################### generate_tgf_file ####################
>>> engine.generate_graph(generate_tgf_file, 'testfile', {'vertices':5})
10
>>> file=open('testfile.tgf','r')
>>> print(file.read())
1
2
3
4
5
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
<BLANKLINE>
>>> #################### generate_dl_file ####################
>>> engine.generate_graph(generate_dl_file, 'testfile', {'vertices':5})
10
>>> file=open('testfile.dl','r')
>>> print(file.read())
dl
format=edgelist1
n=5
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
<BLANKLINE>
>>> #################### generate_gml_file ####################
>>> from networkx.readwrite.gml import read_gml
>>> engine.generate_graph(generate_gml_file, 'testfile', {'vertices':5})
10
>>> gml1 = read_gml("testfile.gml")
>>> type(gml1)
<class 'networkx.classes.graph.Graph'>
>>> nx.is_isomorphic(gml1, nx.complete_graph(5))
True
>>> #################### generate_gexf_file ####################
>>> from networkx.readwrite.gexf import read_gexf
>>> engine.generate_graph(generate_gexf_file, 'testfile', {'vertices':5})
10
>>> gexf1 = read_gexf("testfile.gexf")
>>> type(gexf1)
<class 'networkx.classes.graph.Graph'>
>>> nx.is_isomorphic(gexf1, nx.complete_graph(5))
True
>>> #################### generate_dot_file ####################
>>> import pydot
>>> engine.generate_graph(generate_dot_file, 'testfile', {'vertices':5})
10
>>> file=open('testfile.gv','r')
>>> g1 = pydot.graph_from_dot_data(file.read())
>>> g1[0].get_type()
'graph'
>>> len(g1[0].get_edge_list())
10
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
