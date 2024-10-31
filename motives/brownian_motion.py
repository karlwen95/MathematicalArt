"""
A brownian motion is a random walk, with equal probability for moving up or down in the next step.
Enable weight/skewness to the walk, favouring up or down movement.
"""

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

class Brownian_motion:

    def __init__(self,
                 x_width: int = 10,
                 y_width: int = 10,
                 resolution: int = 1000,
                 ):
        self.x_lim = x_width
        self.y_lim = y_width
        self.y_start = 0


