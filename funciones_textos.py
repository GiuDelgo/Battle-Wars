import pygame
from settings import WHITE

def draw_text(superficie:pygame.Surface, coordenada:tuple[int,int], texto:str, fuente:pygame.font, color:tuple[int,int,int] = WHITE, bg:tuple[int,int,int] = None):
    """Recibe un string y una fuente, crea la superficie del texto, obtiene el reactángulo de la superficie, y dibuja la superficie del texto sobre otra superficie

    Args:
        superficie (pygame.Surface): Superficie sobre la que se renderiza el texto
        coordenada (tuple[int,int]): Coordenada donde se renderiza el texto
        texto (str): Texto que se desea mostrar en pantalla
        fuente (pygame.font): Fuente del texto
        color (tuple[int,int,int], optional): Color de la fuente. Defaults to WHITE.
        bg (tuple[int,int,int], optional): Fondo del texto. Defaults to None.
    """
    sup_text = fuente.render(texto,True,color,bg)
    rect_texto = sup_text.get_rect()
    rect_texto.center = coordenada

    superficie.blit(sup_text,rect_texto)