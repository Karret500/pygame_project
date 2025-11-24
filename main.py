import pygame
from pygame.math import Vector2
import level
from settings import*

# initialize
pygame.init()
screen = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()

#test push

level = level.Level()


run = True
while run:
    screen.fill((0,0,0))
    
    #draw
    level.draw(screen)   
    level.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(60)  # limit FPS

pygame.quit()

