import pygame
from config import *


class Lifes:
    def __init__(self, size: tuple = (20, 20)) -> None:
        super().__init__()

        self.image = pygame.image.load("./images/corazon.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (size))

        self.rect = self.image.get_rect()

        self.lifes = 3

    def show_hearts(self, display, lifes):

        if lifes == 3:
            display.blit(self.image, ((WIDTH // 2)-20, 0))

            display.blit(self.image, ((WIDTH // 2), 0))

            display.blit(self.image, ((WIDTH // 2) + 20, 0))

        elif lifes == 2:

            display.blit(self.image, ((WIDTH // 2)-20, 0))

            display.blit(self.image, ((WIDTH // 2), 0))

        elif lifes == 1:

            display.blit(self.image, ((WIDTH // 2)-20, 0))


    def decrease_lifes(self):
        self.lifes -= 1
