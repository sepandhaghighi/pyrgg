# -*- coding: utf-8 -*-
"""
>>> from pyrgg.functions import *
>>> from pyrgg.graph_gen import *
>>> import pyrgg.params
>>> import random
>>> import os
>>> import json
>>> import pyrgg.engines.geometric_graph as engine
>>> os.environ["PYRGG_TEST_MODE"] = "1"
>>> ######################################
>>> ## ========= logger function =========
>>> ######################################
>>> with open('logfile.log','a') as file:
...     engine.logger(file,'test','2min',{'vertices':100,'edge_number':50,'space_dimension':2,'cutoff_threshold':0.5,'engine':7,'output_format':1})
>>> file = open('logfile.log','r')
>>> print("\\n".join(file.read().splitlines()[1:-1]))
Filename : test
Vertices : 100
Space Dimension : 2
Cutoff Threshold : 0.5
Total Edges : 50
Engine : 7 (gg)
Elapsed Time : 2min
>>> class StrError:
...     def __init__(self):
...         pass
...     def __str__(self):
...         raise ValueError
>>> str_error_object = StrError()
>>> with open('logfile.log','a') as file:
...     engine.logger(file,'test','2min',{'vertices':str_error_object,'edge_number':50,'space_dimension':2,'cutoff_threshold':0.5,'engine':7,'output_format':1})
[Error] Logger failed!
>>> ##########################################
>>> ## ========= edge_gen function =========
>>> ##########################################
>>> random.seed(2)
>>> edge_dict, weight_dict, edge_number = engine.generate_edges(10, 2, 0.5)
>>> edge_dict == {1: [3, 5, 8, 9], 2: [7, 10], 3: [4, 5, 8, 9], 4: [5, 6, 7, 9, 10], 5: [6, 7, 8, 9, 10], 6: [7, 10], 7: [10], 8: [], 9: [], 10: []}
True
>>> weight_dict == {1: [0.24375, 0.48873, 0.23771, 0.40371], 2: [0.48501, 0.42942], 3: [0.45883, 0.2634, 0.28223, 0.22306], 4: [0.3054, 0.17396, 0.25386, 0.36596, 0.22839], 5: [0.4491, 0.27605, 0.40529, 0.34911, 0.37493], 6: [0.27921, 0.1751], 7: [0.12609], 8: [], 9: [], 10: []}
True
>>> edge_number == 23
True
>>> engine.generate_edges(0)
Traceback (most recent call last):
        ...
TypeError: generate_edges() missing 2 required positional arguments: 'd' and 'r'
>>> #########################################
>>> ## ========= generate_graph function =========
>>> #########################################
>>> #################### generate_dimacs_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_dimacs_file, 'testfile', {'vertices': 10, 'space_dimension': 2, 'cutoff_threshold': 0.5})
23
>>> file=open('testfile.gr','r')
>>> print(file.read())
c FILE                  :testfile.gr
c No. of vertices       :10
c No. of edges          :23
c Max. weight           :0.48873
c Min. weight           :0.12609
p sp 10 23
a 1 3 0.24375
a 1 5 0.48873
a 1 8 0.23771
a 1 9 0.40371
a 2 7 0.48501
a 2 10 0.42942
a 3 4 0.45883
a 3 5 0.2634
a 3 8 0.28223
a 3 9 0.22306
a 4 5 0.3054
a 4 6 0.17396
a 4 7 0.25386
a 4 9 0.36596
a 4 10 0.22839
a 5 6 0.4491
a 5 7 0.27605
a 5 8 0.40529
a 5 9 0.34911
a 5 10 0.37493
a 6 7 0.27921
a 6 10 0.1751
a 7 10 0.12609
<BLANKLINE>
>>> #################### generate_json_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_json_file, 'testfile', {'vertices': 10, 'space_dimension': 2, 'cutoff_threshold': 0.5})
23
>>> file=open('testfile.json','r')
>>> testfile_1=json.load(file)
>>> testfile_1['graph']['nodes'][1]
{'id': 2}
>>> testfile_1['graph']['edges'][1]['source']
1
>>> testfile_1['graph']['edges'][1]['target']
5
>>> #################### generate_csv_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_csv_file, 'testfile', {'vertices': 10, 'space_dimension': 2, 'cutoff_threshold': 0.5})
23
>>> file=open('testfile.csv','r')
>>> print(file.read())
1,3,0.24375
1,5,0.48873
1,8,0.23771
1,9,0.40371
2,7,0.48501
2,10,0.42942
3,4,0.45883
3,5,0.2634
3,8,0.28223
3,9,0.22306
4,5,0.3054
4,6,0.17396
4,7,0.25386
4,9,0.36596
4,10,0.22839
5,6,0.4491
5,7,0.27605
5,8,0.40529
5,9,0.34911
5,10,0.37493
6,7,0.27921
6,10,0.1751
7,10,0.12609
<BLANKLINE>
>>> #################### generate_gdf_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_gdf_file, 'testfile', {'vertices': 10, 'space_dimension': 2, 'cutoff_threshold': 0.5})
23
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
1,3,0.24375
1,5,0.48873
1,8,0.23771
1,9,0.40371
2,7,0.48501
2,10,0.42942
3,4,0.45883
3,5,0.2634
3,8,0.28223
3,9,0.22306
4,5,0.3054
4,6,0.17396
4,7,0.25386
4,9,0.36596
4,10,0.22839
5,6,0.4491
5,7,0.27605
5,8,0.40529
5,9,0.34911
5,10,0.37493
6,7,0.27921
6,10,0.1751
7,10,0.12609
<BLANKLINE>
>>> #################### generate_gl_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_gl_file, 'testfile', {'vertices': 10, 'space_dimension': 2, 'cutoff_threshold': 0.5})
23
>>> file=open('testfile.gl','r')
>>> print(file.read())
1 3:0.24375 5:0.48873 8:0.23771 9:0.40371
2 7:0.48501 10:0.42942
3 4:0.45883 5:0.2634 8:0.28223 9:0.22306
4 5:0.3054 6:0.17396 7:0.25386 9:0.36596 10:0.22839
5 6:0.4491 7:0.27605 8:0.40529 9:0.34911 10:0.37493
6 7:0.27921 10:0.1751
7 10:0.12609
<BLANKLINE>
>>> #################### generate_mtx_file ####################
>>> from scipy.io import mmread
>>> random.seed(2)
>>> engine.generate_graph(generate_mtx_file, 'testfile', {'vertices': 10, 'space_dimension': 2, 'cutoff_threshold': 0.5})
23
>>> g = mmread("testfile.mtx")
>>> print(g.data.tolist())
[0.24375, 0.48873, 0.23771, 0.40371, 0.48501, 0.42942, 0.45883, 0.2634, 0.28223, 0.22306, 0.3054, 0.17396, 0.25386, 0.36596, 0.22839, 0.4491, 0.27605, 0.40529, 0.34911, 0.37493, 0.27921, 0.1751, 0.12609]
>>> #################### generate_tsv_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_tsv_file, 'testfile', {'vertices': 10, 'space_dimension': 2, 'cutoff_threshold': 0.5})
23
>>> file=open('testfile.tsv','r')
>>> print(file.read())
1   3   0.24375
1   5   0.48873
1   8   0.23771
1   9   0.40371
2   7   0.48501
2   10  0.42942
3   4   0.45883
3   5   0.2634
3   8   0.28223
3   9   0.22306
4   5   0.3054
4   6   0.17396
4   7   0.25386
4   9   0.36596
4   10  0.22839
5   6   0.4491
5   7   0.27605
5   8   0.40529
5   9   0.34911
5   10  0.37493
6   7   0.27921
6   10  0.1751
7   10  0.12609
<BLANKLINE>
>>> #################### generate_wel_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_wel_file, 'testfile', {'vertices': 10, 'space_dimension': 2, 'cutoff_threshold': 0.5})
23
>>> file=open('testfile.wel','r')
>>> print(file.read())
1 3 0.24375
1 5 0.48873
1 8 0.23771
1 9 0.40371
2 7 0.48501
2 10 0.42942
3 4 0.45883
3 5 0.2634
3 8 0.28223
3 9 0.22306
4 5 0.3054
4 6 0.17396
4 7 0.25386
4 9 0.36596
4 10 0.22839
5 6 0.4491
5 7 0.27605
5 8 0.40529
5 9 0.34911
5 10 0.37493
6 7 0.27921
6 10 0.1751
7 10 0.12609
<BLANKLINE>
>>> #################### generate_lp_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_lp_file, 'testfile', {'vertices': 10, 'space_dimension': 2, 'cutoff_threshold': 0.5})
23
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
edge(1,3,0.24375).
edge(1,5,0.48873).
edge(1,8,0.23771).
edge(1,9,0.40371).
edge(2,7,0.48501).
edge(2,10,0.42942).
edge(3,4,0.45883).
edge(3,5,0.2634).
edge(3,8,0.28223).
edge(3,9,0.22306).
edge(4,5,0.3054).
edge(4,6,0.17396).
edge(4,7,0.25386).
edge(4,9,0.36596).
edge(4,10,0.22839).
edge(5,6,0.4491).
edge(5,7,0.27605).
edge(5,8,0.40529).
edge(5,9,0.34911).
edge(5,10,0.37493).
edge(6,7,0.27921).
edge(6,10,0.1751).
edge(7,10,0.12609).
<BLANKLINE>
>>> #################### generate_tgf_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_tgf_file, 'testfile', {'vertices': 10, 'space_dimension': 2, 'cutoff_threshold': 0.5})
23
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
1 3 0.24375
1 5 0.48873
1 8 0.23771
1 9 0.40371
2 7 0.48501
2 10 0.42942
3 4 0.45883
3 5 0.2634
3 8 0.28223
3 9 0.22306
4 5 0.3054
4 6 0.17396
4 7 0.25386
4 9 0.36596
4 10 0.22839
5 6 0.4491
5 7 0.27605
5 8 0.40529
5 9 0.34911
5 10 0.37493
6 7 0.27921
6 10 0.1751
7 10 0.12609
<BLANKLINE>
>>> #################### generate_dl_file ####################
>>> random.seed(2)
>>> engine.generate_graph(generate_dl_file, 'testfile', {'vertices': 10, 'space_dimension': 2, 'cutoff_threshold': 0.5})
23
>>> file=open('testfile.dl','r')
>>> print(file.read())
dl
format=edgelist1
n=10
data:
1 3 0.24375
1 5 0.48873
1 8 0.23771
1 9 0.40371
2 7 0.48501
2 10 0.42942
3 4 0.45883
3 5 0.2634
3 8 0.28223
3 9 0.22306
4 5 0.3054
4 6 0.17396
4 7 0.25386
4 9 0.36596
4 10 0.22839
5 6 0.4491
5 7 0.27605
5 8 0.40529
5 9 0.34911
5 10 0.37493
6 7 0.27921
6 10 0.1751
7 10 0.12609
<BLANKLINE>
>>> #################### generate_gml_file ####################
>>> from networkx.readwrite.gml import read_gml
>>> random.seed(2)
>>> engine.generate_graph(generate_gml_file, 'testfile', {'vertices': 10, 'space_dimension': 2, 'cutoff_threshold': 0.5})
23
>>> gml1 = read_gml("testfile.gml")
>>> type(gml1)
<class 'networkx.classes.graph.Graph'>
>>> #################### generate_gexf_file ####################
>>> from networkx.readwrite.gexf import read_gexf
>>> random.seed(2)
>>> engine.generate_graph(generate_gexf_file, 'testfile', {'vertices': 10, 'space_dimension': 2, 'cutoff_threshold': 0.5})
23
>>> gexf1 = read_gexf("testfile.gexf")
>>> type(gexf1)
<class 'networkx.classes.graph.Graph'>
>>> #################### generate_dot_file ####################
>>> import pydot
>>> random.seed(2)
>>> engine.generate_graph(generate_dot_file, 'testfile', {'vertices': 10, 'space_dimension': 2, 'cutoff_threshold': 0.5})
23
>>> file=open('testfile.gv','r')
>>> g1 = pydot.graph_from_dot_data(file.read())
>>> g1[0].get_type()
'graph'
>>> len(g1[0].get_edge_list())
23
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
