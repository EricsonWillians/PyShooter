import pygame
from actor.bullet import Bullet
class Weapon:

    def __init__(self):
        self.clip = []
        self.ammo = 0
        self.damage = 0
        self.weapon_cooldown = 0
        self.last_shot = pygame.time.get_ticks()

    def update_bullet_pos(self, actor):
        for bullet in self.clip:
            if not bullet.discharged:
                # TODO: Adjust bullet position
                bullet.set_pos(actor.x + actor.hand_distance_x, actor.y - actor.hand_distance_y)
                bullet.set_angle(actor.angle)

    def reload_clip(self, actor):
        self.clip = [
            Bullet(actor.x, actor.y, actor.angle) for n in range(self.ammo)]

    def check_bullet_collision(self, target):
        for bullet in self.clip:
            if target.rect.contains(bullet.rect):
                bullet.destroy()
                return True
        return False

    def shoot(self):
        for bullet in self.clip:
            if not bullet.discharged:
                now = pygame.time.get_ticks()
                if now - self.last_shot > self.weapon_cooldown:
                    self.last_shot = now
                    bullet.discharged = True

    def draw(self, screen):
        for bullet in self.clip:
            if bullet.discharged:
                bullet.draw(screen)

class Pistol(Weapon):

    def __init__(self):
        Weapon.__init__(self)
        self.damage = 8
        self.ammo = 50
        self.weapon_cooldown = 300
class Shotgun(Weapon):

    def __init__(self):
        Weapon.__init__(self)
        self.damage = 16
        self.ammo = 50
        self.weapon_cooldown = 300