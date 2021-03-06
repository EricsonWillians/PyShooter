import pygame
from image import Image
from actor import bullet
from main import screen
from math import atan2, pi
import time


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.initial_speed = 4
        self.speed = self.initial_speed
        self.running_speed = 6
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
            'SHOOTING': False,
            'RUNNING': False
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
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                self.actions['SHOOTING'] = True
            if event.key == pygame.K_LSHIFT:
                self.actions['RUNNING'] = True
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
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                self.actions['SHOOTING'] = False
            if event.key == pygame.K_LSHIFT:
                self.actions['RUNNING'] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            left_mouse_button = pygame.mouse.get_pressed()[0]
            if left_mouse_button:
                self.actions['SHOOTING'] = True
        if event.type == pygame.MOUSEBUTTONUP:
            left_mouse_button = pygame.mouse.get_pressed()[0]
            if not left_mouse_button:
                self.actions['SHOOTING'] = False
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print(pygame.mouse.get_pos())
            x = mouse_x - (self.x + self.rect.width / 3)
            y = mouse_y - (self.y - self.rect.height / 3)
            self.angle = ((180 / pi) * (-atan2(-x, y))) + 90

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
        self.hand_distance_x = self.rect.width / 3
        self.hand_distance_y = self.rect.height / 3
        for bullet in self.clip:
            if not bullet.discharged:
                # TODO: Adjust bullet position
                bullet.set_pos(self.x + self.hand_distance_x, self.y - self.hand_distance_y)
                bullet.set_angle(self.angle)

    def act(self):
        if self.actions['TURNING_LEFT']:
            self.angle += self.turning_speed % 360
        if self.actions['TURNING_RIGHT']:
            self.angle -= self.turning_speed % 360
        if self.actions['SHOOTING']:
            self.shoot()
        if self.actions['RUNNING']:
            self.speed = self.running_speed
        else:
            self.speed = self.initial_speed
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
