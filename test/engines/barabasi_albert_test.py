# -*- coding: utf-8 -*-
"""
>>> from pyrgg.functions import *
>>> from pyrgg.graph_gen import *
>>> import pyrgg.params
>>> import random
>>> import os
>>> import json
>>> import pyrgg.engines.barabasi_albert as engine
>>> os.environ["PYRGG_TEST_MODE"] = "1"
>>> ######################################
>>> ## ========= logger function =========
>>> ######################################
>>> with open('logfile.log','a') as file:
...     engine.logger(file,'test','2min',{'vertices':100,'edge_number':900,'attaching_edge_number':10,'engine':5,'output_format':1})
>>> file = open('logfile.log','r')
>>> print("\\n".join(file.read().splitlines()[1:-1]))
Filename : test
Vertices : 100
Edges to Attach to a New Node : 10
Total Edges : 900
Engine : 5 (ba)
Elapsed Time : 2min
>>> class StrError:
...     def __init__(self):
...         pass
...     def __str__(self):
...         raise ValueError
>>> str_error_object = StrError()
>>> with open('logfile.log','a') as file:
...     engine.logger(file,'test','2min',{'vertices':str_error_object, 'edge_number':900,'attaching_edge_number':10,'engine':5,'output_format':1})
[Error] Logger failed!
>>> ##########################################
>>> ## ========= generate_edges function =========
>>> ##########################################
>>> random.seed(2)
>>> edge_dict, weight_dict, edge_number = engine.generate_edges(10, 3)
>>> edge_dict == {1: [], 2: [], 3: [], 4: [1, 2, 3], 5: [1, 4, 4], 6: [4, 3, 4], 7: [4, 1, 2], 8: [4, 7, 4], 9: [3, 2, 4], 10: [4, 7, 9]}
True
>>> edge_number == 21
True
>>> engine.generate_edges(0)
Traceback (most recent call last):
        ...
TypeError: generate_edges() missing 1 required positional argument: 'k'
>>> #########################################
>>> ## ========= generate_graph function =========
>>> #########################################
>>> #################### generate_dimacs_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_dimacs_file, 'testfile', {'vertices': 10, 'attaching_edge_number': 3})
21
>>> file=open('testfile.gr','r')
>>> print(file.read())
c FILE                  :testfile.gr
c No. of vertices       :10
c No. of edges          :21
c Max. weight           :1
c Min. weight           :1
p sp 10 21
a 4 1 1
a 4 2 1
a 4 3 1
a 5 1 1
a 5 4 1
a 5 4 1
a 6 4 1
a 6 3 1
a 6 4 1
a 7 4 1
a 7 1 1
a 7 2 1
a 8 4 1
a 8 7 1
a 8 4 1
a 9 3 1
a 9 2 1
a 9 4 1
a 10 4 1
a 10 7 1
a 10 9 1
<BLANKLINE>
>>> #################### generate_json_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_json_file, 'testfile', {'vertices': 10, 'attaching_edge_number': 3})
21
>>> file=open('testfile.json','r')
>>> testfile_1=json.load(file)
>>> testfile_1['graph']['nodes'][1]
{'id': 2}
>>> testfile_1['graph']['edges'][1]['source']
4
>>> testfile_1['graph']['edges'][1]['target']
2
>>> #################### generate_csv_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_csv_file, 'testfile', {'vertices':10, 'attaching_edge_number':3})
21
>>> file=open('testfile.csv','r')
>>> print(file.read())
4,1,1
4,2,1
4,3,1
5,1,1
5,4,1
5,4,1
6,4,1
6,3,1
6,4,1
7,4,1
7,1,1
7,2,1
8,4,1
8,7,1
8,4,1
9,3,1
9,2,1
9,4,1
10,4,1
10,7,1
10,9,1
<BLANKLINE>
>>> #################### gdf_maker ####################
>>> random.seed(2)
>>> engine.generate_graph(gdf_maker, 'testfile', {'vertices':10, 'attaching_edge_number':3})
21
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
4,1,1
4,2,1
4,3,1
5,1,1
5,4,1
5,4,1
6,4,1
6,3,1
6,4,1
7,4,1
7,1,1
7,2,1
8,4,1
8,7,1
8,4,1
9,3,1
9,2,1
9,4,1
10,4,1
10,7,1
10,9,1
<BLANKLINE>
>>> #################### gl_maker ####################
>>> random.seed(2)
>>> engine.generate_graph(gl_maker, 'testfile', {'vertices':10, 'attaching_edge_number':3})
21
>>> file=open('testfile.gl','r')
>>> print(file.read())
4 1:1 2:1 3:1
5 1:1 4:1 4:1
6 4:1 3:1 4:1
7 4:1 1:1 2:1
8 4:1 7:1 4:1
9 3:1 2:1 4:1
10 4:1 7:1 9:1
<BLANKLINE>
>>> #################### mtx_maker ####################
>>> from scipy.io import mmread
>>> random.seed(2)
>>> engine.generate_graph(mtx_maker, 'testfile', {'vertices':10, 'attaching_edge_number':3})
21
>>> g = mmread("testfile.mtx")
>>> print(g.data.tolist())
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
>>> #################### generate_tsv_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_tsv_file, 'testfile', {'vertices':10, 'attaching_edge_number':3})
21
>>> file=open('testfile.tsv','r')
>>> print(file.read())
4	1	1
4	2	1
4	3	1
5	1	1
5	4	1
5	4	1
6	4	1
6	3	1
6	4	1
7	4	1
7	1	1
7	2	1
8	4	1
8	7	1
8	4	1
9	3	1
9	2	1
9	4	1
10	4	1
10	7	1
10	9	1
<BLANKLINE>
>>> #################### wel_maker ####################
>>> random.seed(2)
>>> engine.generate_graph(wel_maker, 'testfile', {'vertices':10, 'attaching_edge_number':3})
21
>>> file=open('testfile.wel','r')
>>> print(file.read())
4 1 1
4 2 1
4 3 1
5 1 1
5 4 1
5 4 1
6 4 1
6 3 1
6 4 1
7 4 1
7 1 1
7 2 1
8 4 1
8 7 1
8 4 1
9 3 1
9 2 1
9 4 1
10 4 1
10 7 1
10 9 1
<BLANKLINE>
>>> #################### lp_maker ####################
>>> random.seed(2)
>>> engine.generate_graph(lp_maker, 'testfile', {'vertices':10, 'attaching_edge_number':3})
21
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
edge(4,1,1).
edge(4,2,1).
edge(4,3,1).
edge(5,1,1).
edge(5,4,1).
edge(5,4,1).
edge(6,4,1).
edge(6,3,1).
edge(6,4,1).
edge(7,4,1).
edge(7,1,1).
edge(7,2,1).
edge(8,4,1).
edge(8,7,1).
edge(8,4,1).
edge(9,3,1).
edge(9,2,1).
edge(9,4,1).
edge(10,4,1).
edge(10,7,1).
edge(10,9,1).
<BLANKLINE>
>>> #################### tgf_maker ####################
>>> random.seed(2)
>>> engine.generate_graph(tgf_maker, 'testfile', {'vertices':10, 'attaching_edge_number':3})
21
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
4 1 1
4 2 1
4 3 1
5 1 1
5 4 1
5 4 1
6 4 1
6 3 1
6 4 1
7 4 1
7 1 1
7 2 1
8 4 1
8 7 1
8 4 1
9 3 1
9 2 1
9 4 1
10 4 1
10 7 1
10 9 1
<BLANKLINE>
>>> #################### dl_maker ####################
>>> random.seed(2)
>>> engine.generate_graph(dl_maker, 'testfile', {'vertices':10, 'attaching_edge_number':3})
21
>>> file=open('testfile.dl','r')
>>> print(file.read())
dl
format=edgelist1
n=10
data:
4 1 1
4 2 1
4 3 1
5 1 1
5 4 1
5 4 1
6 4 1
6 3 1
6 4 1
7 4 1
7 1 1
7 2 1
8 4 1
8 7 1
8 4 1
9 3 1
9 2 1
9 4 1
10 4 1
10 7 1
10 9 1
<BLANKLINE>
>>> #################### gml_maker ####################
>>> from networkx.readwrite.gml import read_gml
>>> random.seed(2)
>>> engine.generate_graph(gml_maker, 'testfile', {'vertices':10, 'attaching_edge_number':3})
21
>>> gml1 = read_gml("testfile.gml")
>>> type(gml1)
<class 'networkx.classes.multigraph.MultiGraph'>
>>> #################### gexf_maker ####################
>>> from networkx.readwrite.gexf import read_gexf
>>> random.seed(2)
>>> engine.generate_graph(gexf_maker, 'testfile', {'vertices':10, 'attaching_edge_number':3})
21
>>> gexf1 = read_gexf("testfile.gexf")
>>> type(gexf1)
<class 'networkx.classes.multigraph.MultiGraph'>
>>> #################### dot_maker ####################
>>> import pydot
>>> random.seed(2)
>>> engine.generate_graph(dot_maker, 'testfile', {'vertices':10, 'attaching_edge_number':3})
21
>>> file=open('testfile.gv','r')
>>> g1 = pydot.graph_from_dot_data(file.read())
>>> g1[0].get_type()
'graph'
>>> len(g1[0].get_edge_list())
21
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