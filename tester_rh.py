
  
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
    def move_y(self):
        self.loc[1] = self.loc[1]+5
        

class Blank(pygame.sprite.Sprite):
    def __init__(self,loc):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("blank.png")
        self.loc = loc
        self.is_visible = True
    def blitme(self):
        if self.is_visible == True:
            screen.blit(self.image,self.loc)
    def move_y(self):
        self.loc[1] = self.loc[1]+5
       
class Target():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("target-1.png.png")
    


#CREATES INITIAL COLUMNS OF FALLING BUTTONS


column_a = ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','x','-','-','-','-','-','-','-','x','-','-','-','-','-','-','-','-','x','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','x']
column_s = ['-','x','x','-','-','-','-','-','-','-','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','-','x','x','-','-','x','x','-','-','-','-','-','-','-','-','-','-','x','x','-']
column_d = ['-','-','-','x','x','-','-','x','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','x','-','-','-','x','x','-','-','-']
column_f = ['-','-','-','-','-','x','x','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','-','-','-','-','-','x','x','-','-','x','x','-','-','-','-','-']
# column_a.reverse()
# column_s.reverse()
# column_d.reverse()
# column_f.reverse()
 
def beatmap():
    buttons_a = []
    buttons_s = []
    buttons_d = []
    buttons_f = []
    row = 0
    spacing = 130
    for space_a,space_s,space_d,space_f in zip(column_a,column_s,column_d,column_f):

        if space_a == "-":
            blank_a = Blank([400,10 - row * spacing])
        
            buttons_a.append(blank_a)
            
        if space_a == "x":
            butt_a = Button([400,10 - row * spacing])
            
            buttons_a.append(butt_a)
            
        if space_s == "-":
            blank_s = Blank([450,10- row * spacing])
            
            buttons_s.append(blank_s)


        if space_s == "x":
            butt_s = Button([450,10- row * spacing])
            
            buttons_s.append(butt_s)


        if space_d == "-":
            blank_d = Blank([500,10- row * spacing])
            
            buttons_d.append(blank_d)

        if space_d == "x":
            butt_d = Button([500,10- row * spacing])
            
            buttons_d.append(butt_d)

        if space_f == "-":
            blank_f = Blank([550,10- row * spacing])
            
            buttons_f.append(blank_f)

        if space_f == "x":
            butt_f = Button([550,10- row * spacing])
            
            buttons_f.append(butt_f)
        
        row += 1
    
    return [buttons_a,buttons_s,buttons_d,buttons_f]
bm = beatmap()
def show_buttons(bm):
    
   
    for ele in bm[0]:
        if type(ele) == Blank:
            print('blank')
        elif type(ele) == Button:
            print('button')
        
        ele.blitme()
        ele.move_y()

    for ele in bm[1]:
        
        ele.blitme()
        ele.move_y()
    for ele in bm[2]:
        
        ele.blitme()
        ele.move_y()
    for ele in bm[3]:
        
        ele.blitme()
        ele.move_y()




pygame.mixer.init()
first_song = pygame.mixer.music.load("./sounds/tt_lit.ogg")
pygame.mixer.music.play()
pygame.event.wait()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if type(bm[0][0]) != Blank:
                    bm[0][0].is_visible = False
        bm[0] = bm[0][1:]

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if type(bm[1][0]) == Button:
                    bm[1][0].is_visible = False
        bm[1] = bm[1][1:]

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if type(bm[2][0]) == Button:
                    bm[2][0].is_visible = False
        bm[2] = bm[2][1:]

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if type(bm[3][0]) == Button:
                    bm[3][0].is_visible = False
        bm[3] = bm[3][1:]
            
    screen.blit(background_image,back_pos )


    t=Target()
    screen.blit(t.image,(375,700))

    show_buttons(bm)
 
    pygame.display.flip()