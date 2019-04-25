import pygame
import time 
WIDTH = 1000
HEIGHT = 1000
C_SPEED = 2
pygame.init()

background_image = pygame.image.load("plain_bg.jpg")
back_pos = [0,0]

screen = pygame.display.set_mode((WIDTH,HEIGHT))
done = False

# LOCATION OF COLUMN ONE
x1 = 400
y1 = 50

#LOCATION OF COLUMN TWO
x2 = 450
y2 = 50

#LOCATION OF COLUMN THREE
x3 = 500
y3 = 50

#LOCATION OF COLUMN FOUR 
x4 = 550
y4 = 50

def circle(color,size):
    pygame.draw.circle(screen,color,size,10)
while not done:
    screen.blit(background_image,back_pos )
    
    circle((0,0,255),(x1,y1))
    circle((0,0,255),(x2,y2))
    circle((0,0,255),(x3,y3))
    circle((0,0,255),(x4,y4))
    y1 = y1 + C_SPEED
    if y1 > HEIGHT:
        y1 = -1

    
    
    
    pygame.display.flip()
        





   
    