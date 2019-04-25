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

class Button(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("blue_button-1-1.png.png")

class Target():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("target-1.png.png")


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

#CREATES INITIAL COLUMNS OF FALLING BUTTONS

    

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
   
    screen.blit(background_image,back_pos )
    #CREATES TARGET
    t=Target()
    screen.blit(t.image,(375,400))

    #CREATES 4 COLUMNS
    button1 = Button()
    button2 = Button()

    button3 = Button()
    button4 = Button()
    screen.blit(button1.image,(x1,y1))
    y1 = y1 + C_SPEED
    if y1 > HEIGHT:
        y1 = -1
    screen.blit(button1.image,(x2,y2))
    y2 = y2 + C_SPEED
    if y2 > HEIGHT:
        y2 = -1
    screen.blit(button1.image,(x3,y3))
    y3 = y3 + C_SPEED
    if y3 > HEIGHT:
        y3 = -1
    screen.blit(button1.image,(x4,y4))
    y4 = y4+ C_SPEED
    if y4 > HEIGHT:
        y4 = -1

    

    
    
    
    pygame.display.flip()
        





   
    