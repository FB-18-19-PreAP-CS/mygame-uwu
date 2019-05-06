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
        self.loc[1] = loc[1]+5
        return self.loc
    

#CREATES INITIAL COLUMNS OF FALLING BUTTONS

buttons = []
buttons.append(Button([400,50]))
buttons.append(Button([450,50]))
buttons.append(Button([500,50]))
buttons.append(Button([550,50]))

time_a = [1.5,2,]

pygame.mixer.init()
first_song = pygame.mixer.music.load('tt_littlestar(1).ogg')
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
                if elapsed == time_a[0]:
                    print('yes')
                    time_a = time_a[1:]
            if event.key == pygame.K_s:
                buttons[1].is_visible = False
            if event.key == pygame.K_d:
                buttons[2].is_visible = False
            if event.key == pygame.K_f:
                buttons[3].is_visible = False

            
    screen.blit(background_image,back_pos )

    # for butt_a,butt_s,butt_d,butt_f in zip(buttons_a,buttons_s,buttons_d,buttons_f):
    #     if butt.is_visible == True:
    #         butt.blitme()
    #         butt.move_y(butt.loc)
    #     if butt_a[0].loc[1]==700:
    #         end_time = time.time()
    #         print(end_time - start_time)

    #     else:
    #         pass
    for butt in buttons:
        if butt.is_visible == True:
            butt.blitme()
            butt.move_y(butt.loc)
        if butt[0].loc[1]==700:
            end_time = time.time()
            print(end_time - start_time)

        else:
            pass





    pygame.display.flip()
    # print(clock.tick(30))
    # print(pygame.time.get_ticks())
    
        
        





   
    

        
