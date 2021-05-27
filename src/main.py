import sys

import pygame
from pygame.locals import *
from screeninfo import get_monitors
from image import Image
from actor import player
from actor import enemy

monitor = get_monitors()[0]
width, height = monitor.width, monitor.height
screen = pygame.display.set_mode((width, height), DOUBLEBUF)

if __name__ == '__main__':

    pygame.init()

    fps = 60
    fps_clock = pygame.time.Clock()

    player = player.Player(width / 2, height / 2)
    enemy = enemy.Enemy(400, 100)

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

        # Update.

        # screen.blit(fireball.image, (200, 200))
        player.draw()
        enemy.draw()

        # Draw.

        pygame.display.flip()
        fps_clock.tick(fps)
