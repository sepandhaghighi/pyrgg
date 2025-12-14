# -*- coding: utf-8 -*-
"""
>>> from pyrgg.functions import *
>>> from pyrgg.graph_gen import *
>>> import pyrgg.params
>>> import random
>>> import os
>>> import json
>>> import pyrgg.engines.watts_strogatz as engine
>>> os.environ["PYRGG_TEST_MODE"] = "1"
>>> ######################################
>>> ## ========= logger function =========
>>> ######################################
>>> with open('logfile.log','a') as file:
...     engine.logger(file,'test','2min',{'vertices':100,'edge_number':500,'mean_degree':10,'rewiring_probability':0.5,'engine':6,'output_format':1})
>>> file = open('logfile.log','r')
>>> print("\\n".join(file.read().splitlines()[1:-1]))
Filename : test
Vertices : 100
Mean Degree : 10
Rewiring Probability : 0.5
Total Edges : 500
Engine : 6 (ws)
Elapsed Time : 2min
>>> class StrError:
...     def __init__(self):
...         pass
...     def __str__(self):
...         raise ValueError
>>> str_error_object = StrError()
>>> with open('logfile.log','a') as file:
...     engine.logger(file,'test','2min',{'vertices':str_error_object,'edge_number':500,'mean_degree':10,'rewiring_probability':0.5,'engine':6,'output_format':1})
[Error] Logger failed!
>>> ##########################################
>>> ## ========= generate_edges function =========
>>> ##########################################
>>> random.seed(2)
>>> edge_dict, weight_dict, edge_number = engine.generate_edges(10, 4, 0.5)
>>> edge_dict == {1: [9, 10, 2, 3], 2: [10, 5, 6], 3: [4, 5], 4: [9, 1], 5: [6, 9], 6: [7, 8], 7: [8, 9], 8: [4, 10], 9: [10], 10: []}
True
>>> edge_number == 20
True
>>> engine.generate_edges(0)
Traceback (most recent call last):
        ...
TypeError: generate_edges() missing 2 required positional arguments: 'k' and 'beta'
>>> #########################################
>>> ## ========= generate_graph function =========
>>> #########################################
>>> #################### generate_dimacs_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_dimacs_file, 'testfile', {'vertices': 10, 'mean_degree': 4, 'rewiring_probability': 0.5})
20
>>> file=open('testfile.gr','r')
>>> print(file.read())
c FILE                  :testfile.gr
c No. of vertices       :10
c No. of edges          :20
c Max. weight           :1
c Min. weight           :1
p sp 10 20
a 1 9 1
a 1 10 1
a 1 2 1
a 1 3 1
a 2 10 1
a 2 5 1
a 2 6 1
a 3 4 1
a 3 5 1
a 4 9 1
a 4 1 1
a 5 6 1
a 5 9 1
a 6 7 1
a 6 8 1
a 7 8 1
a 7 9 1
a 8 4 1
a 8 10 1
a 9 10 1
<BLANKLINE>
>>> #################### json_maker ####################
>>> random.seed(2)
>>> engine.generate_graph(json_maker, 'testfile', {'vertices': 10, 'mean_degree': 4, 'rewiring_probability': 0.5})
20
>>> file=open('testfile.json','r')
>>> testfile_1=json.load(file)
>>> testfile_1['graph']['nodes'][1]
{'id': 2}
>>> testfile_1['graph']['edges'][1]['source']
1
>>> testfile_1['graph']['edges'][1]['target']
10
>>> #################### csv_maker ####################
>>> random.seed(2)
>>> engine.generate_graph(csv_maker, 'testfile', {'vertices': 10, 'mean_degree': 4, 'rewiring_probability': 0.5})
20
>>> file=open('testfile.csv','r')
>>> print(file.read())
1,9,1
1,10,1
1,2,1
1,3,1
2,10,1
2,5,1
2,6,1
3,4,1
3,5,1
4,9,1
4,1,1
5,6,1
5,9,1
6,7,1
6,8,1
7,8,1
7,9,1
8,4,1
8,10,1
9,10,1
<BLANKLINE>
>>> #################### gdf_maker ####################
>>> random.seed(2)
>>> engine.generate_graph(gdf_maker, 'testfile', {'vertices': 10, 'mean_degree': 4, 'rewiring_probability': 0.5})
20
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
1,9,1
1,10,1
1,2,1
1,3,1
2,10,1
2,5,1
2,6,1
3,4,1
3,5,1
4,9,1
4,1,1
5,6,1
5,9,1
6,7,1
6,8,1
7,8,1
7,9,1
8,4,1
8,10,1
9,10,1
<BLANKLINE>
>>> #################### gl_maker ####################
>>> random.seed(2)
>>> engine.generate_graph(gl_maker, 'testfile', {'vertices': 10, 'mean_degree': 4, 'rewiring_probability': 0.5})
20
>>> file=open('testfile.gl','r')
>>> print(file.read())
1 9:1 10:1 2:1 3:1
2 10:1 5:1 6:1
3 4:1 5:1
4 9:1 1:1
5 6:1 9:1
6 7:1 8:1
7 8:1 9:1
8 4:1 10:1
9 10:1
<BLANKLINE>
>>> #################### mtx_maker ####################
>>> from scipy.io import mmread
>>> random.seed(2)
>>> engine.generate_graph(mtx_maker, 'testfile', {'vertices': 10, 'mean_degree': 4, 'rewiring_probability': 0.5})
20
>>> g = mmread("testfile.mtx")
>>> print(g.data.tolist())
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
>>> #################### tsv_maker ####################
>>> random.seed(2)
>>> engine.generate_graph(tsv_maker, 'testfile', {'vertices': 10, 'mean_degree': 4, 'rewiring_probability': 0.5})
20
>>> file=open('testfile.tsv','r')
>>> print(file.read())
1	9	1
1	10	1
1	2	1
1	3	1
2	10	1
2	5	1
2	6	1
3	4	1
3	5	1
4	9	1
4	1	1
5	6	1
5	9	1
6	7	1
6	8	1
7	8	1
7	9	1
8	4	1
8	10	1
9	10	1
<BLANKLINE>
>>> #################### wel_maker ####################
>>> random.seed(2)
>>> engine.generate_graph(wel_maker, 'testfile', {'vertices': 10, 'mean_degree': 4, 'rewiring_probability': 0.5})
20
>>> file=open('testfile.wel','r')
>>> print(file.read())
1 9 1
1 10 1
1 2 1
1 3 1
2 10 1
2 5 1
2 6 1
3 4 1
3 5 1
4 9 1
4 1 1
5 6 1
5 9 1
6 7 1
6 8 1
7 8 1
7 9 1
8 4 1
8 10 1
9 10 1
<BLANKLINE>
>>> #################### lp_maker ####################
>>> random.seed(2)
>>> engine.generate_graph(lp_maker, 'testfile', {'vertices': 10, 'mean_degree': 4, 'rewiring_probability': 0.5})
20
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
edge(1,9,1).
edge(1,10,1).
edge(1,2,1).
edge(1,3,1).
edge(2,10,1).
edge(2,5,1).
edge(2,6,1).
edge(3,4,1).
edge(3,5,1).
edge(4,9,1).
edge(4,1,1).
edge(5,6,1).
edge(5,9,1).
edge(6,7,1).
edge(6,8,1).
edge(7,8,1).
edge(7,9,1).
edge(8,4,1).
edge(8,10,1).
edge(9,10,1).
<BLANKLINE>
>>> #################### tgf_maker ####################
>>> random.seed(2)
>>> engine.generate_graph(tgf_maker, 'testfile', {'vertices': 10, 'mean_degree': 4, 'rewiring_probability': 0.5})
20
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
1 9 1
1 10 1
1 2 1
1 3 1
2 10 1
2 5 1
2 6 1
3 4 1
3 5 1
4 9 1
4 1 1
5 6 1
5 9 1
6 7 1
6 8 1
7 8 1
7 9 1
8 4 1
8 10 1
9 10 1
<BLANKLINE>
>>> #################### dl_maker ####################
>>> random.seed(2)
>>> engine.generate_graph(dl_maker, 'testfile', {'vertices': 10, 'mean_degree': 4, 'rewiring_probability': 0.5})
20
>>> file=open('testfile.dl','r')
>>> print(file.read())
dl
format=edgelist1
n=10
data:
1 9 1
1 10 1
1 2 1
1 3 1
2 10 1
2 5 1
2 6 1
3 4 1
3 5 1
4 9 1
4 1 1
5 6 1
5 9 1
6 7 1
6 8 1
7 8 1
7 9 1
8 4 1
8 10 1
9 10 1
<BLANKLINE>
>>> #################### gml_maker ####################
>>> from networkx.readwrite.gml import read_gml
>>> random.seed(2)
>>> engine.generate_graph(gml_maker, 'testfile', {'vertices': 10, 'mean_degree': 4, 'rewiring_probability': 0.5})
20
>>> gml1 = read_gml("testfile.gml")
>>> type(gml1)
<class 'networkx.classes.graph.Graph'>
>>> #################### gexf_maker ####################
>>> from networkx.readwrite.gexf import read_gexf
>>> random.seed(2)
>>> engine.generate_graph(gexf_maker, 'testfile', {'vertices': 10, 'mean_degree': 4, 'rewiring_probability': 0.5})
20
>>> gexf1 = read_gexf("testfile.gexf")
>>> type(gexf1)
<class 'networkx.classes.graph.Graph'>
>>> #################### dot_maker ####################
>>> import pydot
>>> random.seed(2)
>>> engine.generate_graph(dot_maker, 'testfile', {'vertices': 10, 'mean_degree': 4, 'rewiring_probability': 0.5})
20
>>> file=open('testfile.gv','r')
>>> g1 = pydot.graph_from_dot_data(file.read())
>>> g1[0].get_type()
'graph'
>>> len(g1[0].get_edge_list())
20
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