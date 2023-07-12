import pygame
from config import *

class Pause():
    def __init__(self) -> None:
        super().__init__()
        self.font = pygame.font.Font("./fonts/SuperMario256.ttf",40)
        self.text = self.font.render(f"PAUSE", True, (BLANCO))
        self.center = CENTER

    def show_pause(self, display:pygame.surface.Surface):
        
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.center
        display.blit(self.text, self.text_rect)

