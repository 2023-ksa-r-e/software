import os
import random
import sys

import pygame

from utils import global_path
import window

global_path.set_proj_abs_path(os.path.abspath(__file__))
pygame.init()
screen, screen_x, screen_y = window.setup(window_name="R&E_T1")
clock = pygame.time.Clock()

#######################################################################################################################
#######################################################################################################################
cross = pygame.image.load(
    global_path.get_proj_abs_path("assets/cross.png")
).convert_alpha()
cross = pygame.transform.smoothscale(cross, (screen_x, screen_y))

thankyou = pygame.image.load(global_path.get_proj_abs_path("assets/thankyou.png"))
thankyou = pygame.transform.smoothscale(thankyou, (screen_x, screen_y))

wordset = ["가볍다", "눈", "다리", "병", "철", "장"]

imageset = []

for i in wordset:
    tmp = pygame.image.load(
        global_path.get_proj_abs_path(f"assets/words/{i}_1.png")
    ).convert_alpha()
    tmp = pygame.transform.smoothscale(tmp, (screen_x, screen_y))
    imageset.append(tmp)
    tmp = pygame.image.load(
        global_path.get_proj_abs_path(f"assets/words/{i}_2.png")
    ).convert_alpha()
    tmp = pygame.transform.smoothscale(tmp, (screen_x, screen_y))
    imageset.append(tmp)

random.shuffle(imageset)

#######################################################################################################################

mainLoop = 1
standard_tick = pygame.time.get_ticks()
#######################################################################################################################


RUN_ONCE = True
IMAGE = None
while mainLoop:
    current_tick = pygame.time.get_ticks()
    delta_tick = current_tick - standard_tick
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            mainLoop = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            mainLoop = False

    screen.fill((255, 255, 255))

    if RUN_ONCE:
        cross_fixation_time = random.randrange(3000, 5000 + 1)
        IMAGE = imageset.pop()
        print(delta_tick, standard_tick)
        RUN_ONCE = False

    # fixation cross(random time between 3s-5s)
    if imageset:
        if delta_tick < cross_fixation_time:
            screen.blit(cross, (0, 0))
        elif delta_tick < cross_fixation_time + 1250 + 1:
            screen.blit(IMAGE, (0, 0))
        elif delta_tick < cross_fixation_time + 1250 + 2000 + 1:
            screen.blit(cross, (0, 0))
        elif delta_tick < cross_fixation_time + 1250 + 2000 + 2000 + 1:
            screen.fill((255, 255, 255))
        else:
            print(len(imageset))
            standard_tick = pygame.time.get_ticks()
            RUN_ONCE = True
    else:
        screen.blit(thankyou, (0, 0))

    # fps
    dt = clock.tick(60)

    pygame.display.flip()

pygame.quit()
sys.exit()
