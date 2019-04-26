import pygame
import time 
import pygame_functions
WIDTH = 1000
HEIGHT = 1000
C_SPEED = 2
pygame.init()
screenRefresh = True
background_image = pygame.image.load("plain_bg.jpg")
back_pos = [0,0]

screen = pygame.display.set_mode((WIDTH,HEIGHT))
done = False

class Button(pygame.sprite.Sprite):
    def __init__(self,loc):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("blue_button-1-1.png.png")
        self.loc = loc
        self.is_visible = True
    def blitme(self):
        if self.is_visible == True:
            screen.blit(self.image,self.loc)





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
buttons = []
buttons.append(Button((400,50)))
buttons.append(Button((450,50)))
buttons.append(Button((500,50)))
buttons.append(Button((550,50)))

# button1 = Button((400,50))
# button2 = Button((450,50))
# button3 = Button((500,50)
# button4 = Button((550,50))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                buttons[0].is_visible = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                buttons[1].is_visible = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                buttons[2].is_visible = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                buttons[3].is_visible = False
            
    screen.blit(background_image,back_pos )

    for butt in buttons:
        if butt.is_visible == True:
            butt.blitme()
        else:
            pass
    # screen.blit(button1.image,(x1,y1))
    # y1 = y1 + C_SPEED
    # if y1 > HEIGHT:
    #     y1 = -1
    # screen.blit(button2.image,(x2,y2))
    # y2 = y2 + C_SPEED
    # if y2 > HEIGHT:
    #     y2 = -1
    # screen.blit(button3.image,(x3,y3))
    # y3 = y3 + C_SPEED
    # if y3 > HEIGHT:
    #     y3 = -1
    # screen.blit(button4.image,(x4,y4))
    # y4 = y4+ C_SPEED
    # if y4 > HEIGHT:
    #     y4 = -1
   
    

    
    
    
    pygame.display.flip()
        
        





   
    

        
