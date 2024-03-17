# -*- coding: utf-8 -*-
"""Profile file."""
from pyrgg import *
import pyrgg.params
import pyrgg.engines.pyrgg as pyrgg_engine
import random

os.environ["PYRGG_TEST_MODE"] = "1"
random.seed(400)

pyrgg_engine.gen_using(
    dimacs_maker,
    'profile',
    {
        'min_weight':1,
        'max_weight':5000,
        'vertices':10000,
        'min_edge':5,
        'max_edge':600,
        'sign':0,
        'direct':1,
        'self_loop':1,
        'multigraph':1,
    }
    )
