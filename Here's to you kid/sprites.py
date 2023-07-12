import pygame
from config import *





def get_sprites_hero(size):
    hero_0 = pygame.image.load("./images/sprites_hero/0.png").convert_alpha()
    hero_0 = pygame.transform.scale(hero_0, (size))

    hero_1 = pygame.image.load("./images/sprites_hero/1.png").convert_alpha()
    hero_1 = pygame.transform.scale(hero_1, (size))

    hero_2 = pygame.image.load("./images/sprites_hero/2.png").convert_alpha()
    hero_2 = pygame.transform.scale(hero_2, (size))

    hero_3 = pygame.image.load("./images/sprites_hero/3.png").convert_alpha()
    hero_3 = pygame.transform.scale(hero_3, (size))

    hero_4 = pygame.image.load("./images/sprites_hero/4.png").convert_alpha()
    hero_4 = pygame.transform.scale(hero_4, (size))

    hero_5 = pygame.image.load("./images/sprites_hero/5.png").convert_alpha()
    hero_5 = pygame.transform.scale(hero_5, (size))


    animations = [hero_0,hero_1,hero_2,hero_3,hero_4,hero_5]

    return animations


def get_sprites_fireball(size):
    fireball_0 = pygame.image.load("./images/sprites_hero/0.png").convert_alpha()
    fireball_0 = pygame.transform.scale(fireball_0, (size))

def get_sprites_enemy(size):

    enemy_0 = pygame.image.load("./images/sprite_enemy/0.png").convert_alpha()
    enemy_0 = pygame.transform.scale(enemy_0, (size))

    enemy_1 = pygame.image.load("./images/sprite_enemy/1.png").convert_alpha()
    enemy_1 = pygame.transform.scale(enemy_1, (size))

    enemy_2 = pygame.image.load("./images/sprite_enemy/2.png").convert_alpha()
    enemy_2 = pygame.transform.scale(enemy_2, (size))

    enemy_3 = pygame.image.load("./images/sprite_enemy/3.png").convert_alpha()
    enemy_3 = pygame.transform.scale(enemy_3, (size))

    enemy_4 = pygame.image.load("./images/sprite_enemy/4.png").convert_alpha()
    enemy_4 = pygame.transform.scale(enemy_4, (size))

    enemy_5 = pygame.image.load("./images/sprite_enemy/5.png").convert_alpha()
    enemy_5 = pygame.transform.scale(enemy_5, (size))

    enemy_6 = pygame.image.load("./images/sprite_enemy/6.png").convert_alpha()
    enemy_6 = pygame.transform.scale(enemy_6, (size))

    enemy_7 = pygame.image.load("./images/sprite_enemy/7.png").convert_alpha()
    enemy_7 = pygame.transform.scale(enemy_7, (size))
    ###IZQUIERDA
    enemy_8 = pygame.image.load("./images/sprite_enemy/izquierda/0.png").convert_alpha()
    enemy_8 = pygame.transform.scale(enemy_8, (size))
    
    enemy_9 = pygame.image.load("./images/sprite_enemy/izquierda/1.png").convert_alpha()
    enemy_9 = pygame.transform.scale(enemy_9, (size))

    enemy_10 = pygame.image.load("./images/sprite_enemy/izquierda/2.png").convert_alpha()
    enemy_10 = pygame.transform.scale(enemy_10, (size))

    enemy_11 = pygame.image.load("./images/sprite_enemy/izquierda/3.png").convert_alpha()
    enemy_11 = pygame.transform.scale(enemy_11, (size))

    enemy_12 = pygame.image.load("./images/sprite_enemy/izquierda/4.png").convert_alpha()
    enemy_12 = pygame.transform.scale(enemy_12, (size))

    enemy_13 = pygame.image.load("./images/sprite_enemy/izquierda/5.png").convert_alpha()
    enemy_13 = pygame.transform.scale(enemy_13, (size))

    enemy_14 = pygame.image.load("./images/sprite_enemy/izquierda/6.png").convert_alpha()
    enemy_14 = pygame.transform.scale(enemy_14, (size))

    enemy_15 = pygame.image.load("./images/sprite_enemy/izquierda/7.png").convert_alpha()
    enemy_15 = pygame.transform.scale(enemy_15, (size))



    animations = [enemy_0, enemy_1, enemy_2, enemy_3, enemy_4, enemy_5, enemy_6, enemy_7, enemy_8, enemy_9, enemy_10, enemy_11, enemy_12, enemy_13, enemy_14, enemy_15]

    return animations

