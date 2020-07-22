import pygame
from pygame.locals import *
pygame.init()

w=1200
h=700
l=1
b=1
win=pygame.display.set_mode((w,h))
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
colour check(a):
	if a==1:
		my=pygame.draw.rect(win,(white),[x,y,l,b])
	if a==2:
		my=pygame.draw.rect(win,(black),[x,y,l,b])