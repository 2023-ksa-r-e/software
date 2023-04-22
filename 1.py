import os
import random
import sys

import pygame

from utils import global_path
import window

from win32com.client import Dispatch # win api to get eeg machine


brainrecorder = Dispatch("VisionRecorder.Application")
print("brainrecorder enabled!")

global_path.set_proj_abs_path(os.path.abspath(__file__))
pygame.init()
WINDOW_NAME = "R&E_T1"
screen, screen_x, screen_y = window.setup(window_name=WINDOW_NAME)
clock = pygame.time.Clock()
#######################################################################################################################
#######################################################################################################################
cross = pygame.image.load(
    global_path.get_proj_abs_path("assets/cross.png")
).convert_alpha()
cross = pygame.transform.smoothscale(cross, (screen_x, screen_y))

thankyou = pygame.image.load(global_path.get_proj_abs_path("assets/thankyou.png"))
thankyou = pygame.transform.smoothscale(thankyou, (screen_x, screen_y))

SOUND = pygame.mixer.Sound(
    global_path.get_proj_abs_path("assets/sounds/term.mp3")
)

wordset = ["가볍다", "눈", "다리", "병", "철", "장"]
copied_wordset = []
for i in wordset:
    copied_wordset.append(i+"_1")
    copied_wordset.append(i+"_2")

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

random.seed(42)
random.shuffle(imageset)
random.seed(42)
random.shuffle(copied_wordset)
copied_wordset = copied_wordset[::-1]
print(copied_wordset)

#######################################################################################################################

mainLoop = 1
standard_tick = pygame.time.get_ticks()
#######################################################################################################################


RUN_ONCE = True
SOUND_ONCE = True
IMAGE = None
WORD_TIME = 2000
EEG_ONCE = True

brainrecorder.Acquisition.StartRecording(fname)
brainrecorder.Acquisition.SetMarker(str(trigger), ["Stimulus"])
print("brainrecording started.")
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
        pygame.display.set_caption(WINDOW_NAME + "_" + str(len(imageset)))
        IMAGE = imageset.pop()
        RUN_ONCE = False

    # fixation cross(random time between 3s-5s)
    if imageset:

        if delta_tick < cross_fixation_time:
            screen.blit(cross, (0, 0))
        elif delta_tick < cross_fixation_time + WORD_TIME + 1:
            if SOUND_ONCE:
                SOUND.play()
                SOUND_ONCE = False
            screen.blit(IMAGE, (0, 0))
        elif delta_tick < cross_fixation_time + WORD_TIME + 2000 + 1:
            screen.blit(cross, (0, 0))
            if not SOUND_ONCE:
                SOUND_ONCE = True
        elif delta_tick < cross_fixation_time + WORD_TIME + 2000 + 2000 + 1:
            if SOUND_ONCE:
                SOUND.play()
                SOUND_ONCE = False
            screen.fill((255, 255, 255))
        else:
            print(f"cross_fixation_time = {cross_fixation_time}ms")
            standard_tick = pygame.time.get_ticks()
            RUN_ONCE = True
            SOUND_ONCE = True
    else:
        if EEG_ONCE:
            brainrecorder.Acquisition.StopRecording()
            EEG_ONCE = False
        screen.blit(thankyou, (0, 0))

    # fps
    dt = clock.tick(60)

    pygame.display.flip()

pygame.quit()
sys.exit()
