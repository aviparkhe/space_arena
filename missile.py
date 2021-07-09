import turtle, math, random
from space_arena import *

from sprite import Sprite

class Missile(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.state = "ready"
        self.thrust = 8.0
        self.max_fuel = 200
        self.fuel = self.max_fuel
        self.height = 4
        self.width = 4

    def fire(self, x, y, heading, dx, dy):
        if self.state == "ready":
            self.state = "active"
            self.x = x
            self.y = y
            self.heading = heading
            self.dx = dx
            self.dy = dy

            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust

    def update(self):
        if self.state == "active":
            self.fuel -= self.thrust
            if self.fuel <= 0:
                self.reset()

            self.heading += self.da
            self.heading %= 360

            self.x += self.dx
            self.y += self.dy

            self.border_check()

    def reset(self):
        self.fuel = self.max_fuel
        self.dx = 0
        self.dy = 0
        self.state = "ready"

    def render(self, pen, x_offset, y_offset):
        if self.state == "active":
            pen.shapesize(0.2, 0.2, None)
            pen.goto(self.x - x_offset, self.y - y_offset)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp()

            pen.shapesize(1.0, 1.0, None)