import pygame
from config import *
from sprites import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, path_image,size, center, speed, speed_x: int = 0) -> None:
        super().__init__()
        self.flag_sprites = True
        self.indice = 0
        self.animations = get_sprites_enemy(size)
        # self.image = pygame.image.load(path_image).convert_alpha()
        # self.image = pygame.transform.scale(self.image, (size))
        self.image = self.animations[self.indice]
        self.rect = self.image.get_rect()
        self.rect.center = center

        self.speed_x = speed_x
        self.speed_y = speed

        self.playing = True

    def update(self):
        if self.playing:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y

        elif self.playing == False:
            pass

        #derecha
        if self.playing:
            if self.speed_x > 0:
                self.indice += 1
                if self.indice >= 7:
                    self.indice = 0

            elif self.speed_x < 0:
                if self.flag_sprites == True:
                    self.indice = 8
                    self.flag_sprites = False
                elif self.flag_sprites == False:
                    self.indice += 1
                    if self.indice >= 16:
                        self.indice = 8
                        self.flag_sprites = True
        #ARRIBA
            elif self.speed_y < 0:
                if self.flag_sprites == True:
                    self.indice = 16
                    self.flag_sprites = False
                elif self.flag_sprites == False:
                    self.indice += 1
                    if self.indice >= 23:
                        self.indice = 16
                        self.flag_sprites = True
            

        #ABAJO
            elif self.speed_y > 0:
                if self.flag_sprites == True:
                    self.indice = 24
                    self.flag_sprites = False
                elif self.flag_sprites == False:
                    self.indice += 1
                    if self.indice >= 31:
                        self.indice = 24
                        self.flag_sprites = True

                






        self.image = self.animations[self.indice]




    def play_enemy_damaged(self):
        self.sound_enemy_damaged = pygame.mixer.Sound("./sounds/enemy_damaged.mp3")
        self.sound_enemy_damaged.play()

    def stop(self):
        self.playing = False
