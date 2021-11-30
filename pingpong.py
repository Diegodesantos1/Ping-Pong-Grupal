# pong_1_1.py: Ventana de juego

import pygame
from pygame.locals import QUIT

# Constantes para la inicialización de la superficie de dibujo
VENTANA_HORI = 800  # Ancho de la ventana
VENTANA_VERT = 600  # Alto de la ventana
FPS = 60  # Fotogramas por segundo
BLANCO = (255, 255, 255)  # Color del fondo de la ventana (RGB)


def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 1")

    # Bucle principal
    jugando = True
    while jugando:
        ventana.fill(BLANCO)

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
    # pong_1_2.py: Clase PelotaPong

import random
import pygame
from pygame.locals import QUIT

# Constantes para la inicialización de la superficie de dibujo
VENTANA_HORI = 800  # Ancho de la ventana
VENTANA_VERT = 600  # Alto de la ventana
FPS = 60  # Fotogramas por segundo
BLANCO = (255, 255, 255)  # Color del fondo de la ventana (RGB)


class PelotaPong:
    def __init__(self, fichero_imagen):
        # --- Atributos de la Clase ---

        # Imagen de la Pelota
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()

        # Dimensiones de la Pelota
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la Pelota
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2

        # Dirección de movimiento de la Pelota
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y


def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 2")

    pelota = PelotaPong("bola_roja.png")

    # Bucle principal
    jugando = True
    while jugando:
        pelota.mover()

        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
    def __init__(self, fichero_imagen):
        # --- Atributos de la Clase ---

        # Imagen de la Pelota
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()

        # Dimensiones de la Pelota
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la Pelota
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2

        # Dirección de movimiento de la Pelota
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def __init__(self, imagen):
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()
        self.ancho, self.alto = self.imagen.get_size()
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])
    
    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y
    
    pelota = PelotaPong("bola_roja.png")
    pelota.mover()
    ventana.blit(pelota.imagen, (pelota.x, pelota.y))
# pong_1_3.py: Rebote de la pelota

import random
import pygame
from pygame.locals import QUIT

# Constantes para la inicialización de la superficie de dibujo
VENTANA_HORI = 800  # Ancho de la ventana
VENTANA_VERT = 600  # Alto de la ventana
FPS = 60  # Fotogramas por segundo
BLANCO = (255, 255, 255)  # Color del fondo de la ventana (RGB)


class PelotaPong:
    def __init__(self, fichero_imagen):
        # --- Atributos de la Clase ---

        # Imagen de la Pelota
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()

        # Dimensiones de la Pelota
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la Pelota
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2

        # Dirección de movimiento de la Pelota
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= 0:
            self.dir_x = -self.dir_x
        if self.x + self.ancho >= VENTANA_HORI:
            self.dir_x = -self.dir_x
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= VENTANA_VERT:
            self.dir_y = -self.dir_y


def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 3")

    pelota = PelotaPong("bola_roja.png")

    # Bucle principal
    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()

        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
def rebotar(self):
        if self.x <= 0:
            self.dir_x = -self.dir_x
        if self.x + self.ancho >= VENTANA_HORI:
            self.dir_x = -self.dir_x
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= VENTANA_VERT:
            self.dir_y = -self.dir_y
pelota.rebotar()
 pong_1_4.py: Reiniciar pelota al salir por los lados

import random
import pygame
from pygame.locals import QUIT

# Constantes para la inicialización de la superficie de dibujo
VENTANA_HORI = 800  # Ancho de la ventana
VENTANA_VERT = 600  # Alto de la ventana
FPS = 60  # Fotogramas por segundo
BLANCO = (255, 255, 255)  # Color del fondo de la ventana (RGB)


class PelotaPong:
    def __init__(self, fichero_imagen):
        # --- Atributos de la Clase ---

        # Imagen de la Pelota
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()

        # Dimensiones de la Pelota
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la Pelota
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2

        # Dirección de movimiento de la Pelota
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
        if self.x >= VENTANA_HORI:
            self.reiniciar()
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= VENTANA_VERT:
            self.dir_y = -self.dir_y

    def reiniciar(self):
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5, 5])


def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 4")

    pelota = PelotaPong("bola_roja.png")

    # Bucle principal
    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()

        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
    def reiniciar(self):
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5, 5])
    def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
        if self.x >= VENTANA_HORI:
            self.reiniciar()
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= VENTANA_VERT:
            self.dir_y = -self.dir_y
        
# pong_1_5.py: Clase RaquetaPong

import random
import pygame
from pygame.locals import QUIT

# Constantes para la inicialización de la superficie de dibujo
VENTANA_HORI = 800  # Ancho de la ventana
VENTANA_VERT = 600  # Alto de la ventana
FPS = 60  # Fotogramas por segundo
BLANCO = (255, 255, 255)  # Color del fondo de la ventana (RGB)


class PelotaPong:
    def __init__(self, fichero_imagen):
        # --- Atributos de la Clase ---

        # Imagen de la Pelota
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()

        # Dimensiones de la Pelota
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la Pelota
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2

        # Dirección de movimiento de la Pelota
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
        if self.x >= VENTANA_HORI:
            self.reiniciar()
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= VENTANA_VERT:
            self.dir_y = -self.dir_y

    def reiniciar(self):
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5, 5])


class RaquetaPong:
    def __init__(self):
        self.imagen = pygame.image.load("raqueta.png").convert_alpha()

        # --- Atributos de la Clase ---

        # Dimensiones de la Raqueta
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la Raqueta
        self.x = 0
        self.y = VENTANA_VERT / 2 - self.alto / 2

        # Dirección de movimiento de la Raqueta
        self.dir_y = 0

    def mover(self):
        self.y += self.dir_y


def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 5")

    pelota = PelotaPong("bola_roja.png")

    raqueta_1 = RaquetaPong()
    raqueta_1.x = 60

    raqueta_2 = RaquetaPong()
    raqueta_2.x = VENTANA_HORI - 60 - raqueta_2.ancho

    # Bucle principal
    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()

        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))
        ventana.blit(raqueta_1.imagen, (raqueta_1.x, raqueta_1.y))
        ventana.blit(raqueta_2.imagen, (raqueta_2.x, raqueta_2.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
class RaquetaPong:
    def __init__(self):
        self.imagen = pygame.image.load("raqueta.png").convert_alpha()

        # --- Atributos de la Clase ---

        # Dimensiones de la Raqueta
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la Raqueta
        self.x = 0
        self.y = VENTANA_VERT / 2 - self.alto / 2

        # Dirección de movimiento de la Raqueta
        self.dir_y = 0

    def mover(self):
        self.y += self.dir_y
    
    def __init__(self):
        self.imagen = pygame.image.load("raqueta.png").convert_alpha()
        self.ancho, self.alto = self.imagen.get_size()
        self.x = 0
        self.y = VENTANA_VERT / 2 - self.alto / 2
        self.dir_y = 0
        self.y += self.dir_y

raqueta_1 = RaquetaPong()
    raqueta_1.x = 60

    raqueta_2 = RaquetaPong()
    raqueta_2.x = VENTANA_HORI - 60 - raqueta_2.ancho
    ventana.blit(raqueta_1.imagen, (raqueta_1.x, raqueta_1.y))
        ventana.blit(raqueta_2.imagen, (raqueta_2.x, raqueta_2.y))
        # pong_1_6.py: Mover raqueta con teclado

import random
import pygame
from pygame.locals import QUIT

# Constantes para la inicialización de la superficie de dibujo
VENTANA_HORI = 800  # Ancho de la ventana
VENTANA_VERT = 600  # Alto de la ventana
FPS = 60  # Fotogramas por segundo
BLANCO = (255, 255, 255)  # Color del fondo de la ventana (RGB)


class PelotaPong:
    def __init__(self, fichero_imagen):
        # --- Atributos de la Clase ---

        # Imagen de la Pelota
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()

        # Dimensiones de la Pelota
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la Pelota
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2

        # Dirección de movimiento de la Pelota
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
        if self.x >= VENTANA_HORI:
            self.reiniciar()
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= VENTANA_VERT:
            self.dir_y = -self.dir_y

    def reiniciar(self):
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5, 5])


class RaquetaPong:
    def __init__(self):
        self.imagen = pygame.image.load("raqueta.png").convert_alpha()

        # --- Atributos de la Clase ---

        # Dimensiones de la Raqueta
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la Raqueta
        self.x = 0
        self.y = VENTANA_VERT / 2 - self.alto / 2

        # Dirección de movimiento de la Raqueta
        self.dir_y = 0

    def mover(self):
        self.y += self.dir_y
        if self.y <= 0:
            self.y = 0
        if self.y + self.alto >= VENTANA_VERT:
            self.y = VENTANA_VERT - self.alto


def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 6")

    pelota = PelotaPong("bola_roja.png")

    raqueta_1 = RaquetaPong()
    raqueta_1.x = 60

    raqueta_2 = RaquetaPong()
    raqueta_2.x = VENTANA_HORI - 60 - raqueta_2.ancho

    # Bucle principal
    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()
        raqueta_1.mover()

        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))
        ventana.blit(raqueta_1.imagen, (raqueta_1.x, raqueta_1.y))
        ventana.blit(raqueta_2.imagen, (raqueta_2.x, raqueta_2.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

            # Detecta que se ha pulsado una tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y = -5
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 5

            # Detecta que se ha soltado la tecla
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y = 0
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 0

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
     raqueta_1.mover()
     self.y += self.dir_y
        if self.y <= 0:
            self.y = 0
        if self.y + self.alto >= VENTANA_VERT:
            self.y = VENTANA_VERT - self.alto
        # Detecta que se ha pulsado una tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y = -5
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 5

            # Detecta que se ha soltado la tecla
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y = 0
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 0
                    # pong_1_7.py: Golpe raqueta jugador humano

import random
import pygame
from pygame.locals import QUIT

# Constantes para la inicialización de la superficie de dibujo
VENTANA_HORI = 800  # Ancho de la ventana
VENTANA_VERT = 600  # Alto de la ventana
FPS = 60  # Fotogramas por segundo
BLANCO = (255, 255, 255)  # Color del fondo de la ventana (RGB)


class PelotaPong:
    def __init__(self, fichero_imagen):
        # --- Atributos de la Clase ---

        # Imagen de la Pelota
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()

        # Dimensiones de la Pelota
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la Pelota
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2

        # Dirección de movimiento de la Pelota
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
        if self.x >= VENTANA_HORI:
            self.reiniciar()
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= VENTANA_VERT:
            self.dir_y = -self.dir_y

    def reiniciar(self):
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5, 5])


class RaquetaPong:
    def __init__(self):
        self.imagen = pygame.image.load("raqueta.png").convert_alpha()

        # --- Atributos de la Clase ---

        # Dimensiones de la Raqueta
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la Raqueta
        self.x = 0
        self.y = VENTANA_VERT / 2 - self.alto / 2

        # Dirección de movimiento de la Raqueta
        self.dir_y = 0

    def mover(self):
        self.y += self.dir_y
        if self.y <= 0:
            self.y = 0
        if self.y + self.alto >= VENTANA_VERT:
            self.y = VENTANA_VERT - self.alto

    def golpear(self, pelota):
        if (
            pelota.x < self.x + self.ancho
            and pelota.x > self.x
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x + self.ancho


def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 7")

    pelota = PelotaPong("bola_roja.png")

    raqueta_1 = RaquetaPong()
    raqueta_1.x = 60

    raqueta_2 = RaquetaPong()
    raqueta_2.x = VENTANA_HORI - 60 - raqueta_2.ancho

    # Bucle principal
    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()
        raqueta_1.mover()
        raqueta_1.golpear(pelota)

        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))
        ventana.blit(raqueta_1.imagen, (raqueta_1.x, raqueta_1.y))
        ventana.blit(raqueta_2.imagen, (raqueta_2.x, raqueta_2.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

            # Detecta que se ha pulsado una tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y = -5
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 5

            # Detecta que se ha soltado la tecla
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y = 0
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 0

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
    if (
            pelota.x < self.x + self.ancho
            and pelota.x > self.x
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x + self.ancho
            raqueta_1.golpear(pelota)
            # pong_1_8.py: Jugador controlado por el programa (IA)

import random
import pygame
from pygame.locals import QUIT

# Constantes para la inicialización de la superficie de dibujo
VENTANA_HORI = 800  # Ancho de la ventana
VENTANA_VERT = 600  # Alto de la ventana
FPS = 60  # Fotogramas por segundo
BLANCO = (255, 255, 255)  # Color del fondo de la ventana (RGB)


class PelotaPong:
    def __init__(self, fichero_imagen):
        # --- Atributos de la Clase ---

        # Imagen de la Pelota
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()

        # Dimensiones de la Pelota
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la Pelota
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2

        # Dirección de movimiento de la Pelota
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
        if self.x >= VENTANA_HORI:
            self.reiniciar()
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= VENTANA_VERT:
            self.dir_y = -self.dir_y

    def reiniciar(self):
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5, 5])


class RaquetaPong:
    def __init__(self):
        self.imagen = pygame.image.load("raqueta.png").convert_alpha()

        # --- Atributos de la Clase ---

        # Dimensiones de la Raqueta
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la Raqueta
        self.x = 0
        self.y = VENTANA_VERT / 2 - self.alto / 2

        # Dirección de movimiento de la Raqueta
        self.dir_y = 0

    def mover(self):
        self.y += self.dir_y
        if self.y <= 0:
            self.y = 0
        if self.y + self.alto >= VENTANA_VERT:
            self.y = VENTANA_VERT - self.alto

    def mover_ia(self, pelota):
        if self.y > pelota.y:
            self.dir_y = -3
        elif self.y < pelota.y:
            self.dir_y = 3
        else:
            self.dir_y = 0

        self.y += self.dir_y

    def golpear(self, pelota):
        if (
            pelota.x < self.x + self.ancho
            and pelota.x > self.x
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x + self.ancho

    def golpear_ia(self, pelota):
        if (
            pelota.x + pelota.ancho > self.x
            and pelota.x < self.x + self.ancho
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x - pelota.ancho


def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 8")

    pelota = PelotaPong("bola_roja.png")

    raqueta_1 = RaquetaPong()
    raqueta_1.x = 60

    raqueta_2 = RaquetaPong()
    raqueta_2.x = VENTANA_HORI - 60 - raqueta_2.ancho

    # Bucle principal
    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()
        raqueta_1.mover()
        raqueta_2.mover_ia(pelota)
        raqueta_1.golpear(pelota)
        raqueta_2.golpear_ia(pelota)

        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))
        ventana.blit(raqueta_1.imagen, (raqueta_1.x, raqueta_1.y))
        ventana.blit(raqueta_2.imagen, (raqueta_2.x, raqueta_2.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

            # Detecta que se ha pulsado una tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y = -5
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 5

            # Detecta que se ha soltado la tecla
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y = 0
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 0

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
    def mover_ia(self, pelota):
        if self.y > pelota.y:
            self.dir_y = -3
        elif self.y < pelota.y:
            self.dir_y = 3
        else:
            self.dir_y = 0

        self.y += self.dir_y
            def golpear_ia(self, pelota):
        if (
            pelota.x + pelota.ancho > self.x
            and pelota.x < self.x + self.ancho
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x - pelota.ancho
raqueta_1.mover()
        raqueta_2.mover_ia(pelota)
        raqueta_1.golpear(pelota)
        raqueta_2.golpear_ia(pelota)
        # pong_1_9.py: Mostrar puntuación de la partida

import random
import pygame
from pygame.locals import QUIT

# Constantes para la inicialización de la superficie de dibujo
VENTANA_HORI = 800  # Ancho de la ventana
VENTANA_VERT = 600  # Alto de la ventana
FPS = 60  # Fotogramas por segundo
BLANCO = (255, 255, 255)  # Color del fondo de la ventana (RGB)
NEGRO = (0, 0, 0)  # Color del texto (RGB)


class PelotaPong:
    def __init__(self, fichero_imagen):
        # --- Atributos de la Clase ---

        # Imagen de la Pelota
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()

        # Dimensiones de la Pelota
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la Pelota
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2

        # Dirección de movimiento de la Pelota
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])

        # Puntuación de la pelota
        self.puntuacion = 0
        self.puntuacion_ia = 0

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
            self.puntuacion_ia += 1
        if self.x >= VENTANA_HORI:
            self.reiniciar()
            self.puntuacion += 1
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= VENTANA_VERT:
            self.dir_y = -self.dir_y

    def reiniciar(self):
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5, 5])


class RaquetaPong:
    def __init__(self):
        self.imagen = pygame.image.load("raqueta.png").convert_alpha()

        # --- Atributos de la Clase ---

        # Dimensiones de la Raqueta
        self.ancho, self.alto = self.imagen.get_size()

        # Posición de la Raqueta
        self.x = 0
        self.y = VENTANA_VERT / 2 - self.alto / 2

        # Dirección de movimiento de la Raqueta
        self.dir_y = 0

    def mover(self):
        self.y += self.dir_y
        if self.y <= 0:
            self.y = 0
        if self.y + self.alto >= VENTANA_VERT:
            self.y = VENTANA_VERT - self.alto

    def mover_ia(self, pelota):
        if self.y > pelota.y:
            self.dir_y = -3
        elif self.y < pelota.y:
            self.dir_y = 3
        else:
            self.dir_y = 0

        self.y += self.dir_y

    def golpear(self, pelota):
        if (
            pelota.x < self.x + self.ancho
            and pelota.x > self.x
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x + self.ancho

    def golpear_ia(self, pelota):
        if (
            pelota.x + pelota.ancho > self.x
            and pelota.x < self.x + self.ancho
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x - pelota.ancho


def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 9")

    # Inicialización de la fuente
    fuente = pygame.font.Font(None, 60)

    pelota = PelotaPong("bola_roja.png")

    raqueta_1 = RaquetaPong()
    raqueta_1.x = 60

    raqueta_2 = RaquetaPong()
    raqueta_2.x = VENTANA_HORI - 60 - raqueta_2.ancho

    # Bucle principal
    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()
        raqueta_1.mover()
        raqueta_2.mover_ia(pelota)
        raqueta_1.golpear(pelota)
        raqueta_2.golpear_ia(pelota)

        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))
        ventana.blit(raqueta_1.imagen, (raqueta_1.x, raqueta_1.y))
        ventana.blit(raqueta_2.imagen, (raqueta_2.x, raqueta_2.y))

        texto = f"{pelota.puntuacion} : {pelota.puntuacion_ia}"
        letrero = fuente.render(texto, False, NEGRO)
        ventana.blit(letrero, (VENTANA_HORI / 2 - fuente.size(texto)[0] / 2, 50))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

            # Detecta que se ha pulsado una tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y = -5
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 5

            # Detecta que se ha soltado la tecla
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y = 0
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 0

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
    # Puntuación de la pelota
        self.puntuacion = 0
        self.puntuacion_ia = 0
        def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
            self.puntuacion_ia += 1
        if self.x >= VENTANA_HORI:
            self.reiniciar()
            self.puntuacion += 1
NEGRO = (0, 0, 0)  # Color del texto (RGB)
# Inicialización de la fuente
    fuente = pygame.font.Font(None, 60)
texto = f"{pelota.puntuacion} : {pelota.puntuacion_ia}"
        letrero = fuente.render(texto, False, NEGRO)
        ventana.blit(letrero, (VENTANA_HORI / 2 - fuente.size(texto)[0] / 2, 50))