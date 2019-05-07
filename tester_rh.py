import pygame
import time 
<<<<<<< HEAD
# import pygame_functions
WIDTH = 1000
HEIGHT = 1000
pygame.init()
screenRefresh = True
background_image = pygame.image.load("plain_bg.jpg")
back_pos = [0,0]
clock = pygame.time.Clock()
=======
import pygame_functions
WIDTH = 1000
HEIGHT = 1000
C_SPEED = 2
pygame.init()

pygame.mixer.init()
first_song = pygame.mixer.music.load('./sounds/tt_littlestar.ogg')
pygame.mixer.music.play()

screenRefresh = True
background_image = pygame.image.load("plain_bg.jpg")
back_pos = [0,0]

>>>>>>> master
screen = pygame.display.set_mode((WIDTH,HEIGHT))
done = False

class Button(pygame.sprite.Sprite):
    def __init__(self,loc):
<<<<<<< HEAD

=======
>>>>>>> master
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("blue_button-1-1.png.png")
        self.loc = loc
        self.is_visible = True
    def blitme(self):
        if self.is_visible == True:
            screen.blit(self.image,self.loc)
    def move_y(self,loc):
<<<<<<< HEAD
        self.loc[1] = loc[1]+5
        return self.loc
    
class Target():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("target-1.png")
    def blitme(self):
        screen.blit(self.image,(375,700))
#CREATES INITIAL COLUMNS OF FALLING BUTTONS
targ = Target()
=======
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
>>>>>>> master
buttons = []
buttons.append(Button([400,50]))
buttons.append(Button([450,50]))
buttons.append(Button([500,50]))
buttons.append(Button([550,50]))

<<<<<<< HEAD
time_a = [2.45,0,0,0,0,0,0]

pygame.mixer.init()
first_song = pygame.mixer.music.load('tt_lit.ogg')
pygame.mixer.music.play()
start_time = time.time()
while not done:
#TIME it takes for button to reach target: 2.121
    end_time = time.time()
    elapsed = end_time - start_time
=======

while not done:
>>>>>>> master
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                buttons[0].is_visible = False
<<<<<<< HEAD
                if elapsed-.3 < time_a[0] and elapsed +.3 > time_a[0]:
                    print('yes')
                    time_a = time_a[1:]
            if event.key == pygame.K_s:
                buttons[1].is_visible = False
            if event.key == pygame.K_d:
                buttons[2].is_visible = False
            if event.key == pygame.K_f:
                buttons[3].is_visible = False

    if elapsed-.3 < time_a[0] and elapsed +.3 > time_a[0]:
        print('hit it',elapsed)
    screen.blit(background_image,back_pos )


    targ.blitme()
    
    for butt in buttons:

        butt.blitme()
        butt.move_y(butt.loc)
        if butt.loc[1]==700:
            end_time = time.time()
            print(end_time - start_time)
=======
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
>>>>>>> master

        else:
            pass


<<<<<<< HEAD



    pygame.display.flip()
    # print(clock.tick(30))
    # print(pygame.time.get_ticks())
    
        
        



=======
# column_a = ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','x','-','-','-','-','-','-','-','x','-','-','-','-','-','-','-','-','x','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','x']
# column_s = ['-','x','x','-','-','-','-','-','-','-','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','-','x','x','-','-','x','x','-','-','-','-','-','-','-','-','-','-','x','x','-']
# column_d = ['-','-','-','x','x','-','-','x','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','x','-','-','-','x','x','-','-','-']
# column_f = ['-','-','-','-','-','x','x','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','-','-','-','-','-','x','x','-','-','x','x','-','-','-','-','-']

# for space_a,space_s,space_d,space_f in zip(column_a,column_s,column_d,column_f):

    
    
#     pygame.display.flip()
>>>>>>> master


   
    

        
