import pygame
from pygame.locals import * 

def wait_user(tecla: pygame.event.Event):
    """Regula el bucle principal del juego. Verifica con un bucle que el usuario presione tecla o salga del juego.
        Si el usuario presiona una tecla, se saldrá de la función y el programa principal continuará su ejecución. 
        Si el usuario decide salir, se termina la ejecución del programa.
    Args:
        tecla (pygame.event.Event): tecle que se usa para continuar con la ejecución del programa
    """
    flag_start = True
    while flag_start:
        for event in pygame.event.get(): #relevo los eventos, y con el for analizo los eventos
            if event.type == pygame.QUIT: #si analizo los eventos y se lanza el evento quit (apreto la cruz) se sale del bucle
                terminar()
            if event.type == KEYDOWN: #Tipo de evento (apretar tecla)
                if event.key == tecla: #Tecla para abajo
                    flag_start = False 

def terminar ():
    """Desinicializa módulos de pygame y deja de ejecutar el programa
    """
    pygame.quit ()
    exit()
