import os
import sys
import time

import pygame
from pygame.locals import *

from utils import global_path

from src.Graphics import window

global_path.set_proj_abs_path(os.path.abspath(__file__))
pygame.init()
screen, screen_x, screen_y = window.setup()
clock = pygame.time.Clock()
#######################################################################################################################
SIPZAGA = pygame.image.load(
    global_path.get_proj_abs_path("assets/sipjaga.png")
).convert_alpha()
SIPZAGA = pygame.transform.smoothscale(SIPZAGA, (screen_x, screen_y))
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
    screen.blit(SIPZAGA, (0, 0))

    dt = clock.tick(60)

    pygame.display.flip()

pygame.quit()
sys.exit()
