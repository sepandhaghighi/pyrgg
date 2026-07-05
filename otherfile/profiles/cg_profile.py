# -*- coding: utf-8 -*-
"""Complete Graph Engine Profile."""
from pyrgg import *
import pyrgg.engines.complete_graph as cg_engine
import random

os.environ["PYRGG_TEST_MODE"] = "1"
random.seed(400)

cg_engine.generate_graph(
    generate_dimacs_file,
    'profile',
    {
        'vertices': 10000,
        'min_weight':1,
        'max_weight':5000,
        'direct': 1,
    }
)
