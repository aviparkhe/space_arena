import turtle, math, random
from space_arena import *

from sprite import Sprite

class Enemy(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.max_health = 20
        self.health = self.max_health
        self.type = random.choice(["hunter", "mine", "surveillance"])

        if self.type == "hunter":
            self.color = "red"
            self.shape = "square"

        elif self.type == "mine":
            self.color = "orange"
            self.shape = "square"

        elif self.type == "surveillance":
            self.color = "pink"
            self.shape = "square"


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

            # Code for different types
            if self.type == "hunter":
                if self.x < player.x:
                    self.dx += 0.05
                else:
                    self.dx -= 0.05
                if self.y < player.y:
                    self.dy += 0.05
                else:
                    self.dy -= 0.05

            elif self.type == "mine":
                self.dx = 0
                self.dy = 0

            elif self.type == "surveillance":
                if self.x < player.x:
                    self.dx -= 0.05
                else:
                    self.dx += 0.05
                if self.y < player.y:
                    self.dy -= 0.05
                else:
                    self.dy += 0.05

            # Set max speed
            if self.dx > self.max_dx:
                self.dx = self.max_dx
            elif self.dx < -self.max_dx:
                self.dx = -self.max_dx

            if self.dy > self.max_dy:
                self.dy = self.max_dy
            elif self.dy < -self.max_dy:
                self.dy = -self.max_dy

    def reset(self):
        self.state = "inactive"