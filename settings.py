from random import randint

WIDTH = 800
HEIGHT = 600
SIZE_SCREEN = (WIDTH, HEIGHT)
MID_WIDTH_SCREEN = WIDTH //2
MID_HEIGHT_SCREEN = HEIGHT //2
CENTER_SCREEN = (MID_WIDTH_SCREEN, MID_HEIGHT_SCREEN)
BOTTOM_SCREEN = 550

PISO_WIDTH = WIDTH
PISO_HEIGHT = HEIGHT//4

FPS = 40

#Posiciones texto
POSITION_SCORE = (MID_WIDTH_SCREEN,50)
POSITION_LIVES = (700,50)
POSITION_MUTE = (50, 550)
POSITION_PAUSE = CENTER_SCREEN

POSICION_TITLE = (MID_WIDTH_SCREEN,150)

#Dimension START button
START_WIDTH = 240
START_HEIGHT = 80

#Dimensiones player
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 90
MID_PLAYER_WIDTH = PLAYER_WIDTH//2
SPEED = 5

#Setting Laser
LASER_WIDTH = 10
LASER_HEIGHT = 20
LASER_SPEED = 30
UPGRADE_LASER_WIDTH = 20
UPGRADE_LASER_HEIGHT = 40

#Speed enemys
MIN_SPEED_ENEMY_Y = 1
MAX_SPEED_ENEMY_Y = 4

#Dimendiones enemys
ENEMY_WIDHT = 20
ENEMY_HEIGHT = 70
ENEMY_1_QUANT = 2
ENEMY_2_QUANT = 2

#Tiempos de BONUS
BONUS_TIME_LOOP_MIN = 5000
BONUS_TIME_LOOP_MAX = 30000
RAND_BONUS_LOOP = randint(BONUS_TIME_LOOP_MIN, BONUS_TIME_LOOP_MAX)
BONUS_TIME_END = 8000
BONUS_HEIGHT = 50
BONUS_WIDTH = 50

#Colores
RED = (255, 0, 0)
CUSTOM_RED = (255, 60, 60)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CUSTOM_BLUE = (50, 50, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CUSTOM = (157, 208, 230)
#--------------------------------------------------------------------------

POS_SCORE = (MID_WIDTH_SCREEN, 30)
POS_MUTE = (50, HEIGHT - 50)

ORIGIN = (0,0)

FPS = 40

STAR_BUTTON_SIZE = (200,200)

POS_LAST_SCORE = (150, 50)
POS_HIGH_SCORE = (WIDTH - 150, 50)

TIMEGAME = 20000

#dimensiones player
player_width = 70
player_height = 70
mid_player_width = player_width//2

min_speed_y_coin = 3
max_speed_y_coin = 7

#dimensiones coin
coin_widht = 40
coin_height = 40

count_coins = 25
width_coin = 20
height_coin = 20

laser_width = 6
laser_height = 16
laser_speed = 15

speed = 5

gravedad = True
gravedad_x = True

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CUSTOM = (157, 208, 230)

colors = [RED, BLUE, GREEN, MAGENTA, YELLOW, CYAN, BLACK, WHITE]