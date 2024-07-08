import pygame
from settings import *
from random import randint
from funciones_bloques import *
from funciones_colisiones import *
from pygame.locals import *
from funciones_user import *
from funciones_textos import *
from funciones_listas import *

def credits_play(SCREEN: pygame.display):
    """Genera la pantalla con los créditos del juego

    Args:
        SCREEN (pygame.display): Ventana sobre la cual se renderizan los elementos de la pantalla 
    """

    preferencias = {}
    convert_csv(preferencias)

    #Cargo Fuente
    font_1 = pygame.font.Font("./src/assets/fonts/Military Poster.ttf", preferencias ["size_font_1"])

    clock = pygame.time.Clock()#modulo time con funciones para manejo de tiempos
    speed = 2

    text_1 = font_1 .render("Executive Producer: Giuliana Delgobbo", True, WHITE)
    text_2 = font_1 .render("Executive Project Manager: Giuliana Delgobbo", True, WHITE)
    text_3 = font_1 .render("Creative Director: Giuliana Delgobbo", True, WHITE)
    text_1_rect = text_1.get_rect(center = (MID_WIDTH_SCREEN, HEIGHT + text_1.get_height()))
    text_2_rect = text_2.get_rect(center = (MID_WIDTH_SCREEN, HEIGHT + text_2.get_height() + text_1.get_height()))
    text_3_rect = text_3.get_rect(center = (MID_WIDTH_SCREEN, HEIGHT + text_3.get_height() + text_2.get_height() + text_1.get_height()))

    text_escape = font_1.render("Presione SPACE para ir al menu principal", True, WHITE)
    text_escape_rect = text_escape.get_rect(center = (CENTER_SCREEN))
    running = True
    bandera_space = False

    while running:  
            clock.tick(FPS)

            for event in pygame.event.get(): #relevo los eventos, y con el for analizo los eventos
                if event.type == pygame.QUIT: #si analizo los eventos y se lanza el evento quit (apreto la cruz) se sale del bucle
                    terminar()
                if event.type == KEYDOWN:
                    if event.key == K_p: 
                        draw_text(SCREEN, POSITION_PAUSE, "Pause", font_1, WHITE)
                        pygame.display.flip()  
                        wait_user(K_p)
                    if event.key == K_SPACE: 
                        running = False

            text_1_rect.y -= speed
            text_2_rect.y -= speed
            text_3_rect.y -= speed

            
            if text_3_rect.bottom < 0:
                bandera_space = True

            SCREEN.fill(BLACK)
            
            SCREEN.blit(text_1, text_1_rect)
            SCREEN.blit(text_2, text_2_rect)
            SCREEN.blit(text_3, text_3_rect)
            if bandera_space: 
                SCREEN.blit(text_escape, text_escape_rect)
            pygame.display.flip()
