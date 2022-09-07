# -*- coding: utf-8 -*-
"""Profile file."""
from pyrgg import *
import pyrgg.params
import random

pyrgg.params.PYRGG_TEST_MODE = True
random.seed(400)
dimacs_maker('profile', 1, 5000, 10000, 5, 600, 0, 1, 1, 1)
