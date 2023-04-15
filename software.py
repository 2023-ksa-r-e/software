import os
import random
import sys
import time

import pygame
from pygame.locals import *

from utils import global_path
from utils import global_variables

from src.Graphics import window, word_show

global_path.set_proj_abs_path(os.path.abspath(__file__))
pygame.init()
screen, screen_x, screen_y = window.setup()
clock = pygame.time.Clock()

#######################################################################################################################

wordSet = os.listdir(global_path.get_proj_abs_path("assets/words"))
wordSet = [i.split("_")[0] for i in wordSet]
wordSet = list(set(wordSet))


for i in range(len(wordSet)):
    wordSet[i] = [wordSet[i], wordSet[i]]

random.shuffle(wordSet)
wordSet = wordSet[:global_variables.numOfTests]

#######################################################################################################################
cross = pygame.image.load(
    global_path.get_proj_abs_path("assets/cross.png")
).convert_alpha()
cross = pygame.transform.smoothscale(cross, (screen_x, screen_y))

L = []
for s in wordSet:
    tmp1 = pygame.image.load(
        global_path.get_proj_abs_path(f"assets/words/{s[0]}_1.png")
    ).convert_alpha()
    tmp1 = pygame.transform.smoothscale(tmp1, (screen_x, screen_y))

    tmp2 = pygame.image.load(
        global_path.get_proj_abs_path(f"assets/words/{s[1]}_2.png")
    ).convert_alpha()
    tmp2 = pygame.transform.smoothscale(tmp1, (screen_x, screen_y))

    L.append([tmp1, tmp2])

#######################################################################################################################

mainLoop = 1
start_tick = pygame.time.get_ticks()
#######################################################################################################################

TIMER_BOOL = True
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
    screen.blit(cross, (0, 0))
    word_show(screen, cross, TIMER_BOOL, )

    # fps
    dt = clock.tick(60)

    pygame.display.flip()

pygame.quit()
sys.exit()
