#!/usr/bin/python
import sys, pygame
from random import randint
pygame.init()

size = width, height = 800, 600
speed = [1, 1]
black = 0, 0, 0
white = 255,255,255

screen = pygame.display.set_mode(size)
screen.fill(white)
heli = pygame.image.load("heli.png")
heli1 = pygame.image.load("heli1.png")
helirect = heli.get_rect()
rot=True
while 1:
     for event in pygame.event.get():
         if event.type == pygame.QUIT: sys.exit()

     if rot: 
         helirect = helirect.move(speed)
         if helirect.left < 0 or helirect.right > width or randint(1,50) == 1:
             speed[0] = -speed[0]
         if helirect.top < 0 or helirect.bottom > height or randint(1,50) == 1:
             speed[1] = -speed[1]

     rot=not rot
     screen.fill(white)
     #helirect.fill(white)
     screen.blit(heli if rot else heli1 , helirect)
     pygame.display.flip()
