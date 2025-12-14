# -*- coding: utf-8 -*-
"""Erdős-Rényi Engine Profile."""
from pyrgg import *
import pyrgg.engines.erdos_reyni as er_engine
import random

os.environ["PYRGG_TEST_MODE"] = "1"
random.seed(400)

er_engine.generate_graph(
    generate_dimacs_file,
    'profile',
    {
        'vertices': 10000,
        'edge_number': 5000,
        'direct': 1,
    }
)
