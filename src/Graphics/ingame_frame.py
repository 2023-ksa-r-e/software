import math

import pygame

from src.File import manage_save_file
from utils import global_variables

FRAME_COL = (255, 255, 255)


def draw(screen, screen_x, screen_y, delta_tick):
    if delta_tick < 7250:
        pygame.draw.rect(
            screen,
            FRAME_COL,
            pygame.Rect(
                0,
                0,
                math.sin((delta_tick - 7000) * math.pi / 500) * screen_x,
                screen_y / 160,
            ),
        )
    elif delta_tick < 7500:
        pygame.draw.rect(screen, FRAME_COL, pygame.Rect(0, 0, screen_x, screen_y / 160))
        pygame.draw.rect(
            screen,
            FRAME_COL,
            pygame.Rect(
                screen_x - screen_y / 160 - 1,
                0,
                screen_y / 160 + 2,
                math.sin((delta_tick - 7250) * math.pi / 500) * screen_y,
            ),
        )
    elif delta_tick < 7750:
        pygame.draw.rect(screen, FRAME_COL, pygame.Rect(0, 0, screen_x, screen_y / 160))
        pygame.draw.rect(
            screen,
            FRAME_COL,
            pygame.Rect(screen_x - screen_y / 160 - 1, 0, screen_y / 160 + 2, screen_y),
        )
        pygame.draw.rect(
            screen,
            FRAME_COL,
            pygame.Rect(
                screen_x - math.sin((delta_tick - 7500) * math.pi / 500) * screen_x,
                screen_y - screen_y / 160 + 1,
                screen_x,
                screen_y / 160,
            ),
        )
    elif delta_tick < 8000:
        pygame.draw.rect(screen, FRAME_COL, pygame.Rect(0, 0, screen_x, screen_y / 160))
        pygame.draw.rect(
            screen,
            FRAME_COL,
            pygame.Rect(screen_x - screen_y / 160 - 1, 0, screen_y / 160 + 2, screen_y),
        )
        pygame.draw.rect(
            screen,
            FRAME_COL,
            pygame.Rect(0, screen_y - screen_y / 160 + 1, screen_x, screen_y / 160),
        )
        pygame.draw.rect(
            screen,
            FRAME_COL,
            pygame.Rect(
                0,
                screen_y - math.sin((delta_tick - 7750) * math.pi / 500) * screen_y,
                screen_y / 160,
                screen_y,
            ),
        )
    else:
        if global_variables.PROGRESS_0_ONCE:
            global_variables.PROGRESS = 1
            manage_save_file.write(1)
            global_variables.PROGRESS_0_ONCE = False

        pygame.draw.rect(screen, FRAME_COL, pygame.Rect(0, 0, screen_x, screen_y / 160))
        pygame.draw.rect(
            screen,
            FRAME_COL,
            pygame.Rect(screen_x - screen_y / 160 - 1, 0, screen_y / 160 + 2, screen_y),
        )
        pygame.draw.rect(
            screen,
            FRAME_COL,
            pygame.Rect(0, screen_y - screen_y / 160 + 1, screen_x, screen_y / 160),
        )
        pygame.draw.rect(screen, FRAME_COL, pygame.Rect(0, 0, screen_y / 160, screen_y))
