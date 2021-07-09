import turtle, random, math
from space_arena import *

from sprite import Sprite

class Game():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.level = 1

    def start_level(self):
        sprites.clear()

        # Add player
        sprites.append(player)

        # Add missile
        for missile in missiles:
            sprites.append(missile)

        # Add enemies
        for _ in range(self.level):
            x = random.randint(-self.width/2, self.width/2)
            y = random.randint(-self.height/2, self.height/2)
            dx = random.randint(-2, 2)
            dy = random.randint(-2, -2)
            sprites.append(Enemy(x, y, "square", "red"))
            sprites[-1].dx = dx
            sprites[-1].dy = dy

        # Add powerups
        for _ in range(self.level):
            x = random.randint(-self.width/2, self.width/2)
            y = random.randint(-self.height/2, self.height/2)
            dx = random.randint(-2, 2)
            dy = random.randint(-2, -2)
            sprites.append(Powerup(x, y, "circle", "blue"))
            sprites[-1].dx = dx
            sprites[-1].dy = dy

    def render_border(self, pen, x_offset, y_offset):
        pen.color("white")
        pen.width(3)
        pen.penup()

        left = -self.width/2.0 - x_offset
        right = self.width/2.0 - x_offset
        top = self.height/2.0 - y_offset
        bottom = -self.height/2.0 - y_offset

        pen.goto(left, top)
        pen.pendown()
        pen.goto(right, top)
        pen.goto(right, bottom)
        pen.goto(left, bottom)
        pen.goto(left, top)
        pen.penup()

    def render_info(self, pen, score, active_enemies = 0):
        pen.color("#222255")
        pen.penup()
        pen.goto(400, 0)
        pen.shape("square")
        pen.setheading(90)
        pen.shapesize(10, 32, None)
        pen.stamp()

        pen.color("white")
        pen.width(3)
        pen.goto(300, 400)
        pen.pendown()
        pen.goto(300, -400)

        pen.penup()
        pen.color("white")
        character_pen.scale = 1.0
        character_pen.draw_string(pen, "SPACE ARENA", 400, 270)
        character_pen.draw_string(pen, "SCORE {}".format(score), 400, 240)
        character_pen.draw_string(pen, "ENEMIES {}".format(active_enemies), 400, 210)
        character_pen.draw_string(pen, "LIVES {}".format(player.lives), 400, 180)
        character_pen.draw_string(pen, "LEVEL {}".format(game.level), 400, 150)