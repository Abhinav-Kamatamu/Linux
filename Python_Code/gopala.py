import pygame
import random
import sys
import tkinter
from pygame.locals import *
from time import sleep
from tkinter import messagebox
pygame.init()
 
clock  = pygame.time.Clock()
 
a = 0
b = 0
 
window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Caption')
pygame.display.set_caption('\t YOU:'+str(a)+'AI:'+str(b)+'\t')

rock = pygame.image.load('rock.png')
paper = pygame.image.load('paper.png')
scissors = pygame.image.load('scissors.png')
wall = pygame.image.load('wallpaper.jpg')
window.blit(wall,(0,0))
 
done = False
output = True
blitz = False
 
def redrawgamewindow(blitz):
    window.blit(wall,(0,0))
    if blitz:
        window.blit(ai_play,(320,360))
        window.blit(user_play,(960,360))        
        pygame.display.set_caption('\t YOU:'+str(a)+'AI:'+str(b)+'\t')
        pygame.display.update()
        blitz = False
        sleep(3) 
          
playZ = [rock,paper,scissors]
#mainloop
while not done:
    clock.tick(60)
#    print ("Entering the while loop")
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    ai_play = random.choice(playZ)
    print ("After the random choice")

    if a ==5 or b == 5:
        if a == 5:
            messagebox.showinfo('Notice','You have won the game')
        elif b == 5:
            messagebox.showinfo('Notice','The AI has won the game')
        done = True   
        
    if a < 5 and b < 5:
        keys = pygame.key.get_pressed()
        sleep(5)
        print ("The input has been taken", a, b)
        print(keys[pygame.K_r])
        if  keys[pygame.K_r]:
            print("The key R is pressed")
            user_play = rock
            blitz = True
        if keys[pygame.K_p]:
            user_play = paper
            blitz = True
        if keys[pygame.K_s]:
            user_play = scissors
            blitz = True
        if keys[pygame.K_h]:
            messagebox.showinfo('Notice','r - ROCK','\n' ,'p - PAPER', '\n' ,'s - SCISSORS')
 
        if ai_play == 1:
            ai_play = rock
        elif ai_play == 2:
            ai_play == paper
        elif ai_play == 3:
            ai_play == scissors
     
        if blitz:           
            if (user_play == rock and ai_play == scissors) or (user_play == scissors and ai_play == paper) or (user_play == paper and ai_play == rock):
                a += 1
            elif (user_play == rock and ai_play == paper) or (user_play == scissors and ai_play == rock) or (user_play == paper and ai_play == scissors):
                b += 1  
 
    redrawgamewindow(blitz)
 
pygame.quit()
sys.exit()
