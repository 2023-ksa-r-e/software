import math

import pygame
from src.Graphics.schtarn_games import SCHTARN_COL


def draw(screen, screen_x, screen_y, delta_tick):
    screen.fill(SCHTARN_COL)
    OPENING_COVER = pygame.Surface((screen_x, screen_y))
    OPENING_COVER.set_alpha(int(255 * math.sin((delta_tick - 3500) * math.pi / 7000)))
    OPENING_COVER.fill((0, 0, 0))
    screen.blit(OPENING_COVER, (0, 0))
