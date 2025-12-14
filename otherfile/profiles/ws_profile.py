# -*- coding: utf-8 -*-
"""Watts-Strogatz Engine Profile."""
from pyrgg import *
import pyrgg.engines.watts_strogatz as ws_engine
import random

os.environ["PYRGG_TEST_MODE"] = "1"
random.seed(400)

ws_engine.generate_graph(
    generate_dimacs_file,
    'profile',
    {
        'vertices': 10,
        'mean_degree': 2,
        'rewiring_probability': 0.3,
    }
)
