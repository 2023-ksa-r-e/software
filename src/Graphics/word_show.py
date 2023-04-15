import random

from utils import global_path
import pygame


def show(screen, cross, TIMER_BOOL):
    if TIMER_BOOL:
        randomtime = random.randrange(3000, 5001)
        TIMER_BOOL = False
