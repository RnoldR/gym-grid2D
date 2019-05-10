#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 20:29:09 2019

@author: arnold
"""

import sys
import pygame

clock = pygame.time.Clock()
white = (255, 64, 64)
w = 810
h = 420
screen = pygame.display.set_mode((w, h))
screen.fill((white))

screen.fill((white))
x = 0
y = 0
#screen.blit(redSquare, (x, y))
pygame.display.flip()

running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print('mouse', x, y)