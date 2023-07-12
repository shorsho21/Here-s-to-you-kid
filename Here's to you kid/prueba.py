import pygame
from config import *

class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(CUSTOM)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        pass