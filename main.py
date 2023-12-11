import pygame
import random
import math

from pygame import mixer

# Inicializar Pygame
pygame.init()

# Crear la pantall
pantalla = pygame.display.set_mode((800, 600))

# Titulo e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.png")

# Agregar música
mixer.music.load("musica_fondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Variables de jugador
img_jugador = pygame.image.load("cohete.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0
jugador_y_cambio = 0

# Variables de enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(1)
    enemigo_y_cambio.append(50)

# Variables de bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

# Variables puntuación
puntuacion = 0
fuente = pygame.font.Font("fastest.ttf", 20)
texto_x = 10
texto_y = 10

# Texto de fin de juego
fuente_fin = pygame.font.Font("fastest.ttf", 36)


def texto_fin():
    mi_fuente_final = fuente_fin.render(
        "F I N   D E L   J U E G O", True, (255, 255, 255)
    )
    pantalla.blit(mi_fuente_final, (60, 200))


# Mostar puntuación
def mostrar_puntuacion(x, y):
    puntuacion_texto = fuente.render(
        f"P u n t u a c i ó n :  {puntuacion}", True, (255, 255, 255)
    )
    pantalla.blit(puntuacion_texto, (x, y))


# Función del jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Función del enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


# Función disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# Función colisión
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt((math.pow(x_1 - x_2, 2)) + (math.pow(y_1 - y_2, 2)))
    if distancia < 27:
        return True
    else:
        return False


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
                sonido_bala = mixer.Sound("disparo.mp3")
                sonido_bala.play()
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
    for e in range(cantidad_enemigos):
        # Fin del juego
        if enemigo_y[e] > 450:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_fin()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

        # Mantener dentro de los bordes al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 1
            enemigo_y[e] += enemigo_y_cambio[e]
        if enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -1
            enemigo_y[e] += enemigo_y_cambio[e]

        # Colisión
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound("golpe.mp3")
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntuacion += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Movimiento de la bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    jugador(jugador_x, jugador_y)

    mostrar_puntuacion(texto_x, texto_y)

    # Actualizar
    pygame.display.update()
