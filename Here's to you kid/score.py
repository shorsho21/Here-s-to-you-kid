import pygame
from config import *
#"./fonts/SuperMario256.ttf"
class Score():
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.font = pygame.font.Font(None,40)
        #self.texto = self.font.render(f"Score: {score} ", True, (CUSTOM))
        #self.texto_rect = self.texto.get_rect()
        #self.texto_rect = (2,2)



    def show_score(self, display):
        self.text = self.font.render(f"Score:  ", True, (CUSTOM))
        self.text_rect = self.text.get_rect()
        self.text_rect = (2, 2)
        #display.blit(self.text, self.text_rect)

    def increase_score(self):
        self.score += 1


    





    