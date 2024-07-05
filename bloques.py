import pygame
from random import randint
from settings import *

def create_block (imagen: pygame.Surface = None, left = 0, top = 0, width = 50, height = 50, color = (255, 255, 255), dir = 3, borde = 0, radio = -1): 
    if imagen: 
        imagen = pygame.transform.scale (imagen, (width, height))
    return {"rect": pygame.Rect(left, top, width, height), "color": color, "dir": dir, "borde": borde, "radio": radio, "img": imagen}
    
def create_enemy(imagen: pygame.Surface = None):
    block =  create_block (imagen, randint(0, WIDTH-ENEMY_WIDHT), randint(-HEIGHT, 0 - ENEMY_HEIGHT), ENEMY_WIDHT, ENEMY_HEIGHT)
    block ["speed_y"] = randint(MIN_SPEED_ENEMY_Y, MAX_SPEED_ENEMY_Y)
    return block

def load_enemy_list (lista: list, quant_enemy: int, imagen:pygame.Surface = None):
    for  _ in range (quant_enemy):
        lista.append (create_enemy(imagen))

def create_player (imagen: pygame.Surface = None): 
    return create_block (imagen, randint(0, WIDTH-player_width), randint(0, HEIGHT - player_height), player_width, player_height, BLUE, radio = player_height//2)

def create_laser(midBottom:tuple[int,int],color:tuple[int,int,int] = RED, laser_w = LASER_WIDTH, laser_h = LASER_WIDTH):
    block = {"rect":pygame.Rect(0,0,laser_w,laser_h),"color":color,"speed": LASER_SPEED}
    block["rect"].midbottom = midBottom
    return block

