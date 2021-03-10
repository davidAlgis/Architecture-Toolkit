from Selectable import *
import numpy as np

class Wall(Selectable):
    def __init__(self, origin:np.array(2, dtype=float), width = 0.15, length = 1, angle = 0):
        self.origin = origin
        self.width = width
        self.length = length
        self.angle = angle


