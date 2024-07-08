import pygame

def detectar_colision (block_1: pygame.Rect, block_2: pygame.Rect)->bool:
    """Evalua si dos rectángulos se tocan entre sí.

    Args:
        block_1 (pygame.Rect): primer rectangulo
        block_2 (pygame.Rect): segundo rectangulo

    Returns:
        bool: devuelve True si los rectangulos se tocan y False si los rectangulos no se tocan.
    """
    if punto_in_block (block_1.topleft, block_2) or punto_in_block (block_1.topright, block_2) or \
        punto_in_block (block_1.bottomleft, block_2) or punto_in_block (block_1.bottomright, block_2) or\
        punto_in_block (block_2.topleft, block_1) or punto_in_block (block_2.topright, block_1) or \
        punto_in_block (block_2.bottomleft, block_1) or punto_in_block (block_2.bottomright, block_1):
        return True
    else: 
        return False

def punto_in_block (punto, block)->bool:
    """Recibe un punto y un rectángulo por parámetro. 

    Args:
        punto (_type_):  primer rectangulo
        block (_type_):rectangulo

    Returns:
        bool: devuelve True el punto coindice con el área rectángulo, sino False. 
    """
    x, y = punto
    return x >= block.left and x <= block.right and y >= block.top and y <= block.bottom
