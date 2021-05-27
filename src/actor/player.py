import pygame
from image import Image
from actor import bullet
from main import screen
import time


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 4
        self.turning_speed = 2.4
        self.image = Image('assets/player.png').image
        self.transformed_image = self.image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = -90
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
        self.ammo = 999
        self.clip = []
        self.reload_clip()
        self.last_shot = pygame.time.get_ticks()
        self.weapon_cooldown = 300

    def draw(self):
        self.update()
        screen.blit(self.transformed_image, self.rect)
        for bullet in self.clip:
            if bullet.discharged:
                bullet.draw()

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
                self.actions['TURNING_LEFT'] = True
            if event.key == pygame.K_RIGHT:
                self.actions['TURNING_RIGHT'] = True
            if event.key == pygame.K_UP:
                self.actions['SHOOTING'] = True
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
                self.actions['TURNING_LEFT'] = False
            if event.key == pygame.K_RIGHT:
                self.actions['TURNING_RIGHT'] = False
            if event.key == pygame.K_UP:
                self.actions['SHOOTING'] = False

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
        for bullet in self.clip:
            if not bullet.discharged:
                bullet.set_pos(self.x + self.rect.width / 3, self.y - self.rect.height / 3)
                bullet.set_angle(self.angle)

    def act(self):
        if self.actions['TURNING_LEFT']:
            self.angle += self.turning_speed % 360
        if self.actions['TURNING_RIGHT']:
            self.angle -= self.turning_speed % 360
        if self.actions['SHOOTING']:
            self.shoot()
        if abs(self.angle) > 360:
            self.angle = 0

    def shoot(self):
        for bullet in self.clip:
            if not bullet.discharged:
                now = pygame.time.get_ticks()
                if now - self.last_shot > self.weapon_cooldown:
                    self.last_shot = now
                    bullet.discharged = True

    def reload_clip(self):
        self.clip = [
            bullet.Bullet(self.x, self.y, self.angle) for n in range(self.ammo)]
