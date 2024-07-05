import pygame
from settings import *
from random import randint
from bloques import *
from colisiones import *
from pygame.locals import * #importo todas los eventos de pygame 

def terminar ():
    """Desinicializa módulos de pygame y deja de ejecutar el programa
    """
    pygame.quit ()
    exit()

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

def wait_user_click(rect_button: pygame.Rect):
    """Regula el bucle principal del juego. Verifica con un bucle que el usuario presione con el mouse el botón o salga del juego.
        Si el usuario presiona el botón, se saldrá de la función y el programa principal continuará su ejecución. 
        Si el usuario decide salir, se termina la ejecución del programa.
    Args:
        rect_button (pygame.Rect): rectangulo que funciona como boton
    """
    from colisiones import punto_in_block
    flag_start = True
    while flag_start:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                terminar()
            if event.type == MOUSEBUTTONDOWN: 
                if event.button == 1:
                    if punto_in_block (event.pos, rect_button):
                        flag_start = False 

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

#Inicializo modulos de Pygame
pygame.init()

#Configuro la ventana
pygame.display.set_caption("Battle Wars") #cambio el título de la ventana 

#Cargo icono juego
icono = pygame.image.load("./src/assets/images/icono.png")
pygame.display.set_icon(icono)

#Configuro pantalla
SCREEN = pygame.display.set_mode(SIZE_SCREEN)

#Eevento tiempo
LOOPBONUS = USEREVENT + 1
TIMEBONUSEND = USEREVENT + 2

#Cargo y escalo imagenes de fondo
imagen_fondo = pygame.image.load("./src/assets/images/ciudad_fondo.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo, SIZE_SCREEN)
piso_fondo = pygame.image.load("./src/assets/images/fondo_suelo_2.jpg")
imagen_fondo_piso = create_block(piso_fondo, top=450,width=PISO_WIDTH, height=PISO_HEIGHT)
imagen_pantalla_fin = pygame.image.load("./src/assets/images/fondo_pantalla_fin.jpg")
imagen_pantalla_fin = pygame.transform.scale(imagen_pantalla_fin, SIZE_SCREEN)

#Cargo imagen boton inicio 
start_button_img = pygame.image.load("./src/assets/images/start.png")

#Cargo imagen jugador
tank_img = pygame.image.load("./src/assets/images/tanque_guerra.png")

#Cargo imagen enemys
enemy_1_img = pygame.image.load("./src/assets/images/bomba_1.png")
enemy_2_img = pygame.image.load("./src/assets/images/bomba_2.png")

#Cargo imagen bonus
upgrade_img = pygame.image.load("./src/assets/images/upgrade.png")

#Cargo Fuente
font_1 = pygame.font.Font("./src/assets/fonts/Military Poster.ttf", 36)
font_2 = pygame.font.Font("./src/assets/fonts/Military Poster.ttf", 42)
font_3 = pygame.font.Font("./src/assets/fonts/Military Poster.ttf", 120)

#Cargo sonidos
explosion_1_sound = pygame.mixer.Sound("./src/assets/sounds/explosion_1.mp3")
explosion_1_sound.set_volume(0.2)
explosion_2_sound = pygame.mixer.Sound("./src/assets/sounds/explosion_2.mp3")
explosion_2_sound.set_volume(0.2)
error_sound = pygame.mixer.Sound("./src/assets/sounds/error.mp3")
error_sound.set_volume(1)
power_up_sound = pygame.mixer.Sound("./src/assets/sounds/power_up.mp3")
power_up_sound.set_volume(0.2)
game_over_sound = pygame.mixer.Sound("./src/assets/sounds/game_over.mp3")
game_over_sound.set_volume(0.2)

#Configuro Bucle
clock = pygame.time.Clock()#modulo time con funciones para manejo de tiempos

high_score = 0

while True: 
    #Pantalla Inicio
    SCREEN.blit(imagen_fondo,ORIGIN)
    draw_text(SCREEN,POSICION_TITLE,"Battle Wars",font_3,CUSTOM_RED)
    start_button = create_block(start_button_img, width=START_WIDTH, height=START_HEIGHT)
    start_button["rect"].center = CENTER_SCREEN
    SCREEN.blit(start_button["img"] , start_button["rect"])
    pygame.display.flip()
    wait_user_click(start_button["rect"])

    #Cargo musica
    pygame.mixer.music.load("./src/assets/music/game_music.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    playing_music = True

    #Creo jugador
    player = create_block (tank_img, MID_WIDTH_SCREEN-MID_PLAYER_WIDTH, BOTTOM_SCREEN-PLAYER_HEIGHT, width=PLAYER_WIDTH, height=PLAYER_HEIGHT)

    #Creo enemigos
    enemys_1 = []
    enemys_2 = []
    load_enemy_list(enemys_1, ENEMY_1_QUANT, enemy_1_img)
    load_enemy_list(enemys_2, ENEMY_2_QUANT, enemy_2_img)
    
    #Direcciones
    move_left = True
    move_right = True
    move_up = True
    move_down = True

    laser = None

    upgrade = None
    bandera_upgrade = False

    lives = 3
    score = 0

    # Configurar el temporizador para el evento LOOPBONUS
    pygame.time.set_timer(LOOPBONUS,RAND_BONUS_LOOP,1)

    is_running = True

    while is_running: 
        clock.tick(FPS)

        #ANALIZO EVENTOS
        for event in pygame.event.get(): #relevo los eventos, y con el for analizo los eventos
            if event.type == pygame.QUIT: #si analizo los eventos y se lanza el evento quit (apreto la cruz) se sale del bucle
                terminar()

            if event.type == KEYDOWN:

                if event.key == K_SPACE:
                    if not laser:
                        if bandera_upgrade:
                            laser = create_laser(player["rect"].midtop,laser_h= UPGRADE_LASER_HEIGHT, laser_w= UPGRADE_LASER_WIDTH, color= BLACK)
                            explosion_1_sound.play()
                        else: 
                            laser = create_laser(player["rect"].midtop, color= BLACK)
                            explosion_1_sound.play()
                #Mutear
                if event.key == K_m:
                    if playing_music:
                        pygame.mixer.music.pause()
                    else: 
                        pygame.mixer.music.unpause()
                    playing_music = not playing_music

                #Pausar juego
                if event.key == K_p: 
                    pygame.mixer.music.pause()
                    draw_text(SCREEN, POSITION_PAUSE, "Pause", font_1, WHITE)
                    pygame.display.flip()  
                    wait_user(K_p)
                    if playing_music: 
                        pygame.mixer.music.unpause()  
                
                if event.key == K_DOWN or event.key == K_s:
                    move_down = True
                    move_up = False
                if event.key == K_UP or event.key == K_w:
                    move_up = True
                    move_down = False
                if event.key == K_LEFT or event.key == K_a:
                    move_left = True
                    move_right = False
                if event.key == K_RIGHT or event.key == K_d:
                    move_right = True
                    move_left = False

            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    move_down = False
                if event.key == K_UP or event.key == K_w:
                    move_up = False
                if event.key == K_LEFT or event.key == K_a:
                    move_left = False
                if event.key == K_RIGHT or event.key == K_d:
                    move_right = False

            if event.type == LOOPBONUS:
                upgrade = create_block(upgrade_img, randint(0 + BONUS_WIDTH, WIDTH - BONUS_WIDTH), randint(imagen_fondo_piso["rect"].top + BONUS_HEIGHT, imagen_fondo_piso["rect"].bottom - BONUS_HEIGHT), BONUS_WIDTH, BONUS_HEIGHT)
                pygame.time.set_timer(LOOPBONUS,RAND_BONUS_LOOP,1)

            if event.type == TIMEBONUSEND: 
                bandera_upgrade = False

        #MUEVO BLOQUES/COLISIONES

        if move_left and player["rect"].left > 0:
            player["rect"].x -= SPEED
            if player["rect"].left < 0:
                player["rect"].left = 0
        if move_right and player["rect"].right < WIDTH:
            player["rect"].x += SPEED
            if player["rect"].right > WIDTH:
                player["rect"].right = WIDTH
        if move_up and player["rect"].top > HEIGHT - PISO_HEIGHT:
            player["rect"].y -= SPEED
            if player["rect"].top < 0:
                player["rect"].top = 0
        if move_down and player["rect"].bottom < HEIGHT:
            player["rect"].y += SPEED
            if player["rect"].bottom > HEIGHT:
                player["rect"].bottom = HEIGHT

        if laser:
            laser["rect"].move_ip(0,-laser["speed"])
            if laser["rect"].bottom < 0:
                laser = None

        for enemy in enemys_1:
            enemy["rect"].move_ip(0,enemy["speed_y"])
            if enemy["rect"].top > HEIGHT:
                enemy["rect"].bottom = 0
        
        for enemy in enemys_2:
            enemy["rect"].move_ip(0,enemy["speed_y"])
            if enemy["rect"].top > HEIGHT:
                enemy["rect"].bottom = 0

        for enemy in enemys_1[:]:
            if laser:
                if detectar_colision(enemy["rect"],laser["rect"]):
                    explosion_2_sound.play()
                    enemys_1.remove(enemy)
                    laser = None
                    score += 1
                    if len(enemys_1) == 0:
                        load_enemy_list(enemys_1, ENEMY_1_QUANT, enemy_1_img)

            if detectar_colision(enemy["rect"], imagen_fondo_piso["rect"]):
                error_sound.play()
                enemys_1.remove(enemy)
                lives -=1
                if lives == 0:
                    is_running = False
                if len(enemys_2) == 0:
                        load_enemy_list(enemys_1, ENEMY_1_QUANT, enemy_1_img)

        for enemy in enemys_2[:]:
            if laser:
                if detectar_colision(enemy["rect"],laser["rect"]):
                    explosion_2_sound.play()
                    enemys_2.remove(enemy)
                    laser = None
                    score += 1
                    if len(enemys_2) == 0:
                        load_enemy_list(enemys_2, ENEMY_2_QUANT, enemy_2_img)

            if detectar_colision(enemy["rect"], imagen_fondo_piso["rect"]):
                error_sound.play()
                enemys_2.remove(enemy)
                lives -=1
                if lives == 0:
                    is_running = False
                if len(enemys_2) == 0:
                        load_enemy_list(enemys_2, ENEMY_2_QUANT, enemy_2_img)
        
        if upgrade:
            if detectar_colision(player["rect"],upgrade["rect"]):
                power_up_sound.play()
                pygame.time.set_timer(TIMEBONUSEND,BONUS_TIME_END,1)
                bandera_upgrade = True
                upgrade = None
    
        #DIBUJO PANTALLA

        #Dibujo fondo
        SCREEN.blit(imagen_fondo, ORIGIN)
        SCREEN.blit(imagen_fondo_piso["img"], imagen_fondo_piso["rect"])

        #Dibujo jugador
        SCREEN.blit(player["img"], player ["rect"])

        #Dibujo laser
        if laser:
            pygame.draw.rect(SCREEN,laser["color"],laser["rect"])
        
        #Dibujo enemy
        for enemy in enemys_1:             
            SCREEN.blit(enemy["img"], enemy["rect"])
        for enemy in enemys_2:             
            SCREEN.blit(enemy["img"], enemy["rect"])

        #Dibujo upgrade
        if upgrade: 
            SCREEN.blit(upgrade["img"], upgrade["rect"])
        
        draw_text(SCREEN,POSITION_LIVES, f"Lives: {lives}",font_1,WHITE)
        draw_text(SCREEN,POSITION_SCORE, f"Score: {score}",font_2,CUSTOM_RED)

        if not playing_music: 
            draw_text(SCREEN, POSITION_MUTE, "Mute", font_1, WHITE)
        
        pygame.display.flip()  
    
    # Pantalla fin

    if score > high_score: 
        high_score = score

    pygame.mixer.music.stop()
    game_over_sound.play()
    SCREEN.blit(imagen_pantalla_fin,ORIGIN)

    draw_text(SCREEN, CENTER_SCREEN, "GAME OVER", font_3, CUSTOM_RED,)
    draw_text(SCREEN, (WIDTH//2, HEIGHT - 50), "Presione SPACE para comenzar", font_2, CUSTOM_RED, bg=WHITE)

    draw_text(SCREEN, POS_HIGH_SCORE, f"Last Score: {score}", font_2, WHITE)
    draw_text(SCREEN, POS_LAST_SCORE, f"High Score: {high_score}", font_2, WHITE)

    pygame.display.flip()
    wait_user(K_SPACE)

terminar()

