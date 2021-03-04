import pygame
from image import Image
from main import screen


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 4
        self.turning_speed = 2.4
        self.image = Image('assets/python_logo.png').image
        self.transformed_image = self.image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = 360
        self.directions = {
            'UP': False,
            'DOWN': False,
            'LEFT': False,
            'RIGHT': False
        }
        self.actions = {
            'TURN_LEFT': False,
            'TURN_RIGHT': False,
            'SHOOTING': False
        }

    def draw(self):
        self.update()
        screen.blit(self.transformed_image, self.rect)

    def update(self):
        self.transformed_image = pygame.transform.rotate(
            self.image, self.angle)
        x, y = self.rect.center
        self.rect = self.transformed_image.get_rect()
        self.rect.center = (x, y)

    def capture_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.directions['LEFT'] = True
            if event.key == pygame.K_d:
                self.directions['RIGHT'] = True
            if event.key == pygame.K_w:
                self.directions['UP'] = True
            if event.key == pygame.K_s:
                self.directions['DOWN'] = True
            if event.key == pygame.K_LEFT:
                self.actions['TURN_LEFT'] = True
            if event.key == pygame.K_RIGHT:
                self.actions['TURN_RIGHT'] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.directions['LEFT'] = False
            if event.key == pygame.K_d:
                self.directions['RIGHT'] = False
            if event.key == pygame.K_w:
                self.directions['UP'] = False
            if event.key == pygame.K_s:
                self.directions['DOWN'] = False
            if event.key == pygame.K_LEFT:
                self.actions['TURN_LEFT'] = False
            if event.key == pygame.K_RIGHT:
                self.actions['TURN_RIGHT'] = False

    def move(self):
        if self.directions['LEFT']:
            self.x -= self.speed
        if self.directions['RIGHT']:
            self.x += self.speed
        if self.directions['UP']:
            self.y -= self.speed
        if self.directions['DOWN']:
            self.y += self.speed
        self.rect.center = (self.x, self.y)

    def act(self):
        if self.actions['TURN_LEFT']:
            self.angle += self.turning_speed % 360
        if self.actions['TURN_RIGHT']:
            self.angle -= self.turning_speed % 360
