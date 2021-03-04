import sys

import pygame
from pygame.locals import *
from image import Image
from actor import player

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

if __name__ == '__main__':

    pygame.init()

    fps = 60
    fpsClock = pygame.time.Clock()

    player = player.Player(200, 300)

    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            player.capture_events(event)

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        player.move()
        player.act()

        # Update.

        screen.blit(fireball.image, (200, 200))
        player.draw()

        # Draw.

        pygame.display.flip()
        fpsClock.tick(fps)
