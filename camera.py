import turtle, math, random
from space_arena import *

class Camera():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, x, y):
        self.x = x
        self.y = y