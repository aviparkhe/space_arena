import turtle, math, random
from space_arena import *

from sprite import Sprite

class Powerup(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)