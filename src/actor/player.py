import pygame
from image import Image
from math import atan2, pi
import time

from weapon import Pistol, Shotgun

class Player:

    PISTOL_SELECTED = 0
    SHOTGUN_SELECTED = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.initial_speed = 4
        self.speed = self.initial_speed
        self.running_speed = 6
        self.turning_speed = 2.4
        self.image = Image('assets/player/player_pistol.png').image
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
        self.health = 100
        self.current_weapons = [Pistol(), Shotgun()]
        self.selected_weapon = self.PISTOL_SELECTED
        for weapon in self.current_weapons:
            weapon.reload_clip(self)

    def draw(self, screen):
        self.update()
        screen.blit(self.transformed_image, self.rect)
        self.current_weapons[self.selected_weapon].draw(screen)

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
            if event.key == pygame.K_1:
                self.change_weapon(self.PISTOL_SELECTED)
            if event.key == pygame.K_2:
                self.change_weapon(self.SHOTGUN_SELECTED)
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
        self.current_weapons[self.selected_weapon].update_bullet_pos(self)

    def act(self):
        if self.actions['TURNING_LEFT']:
            self.angle += self.turning_speed % 360
        if self.actions['TURNING_RIGHT']:
            self.angle -= self.turning_speed % 360
        if self.actions['SHOOTING']:
            self.current_weapons[self.selected_weapon].shoot()
        if self.actions['RUNNING']:
            self.speed = self.running_speed
        else:
            self.speed = self.initial_speed
        if abs(self.angle) > 360:
            self.angle = 0

    def change_weapon(self, weapon: int):
        self.selected_weapon = weapon
        if (self.selected_weapon == self.PISTOL_SELECTED):
            self.image = Image('assets/player/player_pistol.png').image
        elif (self.selected_weapon == self.SHOTGUN_SELECTED):
            self.image = Image('assets/player/player_shotgun.png').image