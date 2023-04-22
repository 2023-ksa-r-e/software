import random

import pygame

from utils import global_path, global_variables

random_time = 0


def show(screen, cross, delta_tick, imageset):
    global random_time
    if global_variables.Timer_BOOL:
        random_time = random.randrange(3000, 5001)
        global_variables.Timer_BOOL = False
        print(f"{random_time}ms for cross fixation")
    if delta_tick < random_time:
        screen.blit(cross, (0, 0))
    elif delta_tick < random_time + 3000:
        screen.blit(imageset[-1], (0, 0))
    elif delta_tick < random_time + 3000 + 2000:
        if global_variables.tmpBool:
            imageset.pop()
            global_variables.tmpBool = False
        screen.fill((255, 255, 255))
    elif delta_tick < random_time + 3000 + 2000 + random_time:
        if not global_variables.tmpBool:
            global_variables.tmpBool = True
        screen.blit(cross, (0, 0))
    elif delta_tick < random_time + 3000 + 2000 + random_time + 3000:
        screen.blit(imageset[-1], (0, 0))
    elif delta_tick < random_time + 3000 + 2000 + random_time + 3000 + 2000:
        screen.fill((255, 255, 255))
    else:
        global_variables.Timer_BOOL = True
        global_variables.start_tick = pygame.time.get_ticks()
        print(len(imageset))
        print(imageset)
