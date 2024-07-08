import pygame
from pygame.locals import *
from settings import *
from funciones_user import *
from funciones_textos import *

def ranking(SCREEN: pygame.display):
    """Pantalla del ranking de score de jugadores

    Args:
        SCREEN (pygame.display): Ventana sobre la cual se renderizan los elementos de la pantalla 
    """
    
    imagen_pantalla_fin = pygame.image.load("./src/assets/images/fondo_pantalla_fin.jpg")
    imagen_pantalla_fin = pygame.transform.scale(imagen_pantalla_fin, SIZE_SCREEN)

    font_1 = pygame.font.Font("./src/assets/fonts/Military Poster.ttf", preferencias ["size_font_1"])
    font_3 = pygame.font.Font("./src/assets/fonts/Military Poster.ttf", preferencias ["size_font_3"])

    running = True
    no_file = False
    scores = []
    import json 

    try:
        with open("./src/scores.json", "r", encoding="utf-8") as archivo:
            scores = json.load(archivo)
    except FileNotFoundError:
        no_file = True
        print("El archivo no existe. No hay jugadores previos.")
    except json.JSONDecodeError:
        print("El archivo JSON está vacío o contiene un formato inválido.")

    while running:
        
        SCREEN.blit(imagen_pantalla_fin,ORIGIN)

        draw_text(SCREEN, (MID_WIDTH_SCREEN, 60), "RANKING", font_3, CUSTOM_RED,)

        if no_file or len(scores) == 0: 
            draw_text(SCREEN, (MID_WIDTH_SCREEN, 200), "No hay jugadores previos", font_1, CUSTOM_RED, bg=WHITE)
        elif scores: 
            if len(scores)>3:
                for i in range(0,3):
                    draw_text(SCREEN, (MID_WIDTH_SCREEN, 200+50*(i+1)), f"{i+1} - Nombre: {scores[i]["name"]}    Score: {scores[i]["score"]}", font_1, CUSTOM_RED, bg=WHITE)
            else: 
                for i in range (len(scores)):
                    draw_text(SCREEN, (MID_WIDTH_SCREEN, 200+50*(i+1)), f"{i+1} - Nombre: {scores[i]["name"]}    Score: {scores[i]["score"]}", font_1, CUSTOM_RED, bg=WHITE)

        draw_text(SCREEN, (MID_WIDTH_SCREEN, 550), "Presione SPACE para ir al menu principal", font_1, CUSTOM_BLUE, bg=WHITE)

        pygame.display.flip()
        wait_user(K_SPACE)
        running = False