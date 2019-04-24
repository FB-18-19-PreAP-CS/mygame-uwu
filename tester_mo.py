import pygame
import time 
WIDTH = 1000
HEIGHT = 1000

pygame.init()

screen = pygame.display.set_mode((WIDTH,WIDTH))
done = False



def circle(color,x,y,width):
    pygame.draw.circle(screen,color,(x,y),width)

while not done:

    for i in range(5):
        pygame.display.init
        circle((255,0,0),500-i,500-i,50)
   





    pygame.display.flip()
    