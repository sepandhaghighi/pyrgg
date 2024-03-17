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
