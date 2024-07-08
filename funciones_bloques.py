import pygame
from random import randint
from settings import *

def validar_lista (lista: list)->None:
    """Valida que el parametro sea de tipo lista

    Args:
        lista (list): parametro a verifiar como lista

    Raises:
        TypeError: en caso de que no se haya pasado una lista la función devuleve un error de tipo
    """
    if not isinstance(lista,list):
        raise TypeError("Se esperaba una lista")

def create_block (imagen: pygame.Surface = None, left:int = 0, top:int = 0, width:int = 50, height:int = 50, color:tuple [int, int, int] = (255, 255, 255), dir:int = 3, borde:int = 0, radio:int = -1) -> dict:
    """Recibe parámetros y crea un rectángulo. En caso de recibir una imagen crea una superficie con su rectángulo asociado. 

    Args:
        imagen (pygame.Surface, optional): Imagen, en caso de qurer crear una superficie con imagen. Defaults to None.
        left (int, optional): coordenada X de la esquina superior izquierda. Defaults to 0.
        top (int, optional): coordenada Y de la esquina superior izquierda del rectángulo. Defaults to 0.
        width (int, optional): ancho del rectángulo. Defaults to 50.
        height (int, optional): alto del rectángulo. Defaults to 50.
        color (tuple[int, int, int], optional): color del rectángulo. Defaults to (255, 255, 255).
        dir (int, optional): dirección del rectángulo. Defaults to 3.
        borde (int, optional): borde del rectángulo. Defaults to 0.
        radio (int, optional): radio del rectángulo. Defaults to -1.

    Returns:
        dict: Diccionario con el rectángulo, color, dirección, borde, radio e imagen (si se proporciona).
    """
    if not isinstance(left, int) or not isinstance(top, int):
        raise ValueError("Las coordenadas 'left' y 'top' deben ser enteros.")
    
    if not isinstance(width, int) or width <= 0:
        raise ValueError("El 'width' debe ser un entero positivo.")
    
    if not isinstance(height, int) or height <= 0:
        raise ValueError("El 'height' debe ser un entero positivo.")
    
    if not isinstance(color, tuple) or len(color) != 3 or not all(isinstance(c, int) for c in color):
        raise ValueError("El 'color' debe ser una tupla de tres enteros.")
    
    if imagen and not isinstance(imagen, pygame.Surface):
        raise ValueError("La 'imagen' debe ser una instancia de pygame.Surface o None.")
    
    if imagen: 
        imagen = pygame.transform.scale (imagen, (width, height))
    return {"rect": pygame.Rect(left, top, width, height), "color": color, "dir": dir, "borde": borde, "radio": radio, "img": imagen}
    
def create_enemy(imagen: pygame.Surface = None) -> dict:
    """Crea una superficie con una direccion en Y aleatoria entre dos valores. 

    Args:
        imagen (pygame.Surface, optional): Imagen de la superifice. Defaults to None.

    Returns:
        dict: Diccionario con el bloque del enemigo y su velocidad en Y.
    """
    if imagen and not isinstance(imagen, pygame.Surface):
        raise ValueError("La 'imagen' debe ser una instancia de pygame.Surface o None.")

    block =  create_block (imagen, randint(0+5, WIDTH-ENEMY_WIDHT-5), randint(-HEIGHT, 0 - ENEMY_HEIGHT), ENEMY_WIDHT, ENEMY_HEIGHT)
    block ["speed_y"] = randint(MIN_SPEED_ENEMY_Y, MAX_SPEED_ENEMY_Y)
    return block

def load_enemy_list (lista: list, quant_enemy: int, imagen:pygame.Surface = None) -> None:
    """Carga una lista de superficies obstáculo.

    Args:
        lista (list): lista vacía
        quant_enemy (int): cantidad de superficie obstáculo que se crearán. 
        imagen (pygame.Surface, optional): imagen de la superficie obstáculo. Defaults to None.
        Returns: None
    """
    validar_lista (lista)
    for  _ in range (quant_enemy):
        lista.append (create_enemy(imagen))

def create_laser(midBottom:tuple[int,int],color:tuple[int,int,int] = RED, laser_w = LASER_WIDTH, laser_h = LASER_WIDTH)-> pygame.Rect:
    """Crea un rectángulo que colisiona con las superficie obstáculo y las elimina. 

    Args:
        midBottom (tuple[int,int]): Coordenada inferior central del rectángulo.
        color (tuple[int,int,int], optional): Color del rectángulo. Defaults to RED.
        laser_w (_type_, optional): Ancho del rectángulo. Defaults to LASER_WIDTH.
        laser_h (_type_, optional): Alto del rectángulo. Defaults to LASER_WIDTH.

    Returns:
        pygame.Rect: Diccionario con el rectángulo, color y velocidad.
    """
    if not isinstance(midBottom, tuple) or len(midBottom) != 2 or not all(isinstance(i, int) for i in midBottom):
        raise ValueError("El parámetro 'midBottom' debe ser una tupla de dos enteros.")
    
    if not isinstance(color, tuple) or len(color) != 3 or not all(isinstance(c, int) for c in color):
        raise ValueError("El parámetro 'color' debe ser una tupla de tres enteros.")
    
    if not isinstance(laser_w, int) or laser_w <= 0:
        raise ValueError("El 'laser_w' debe ser un entero positivo.")
    
    if not isinstance(laser_h, int) or laser_h <= 0:
        raise ValueError("El 'laser_h' debe ser un entero positivo.")

    block = {"rect":pygame.Rect(0,0,laser_w,laser_h),"color":color,"speed": LASER_SPEED}
    block["rect"].midbottom = midBottom
    return block

