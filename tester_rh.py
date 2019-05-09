import pygame
import time 
import pygame_functions
WIDTH = 1000
HEIGHT = 1000
<<<<<<< HEAD


pygame.init()
=======
C_SPEED = 2
pygame.init()

pygame.mixer.init()
first_song = pygame.mixer.music.load('./sounds/tt_littlestar.ogg')
pygame.mixer.music.play()

>>>>>>> master
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
<<<<<<< HEAD
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
    
    for space_a,space_s,space_d,space_f in zip(column_a,column_s,column_d,column_f):

        if space_a == "-":
            butt_a = Blank([400,10 - row * 40])
        
            buttons_a.append(butt_a)
            
        if space_a == "x":
            butt_a = Button([400,10 - row * 40])
            
            buttons_a.append(butt_a)
            
        if space_s == "-":
            butt_s = Blank([450,10- row * 40])
            
            buttons_s.append(butt_s)


        if space_s == "x":
            butt_s = Button([450,10- row * 40])
            
            buttons_s.append(butt_s)


        if space_d == "-":
            butt_d = Blank([500,10- row * 40])
            
            buttons_d.append(butt_d)

        if space_d == "x":
            butt_d = Button([500,10- row * 40])
            
            buttons_d.append(butt_d)

        if space_f == "-":
            butt_f = Blank([550,10- row * 40])
            
            buttons_f.append(butt_f)

        if space_f == "x":
            butt_f = Button([550,10- row * 40])
            
            buttons_f.append(butt_f)
        
        row += 1
    
    return [buttons_a,buttons_s,buttons_d,buttons_f]

def show_buttons(bm):
    
    
    for ele in bm[0]:
        print(ele.loc)
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

bm = beatmap()


pygame.mixer.init()
first_song = pygame.mixer.music.load("./sounds/tt_littlestar.ogg")
pygame.mixer.music.play()
pygame.event.wait()

=======
    def move_y(self,loc):
        self.loc[1] = loc[1]+1
        return self.loc
    





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
buttons.append(Button([400,50]))
buttons.append(Button([450,50]))
buttons.append(Button([500,50]))
buttons.append(Button([550,50]))


>>>>>>> master
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
<<<<<<< HEAD

        
        
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

    show_buttons(bm)
 
    pygame.display.flip()
        
        



=======
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
            butt.move_y(butt.loc)

        else:
            pass


# column_a = ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','x','-','-','-','-','-','-','-','x','-','-','-','-','-','-','-','-','x','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','x']
# column_s = ['-','x','x','-','-','-','-','-','-','-','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','-','x','x','-','-','x','x','-','-','-','-','-','-','-','-','-','-','x','x','-']
# column_d = ['-','-','-','x','x','-','-','x','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','x','-','-','-','x','x','-','-','-']
# column_f = ['-','-','-','-','-','x','x','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','-','-','-','-','-','x','x','-','-','x','x','-','-','-','-','-']

# for space_a,space_s,space_d,space_f in zip(column_a,column_s,column_d,column_f):

    
    
#     pygame.display.flip()
>>>>>>> master


   
    

        
