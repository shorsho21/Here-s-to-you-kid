import pygame
import sys
import random
from config import *
from hero import *
from fireball import *
from score import *
from enemy import *
from mana import *
from lifes import *
from item_speed import *
from prueba import *
from item_size import *
from timer import *
from pause import *
from item_mana import *
from item_life import *
import time

class Game:
    def __init__(self) -> None:
        #BANDERA DE SCORE- ITEM SPAWM
        self.aux_flag_score = 0
        #FLAG PARA EL PAUSE INPUT
        self.flag_input = True
        # SETEAMOS
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode(SIZE_SCREEN)
        self.display.fill(CUSTOM)
        pygame.display.set_caption("Here's to you Kid")
        # FONDO DE PANTALLA JUEGO
        self.background = pygame.image.load("./images/fondo_game_neo.png").convert()
        self.background = pygame.transform.scale(self.background, SIZE_SCREEN)

        # FONDO DE START GAME
        self.background_start = pygame.image.load(
            "./images/start_fondo.jpg").convert()
        self.background_start = pygame.transform.scale(
            self.background_start, SIZE_SCREEN)
        
        #FONDO DE GAME OVER
        self.background_game_over = pygame.image.load(
            "./images/game_over.jpg").convert()
        self.background_game_over = pygame.transform.scale(
            self.background_game_over, SIZE_SCREEN)

        #SONIDO
        #SONIDO DE MENU DE ESTART
        self.music_start_menu = pygame.mixer.Sound("./sounds/start menu.mp3")
        #MUSICA DE PLAYING GAME
        self.music_playing = pygame.mixer.Sound("./sounds/playing_game.mp3")
        

        # HEROE
        #VARIABLE DE TAMA;O DEL HEROE
        self.size_hero = SIZE_HERO
        #SETEO DE LA CLASE HEROE
        self.hero = Hero("./images/hero.png", self.size_hero, CENTER)

        # sprites
        self.sprites = pygame.sprite.Group()
        self.fireballs = pygame.sprite.Group()
        self.sprites.add(self.hero)

        #SETEO LA CLASE TIMER
        self.start_time = time.time()
        
        #SETEO LOS ENEMIGOS
        self.enemys = pygame.sprite.Group()
        self.enemy = Enemy("./images/enemy.png",
                                  SIZE_ENEMY, CENTER, 0, 0)

        #CONTADOR DE SCORE
        self.score = 0

        # FUENTES
        #"./fonts/SuperMario256.ttf"
        self.font = pygame.font.Font("./fonts/SuperMario256.ttf", 48)
        self.font_mini = pygame.font.Font("./fonts/SuperMario256.ttf", 30)

        # SETEO DE DIFICULTAD
        self.dificult = 0

        #SETEO DE LA CLASE MANA
        self.mana = Mana()

        # SETEO DE LA CLASE VIDAS
        self.lifes = Lifes()


        #ITEM SPEED UP
        self.item_speed = ItemSpeed()
        #self.sprites.add(self.item_speed)

        #ITEM LIFE POCION
        self.item_life = ItemLife()

        #ITEM SIZE TAMA;O (SE CAMBIO A QUE AUMENTE LA VELOCIDAD DEL PROYECTIL)
        self.item_size = ItemSize()

        #SETEO DE LA CLASE DEL ITEM DE MANA
        self.item_mana = ItemMana()

        #SETEO DE VELOCIDAD DEL HEROE
        self.speed = SPEED_HERO

        #SETEO DE LA CLASE TIMER DEL RELOJ
        self.timer = Timer()

        #SETEO DE LA CLASE PAUSE
        self.pause = Pause()

        #MAXIMOS DE ENEMIGOS
        self.max_enemy = MAX_ENEMY

        #VELOCIDAD DE LOS ENEMIGOS
        self.speed_enemy = SPEED_ENEMY

        #sprite
        # self.sprite1 = MySprite(100, 100)
        # self.sprites.add(self.sprite1)

        # BANDERAS
        self.is_playing = False
        self.is_game_over = False
        self.is_running = False
    
    def play(self):
        self.is_playing = True
        self.is_running = True
        self.is_game_over = False
        self.is_pause = False
        flag = True

        while flag:
            flag = self.show_start_screen()

        while self.is_running:
            self.clock.tick(FPS)
            self.handler_events()
            self.update()
            self.render()

    def handler_events(self):
        #CONDICION DE CIERRE DE VENTANA Y CONTROLES
        self.window_close_and_controllers()
        #CONDICION DE AUMENTO DE DIFICULTAD
        self.dificult_progress()
        #CONDICION DE APARICION DEL ITEM SPEED
        self.item_spawm()
        
        #MUESTRA EL TIMER EN PANTALLA
        self.play_timer()
        
    def update(self):
        #elmina los sprites que estan fuera de pantalla
        self.kill_elements_out_display()
        if self.is_playing:
            self.collide_detection()
        
        #FUNCION QUE DETECTA LA COLISION CON LOS ITEMS Y APLICA EL EFECTO SEGUN EL ITEM
        self.item_collide()

        #FUNCION QUE GENERA LOS ENEMIGOS SEGUN LA DIFICULTAD DEL SELF.DIFICULT
        self.generate_enemys(self.dificult)

        #ACTUALIZACION DE LOS SPRITES
        self.sprites.update()

    def render(self):
        # juego / inicio/ game over
        if self.is_game_over:
            #MUESTRA GAME OVER SI ISGAMEOVER ES TRUE
            self.show_game_over_screen()

        elif self.is_playing:
            #MUESTRA EL FONDO DEL JUEGO JUGANDO
            self.display.blit(self.background, ORIGIN)
            #MUESTRA EN PANTALLA EL INDICADOR DE MANA
            self.mana.show_mana(self.display, self.hero.mana)
            #DIBUJA LOS SPRITES EN PANTALLA
            self.sprites.draw(self.display)
            #DIBUJA EL CONTADOR DE SCORE EN PANTALLA
            self.show_score(self.score)
            #DIBUJA EN PANTALLA EL ITEM DE MANA
            self.item_speed.show_item(self.display)
            #IMPRIME EN PANTALLA EL ITEM DE SIZE(TAMA;O)  (AHORA ES UN ITEM DE VELOCIDAD DE PROYECTIL)(BECAUSE REASONS)
            self.item_size.show_item(self.display)
            #MUESTRA EL ITEM DE MANA EN PANTALLA
            self.item_mana.show_item(self.display)
            #MUESTRA EN PANTALLA EL ITEM DE VIDA
            self.item_life.show_item(self.display)
            #MUESTRA EN PANTALLA EL RELOJ\TIMER
            self.timer.show_timer(self.display)
            #MUESTRA EN PANTALLA LOS CORAZONES QUE INDICAN LA VIDA DEL PERSONAJE
            self.lifes.show_hearts(self.display, self.lifes.lifes)

            if self.is_pause:
                #MUESTRA LA PANTALLA DE PAUSA Y HACE STOP A TODOS LOS ELEMENTOS (EN PROCESO)
                self.pause.show_pause(self.display)
                self.stop_elements()
            else:
                #DEVUELVE AL ESTADO DE PLAYING A LOS ENEMIGOS
                for enemy in self.enemys:
                    enemy.playing = True
                #VUELVE TRANSPARENTE LA IMAGEN DE PAUSA
                self.pause.text.set_alpha(255)
                #PONE EN PLAYING AL HEROE, HACIENDO QUE PUEDA MOVERSE
                self.hero.playing = True
                #PONE EN PLAYING A LAS BOLAS DE FUEGO
                self.fireballs.playing = True
                #PONE EN PLAY AL TIMER
                self.timer.is_running = True
                
        else:
            #MUESTRA LA PANTALLA DE INICIO
            self.show_start_screen()
            

        pygame.display.flip()

    def show_start_screen(self):
        #SETEO DE MUSIC PAUSE Y PLAY DE MUSICA 
        flag = True
        dificult = 0
        self.music_playing.stop()
        self.music_start_menu.set_volume(0.5)
        self.music_start_menu.play(-1)

        #EVENTO DE START MENU, PIDE QUE INGRESE UNA DIFICULTAD PARA EMPEZAR LA PARTIDA
        while flag:
            
            self.clock.tick(FPS)
            for evento in pygame.event.get():

                if evento.type == pygame.KEYDOWN:

                    if evento.key == pygame.K_s:
                        flag = False
                    elif evento.key == pygame.K_1:
                        flag = False
                        dificult = self.dificult = 1
                    elif evento.key == pygame.K_2:
                        flag = False
                        dificult = self.dificult = 2
                    elif evento.key == pygame.K_3:
                        flag = False
                        dificult = self.dificult = 3
            #SETEO DE MENSAJE EN PANTALLA DE START MENU
            texto = self.font.render("HERE'S TO YOU KID", True, (BLANCO))
            texto_rect = texto.get_rect()
            texto_rect.center = CENTER

            texto2 = self.font_mini.render("PRESS 'S' TO START", True, (BLANCO))
            texto2_rect = texto2.get_rect()
            texto2_rect.center = DISPLAY_CUSTOM

            texto3 = self.font_mini.render(" LEVEL SELECT: [S] [1] [2] [3]", True, (BLANCO))
            texto3_rect = texto3.get_rect()
            texto3_rect = (2, HEIGHT - 45)

            #BLITEO DE LOS TEXTO DE START MENU
            self.display.blit(self.background_start, ORIGIN)
            self.display.blit(texto, texto_rect)
            self.display.blit(texto2, texto2_rect)
            self.display.blit(texto3, texto3_rect)
            pygame.display.flip()
        self.restart_game()
        self.dificult = dificult
        
                
                

        #SETEO DE PLAYIN PASA A TRUE AL SALIR DEL START MENU
        self.is_playing = True

        #SETEO DE MUSICA PARA LA PANTALLA DE PLAYING GAME
        self.music_start_menu.stop()
        self.music_playing.set_volume(0.45)
        self.music_playing.play(-1)
        
        return False

    def show_game_over_screen(self):

        #LETRAS GAME OVER
        texto = self.font.render("Game Over", True, (BLANCO))
        texto_rect = texto.get_rect()
        texto_rect.center = CENTER
        #LETRAS DE SCORE
        texto2 = self.font_mini.render(f"YOUR SCORE IT WAS {self.score}", True, (BLANCO))
        texto2_rect = texto2.get_rect()
        texto2_rect.center = (WIDTH // 2, (HEIGHT // 2) + 50)

        texto3 = self.font_mini.render(f"you survived {self.timer.time_minutes:02d}:{self.timer.time_seconds:02d}", True, (BLANCO))
        texto3_rect = texto3.get_rect()
        texto3_rect.center = (WIDTH // 2, (HEIGHT // 2) + 80)

        #BLITEO DEL FONDO Y LOS TEXTOS DE GAME OVER
        self.display.blit(self.background_game_over, ORIGIN)
        self.display.blit(texto, texto_rect)
        self.display.blit(texto2, texto2_rect)
        self.display.blit(texto3, texto3_rect)

        pygame.display.flip()
        pygame.time.delay(2000)
        #SETEO DE BANDERAS CUANDO SE TERMINE EL SCREEN DE GAME OVER
        self.is_game_over = False
        self.is_playing = False

    def restart_game(self):
        """resetea los parametros (mana, vida, score) y los enemigos
        """
        self.score = 0
        self.sprites.empty()
        self.enemys.empty()
        #self.reset()
        self.lifes.lifes = 3
        
        self.hero.mana = 50
        self.dificult = 0
        self.speed = SPEED_HERO
        self.hero.size = SIZE_HERO
        self.size_hero = SIZE_HERO
        self.hero.image = self.hero.aux
        self.sprites.add(self.hero)

        self.item_size.rect.center = (-30,-30)
        self.item_speed.rect.center = (-30,-30)
        self.item_mana.rect.center = (-30,-30)
        self.item_life.rect.center = (-30,-30)

        self.max_enemy = MAX_ENEMY
        self.speed_enemy = SPEED_ENEMY

        self.start_time = time.time()

        self.hero.speed_fireball = SPEED_FIREBALL

        
        #RESETA LA POSICION DEL HEROE
        self.reset()

    def reset(self):
        """resetea la posicion del heroe
        """
        self.hero.rect.center = CENTER
        self.hero.speed_x = 0
        self.hero.speed_y = 0

    def show_score(self, score: int):
        """Recibe un entero que es el score del juego, la llamada a la funcion muestra en pantalla el score

        Args:
            score (int): El score que muestra en pantalla
        """
        texto = self.font.render(f"SCORE: {score}", True, (BLANCO))
        texto_rect = texto.get_rect()
        texto_rect.topleft = (2, 2)

        self.display.blit(texto, texto_rect)
        pygame.display.flip()

    def generate_enemys(self, type):
        """Genera los enemigos segun la dificultad que se setee

        Args:
            type (int): seteo de dificultad
        """
        if len(self.enemys) == 0:
            # oleada desde arriba hacia abajo
            if type >= 0:
                for i in range(self.max_enemy):
                    x = random.randrange(16, WIDTH - 16)
                    y = random.randrange(0, HEIGHT // 3)
                    enemy = Enemy("./images/enemy.png",
                                SIZE_ENEMY, (x, y), self.speed_enemy)
                    self.enemys.add(enemy)
                    self.sprites.add(enemy)

            # oleada desde abajo hacia arriba
            if type >= 1:
                for i in range(self.max_enemy):
                    x = random.randrange(16, WIDTH - 16)
                    y = random.randrange(HEIGHT - 10, HEIGHT)
                    enemy = Enemy("./images/enemy.png",
                                  SIZE_ENEMY, (x, y), -self.speed_enemy)
                    self.enemys.add(enemy)
                    self.sprites.add(enemy)

            if type >= 2:
                # oleada desde izquierda a derecha
                for i in range(self.max_enemy):
                    x = random.randrange(0, 40)
                    y = random.randrange(10, HEIGHT - 10)
                    enemy = Enemy("./images/enemy.png",
                                  SIZE_ENEMY, (x, y), 0, self.speed_enemy)
                    self.enemys.add(enemy)
                    self.sprites.add(enemy)

            if type == 3:
                # oleada desde derecha a izquierda
                for i in range(self.max_enemy):
                    x = random.randrange(WIDTH - 30, WIDTH)
                    y = random.randrange(10, HEIGHT)
                    enemy = Enemy("./images/enemy.png",
                                  SIZE_ENEMY, (x, y), 0, -self.speed_enemy)
                    self.enemys.add(enemy)
                    self.sprites.add(enemy)

    def kill_elements_out_display(self):
        """elimina los elementos sprites que estan fuera de pantalla
        """
        for enemy in self.enemys:
            # LOS DE ARRIBA HACIA ABAJO
            if enemy.rect.top >= HEIGHT:
                enemy.kill()
            # LOS DE ABAJO HACIA ARRIBA
            elif enemy.rect.bottom <= 0:
                enemy.kill()
            # LOS DE DERECHA A IZQUIERDA
            elif enemy.rect.right <= 0:
                enemy.kill()
            # LOS DE IZQUIERDA A DERECHA
            elif enemy.rect.left >= WIDTH:
                enemy.kill()

    def collide_detection(self):
        """detecta las coliciones de los enemigos con las fireballs y la del heroe con los enemigos
        """
        for fireball in self.fireballs:

            lista = pygame.sprite.spritecollide(fireball, self.enemys, True)
            if len(lista) != 0:
                fireball.kill()
                self.score += 1
                self.enemy.play_enemy_damaged()

        lista = pygame.sprite.spritecollide(self.hero, self.enemys, True)
        if len(lista) != 0:
            self.lifes.lifes -= 1
            self.hero.play_hero_damage_sound()
        
        if self.lifes.lifes == 0:
            self.hero.play_game_over_sound()
            self.is_game_over = True


    def item_spawm(self):
        """funcion que genera los items en pantalla de forma aleatoria segun el score
        """
        
        if self.score == 4 or self.score == self.aux_flag_score + 7:
            self.aux_flag_score = self.score
            #SPAWM DE ITEM DE SPEED
            x = random.randrange(15, WIDTH - 15)
            y = random.randrange(15, HEIGHT - 15)
            self.item_speed.rect.center = (x,y)
            self.score += 1

            #SPAWM DE ITEM DE SIZE
            x = random.randrange(15, WIDTH - 15)
            y = random.randrange(15, HEIGHT - 15)
            self.item_size.rect.center = (x,y)

            #SPAWM DE ITEM MANA
            x = random.randrange(15, WIDTH - 15)
            y = random.randrange(15, HEIGHT - 15)
            self.item_mana.rect.center = (x,y)

            #SPAWM DE ITEM POCION LIFE
            x = random.randrange(15, WIDTH - 15)
            y = random.randrange(15, HEIGHT - 15)
            self.item_life.rect.center = (x,y)

    def item_collide(self):
        """FUNCON QUE DETECTA LAS COLICIONES DEL HEROE CON EL ITEM Y GENERA LOS EFECTOS DEL ITEM
        """
        #COLISION CON EL ITEM SPEED
        if self.hero.rect.colliderect(self.item_speed.rect):
            self.speed += SPEED_UP_ITEM
            self.item_speed.rect.center = (-30,-30)
            self.item_speed.get_item()
            
        #COLISION CON EL ITEM SIZE
        if self.hero.rect.colliderect(self.item_size.rect):
            # x , y = self.size_hero
            # self.size_hero = (x - ITEM_SIZE_REDUCE, y - ITEM_SIZE_REDUCE)
            # self.hero.size = self.size_hero
            self.hero.speed_fireball += 10
            #self.sprites.add(self.hero)
            self.item_size.rect.center = (-30,-30)
            self.item_size.get_item()
        #COLISION CON EL ITEM DE MANA
        if self.hero.rect.colliderect(self.item_mana.rect):
            self.hero.mana += 10
            self.item_speed.get_item()
            self.item_mana.rect.center = (-30,-30)
        #COLISION CON EL ITEM DE VIDA
        if self.hero.rect.colliderect(self.item_life.rect):
            if self.lifes.lifes == 3:
                pass
            else:
                self.lifes.lifes += 1
            self.item_life.get_item()
            self.item_life.rect.center = (-30,-30)
    
    def dificult_progress(self):
        """FUNCION QUE AUMENTA LA CANTIDAD DE ENEMIGOS Y SU VELOCIDAD SEGUN EL SCORE 
        """
        if self.score == 5 :
            self.dificult = 1
            self.max_enemy += 1
            self.speed_enemy += 1
            self.score += 1
            
        elif self.score == 10:
            self.dificult = 2
            self.max_enemy += 1
            self.speed_enemy += 1
            self.score += 1

        elif self.score == 15 :
            self.dificult = 3
            self.max_enemy += 1
            self.speed_enemy += 1
            self.score += 1

    def window_close_and_controllers(self):
        """FUNCION QUE APLICA LOS MOVIMIENTOS DEL PERSONAJE, DEL PAUSE Y LA FUNCION DE CERRAR LA VENTANA DEL JUEGO
        """
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # MOVIMIENTO DEL PERSONAJE
            elif evento.type == pygame.KEYDOWN:
                # PULSACION DE LA TECLA
                if evento.key == pygame.K_a:
                    self.hero.speed_x = -self.speed

                elif evento.key == pygame.K_d:
                    self.hero.speed_x = self.speed

                if evento.key == pygame.K_w:
                    self.hero.speed_y = -self.speed

                elif evento.key == pygame.K_s:
                    self.hero.speed_y = self.speed

                elif evento.key == pygame.K_i:
                    self.hero.cast(self.sprites, self.fireballs, "A",self.is_pause)

                elif evento.key == pygame.K_k:
                    self.hero.cast(self.sprites, self.fireballs, "B",self.is_pause)

                elif evento.key == pygame.K_j:
                    self.hero.cast(self.sprites, self.fireballs, "C",self.is_pause)

                elif evento.key == pygame.K_l:
                    self.hero.cast(self.sprites, self.fireballs, "D",self.is_pause)

                elif evento.key == pygame.K_p and self.flag_input:
                    self.is_pause = True
                    self.flag_input = False 
                elif evento.key == pygame.K_p and self.flag_input == False:
                    self.is_pause = False
                    self.flag_input = True



            elif evento.type == pygame.KEYUP:
                # CUANDO LAS TECLAS NO ESTAN PRESIONADAS
                if evento.key == pygame.K_a and self.hero.speed_x < 0:
                    self.hero.speed_x = 0

                elif evento.key == pygame.K_d and self.hero.speed_x > 0:
                    self.hero.speed_x = 0

                if evento.key == pygame.K_w and self.hero.speed_y < 0:
                    self.hero.speed_y = 0

                elif evento.key == pygame.K_s and self.hero.speed_y > 0:
                    self.hero.speed_y = 0

    def stop_elements(self):
        """FUNCION QUE PAUSA EL MOVIMIENTO DE TODOS LOS ELEMENTOS EN PANTALLA
        """
        self.hero.stop()

        for enemy in self.enemys:
            #self.enemy.stop()
            enemy.stop()
            #self.enemy.playing = False
            #self.enemy.update()

        for fireball in self.fireballs:
            fireball.stop()

        for sprites in self.sprites:
            sprites.stop()
        
        self.timer.is_running = False

    def play_timer(self):
        """INICIA EL TIEMPO DEL RELOJ
        """

        current_time = time.time() - self.start_time
        if self.is_playing:
                self.timer.update_timer(int(current_time // 60), int(current_time % 60))