import pygame
from settings import *
from random import randint
from funciones_bloques import *
from funciones_colisiones import *
from pygame.locals import * #importo todas los eventos de pygame 
from funciones_textos import *
from screen_game import *
from screen_credits import *
from screen_ranking import *

#Inicializo modulos de Pygame
pygame.init()

#Configuro la ventana
pygame.display.set_caption("Battle Wars") #cambio el título de la ventana 

#Cargo icono juego
icono = pygame.image.load("./src/assets/images/icono.png")
pygame.display.set_icon(icono)

#Configuro pantalla
SCREEN = pygame.display.set_mode(SIZE_SCREEN)

#Cargo y escalo imagenes de fondo
imagen_fondo = pygame.image.load("./src/assets/images/ciudad_fondo.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo, SIZE_SCREEN)
start_button_img = pygame.image.load("./src/assets/images/start.png")

preferencias = {}
convert_csv(preferencias)

#Cargo Fuente
font_2 = pygame.font.Font("./src/assets/fonts/Military Poster.ttf", preferencias ["size_font_2"])
font_3 = pygame.font.Font("./src/assets/fonts/Military Poster.ttf", preferencias ["size_font_3"])

#Configuro Bucle
clock = pygame.time.Clock()#modulo time con funciones para manejo de tiempos

def main_menu():
    """Genera la pantalla principal del juego con su menu de opciones.
    """
    while True: 
        #Pantalla Inicio
        SCREEN.blit(imagen_fondo,ORIGIN)
        draw_text(SCREEN,POSICION_TITLE,"Battle Wars",font_3,CUSTOM_RED)

        play_button = font_2 .render('Play', True, CUSTOM_BLUE, WHITE)
        credits_button = font_2 .render('Credits', True, CUSTOM_BLUE, WHITE)
        ranking_button = font_2 .render('Ranking', True, CUSTOM_BLUE, WHITE)

        SCREEN.blit (play_button, (MID_WIDTH_SCREEN- play_button.get_width() // 2, 250))
        SCREEN.blit (credits_button, (MID_WIDTH_SCREEN - credits_button.get_width() // 2, 350))
        SCREEN.blit (ranking_button, (MID_WIDTH_SCREEN - ranking_button.get_width() // 2, 450))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 250 < event.pos[1] < 250 + play_button.get_height():
                    game_play(SCREEN)
                elif 350 < event.pos[1] < 350 + credits_button.get_height():
                    credits_play(SCREEN)
                elif 450 < event.pos[1] < 450 + ranking_button.get_height():
                    ranking(SCREEN)

if __name__ == '__main__':
    main_menu()



