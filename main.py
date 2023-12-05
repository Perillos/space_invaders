import pygame

# Inicializar Pygame
pygame.init()

# Crear la pantall
pantalla = pygame.display.set_mode((800, 600))

# Titulo e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

# Variables de jugador
img_jugador = pygame.image.load("cohete.png")
jugador_x = 368
jugador_y = 536
jugador_x_cambio = 0
jugador_y_cambio = 0


# Función del jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Loop del juego
se_ejecuta = True
while se_ejecuta:

    # RGB
    pantalla.fill((205, 144, 228))

    # Iterrar eventos
    for evento in pygame.event.get():

        # Cerrar programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Presionar flechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
              jugador_x_cambio = - 1
            if evento.key == pygame.K_RIGHT:
              jugador_x_cambio = + 1

        # Soltar flechas
        if evento.type == pygame.KEYUP:
           if evento.key == pygame.K_LEFT or pygame.K_RIGHT:
              jugador_x_cambio = 0
    
    # Modificar ubicación
    jugador_x += jugador_x_cambio

    # Mantener dentro de los bordes
    if jugador_x <= 0:
       jugador_x = 0
    if jugador_x >= 736:
       jugador_x = 736


    jugador(jugador_x, jugador_y)

    # Actualizar
    pygame.display.update()