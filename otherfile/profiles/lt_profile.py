# -*- coding: utf-8 -*-
"""Labeled Tree Generator Engine Profile."""
from pyrgg import *
import pyrgg.engines.labeled_tree as lt_engine
import random

os.environ["PYRGG_TEST_MODE"] = "1"
random.seed(400)

lt_engine.generate_graph(
    generate_dimacs_file,
    'profile',
    {
        'vertices': 10000,
    }
)
