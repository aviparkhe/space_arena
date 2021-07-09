import turtle, math, random
from space_arena import *

class Radar():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render(self, pen, sprites):

        # Draw radar circle
        pen.color("white")
        pen.setheading(90)
        pen.goto(self.x + self.width / 2.0, self.y)
        pen.pendown()
        pen.circle(self.width / 2.0)
        pen.penup()

        # Draw sprites
        for sprite in sprites:
            if sprite.state == "active":
                radar_x = self.x + (sprite.x - player.x) * (self.width/game.width)
                radar_y = self.y + (sprite.y - player.y) * (self.height/game.height)
                pen.goto(radar_x, radar_y)
                pen.color(sprite.color)
                pen.shape(sprite.shape)
                pen.setheading(sprite.heading)
                pen.shapesize(0.1, 0.1, None)

                # Make sure the sprite is close to the player
                distance = ((player.x-sprite.x)**2 + (player.y-sprite.y)**2)**0.5
                if distance < player.radar:
                    pen.stamp()