import pygame


class Image:

    WIDTH = 32
    HEIGHT = 32

    def __init__(self, path, width=WIDTH, height=HEIGHT):
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (width, height))
