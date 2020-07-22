# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 18:42:13 2018

@author: abhinav
"""

import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Abhinav"s Screen')
screen.fill((0,0,0))
done=False

segment_width=5
segment_length=5

image = pygame.Surface([segment_width, segment_length])
image.fill((255,255,255))
rect = image.get_rect()
image.draw(screen)

while not done:
    for event in pygame.event.get():
        print(event.type)
        print(event)
        if event.type == pygame.QUIT:
            done = True
            print("I got a QUIT from the user")
pygame.quit()