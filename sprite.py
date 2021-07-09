import turtle, math, random
from space_arena import *

class Sprite():
    # Constructor
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.dx = 0
        self.dy = 0
        self.heading = 0
        self.da = 0
        self.thrust = 0.0
        self.acceleration = 0.2
        self.health = 100
        self.max_health = 100
        self.width = 20
        self.height = 20
        self.state = "active"
        self.radar = 200
        self.max_dx = 5
        self.max_dy = 5

    def is_collision(self, other):
        if self.x < other.x + other.width and \
                self.x + self.width > other.x and \
                self.y < other.y + other.height and \
                self.y + self.height > other.y:
            return True
        else:
            return False

    def bounce(self, other):
        temp_dx = self.dx
        temp_dy = self.dy

        self.dx = other.dx
        self.dy = other.dy

        other.dx = temp_dx
        other.dy = temp_dy

    def update(self):
        self.heading += self.da
        self.heading %= 360

        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust

        self.x += self.dx
        self.y += self.dy

        self.border_check()

    def border_check(self):
        if self.x > game.width/2.0 - 10:
            self.x = game.width/2.0 - 10
            self.dx *= -1

        elif self.x < -game.width/2.0 + 10:
            self.x = -game.width/2.0 + 10
            self.dx *= -1

        if self.y > game.height/2.0 - 10:
            self.y = game.height/2.0 - 10
            self.dy *= -1

        elif self.y < -game.height/2.0 + 10:
            self.y = -game.height/2.0 + 10
            self.dy *= -1

    def render(self, pen, x_offset, y_offset):
        if self.state == "active":
            pen.goto(self.x - x_offset, self.y - y_offset)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp()

            self.render_health_meter(pen, x_offset, y_offset)

    def render_health_meter(self, pen, x_offset, y_offset):
        # Draw health meter
        pen.goto(self.x - x_offset - 10, self.y - y_offset + 20)
        pen.width(3)
        pen.pendown()
        pen.setheading(0)

        if self.health/self.max_health < 0.3:
            pen.color("red")
        elif self.health/self.max_health < 0.7:
            pen.color("yellow")
        else:
            pen.color("green")

        pen.fd(20.0 * (self.health/self.max_health))

        if self.health != self.max_health:
            pen.color("grey")
            pen.fd(20.0 * ((self.max_health-self.health)/self.max_health))

        pen.penup()