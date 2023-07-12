import pygame


class Fireball(pygame.sprite.Sprite):
    def __init__(self,size: tuple, midbottom: tuple, option, speed: int = 10) -> None:
        super().__init__()

        
        self.image = pygame.image.load("./images/fireball.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (size))


        self.rect = self.image.get_rect()
        self.rect.center = midbottom

        self.speed_x = speed
        self.speed_y = speed

        self.option = option
        self.playing = True


    def update(self):
        if self.playing:
            match self.option:
                case "A":
                    # DISPARAR ARRIBA
                    self.rect.y -= self.speed_y
                case "B":
                    # DISPARAR ABAJO
                    self.rect.y += self.speed_y
                case "C":
                    # DISPARAR IZQUIERDA
                    self.rect.x -= self.speed_x
                case "D":
                    # DISPARAR DERECHA
                    self.rect.x += self.speed_x
                case _:
                    # Opción por defecto
                    print("Opción inválida")
        elif self.playing == False:
            self.speed_x = 0
            self.speed_y = 0


    def stop(self):
        self.playing = False





