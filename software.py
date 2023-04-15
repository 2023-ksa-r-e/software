import os
import random
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
SIPJAGA = pygame.image.load(
    global_path.get_proj_abs_path("assets/sipjaga.png")
).convert_alpha()
SIPJAGA = pygame.transform.smoothscale(SIPJAGA, (screen_x, screen_y))
#######################################################################################################################
mainLoop = 1
start_tick = pygame.time.get_ticks()
#######################################################################################################################

randomtime = random.randrange(3000, 5001)
while mainLoop:
    current_tick = pygame.time.get_ticks()
    delta_tick = current_tick - start_tick
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            mainLoop = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            mainLoop = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            start_tick = pygame.time.get_ticks()

    screen.fill((255, 255, 255))

    # fixation cross(random time between 3s-5s)
    if delta_tick < randomtime:
        screen.blit(SIPJAGA, (0, 0))

    else:
        pass

    # fps
    dt = clock.tick(60)

    pygame.display.flip()

pygame.quit()
sys.exit()
