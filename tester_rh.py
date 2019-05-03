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
buttons_a = []
buttons_s = []
buttons_d = []
buttons_f = []

column_a = ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','x','-','-','-','-','-','-','-','x','-','-','-','-','-','-','-','-','x','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','x']
    column_s = ['-','x','x','-','-','-','-','-','-','-','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','-','x','x','-','-','x','x','-','-','-','-','-','-','-','-','-','-','x','x','-']
    column_d = ['-','-','-','x','x','-','-','x','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','x','-','-','-','x','x','-','-','-']
    column_f = ['-','-','-','-','-','x','x','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','-','-','-','-','-','x','x','-','-','x','x','-','-','-','-','-']

#BRO THIS AINT RIGHT FIX IT 
def beatmap():
    for space_a,space_s,space_d,space_f in zip(column_a,column_s,column_d,column_f):

        if space_a == "-":
            butt_a = Button([400,10])
            buttons_a.append(butt_a)
            butt_a.is_visible ==False
        if space_a == "x":
            butt_a = Button([400,10])
            buttons_a.append(butt_a)
            butt_a.is_visible ==True

        if space_s == "x":
            pass
        if space_d == "x":
            pass
        if space_f == "x":
            pass

# buttons_a.append(Button([400,10]))
# buttons_a.append(Button([400,50]))

# buttons_s.append(Button([450,10]))
# buttons_s.append(Button([450,50]))

# buttons_d.append(Button([500,10]))
# buttons_d.append(Button([500,50]))

# buttons_f.append(Button([550,10]))
# buttons_f.append(Button([550,50]))


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
                for i in range(len(buttons_a)):
                    buttons_a[i].is_visible = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                for i in range(len(buttons_s)):
                    buttons_s[i].is_visible = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                for i in range(len(buttons_d)):
                    buttons_d[i].is_visible = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                for i in range(len(buttons_f)):
                    buttons_f[i].is_visible = False

            
    screen.blit(background_image,back_pos )

    t=Target()
    screen.blit(t.image,(375,700))


    
    #I DONT KNOW WHERE THIS GOES IT'S JUST HERE 

    for butt_a,butt_s,butt_d,butt_f in zip(buttons_a,buttons_s,buttons_d,buttons_f):
        
        butt_a.blitme()
        butt_a.move_y(butt_a.loc)

        if butt_s.is_visible == True:
            butt_s.blitme()
            butt_s.move_y(butt_s.loc)

        if butt_d.is_visible == True:
            butt_d.blitme()
            butt_d.move_y(butt_d.loc)

        if butt_f.is_visible == True:
            butt_f.blitme()
            butt_f.move_y(butt_f.loc)
            
        else:
            pass


    

    
    
    
    pygame.display.flip()
        
        





   
    

        
