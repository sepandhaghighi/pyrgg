# -*- coding: utf-8 -*-
"""Profile file."""
from pyrgg import *
import pyrgg.engines.erdos_reyni as er_engine
import random

os.environ["PYRGG_TEST_MODE"] = "1"
random.seed(400)

er_engine.gen_using(
    dimacs_maker,
    'profile',
    {
        'vertices': 10000,
        'edge_number': 5000,
        'direct': 1,
    }
)
