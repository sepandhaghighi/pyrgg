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
Cut-off Threshold : 0.5
Total Edges : 50
Engine : 7 (gg)
Elapsed Time : 2min
"""