# -*- coding: utf-8 -*-
"""Random Geometric Graph Engine Profile."""
from pyrgg import *
import pyrgg.engines.geometric_graph as gg_engine
import random

os.environ["PYRGG_TEST_MODE"] = "1"
random.seed(400)

gg_engine.gen_using(
    dimacs_maker,
    'profile',
    {
        'vertices': 10000,
        'space_dimension': 10,
        'cutoff_threshold': 0.5,
    }
)
