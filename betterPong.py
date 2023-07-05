import random
import pygame as pg
import math as maths
import csv
import os

SCREEN_SIZE = (1000, 800)

pg.init()
window = pg.display.set_mode(SCREEN_SIZE)

clock = pg.time.Clock()

middle_of_screen = pg.Vector2(window.get_width() / 2, window.get_height() / 2)


WASD = ["w", "a", "s", "d"]
ARROWS = ["UP", "LEFT", "DOWN", "RIGHT"]

class BALL():
    def __init__(self, position, colour, size, speed, direction, angle, degree_of_angle):
        self.position = position
        self.colour = colour
        self.size = size
        self.speed = speed
        self.direction = direction
        self.angle = angle
        self.degree_of_angle = degree_of_angle
        
    def Place_on_screen(self):
        pg.draw.circle(window, "white", self.position, self.size)

    def Move(self):
        if self.direction == "left":
            self.position.x -= self.speed * dt
        if self.direction == "right":
            self.position.x += self.speed *dt

        if self.angle == "up":
            self.position.y -= self.degree_of_angle * dt
        if self.angle == "down":
            self.position.y += self.degree_of_angle * dt

    def collision(self, Rpaddle, Lpaddle, middle):
        self.position.x = int(self.position.x)
        self.position.y = int(self.position.y)
        
        if self.position.x <= 50:
            if Lpaddle.position[1] <= self.position.y and Lpaddle.position[1] + 125 >= self.position.y:
                self.direction = "right"
                self.speed += 15
            elif self.position.x < 1000:
                self.position = pg.Vector2(window.get_width() / 2, window.get_height() / 2)
                Rpaddle.points += 1
                self.speed = 250
        elif self.position.x >= 950:
            if Rpaddle.position[1] <= self.position.y and Rpaddle.position[1] + 125 >= self.position.y:
                self.direction = "left"
                self.speed += 15
            elif self.position.x > 0:
                self.position = pg.Vector2(window.get_width() / 2, window.get_height() / 2)
                Lpaddle.points += 1
                self.speed = 250
            
        

class PADDLE():
    def __init__(self, position, colour, collision_point, key_set, points):
        self.position = position
        self.colour = colour
        self.collision_point = collision_point
        self.key_set = key_set
        self.points = points

    def Place_on_The_screen(self):
        pg.draw.rect(window, self.colour, pg.Rect(self.position))

    def Move(self, WASD, ARROWS):
        KEY = pg.key.get_pressed()
        if self.key_set == "arrows":
            
            if KEY[pg.K_UP]:
                self.position[1] -= 8
            if KEY[pg.K_DOWN]:
                self.position[1] += 8
                
        elif self.key_set == "wasd":
        
            if KEY[pg.K_w]:
                self.position[1] -= 8
            if KEY[pg.K_s]:
                self.position[1] += 8

class SCORE():
    def __init__(self, score, position, side):
        self.score = score
        self.position = position
        self.side = side
        self.scores =  ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
        self.image = ""

    def Display(self, true_score):
        self.score = true_score
        self.image = pg.image.load(self.scores[self.score] + ".png")
        window.blit(self.image, self.position)
        
        
the_ball = BALL(middle_of_screen, "white", 8, 300, random.choice(["left", "right"]), "middle", 0)

left_score = SCORE(0, (150.0, 0.0), "left")
right_score = SCORE(0, (650.0, 0.0), "right")

right_paddle = PADDLE([950, 350, 20, 125], "white", 0, "arrows", 0)
left_paddle = PADDLE([30, 350, 20, 125], "white", 0, "wasd", 0)

dt = 0# this has something todo with the framerate
run = True #this is what decides whether the main loop is running or not

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            
    window.fill("black")

    pg.draw.line(window, "white", (500, 0), (500, 800), width = 3)

    the_ball.Move()
    the_ball.Place_on_screen()

    left_paddle.Move(WASD, ARROWS)
    left_paddle.Place_on_The_screen()

    right_paddle.Move(WASD, ARROWS)
    right_paddle.Place_on_The_screen()

    left_score.Display(left_paddle.points)
    right_score.Display(right_paddle.points)

    the_ball.collision(right_paddle, left_paddle, middle_of_screen)
        
    pg.display.flip()
    dt = clock.tick(60)/ 1000

