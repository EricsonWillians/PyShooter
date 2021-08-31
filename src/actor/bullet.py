import pygame
import math
from image import Image
from main import screen


class Bullet:

    WIDTH = 4
    HEIGHT = 4

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 24
        self.image = Image('assets/fireball.png',
                           Bullet.WIDTH, Bullet.HEIGHT).image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.discharged = False
        self.hit = False

    def draw(self):
        screen.blit(self.image, self.rect)
        if self.discharged:
            self.move()

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)

    def set_angle(self, angle):
        self.angle = angle

    def move(self):
        dx = -math.cos(math.radians(self.angle)) * self.speed
        dy = math.sin(math.radians(self.angle)) * self.speed

        self.set_pos(self.x + dx, self.y + dy)

