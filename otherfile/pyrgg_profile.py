# -*- coding: utf-8 -*-
"""Profile file."""
from pyrgg import *
import pyrgg.params
import random

pyrgg.params.PYRGG_TEST_MODE = True
random.seed(400)

file_name = 'profile'
min_weight = 1
max_weight = 5000
vertices = 10000
min_edge = 5
max_edge = 600
sign = 0
direct = 1
self_loop = 1
multigraph = 1

pyrgg_gen_using(dimacs_maker,
                     file_name,
                     min_weight,
                     max_weight,
                     vertices,
                     min_edge,
                     max_edge,
                     sign,
                     direct,
                     self_loop,
                     multigraph)