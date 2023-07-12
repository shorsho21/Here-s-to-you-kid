import pygame
from config import *
from fireball import *
from mana import *
from game import *
from sprites import *

class Hero (pygame.sprite.Sprite):
    def __init__(self, path_image: str, size: tuple, center: tuple) -> None:
        super().__init__()
        self.flag = True
        self.size = size
        self.indice = 0
        # self.image = pygame.image.load(path_image).convert_alpha()
        # self.image = pygame.transform.scale(self.image, (self.size))
        self.animations = get_sprites_hero(self.size)
        self.image = self.animations[self.indice]
        self.aux = self.image
        #mana
        self.mana = 50

        self.rect = self.image.get_rect()
        self.rect.center = center

        self.speed_x = 0
        self.speed_y = 0

        self.sound_fireball = pygame.mixer.Sound("./sounds/fireball.mp3")

        self.playing = True

        self.speed_fireball = SPEED_FIREBALL

        




    #movimiento del personaje, cordenadas
    def update(self):
        if self.playing:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y

            #PARA QUE NO SE SALGA DELOS BORDES
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right >= WIDTH:
                self.rect.right = WIDTH

            if self.rect.top <= 0:
                self.rect.top = 0
            elif self.rect.bottom >= HEIGHT:
                self.rect.bottom = HEIGHT

            #MOVIMIENTO DE SPRITES
            #IZQUIERDA
            if self.speed_x < 0:
                self.indice += 1
                if self.indice >= 2:
                    self.indice = 0
            #DERECHA
            elif self.speed_x > 0:
                if self.flag:
                    self.indice = 2
                    self.flag = False
                else:
                    self.indice = 3
                    self.flag = True
            
                #ARRIBA
            elif self.speed_y < 0:
                self.indice = 4
            
            elif self.speed_y > 0:
                self.indice = 5

            

            



        self.image = self.animations[self.indice]

    def cast(self, sprites, fireballs, direction:str, is_pause:bool):
        if self.mana > 0 and is_pause == False:
            fireball = Fireball(SIZE_FIREBALL, self.rect.center, direction , self.speed_fireball)
            self.sound_fireball.play()
            sprites.add(fireball)
            fireballs.add(fireball)
            self.mana -= 1

    def play_hero_damage_sound(self):
        self.sound_hero_damaged = pygame.mixer.Sound("./sounds/heroe_golpeado.mp3")
        self.sound_hero_damaged.play()

    def play_game_over_sound(self):
        self.sound_game_over = pygame.mixer.Sound("./sounds/game_over_sound.mp3")
        self.sound_game_over.play()



            


    def stop(self):
        self.playing = False