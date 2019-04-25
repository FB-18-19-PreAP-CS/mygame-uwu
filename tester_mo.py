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

#make sprite class, import image
while not done:
    screen.blit(background_image,back_pos )
    
    pygame.draw.circle(screen,(0,0,255),(x1,y1),10)
    pygame.draw.circle(screen,(0,0,255),(x2,y2),10)

    pygame.draw.circle(screen,(0,0,255),(x3,y3),10)
    pygame.draw.circle(screen,(0,0,255),(x4,y4),10)
    y1 = y1 + C_SPEED
    if y1 > HEIGHT:
        y1 = -1

    
    
    
    pygame.display.flip()
        





   
    