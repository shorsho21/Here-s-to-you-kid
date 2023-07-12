import pygame
from config import *
import time

class Timer():
    def __init__(self) -> None:
        super().__init__()
        

        self.font = pygame.font.Font(None, 50)
        #self.texto = self.font.render(f"Score: {score} ", True, (CUSTOM))
        #self.texto_rect = self.texto.get_rect()
        #self.texto_rect = (2,2)
        self.color = BLANCO
        self.is_running = True



    def update_timer(self, time_minutes, time_seconds):
        if self.is_running:
            self.time_minutes = time_minutes
            self.time_seconds = time_seconds
            return self.time_seconds
        #print(self.tiempo)
        


    def show_timer(self, display):
        self.text = self.font.render(f"{self.time_minutes:02d}:{self.time_seconds:02d}", True, (self.color))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = ((WIDTH // 2) - 35, HEIGHT - 40)
        display.blit(self.text, self.text_rect.center)
    
    # def timer_count(self, display,start_time, current_time):
            
    #         self.start_time = start_time
    #         self.current_time = current_time
    #         if self.current_time >= 60:  # Si ha pasado 1 minuto, detener el cronómetro
    #             self.current_time = 60
    #             self.running = False

            
    #         minutes = int(self.current_time // 60)
    #         seconds = int(self.current_time % 60)
    #         time_text = "{:02d}:{:02d}".format(minutes, seconds)
    #         text = self.font.render(time_text, True, self.WHITE)  # Renderizar el tiempo en la pantalla
    #         display.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 40))
    #         pygame.display.flip()





