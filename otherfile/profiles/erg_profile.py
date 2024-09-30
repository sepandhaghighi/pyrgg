# -*- coding: utf-8 -*-
"""Profile file."""
from pyrgg import *
import pyrgg.engines.erdos_reyni_gilbert as erg_engine
import random

os.environ["PYRGG_TEST_MODE"] = "1"
random.seed(400)

erg_engine.gen_using(
    dimacs_maker,
    'profile',
    {
        'vertices': 10000,
        'probability': 0.5,
        'direct': 1,
    }
)
