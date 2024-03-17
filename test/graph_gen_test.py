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
>>> os.environ["PYRGG_TEST_MODE"] = "1"
>>> dimacs_maker({}, {})
Traceback (most recent call last):
        ...
TypeError: dimacs_maker() missing 1 required positional argument: 'mdata'
>>> random.seed(2)
>>> engine.gen_using(json_maker, 'testfile', {'min_weight':0, 'max_weight':200, 'vertices':10, 'min_edge':0, 'max_edge':2, 'sign':True, 'direct':True, 'self_loop':True, 'multigraph':False})
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
>>> engine.gen_using(json_maker, 'testfile2', {'min_weight':0, 'max_weight':50, 'vertices':30, 'min_edge':0, 'max_edge':4, 'sign':True, 'direct':True, 'self_loop':True, 'multigraph':False})
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
>>> engine.gen_using(json_maker, 'testfile3', {'min_weight':10, 'max_weight':30, 'vertices':100, 'min_edge':0, 'max_edge':4, 'sign':False, 'direct':True, 'self_loop':True, 'multigraph':False})
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
>>> os.remove('testfile.json')
>>> os.remove('testfile.p')
>>> os.remove('testfile.yaml')
>>> os.remove('testfile2.json')
>>> os.remove('testfile2.p')
>>> os.remove('testfile2.yaml')
>>> os.remove('testfile3.json')
>>> os.remove('testfile3.p')
>>> os.remove('testfile3.yaml')
"""
