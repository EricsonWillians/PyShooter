import pygame
from image import Image
from main import screen


class Bullet:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 4
        self.image = Image('assets/fireball_0.png').image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.discharged = False
        self.hit = False

    def draw(self):
        screen.blit(self.image, self.rect)

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)
