# -*- coding: utf-8 -*-
"""Profile file."""
from pyrgg import *
import pyrgg.engines.watts_strogatz as ws_engine
import random

os.environ["PYRGG_TEST_MODE"] = "1"
random.seed(400)

ws_engine.gen_using(
    dimacs_maker,
    'profile',
    {
        'vertices': 10000,
        'mean_degree': 500,
        'rewiring_probability': 0.3,
    }
)
