import os
import random
import sys

import pygame

from utils import global_path
from utils import global_variables

from src.Graphics import word_show
import window

global_path.set_proj_abs_path(os.path.abspath(__file__))
pygame.init()
screen, screen_x, screen_y = window.setup()
clock = pygame.time.Clock()

#######################################################################################################################
#######################################################################################################################
cross = pygame.image.load(
    global_path.get_proj_abs_path("assets/cross.png")
).convert_alpha()
cross = pygame.transform.smoothscale(cross, (screen_x, screen_y))

wordSet = os.listdir(global_path.get_proj_abs_path("assets/words"))

print(wordSet)

L = []
for s in wordSet:
    tmp1 = pygame.image.load(
        global_path.get_proj_abs_path(f"assets/words/{s}")
    ).convert_alpha()
    tmp1 = pygame.transform.smoothscale(tmp1, (screen_x, screen_y))

    L.append(tmp1)

L = L[: global_variables.numOfTests]
random.shuffle(L)
print(L)


#######################################################################################################################

mainLoop = 1
global_variables.start_tick = pygame.time.get_ticks()
#######################################################################################################################

while mainLoop:
    current_tick = pygame.time.get_ticks()
    delta_tick = current_tick - global_variables.start_tick
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
    screen.blit(cross, (0, 0))
    word_show.show(screen, cross, delta_tick, L)

    # fps
    dt = clock.tick(60)

    pygame.display.flip()

pygame.quit()
sys.exit()
