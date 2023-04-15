import os
import sys
import time

import pygame
from pygame.locals import *

from utils import global_path

from src.Graphics import window, schtarn_games, opening_transition, ingame_frame
from src.File import manage_save_file

global_path.set_proj_abs_path(os.path.abspath(__file__))
pygame.init()
screen, screen_x, screen_y = window.setup()
clock = pygame.time.Clock()
#######################################################################################################################
SCHTARN_GAME = pygame.image.load(
    global_path.get_proj_abs_path("assets/images/schtarn_game.png")
).convert_alpha()
SCHTARN_GAME = pygame.transform.smoothscale(SCHTARN_GAME, (screen_x, screen_y))

SCHTARN_GAME_SOUND = pygame.mixer.Sound(
    global_path.get_proj_abs_path("assets/sounds/schtarn_game.mp3")
)

SHIUEO_SOUNDTRACK_INITIUM_NOVUM = pygame.mixer.Sound(
    global_path.get_proj_abs_path("assets/sounds/shiueo/01_ita_est.mp3")
)

LOUIS_HOFMANN = pygame.image.load(
    global_path.get_proj_abs_path("assets/images/Louis-Hofmann.png")
).convert_alpha()
LOUIS_HOFMANN = pygame.transform.smoothscale(
    LOUIS_HOFMANN, (screen_y / 8, screen_y / 8)
)

MIA_PAGE = pygame.image.load(
    global_path.get_proj_abs_path("assets/images/Mia-Page.png")
).convert_alpha()
MIA_PAGE = pygame.transform.smoothscale(MIA_PAGE, (screen_y / 8, screen_y / 8))
#######################################################################################################################
mainLoop = 1
start_tick = pygame.time.get_ticks()
#######################################################################################################################
u = True
while mainLoop:
    current_tick = pygame.time.get_ticks()
    delta_tick = current_tick - start_tick
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            mainLoop = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            mainLoop = False

    screen.fill((0, 0, 0))
    if delta_tick < 3500:
        schtarn_games.draw(
            SCHTARN_GAME, screen, screen_x, screen_y, SCHTARN_GAME_SOUND, delta_tick
        )
    elif delta_tick < 7000:
        opening_transition.draw(screen, screen_x, screen_y, delta_tick)
    else:
        if global_variables.PROGRESS == "0":
            ingame_frame.draw(screen, screen_x, screen_y, delta_tick)
            if global_variables.SHIUEO_ITA_EST_SOUND_PLAY_ONCE:
                SHIUEO_SOUNDTRACK_INITIUM_NOVUM.play()
                global_variables.SHIUEO_ITA_EST_SOUND_PLAY_ONCE = False

    dt = clock.tick(60)

    pygame.display.flip()

pygame.quit()
sys.exit()
