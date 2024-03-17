# -*- coding: utf-8 -*-
"""
>>> from pyrgg import *
>>> import pyrgg.params
>>> import pyrgg.engines.pyrgg as engine
>>> import random
>>> import os
>>> import json
>>> import yaml
>>> import pickle
>>> from scipy.io import mmread
>>> from networkx.readwrite.gml import read_gml
>>> from networkx.readwrite.gexf import read_gexf
>>> os.environ["PYRGG_TEST_MODE"] = "1"
>>> dimacs_maker({}, {})
Traceback (most recent call last):
        ...
TypeError: dimacs_maker() missing 1 required positional argument: 'mdata'
>>> random.seed(2)
>>> engine.gen_using(json_maker, 'testfile', {'min_weight':0, 'max_weight':200, 'vertices':10, 'min_edge':0, 'max_edge':2, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
7
>>> json_to_yaml('testfile')
>>> file=open('testfile.yaml','r')
>>> testfile_1_yaml=yaml.safe_load(file)
>>> testfile_1_yaml['graph']['edges'][1]['source']
5
>>> testfile_1_yaml['graph']['edges'][1]['target']
6
>>> testfile_1_yaml['graph']['edges'][1]['weight']
148
>>> testfile_1_yaml['properties']['signed']
True
>>> testfile_1_yaml['properties']['directed']
True
>>> testfile_1_yaml['properties']['self_loop']
True
>>> testfile_1_yaml['properties']['multigraph']
False
>>> testfile_1_yaml['properties']['weighted']
True
>>> json_to_pickle('testfile')
>>> testfile_1_p=pickle.load( open( 'testfile.p', 'rb' ) )
>>> testfile_1_p['graph']['edges'][1]['source']
5
>>> testfile_1_p['graph']['edges'][1]['target']
6
>>> testfile_1_p['graph']['edges'][1]['weight']
148
>>> testfile_1_p['properties']['signed']
True
>>> testfile_1_p['properties']['directed']
True
>>> testfile_1_p['properties']['self_loop']
True
>>> testfile_1_p['properties']['multigraph']
False
>>> testfile_1_p['properties']['weighted']
True
>>> random.seed(4)
>>> engine.gen_using(json_maker, 'testfile2', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':1, 'direct':1, 'self_loop':1, 'multigraph':0})
35
>>> json_to_yaml('testfile2')
>>> file=open('testfile2.yaml','r')
>>> testfile_2_yaml=yaml.safe_load(file)
>>> testfile_2_yaml['graph']['nodes'][1]
{'id': 2}
>>> testfile_2_yaml['graph']['edges'][1]['source']
2
>>> testfile_2_yaml['graph']['edges'][1]['target']
18
>>> testfile_2_yaml['graph']['edges'][1]['weight']
5
>>> testfile_2_yaml['properties']['signed']
True
>>> testfile_2_yaml['properties']['directed']
True
>>> testfile_2_yaml['properties']['self_loop']
True
>>> testfile_2_yaml['properties']['multigraph']
False
>>> testfile_2_yaml['properties']['weighted']
True
>>> json_to_pickle('testfile2')
>>> testfile_2_p=pickle.load( open( 'testfile2.p', 'rb' ) )
>>> testfile_2_p['graph']['edges'][1]['source']
2
>>> testfile_2_p['graph']['edges'][1]['target']
18
>>> testfile_2_p['graph']['edges'][1]['weight']
5
>>> testfile_2_p['properties']['signed']
True
>>> testfile_2_p['properties']['directed']
True
>>> testfile_2_p['properties']['self_loop']
True
>>> testfile_2_p['properties']['multigraph']
False
>>> testfile_2_p['properties']['weighted']
True
>>> random.seed(20)
>>> engine.gen_using(json_maker, 'testfile3', {'min_weight':10, 'max_weight':30, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':0, 'direct':1, 'self_loop':1, 'multigraph':0})
137
>>> json_to_yaml('testfile3')
>>> file=open('testfile3.yaml','r')
>>> testfile_3_yaml=yaml.safe_load(file)
>>> testfile_3_yaml['graph']['nodes'][1]
{'id': 2}
>>> testfile_3_yaml['graph']['edges'][1]['source']
3
>>> testfile_3_yaml['graph']['edges'][1]['target']
76
>>> testfile_3_yaml['graph']['edges'][1]['weight']
15
>>> testfile_3_yaml['properties']['signed']
False
>>> testfile_3_yaml['properties']['directed']
True
>>> testfile_3_yaml['properties']['self_loop']
True
>>> testfile_3_yaml['properties']['multigraph']
False
>>> testfile_3_yaml['properties']['weighted']
True
>>> json_to_yaml('testfile24')
[Error] Failed to generate YAML file!
>>> json_to_pickle('testfile24')
[Error] Failed to generate Pickle file!
>>> json_maker({}, {})
Traceback (most recent call last):
        ...
TypeError: json_maker() missing 1 required positional argument: 'mdata'
>>> json_to_pickle('testfile3')
>>> testfile_3_p=pickle.load( open( 'testfile3.p', 'rb' ) )
>>> testfile_3_p['graph']['edges'][1]['source']
3
>>> testfile_3_p['graph']['edges'][1]['target']
76
>>> testfile_3_p['graph']['edges'][1]['weight']
15
>>> testfile_3_p['properties']['signed']
False
>>> testfile_3_p['properties']['directed']
True
>>> testfile_3_p['properties']['self_loop']
True
>>> testfile_3_p['properties']['multigraph']
False
>>> testfile_3_p['properties']['weighted']
True
>>> gl_maker({})
Traceback (most recent call last):
        ...
TypeError: gl_maker() missing 2 required positional arguments: 'weight_dic' and 'mdata'
>>> csv_maker({}, {})
Traceback (most recent call last):
        ...
TypeError: csv_maker() missing 1 required positional argument: 'mdata'
>>> gdf_maker({})
Traceback (most recent call last):
        ...
TypeError: gdf_maker() missing 2 required positional arguments: 'weight_dic' and 'mdata'
>>> tsv_maker({}, {})
Traceback (most recent call last):
        ...
TypeError: tsv_maker() missing 1 required positional argument: 'mdata'
>>> wel_maker({}, {})
Traceback (most recent call last):
        ...
TypeError: wel_maker() missing 1 required positional argument: 'mdata'
>>> random.seed(2)
>>> pyrgg_gen_using(lp_maker, file_name='testfile', min_weight=0, max_weight=200, vertices_number=10, min_edge=0, max_edge=2, sign=True, direct=True, self_loop=True, multigraph=False)
7
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
edge(5,6,148).
edge(5,9,110).
edge(6,10,-139).
edge(7,7,7).
edge(8,2,-97).
edge(9,1,60).
<BLANKLINE>
>>> random.seed(4)
>>> pyrgg_gen_using(lp_maker, file_name='testfile2', min_weight=0, max_weight=50, vertices_number=30, min_edge=0, max_edge=4, sign=True, direct=True, self_loop=True, multigraph=False)
35
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
edge(2,18,5).
edge(2,4,25).
edge(2,22,-48).
edge(4,23,-17).
edge(5,7,-13).
edge(7,15,10).
edge(7,17,-40).
edge(8,8,-42).
edge(8,25,11).
edge(9,29,-5).
edge(10,3,-36).
edge(10,27,-48).
edge(11,13,-27).
edge(11,26,-27).
edge(11,21,14).
edge(11,16,-2).
edge(14,20,-44).
edge(14,14,43).
edge(14,12,26).
edge(15,28,-11).
edge(16,30,-40).
edge(16,24,20).
edge(19,19,7).
edge(20,12,-29).
edge(20,1,22).
edge(22,24,20).
edge(22,23,-9).
edge(23,18,18).
edge(23,27,28).
edge(24,6,-24).
edge(25,17,23).
edge(27,6,-50).
edge(28,21,28).
edge(28,13,-13).
<BLANKLINE>
>>> random.seed(2)
>>> pyrgg_gen_using(tgf_maker, file_name='testfile', min_weight=0, max_weight=200, vertices_number=10, min_edge=0, max_edge=2, sign=True, direct=True, self_loop=True, multigraph=False)
7
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
5 6 148
5 9 110
6 10 -139
7 7 7
8 2 -97
9 1 60
<BLANKLINE>
>>> random.seed(4)
>>> pyrgg_gen_using(tgf_maker, file_name='testfile2', min_weight=0, max_weight=50, vertices_number=30, min_edge=0, max_edge=4, sign=True, direct=True, self_loop=True, multigraph=False)
35
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
2 18 5
2 4 25
2 22 -48
4 23 -17
5 7 -13
7 15 10
7 17 -40
8 8 -42
8 25 11
9 29 -5
10 3 -36
10 27 -48
11 13 -27
11 26 -27
11 21 14
11 16 -2
14 20 -44
14 14 43
14 12 26
15 28 -11
16 30 -40
16 24 20
19 19 7
20 12 -29
20 1 22
22 24 20
22 23 -9
23 18 18
23 27 28
24 6 -24
25 17 23
27 6 -50
28 21 28
28 13 -13
<BLANKLINE>
>>> random.seed(2)
>>> pyrgg_gen_using(dl_maker, file_name='testfile', min_weight=0, max_weight=200, vertices_number=10, min_edge=0, max_edge=2, sign=True, direct=True, self_loop=True, multigraph=False)
7
>>> file=open('testfile.dl','r')
>>> print(file.read())
dl
format=edgelist1
n=10
data:
4 3 -64
5 6 148
5 9 110
6 10 -139
7 7 7
8 2 -97
9 1 60
<BLANKLINE>
>>> random.seed(4)
>>> pyrgg_gen_using(dl_maker, file_name='testfile2', min_weight=0, max_weight=50, vertices_number=30, min_edge=0, max_edge=4, sign=True, direct=True, self_loop=True, multigraph=False)
35
>>> file=open('testfile2.dl','r')
>>> print(file.read())
dl
format=edgelist1
n=30
data:
1 10 46
2 18 5
2 4 25
2 22 -48
4 23 -17
5 7 -13
7 15 10
7 17 -40
8 8 -42
8 25 11
9 29 -5
10 3 -36
10 27 -48
11 13 -27
11 26 -27
11 21 14
11 16 -2
14 20 -44
14 14 43
14 12 26
15 28 -11
16 30 -40
16 24 20
19 19 7
20 12 -29
20 1 22
22 24 20
22 23 -9
23 18 18
23 27 28
24 6 -24
25 17 23
27 6 -50
28 21 28
28 13 -13
<BLANKLINE>
>>> random.seed(4)
>>> pyrgg_gen_using(dimacs_maker, file_name='testfile4', min_weight=0, max_weight=50, vertices_number=30, min_edge=0, max_edge=4, sign=True, direct=True, self_loop=False, multigraph=False)
37
>>> file=open('testfile4.gr','r')
>>> print(file.read())
c FILE                  :testfile4.gr
c No. of vertices       :30
c No. of edges          :37
c Max. weight           :50
c Min. weight           :0
c Min. edge             :0
c Max. edge             :4
p sp 30 37
a 1 11 46
a 2 19 5
a 2 5 25
a 2 23 -48
a 4 24 -17
a 5 8 -13
a 7 16 10
a 7 18 -40
a 8 9 -42
a 8 26 11
a 9 30 -5
a 10 29 0
a 10 14 -48
a 10 22 26
a 10 20 -27
a 11 12 19
a 11 17 5
a 11 3 -40
a 12 25 -44
a 12 15 43
a 13 6 -12
a 14 27 22
a 14 28 -40
a 14 21 -6
a 16 19 7
a 17 15 -29
a 17 1 22
a 19 25 20
a 20 21 49
a 20 28 -39
a 21 4 -39
a 21 18 -18
a 22 24 -38
a 23 13 23
a 25 6 -50
a 26 29 28
a 26 3 -13
<BLANKLINE>
>>> random.seed(2)
>>> pyrgg_gen_using(gml_maker, file_name='testfile', min_weight=0, max_weight=200, vertices_number=10, min_edge=0, max_edge=2, sign=True, direct=True, self_loop=True, multigraph=False)
7
>>> gml1 = read_gml("testfile.gml")
>>> type(gml1)
<class 'networkx.classes.digraph.DiGraph'>
>>> random.seed(4)
>>> pyrgg_gen_using(gml_maker, file_name='testfile2', min_weight=0, max_weight=50, vertices_number=30, min_edge=0, max_edge=4, sign=True, direct=True, self_loop=True, multigraph=True)
38
>>> gml2 = read_gml("testfile2.gml")
>>> type(gml2)
<class 'networkx.classes.multidigraph.MultiDiGraph'>
>>> random.seed(20)
>>> pyrgg_gen_using(gml_maker, file_name='testfile3', min_weight=0, max_weight=50, vertices_number=30, min_edge=0, max_edge=4, sign=True, direct=False, self_loop=True, multigraph=True)
35
>>> gml3 = read_gml("testfile3.gml")
>>> type(gml3)
<class 'networkx.classes.multigraph.MultiGraph'>
>>> random.seed(120)
>>> pyrgg_gen_using(gml_maker, file_name='testfile4', min_weight=0, max_weight=50, vertices_number=30, min_edge=0, max_edge=4, sign=True, direct=False, self_loop=True, multigraph=False)
35
>>> gml4 = read_gml("testfile4.gml")
>>> type(gml4)
<class 'networkx.classes.graph.Graph'>
>>> random.seed(2)
>>> pyrgg_gen_using(gexf_maker, file_name='testfile', min_weight=0, max_weight=200, vertices_number=10, min_edge=0, max_edge=2, sign=True, direct=True, self_loop=True, multigraph=False)
7
>>> gexf1 = read_gexf("testfile.gexf")
>>> type(gexf1)
<class 'networkx.classes.digraph.DiGraph'>
>>> random.seed(8)
>>> pyrgg_gen_using(gexf_maker, file_name='testfile2', min_weight=0, max_weight=50, vertices_number=30, min_edge=0, max_edge=4, sign=True, direct=True, self_loop=True, multigraph=True)
35
>>> gexf2 = read_gexf("testfile2.gexf")
>>> type(gexf2)
<class 'networkx.classes.multidigraph.MultiDiGraph'>
>>> random.seed(20)
>>> pyrgg_gen_using(gexf_maker, file_name='testfile3', min_weight=0, max_weight=50, vertices_number=30, min_edge=0, max_edge=4, sign=True, direct=False, self_loop=True, multigraph=True)
35
>>> gexf3 = read_gexf("testfile3.gexf")
>>> type(gexf3)
<class 'networkx.classes.multigraph.MultiGraph'>
>>> random.seed(120)
>>> pyrgg_gen_using(gexf_maker, file_name='testfile4', min_weight=0, max_weight=50, vertices_number=30, min_edge=0, max_edge=4, sign=True, direct=False, self_loop=True, multigraph=False)
35
>>> gexf4 = read_gexf("testfile4.gexf")
>>> type(gexf4)
<class 'networkx.classes.graph.Graph'>
>>> random.seed(120)
>>> pyrgg_gen_using(gexf_maker, file_name='testfile5', min_weight=0, max_weight=50.2, vertices_number=30, min_edge=0, max_edge=4, sign=True, direct=False, self_loop=True, multigraph=False)
40
>>> gexf5 = read_gexf("testfile5.gexf")
>>> type(gexf5)
<class 'networkx.classes.graph.Graph'>
>>> random.seed(2)
>>> pyrgg_gen_using(csv_maker, file_name='testfile4', min_weight=0.0, max_weight=200.22, vertices_number=10, min_edge=0, max_edge=2, sign=True, direct=True, self_loop=True, multigraph=False)
5
>>> file = open("testfile4.csv")
>>> print(file.read())
4,3,-50.37
6,1,200.16
6,9,-160.91
7,7,-100.52
10,10,-181.75
<BLANKLINE>
>>> random.seed(2)
>>> pyrgg_gen_using(csv_maker, file_name='testfile4', min_weight=0.0, max_weight=200.222, vertices_number=10, min_edge=0, max_edge=2, sign=True, direct=True, self_loop=True, multigraph=False)
5
>>> file = open("testfile4.csv")
>>> print(file.read())
4,3,-50.373
6,1,200.166
6,9,-160.912
7,7,-100.525
10,10,-181.752
<BLANKLINE>
>>> import pydot
>>> random.seed(4)
>>> pyrgg_gen_using(dot_maker, file_name='testfile', min_weight=0, max_weight=50, vertices_number=30, min_edge=0, max_edge=4, sign=True, direct=True, self_loop=False, multigraph=False)
37
>>> file=open('testfile.gv','r')
>>> g1 = pydot.graph_from_dot_data(file.read())
>>> g1[0].get_type()
'digraph'
>>> len(g1[0].get_edge_list())
37
>>> random.seed(4)
>>> pyrgg_gen_using(dot_maker, file_name='testfile2', min_weight=0, max_weight=50, vertices_number=30, min_edge=0, max_edge=4, sign=True, direct=False, self_loop=False, multigraph=False)
37
>>> file=open('testfile2.gv','r')
>>> g2 = pydot.graph_from_dot_data(file.read())
>>> g2[0].get_type()
'graph'
>>> len(g2[0].get_edge_list())
37
>>> random.seed(4)
>>> pyrgg_gen_using(dot_maker, file_name='testfile3', min_weight=0, max_weight=50, vertices_number=30, min_edge=0, max_edge=4, sign=True, direct=False, self_loop=False, multigraph=True)
40
>>> file=open('testfile3.gv','r')
>>> g3 = pydot.graph_from_dot_data(file.read())
>>> g3[0].get_type()
'graph'
>>> len(g3[0].get_edge_list())
40
>>> random.seed(4)
>>> pyrgg_gen_using(dot_maker, file_name='testfile4', min_weight=1, max_weight=1, vertices_number=30, min_edge=0, max_edge=4, sign=True, direct=False, self_loop=False, multigraph=True)
42
>>> file=open('testfile4.gv','r')
>>> g4 = pydot.graph_from_dot_data(file.read())
>>> g4[0].get_type()
'graph'
>>> len(g4[0].get_edge_list())
42
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
>>> os.remove('testfile.gv')
>>> os.remove('testfile2.gv')
>>> os.remove('testfile3.gv')
>>> os.remove('testfile4.gv')
>>> os.remove('logfile.log')

"""
