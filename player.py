import turtle, math, random
from space_arena import *

from sprite import Sprite

class Player(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, 0, 0, shape, color)
        self.lives = 3
        self.score = 0
        self.heading = 90
        self.da = 0

    def rotate_left(self):
        self.da = 5

    def rotate_right(self):
        self.da = -5

    def stop_rotation(self):
        self.da = 0

    def accelerate(self):
        self.thrust += self.acceleration

    def decelerate(self):
        self.thrust = 0.0

    def fire(self):
        num_of_missiles = 0
        for missile in missiles:
            if missile.state == "ready":
                num_of_missiles += 1

        print(num_of_missiles)

        # 1 missile ready
        if num_of_missiles == 1:
            directions = []
            for missile in missiles:
                if missile.state == "ready":
                    missile.fire(self.x, self.y, self.heading + directions.pop(), self.dx, self. dy)

        # 2 missiles ready
        if num_of_missiles == 2:
            directions = [-5, 5]
            for missile in missiles:
                if missile.state == "ready":
                    missile.fire(self.x, self.y, self.heading + directions.pop(), self.dx, self. dy)

        # 3 missiles ready
        if num_of_missiles == 3:
            directions = [0, -5, 5]
            for missile in missiles:
                if missile.state == "ready":
                    missile.fire(self.x, self.y, self.heading +directions.pop(), self.dx, self. dy)

    def update(self):
        if self.state == "active":
            self.heading += self.da
            self.heading %= 360

            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust

            self.x += self.dx
            self.y += self.dy

            self.border_check()

            # Check health
            if self.health <= 0:
                self.reset()

    def reset(self):
        self.x = 0
        self.y = 0
        self.health = self.max_health
        self.heading = 90
        self.dx = 0
        self.dy = 0
        self.lives -= 1

    def render(self, pen, x_offset, y_offset):
        pen.shapesize(0.5, 1.0, None)
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.setheading(self.heading)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()

        pen.shapesize(1.0, 1.0, None)

        self.render_health_meter(pen, x_offset, y_offset)