import pygame
import time 
import pygame_functions
WIDTH = 1000
HEIGHT = 1000
pygame.init()
screenRefresh = True
background_image = pygame.image.load("plain_bg.jpg")
back_pos = [0,0]
clock = pygame.time.Clock()
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
    def move_y(self,loc):
        self.loc[1] = loc[1]+10
        return self.loc
    

#CREATES INITIAL COLUMNS OF FALLING BUTTONS
buttons = []
buttons.append(Button([400,50]))
buttons.append(Button([450,50]))
buttons.append(Button([500,50]))
buttons.append(Button([550,50]))

column_a = ['-','x','x','-']

pygame.mixer.init()
first_song = pygame.mixer.music.load('tt_littlestar.ogg')
pygame.mixer.music.play()
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                buttons[0].is_visible = False
            if event.key == pygame.K_s:
                buttons[1].is_visible = False
            if event.key == pygame.K_d:
                buttons[2].is_visible = False
            if event.key == pygame.K_f:
                buttons[3].is_visible = False
            
    screen.blit(background_image,back_pos )

    for butt in buttons:
        if butt.is_visible == True:
            butt.blitme()
            butt.move_y(butt.loc)

        else:
            pass
    start_time = pygame.time.get_ticks()
    for space_a in zip(column_a):
        if buttons[0].is_visible == False:
            if space_a == 'x':
                pygame.draw.circle(screen,'blue',(500,500),10,10)


    pygame.display.flip()
    # print(clock.tick(30))
    print(pygame.time.get_ticks())
    
        
        





   
    

        
