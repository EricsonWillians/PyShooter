import sys

import pygame
from pygame.locals import *
from screeninfo import get_monitors
from image import Image
from actor import player
from actor import enemy
from map import Map
from weapon import Weapon

monitor = get_monitors()[0]
width, height = int(monitor.width / 2), int(monitor.height / 2)
screen = pygame.display.set_mode((width, height), DOUBLEBUF)

if __name__ == '__main__':

    pygame.init()

    fps = 60
    fps_clock = pygame.time.Clock()

    player = player.Player(width / 2, height / 2)
    enemy = enemy.Enemy(400, 100)
    weapon = Weapon()

    _map = Map('test_area')
    
    

    while True:
        screen.fill((50, 50, 50))
        for event in pygame.event.get():
            player.capture_events(event)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        player.move()
        player.act()
        if weapon.check_bullet_collision(enemy):
            print('DEAD!')

        # screen.blit(fireball.image, (200, 200))
        _map.draw(screen, player)
        player.draw(screen)
        enemy.draw(screen)
        

        # Draw.

        pygame.display.flip()
        fps_clock.tick(fps)
