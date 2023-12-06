import pygame
import random

# Inicializar Pygame
pygame.init()

# Crear la pantall
pantalla = pygame.display.set_mode((800, 600))

# Titulo e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.png")

# Variables de jugador
img_jugador = pygame.image.load("cohete.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0
jugador_y_cambio = 0


# Variables de enemigo
img_enemigo = pygame.image.load("enemigo.png")
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
enemigo_x_cambio = 1
enemigo_y_cambio = 50


# Variables de bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False


# Función del jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Función del enemigo
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))

# Función disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

# Loop del juego
se_ejecuta = True
while se_ejecuta:

    # Imagen de fondo
    pantalla.blit(fondo, (0, 0))

    # Iterrar eventos
    for evento in pygame.event.get():

        # Cerrar programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Presionar controles
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
              jugador_x_cambio = -1
            if evento.key == pygame.K_RIGHT:
              jugador_x_cambio = 1
            if evento.key == pygame.K_SPACE and not bala_visible:
                bala_x = jugador_x
                disparar_bala(bala_x, bala_y)

        # Soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or pygame.K_RIGHT:
               jugador_x_cambio = 0
    
    # Modificar ubicación del jugador
    jugador_x += jugador_x_cambio

    # Mantener dentro de los bordes al jugador
    if jugador_x <= 0:
       jugador_x = 0
    if jugador_x >= 736:
       jugador_x = 736

    # Modificar ubicación del enemigo
    enemigo_x += enemigo_x_cambio

    # Mantener dentro de los bordes al enemigo
    if enemigo_x <= 0:
       enemigo_x_cambio = 1
       enemigo_y += enemigo_y_cambio
    if enemigo_x >= 736:
       enemigo_x_cambio = -1
       enemigo_y += enemigo_y_cambio

    # Movimiento de la bala
    if bala_y <= -64:
       bala_y = 500
       bala_visible = False
       
    if bala_visible:
       disparar_bala(bala_x, bala_y)
       bala_y -= bala_y_cambio


    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)

    # Actualizar
    pygame.display.update()