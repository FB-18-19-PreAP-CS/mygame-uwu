import pygame
import time 
import pygame_functions
WIDTH = 1000
HEIGHT = 1000


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
    def move_y(self,loc):
        self.loc[1] = loc[1]+5
        return self.loc

class Target():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("target-1.png.png")
    


#CREATES INITIAL COLUMNS OF FALLING BUTTONS
buttons = []
buttons.append(Button([400,50]))
buttons.append(Button([450,50]))
buttons.append(Button([500,50]))
buttons.append(Button([550,50]))


pygame.mixer.init()
first_song = pygame.mixer.music.load("./sounds/tt_littlestar.ogg")
pygame.mixer.music.play()
pygame.event.wait()

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

    t=Target()
    screen.blit(t.image,(375,700))


    for butt in buttons:
        if butt.is_visible == True:
            butt.blitme()
            butt.move_y(butt.loc)
            
        else:
            pass

    column_a = ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','x','-','-','-','-','-','-','-','x','-','-','-','-','-','-','-','-','x','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','x']
    column_s = ['-','x','x','-','-','-','-','-','-','-','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','-','x','x','-','-','x','x','-','-','-','-','-','-','-','-','-','-','x','x','-']
    column_d = ['-','-','-','x','x','-','-','x','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','x','-','-','-','x','x','-','-','-']
    column_f = ['-','-','-','-','-','x','x','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','-','-','-','-','-','x','x','-','-','x','x','-','-','-','-','-']



    for space_a,space_s,space_d,space_f in zip(column_a,column_s,column_d,column_f):
        if space_a == "x":
            pass
        if space_s == "x":
            pass
        if space_d == "x":
            pass
        if space_f == "x":
            pass



    

    
    
    
    pygame.display.flip()
        
        





   
    

        
