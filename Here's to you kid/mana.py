import pygame
from config import *

class Mana:
    def __init__(self) -> None:
        super().__init__()

        

        self.font = pygame.font.Font("./fonts/SuperMario256.ttf", 40)
        self.color = BLANCO


    def show_mana(self, display, mana):
        text = self.font.render(f"Mana: {mana}",True, self.color)
        rect_text = text.get_rect()
        rect_text.topright = (WIDTH - 2, 2)
        display.blit(text, rect_text)


