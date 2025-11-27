# -*- coding: utf-8 -*-
"""Barabási-Albert Engine Profile."""
from pyrgg import *
import pyrgg.engines.barabasi_albert as ba_engine
import random

os.environ["PYRGG_TEST_MODE"] = "1"
random.seed(400)

ba_engine.generate_graph(
    dimacs_maker,
    'profile',
    {
        'vertices': 10000,
        'attaching_edge_number': 500,
    }
)
