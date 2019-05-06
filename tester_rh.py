import pygame
import time 
# import pygame_functions
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
buttons = []
buttons.append(Button([400,50]))
buttons.append(Button([450,50]))
buttons.append(Button([500,50]))
buttons.append(Button([550,50]))

time_a = [2.45,0,0,0,0,0,0]

pygame.mixer.init()
first_song = pygame.mixer.music.load('tt_lit.ogg')
pygame.mixer.music.play()
start_time = time.time()
while not done:
#TIME it takes for button to reach target: 2.121
    end_time = time.time()
    elapsed = end_time - start_time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                buttons[0].is_visible = False
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

        else:
            pass





    pygame.display.flip()
    # print(clock.tick(30))
    # print(pygame.time.get_ticks())
    
        
        





   
    

        
