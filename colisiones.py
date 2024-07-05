def detectar_colision (block_1, block_2)->bool:
    if punto_in_block (block_1.topleft, block_2) or punto_in_block (block_1.topright, block_2) or \
        punto_in_block (block_1.bottomleft, block_2) or punto_in_block (block_1.bottomright, block_2) or\
        punto_in_block (block_2.topleft, block_1) or punto_in_block (block_2.topright, block_1) or \
        punto_in_block (block_2.bottomleft, block_1) or punto_in_block (block_2.bottomright, block_1):
        return True
    else: 
        return False

def punto_in_block (punto, block)->bool:
    x, y = punto
    return x >= block.left and x <= block.right and y >= block.top and y <= block.bottom

def distancia_entre_puntos (punto1: tuple[int,int], punto2: tuple[int,int])->float: 
    return ((punto1[0] - punto2[0])**2 + (punto1[1] - punto2[1])**2)**0.5

def calcular_radio (block) -> int:
    radio = block.width // 2
    return radio

def detectar_colision_circulos (block_1, block_2)->bool:
    r1 = calcular_radio (block_1)
    r2 = calcular_radio (block_2)

    distancia = distancia_entre_puntos(block_1.center, block_2.center)

    return distancia <= r1+r2