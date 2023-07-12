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

    animations = [hero_0, hero_1, hero_2, hero_3, hero_4, hero_5]

    return animations


def get_sprites_fireball(size):
    fireball_0 = pygame.image.load(
        "./images/sprites_hero/0.png").convert_alpha()
    fireball_0 = pygame.transform.scale(fireball_0, (size))


def get_sprites_enemy(size):
    # DERECHA
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
    # IZQUIERDA
    enemy_8 = pygame.image.load(
        "./images/sprite_enemy/izquierda/0.png").convert_alpha()
    enemy_8 = pygame.transform.scale(enemy_8, (size))

    enemy_9 = pygame.image.load(
        "./images/sprite_enemy/izquierda/1.png").convert_alpha()
    enemy_9 = pygame.transform.scale(enemy_9, (size))

    enemy_10 = pygame.image.load(
        "./images/sprite_enemy/izquierda/2.png").convert_alpha()
    enemy_10 = pygame.transform.scale(enemy_10, (size))

    enemy_11 = pygame.image.load(
        "./images/sprite_enemy/izquierda/3.png").convert_alpha()
    enemy_11 = pygame.transform.scale(enemy_11, (size))

    enemy_12 = pygame.image.load(
        "./images/sprite_enemy/izquierda/4.png").convert_alpha()
    enemy_12 = pygame.transform.scale(enemy_12, (size))

    enemy_13 = pygame.image.load(
        "./images/sprite_enemy/izquierda/5.png").convert_alpha()
    enemy_13 = pygame.transform.scale(enemy_13, (size))

    enemy_14 = pygame.image.load(
        "./images/sprite_enemy/izquierda/6.png").convert_alpha()
    enemy_14 = pygame.transform.scale(enemy_14, (size))

    enemy_15 = pygame.image.load(
        "./images/sprite_enemy/izquierda/7.png").convert_alpha()
    enemy_15 = pygame.transform.scale(enemy_15, (size))

    # ARRIBA
    enemy_16 = pygame.image.load(
        "./images/sprite_enemy/arriba/0.png").convert_alpha()
    enemy_16 = pygame.transform.scale(enemy_16, (size))

    enemy_17 = pygame.image.load(
        "./images/sprite_enemy/arriba/1.png").convert_alpha()
    enemy_17 = pygame.transform.scale(enemy_17, (size))

    enemy_18 = pygame.image.load(
        "./images/sprite_enemy/arriba/2.png").convert_alpha()
    enemy_18 = pygame.transform.scale(enemy_18, (size))

    enemy_19 = pygame.image.load(
        "./images/sprite_enemy/arriba/3.png").convert_alpha()
    enemy_19 = pygame.transform.scale(enemy_19, (size))

    enemy_20 = pygame.image.load(
        "./images/sprite_enemy/arriba/4.png").convert_alpha()
    enemy_20 = pygame.transform.scale(enemy_20, (size))

    enemy_21 = pygame.image.load(
        "./images/sprite_enemy/arriba/5.png").convert_alpha()
    enemy_21 = pygame.transform.scale(enemy_21, (size))

    enemy_22 = pygame.image.load(
        "./images/sprite_enemy/arriba/6.png").convert_alpha()
    enemy_22 = pygame.transform.scale(enemy_22, (size))

    enemy_23 = pygame.image.load(
        "./images/sprite_enemy/arriba/7.png").convert_alpha()
    enemy_23 = pygame.transform.scale(enemy_23, (size))

    # ABAJO

    enemy_24 = pygame.image.load(
        "./images/sprite_enemy/abajo/0.png").convert_alpha()
    enemy_24 = pygame.transform.scale(enemy_24, (size))

    enemy_25 = pygame.image.load(
        "./images/sprite_enemy/abajo/1.png").convert_alpha()
    enemy_25 = pygame.transform.scale(enemy_25, (size))

    enemy_26 = pygame.image.load(
        "./images/sprite_enemy/abajo/2.png").convert_alpha()
    enemy_26 = pygame.transform.scale(enemy_26, (size))

    enemy_27 = pygame.image.load(
        "./images/sprite_enemy/abajo/3.png").convert_alpha()
    enemy_27 = pygame.transform.scale(enemy_27, (size))

    enemy_28 = pygame.image.load(
        "./images/sprite_enemy/abajo/4.png").convert_alpha()
    enemy_28 = pygame.transform.scale(enemy_28, (size))

    enemy_29 = pygame.image.load(
        "./images/sprite_enemy/abajo/5.png").convert_alpha()
    enemy_29 = pygame.transform.scale(enemy_29, (size))

    enemy_30 = pygame.image.load(
        "./images/sprite_enemy/abajo/6.png").convert_alpha()
    enemy_30 = pygame.transform.scale(enemy_30, (size))

    enemy_31 = pygame.image.load(
        "./images/sprite_enemy/abajo/7.png").convert_alpha()
    enemy_31 = pygame.transform.scale(enemy_31, (size))

    animations = [enemy_0, enemy_1, enemy_2, enemy_3, enemy_4, enemy_5, enemy_6, enemy_7, enemy_8, enemy_9, enemy_10, enemy_11,
                  enemy_12, enemy_13, enemy_14, enemy_15, enemy_16, enemy_17, enemy_18, enemy_19, enemy_20, enemy_21, enemy_22, enemy_23, enemy_24, enemy_25, enemy_26, enemy_27, enemy_28, enemy_29, enemy_30, enemy_31]

    return animations
