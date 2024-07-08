import pygame
from settings import *
from random import randint
from funciones_bloques import *
from funciones_colisiones import *
from pygame.locals import * 
from funciones_user import *
from funciones_textos import *
from funciones_listas import *
from screen_game_over import *

def game_over(SCREEN: pygame.display, score: int):
    """Pantalla de game over. Se muestra cada vez que un jugador pierde todas sus vidas.

    Args:
        SCREEN (pygame.display): Ventana sobre la cual se renderizan los elementos de la pantalla 
        score (int): puntuación del jugador
    """
    game_over_sound = pygame.mixer.Sound("./src/assets/sounds/game_over.mp3")
    game_over_sound.set_volume(preferencias["volumen"])

    imagen_pantalla_fin = pygame.image.load("./src/assets/images/fondo_pantalla_fin.jpg")
    imagen_pantalla_fin = pygame.transform.scale(imagen_pantalla_fin, SIZE_SCREEN)

    font_1 = pygame.font.Font("./src/assets/fonts/Military Poster.ttf", preferencias["size_font_1"])
    font_2 = pygame.font.Font("./src/assets/fonts/Military Poster.ttf", preferencias["size_font_2"])
    font_3 = pygame.font.Font("./src/assets/fonts/Military Poster.ttf", preferencias["size_font_3"])

    pygame.mixer.music.stop()
    game_over_sound.play()

    # Muestra pantalla inicial de Game Over
    SCREEN.blit(imagen_pantalla_fin, ORIGIN)
    draw_text(SCREEN, CENTER_SCREEN, "GAME OVER", font_3, CUSTOM_RED)
    draw_text(SCREEN, (WIDTH // 2, HEIGHT - 50), "Presione SPACE para ir al menu principal", font_2, CUSTOM_RED, bg=WHITE)
    draw_text(SCREEN, POS_LAST_SCORE, f"Last Score: {score}", font_1, WHITE)

    pygame.display.flip()

    name = input("Ingrese su nombre: ")

    import json

    # Cargar y actualizar la lista de puntuaciones
    try:
        with open("./src/scores.json", "r", encoding="utf-8") as archivo:
            scores = json.load(archivo)
    except FileNotFoundError:
        print("El archivo no existe. Se creará uno nuevo.")
        scores = []
    except json.JSONDecodeError:
        print("El archivo JSON está vacío o contiene un formato inválido. Se sobreescribirá el archivo.")
        scores = []

    scores.append({"name": name, "score": score})

    try:
        ordenar_lista(lambda ant, act: ant["score"] < act["score"], scores)
    except TypeError as error:
        print(error)

    with open("./src/scores.json", "w", encoding="utf-8") as archivo:
        json.dump(scores, archivo, indent=4)

    if score == scores[0]["score"]:
        high_score = score
    else:
        high_score = scores[0]["score"]

    # Actualiza y muestra pantalla de Game Over con la puntuación actualizada
    SCREEN.blit(imagen_pantalla_fin, ORIGIN)
    draw_text(SCREEN, CENTER_SCREEN, "GAME OVER", font_3, CUSTOM_RED)
    draw_text(SCREEN, (WIDTH // 2, HEIGHT - 50), "Presione SPACE para ir al menu principal", font_2, CUSTOM_RED, bg=WHITE)
    draw_text(SCREEN, POS_LAST_SCORE, f"Last Score: {score}", font_1, WHITE)
    draw_text(SCREEN, POS_HIGH_SCORE, f"NEW High Score: {high_score}" if score == high_score else f"LAST High Score: {high_score}", font_1, WHITE)

    pygame.display.flip()

    wait_user(K_SPACE)