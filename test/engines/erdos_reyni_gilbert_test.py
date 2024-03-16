# -*- coding: utf-8 -*-
"""
>>> from pyrgg.functions import *
>>> import pyrgg.params
>>> import random
>>> import os
>>> import pyrgg.engines.erdos_reyni_gilbert as engine
>>> os.environ["PYRGG_TEST_MODE"] = "1"
>>> ######################################
>>> ## ========= logger function =========
>>> ######################################
>>> with open('logfile.log','a') as file:
...     engine.logger(file,'test','2min',{'vertices':100,'edge_number':50,'engine':1,'probability':0.5,'output_format':1})
>>> file = open('logfile.log','r')
>>> print("\\n".join(file.read().splitlines()[1:-1]))
Filename : test
Probability : 0.5
Vertices : 100
Total Edges : 50
Engine : 1 (pyrgg)
Elapsed Time : 2min
>>> class StrError:
...     def __init__(self):
...         pass
...     def __str__(self):
...         raise ValueError
>>> str_error_object = StrError()
>>> with open('logfile.log','a') as file:
...     engine.logger(file,'test','2min',{'vertices':str_error_object,'edge_number':50,'engine':1,'probability':0.5,'output_format':1})
[Error] Logger failed!
>>> ##########################################
>>> ## ========= edge_gen function =========
>>> ##########################################
>>> random.seed(2)
>>> engine.edge_gen(20, 0.5)
[{1: [4, 5, 9, 13, 14, 15, 20], 2: [3, 4, 5, 6, 7, 8, 12, 13, 14, 15, 19], 3: [9, 12, 15, 17], 4: [5, 8, 12, 13, 14, 16, 18, 20], 5: [12, 13, 17], 6: [7, 9, 11, 12, 14, 17, 18, 20], 7: [9, 10, 11, 13, 15, 17, 18, 20], 8: [9, 11, 12, 14, 15, 16, 19, 20], 9: [10, 11, 18, 19], 10: [11, 12, 13, 15, 17, 19], 11: [12, 14, 15, 17, 18, 19, 20], 12: [13, 19, 20], 13: [14, 19, 20], 14: [16, 17, 18, 19], 15: [16, 17, 18, 19, 20], 16: [18, 19], 17: [18], 18: [20], 19: [], 20: []}, 93]
>>> random.seed(11)
>>> engine.edge_gen(20, 0.1)
[{1: [12, 14, 17], 2: [5, 7, 10], 3: [10, 17], 4: [7, 11, 18], 5: [], 6: [17, 18], 7: [], 8: [17], 9: [16], 10: [14, 17], 11: [20], 12: [13, 17], 13: [16], 14: [], 15: [], 16: [], 17: [18], 18: [], 19: [], 20: []}, 22]
>>> engine.edge_gen(0)
Traceback (most recent call last):
        ...
TypeError: edge_gen() missing 1 required positional argument: 'p'
>>> #########################################
>>> ## ========= gen_using function =========
>>> #########################################
>>> os.remove('logfile.log')
"""