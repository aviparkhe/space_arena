# Space Arena - The Ultimate Turtle Graphics Game

import turtle
import math
import random

from game import Game
from character_pen import CharacterPen
from sprite import Sprite
from player  import Player
from missile import Missile
from enemy import Enemy
from powerup import Powerup
from camera import Camera
from radar import Radar

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

wn = turtle.Screen()
wn.setup(SCREEN_WIDTH + 220, SCREEN_HEIGHT + 20)
wn.title("Space Arena")
wn.bgcolor("black")
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

character_pen = CharacterPen("red", 3.0)


# Create game object
game = Game(700, 500)

# Create the radar object
radar = Radar(400, -200, 200, 200)

# Create player sprite
player = Player(0, 0, "triangle", "white")

# Create camera
camera = Camera(player.x, player.y)

# Create missile objects
missiles = []
for _ in range(3):
    missiles.append(Missile(0, 100, "circle", "yellow"))

# Sprites list
sprites = []

# Setup the level
game.start_level()

# Keyboard bindings
wn.listen()
wn.onkeypress(player.rotate_left, "Left")
wn.onkeypress(player.rotate_right, "Right")

wn.onkeyrelease(player.stop_rotation, "Left")
wn.onkeyrelease(player.stop_rotation, "Right")

wn.onkeypress(player.accelerate, "Up")
wn.onkeyrelease(player.decelerate, "Up")

wn.onkeypress(player.fire, "space")

# Main Loop
while True:
    # Clear screen
    pen.clear()

    # Do game stuff
    # Update sprites
    for sprite in sprites:
        sprite.update()

    # Check for collisions
    for sprite in sprites:
        if isinstance(sprite, Enemy) and sprite.state == "active":
            if player.is_collision(sprite):
                sprite.health -= 10
                player.health -= 10
                player.bounce(sprite)

            for missile in missiles:
                if missile.state == "active" and missile.is_collision(sprite):
                    sprite.health -= 10
                    missile.reset()

        if isinstance(sprite, Powerup):
            if player.is_collision(sprite):
                sprite.x = 100
                sprite.y = 100

            for missile in missiles:
                if missile.state == "active" and missile.is_collision(sprite):
                    sprite.x = 100
                    sprite.y = -100
                    missile.reset()


    # Render sprites
    for sprite in sprites:
        sprite.render(pen, camera.x + 100, camera.y)

    game.render_border(pen, camera.x + 100, camera.y)

    # Check for end of level
    end_of_level = True
    for sprite in sprites:
        # Look for an active enemy
        if isinstance(sprite, Enemy) and sprite.state == "active":
            end_of_level = False
    if end_of_level:
        game.level += 1
        game.start_level()

    # Update the camera
    camera.update(player.x, player.y)

    # Draw text
    game.render_info(pen, 0, 0)

    # Render the radar
    radar.render(pen, sprites)


    # Update the screen
    wn.update()

