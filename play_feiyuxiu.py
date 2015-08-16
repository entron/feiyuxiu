#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pygame
import os, glob


mp3_files = glob.glob("*.mp3")
mp3_file = mp3_files[0]

pygame.mixer.init()
pygame.mixer.music.set_volume(0.9)
pygame.mixer.music.load(mp3_file)
pygame.mixer.music.play()

import time
time.sleep(4500)
pygame.mixer.music.stop()
