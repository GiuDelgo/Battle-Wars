import pygame
from settings import *
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

preferencias = {}
convert_csv(preferencias)

#Cargo Fuente
font_2 = pygame.font.Font("./src/assets/fonts/Military Poster.ttf", preferencias ["size_font_2"])
font_3 = pygame.font.Font("./src/assets/fonts/Military Poster.ttf", preferencias ["size_font_3"])


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

        play_button_rect = play_button.get_rect(center=(MID_WIDTH_SCREEN, 250))
        credits_button_rect = credits_button.get_rect(center=(MID_WIDTH_SCREEN, 350))
        ranking_button_rect = ranking_button.get_rect(center=(MID_WIDTH_SCREEN, 450))

        SCREEN.blit(play_button, play_button_rect)
        SCREEN.blit(credits_button, credits_button_rect)
        SCREEN.blit(ranking_button, ranking_button_rect)

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if punto_in_block((x,y), play_button_rect):
                    game_play(SCREEN)
                elif punto_in_block((x,y), credits_button_rect):
                    credits_play(SCREEN)
                elif punto_in_block((x,y), ranking_button_rect):
                    ranking(SCREEN)

if __name__ == '__main__':
    main_menu()



