import math

import pygame

from utils import global_variables

SCHTARN_COL = (255, 10, 84)


def draw(IMG_SCHTARN_GAME, screen, screen_x, screen_y, SCHTARN_GAME_SOUND, delta_tick):
    screen.blit(IMG_SCHTARN_GAME, (0, 0))
    if delta_tick < 1000:
        if global_variables.SCHTARN_GAME_SOUND_PLAY_ONCE:
            SCHTARN_GAME_SOUND.play()
            global_variables.SCHTARN_GAME_SOUND_PLAY_ONCE = False
        pygame.draw.rect(
            screen,
            SCHTARN_COL,
            pygame.Rect(
                0, 0, math.sin(delta_tick * math.pi / 2000) * screen_x, screen_y / 35
            ),
        )
    elif delta_tick < 1500:
        pygame.draw.rect(
            screen, SCHTARN_COL, pygame.Rect(0, 0, screen_x, screen_y / 35)
        )
        pygame.draw.rect(
            screen,
            SCHTARN_COL,
            pygame.Rect(
                screen_x - screen_y / 35 + 1,
                0,
                screen_y / 35,
                math.sin((delta_tick - 1000) * math.pi / 1000) * screen_y,
            ),
        )
    elif delta_tick < 2500:
        pygame.draw.rect(
            screen, SCHTARN_COL, pygame.Rect(0, 0, screen_x, screen_y / 35)
        )
        pygame.draw.rect(
            screen,
            SCHTARN_COL,
            pygame.Rect(screen_x - screen_y / 35 + 1, 0, screen_y / 35, screen_y),
        )
        pygame.draw.rect(
            screen,
            SCHTARN_COL,
            pygame.Rect(
                screen_x - math.sin((delta_tick - 1500) * math.pi / 2000) * screen_x,
                screen_y - screen_y / 35 + 1,
                screen_x,
                screen_y / 35,
            ),
        )
    elif delta_tick < 3000:
        pygame.draw.rect(
            screen, SCHTARN_COL, pygame.Rect(0, 0, screen_x, screen_y / 35)
        )
        pygame.draw.rect(
            screen,
            SCHTARN_COL,
            pygame.Rect(screen_x - screen_y / 35 + 1, 0, screen_y / 35, screen_y),
        )
        pygame.draw.rect(
            screen,
            SCHTARN_COL,
            pygame.Rect(0, screen_y - screen_y / 35 + 1, screen_x, screen_y / 35),
        )
        pygame.draw.rect(
            screen,
            SCHTARN_COL,
            pygame.Rect(
                0,
                screen_y - math.sin((delta_tick - 2500) * math.pi / 1000) * screen_y,
                screen_y / 35,
                screen_y,
            ),
        )
    else:
        pygame.draw.rect(
            screen, SCHTARN_COL, pygame.Rect(0, 0, screen_x, screen_y / 35)
        )
        pygame.draw.rect(
            screen,
            SCHTARN_COL,
            pygame.Rect(screen_x - screen_y / 35 + 1, 0, screen_y / 35, screen_y),
        )
        pygame.draw.rect(
            screen,
            SCHTARN_COL,
            pygame.Rect(0, screen_y - screen_y / 35 + 1, screen_x, screen_y / 35),
        )
        pygame.draw.rect(
            screen, SCHTARN_COL, pygame.Rect(0, 0, screen_y / 35, screen_y)
        )
        pygame.draw.rect(
            screen,
            SCHTARN_COL,
            pygame.Rect(
                0,
                0,
                (math.sin((delta_tick - 3000) * math.pi / 1000)) ** 4 * screen_x,
                screen_y,
            ),
        )
