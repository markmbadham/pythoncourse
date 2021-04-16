#!/usr/bin/python
import sys, pygame
from random import randint
from itertools import cycle
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
for rot in cycle([0, 0, 0, 1, 1, 1]):
     for event in pygame.event.get():
         if event.type == pygame.QUIT: sys.exit()

     helirect = helirect.move(speed)
     if helirect.left < 0 or helirect.right > width or randint(1,150) == 1:
         speed[0] = -speed[0]
     if helirect.top < 0 or helirect.bottom > height or randint(1,150) == 1:
         speed[1] = -speed[1]

     #rot = no§t rot
     screen.fill(white)
     #helirect.fill(white)
     screen.blit(heli if rot else heli1 , helirect)
     pygame.display.flip()
