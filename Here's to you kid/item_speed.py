import pygame
from config import *
from hero import *
import random


class ItemSpeed:
    def __init__(self) -> None:
        super().__init__()

        self.image = pygame.image.load("./images/item_speed.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (SIZE_ITEM))

        self.rect = self.image.get_rect()
        self.rect.center = (-30, -30)

        self.sonido_item = pygame.mixer.Sound("./sounds/item_speed.mp3")

    def get_item(self):
            self.sonido_item.play()

    def show_item(self, display):
        display.blit(self.image, self.rect)

    def update(self):
        pass
