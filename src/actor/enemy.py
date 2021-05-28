import pygame
from image import Image
from actor import bullet
from enum import Enum
import main
import time


class EnemyType(Enum):
    WEAK_ZOMBIE = 0


class Enemy:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 4
        self.turning_speed = 2.4
        self.image = Image('assets/enemy.png').image
        self.transformed_image = self.image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = 90
        self.directions = {
            'UP': False,
            'DOWN': False,
            'LEFT': False,
            'RIGHT': False
        }
        self.actions = {
            'TURNING_LEFT': False,
            'TURNING_RIGHT': False,
            'SHOOTING': False
        }
        self.start_time = pygame.time.get_ticks()
        self.last_shot = pygame.time.get_ticks()
        self.type = EnemyType.WEAK_ZOMBIE

    def draw(self):
        self.update()
        main.screen.blit(self.transformed_image, self.rect)

    def update(self):
        self.transformed_image = pygame.transform.rotate(
            self.image, self.angle)
        x, y = self.rect.center
        self.rect = self.transformed_image.get_rect()
        self.rect.center = (x, y)
