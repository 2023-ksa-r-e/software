import os

import pygame
from pygame.locals import *

from utils import global_path


def setup():
    icon = pygame.image.load(global_path.get_proj_abs_path("assets/zuvenz_icon.png"))
    pygame.display.set_icon(icon)

    dev = False

    if dev:
        screen_x, screen_y = 1280, 720
        flags = DOUBLEBUF | HWSURFACE | HWACCEL

    else:
        flags = DOUBLEBUF | FULLSCREEN | HWSURFACE | HWACCEL | SCALED
        screen_x, screen_y = (
            pygame.display.Info().current_w,
            pygame.display.Info().current_h,
        )

    screen = pygame.display.set_mode((screen_x, screen_y), flags)
    pygame.display.set_caption("ZUVENZ")
    print(screen_x, screen_y)
    return screen, screen_x, screen_y
