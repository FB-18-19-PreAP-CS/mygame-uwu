import pygame
import time 
# import pygame_functions
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
time_a = ['8.00','11.2','14.40','20.8']
time_s = ['2.3','2.6','7.20','7.60','10.4','10.8''13.60','14.0','15.2','15.6','20','20.4']
time_d = ['2.90','3.3','4.43''6.40','6.80','9.60','10.0''12.80','13.20','16','16.4','17.6''19.2','19.6']
time_f = ['3.66','4.04','5.10','5.5','8.80','9.2','12.0','12.40''16.8','17.2','18.4','18.8']
 
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

font_name = pygame.font.match_font('arial')

def draw_text(surf,text,size,x,y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True, (255,0,0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface,text_rect)






pygame.mixer.init()
first_song = pygame.mixer.music.load("tt_lit.ogg")
pygame.mixer.music.play()
pygame.event.wait()
# start = time.time()
score_range = 100
score = 0
while not done:
    # end = time.time()
    # elapsed = end-start
    # presstime_a = abs(elapsed-float(time_a[0])-.18)
    # presstime_s = abs(elapsed-float(time_s[0])-.18)
    # presstime_d = abs(elapsed-float(time_d[0])-.18)
    # presstime_f = abs(elapsed-float(time_f[0])-.18)
    window_a = abs(bm[0][0].loc[1]- 700)
    window_s = abs(bm[1][0].loc[1]- 700)
    window_d = abs(bm[2][0].loc[1]- 700)
    window_f = abs(bm[3][0].loc[1]- 700)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:

                while not type(bm[0][0]) == Button:
                    bm[0] = bm[0][1:]
                if window_a < score_range:
                    score += 50
                    print('yes')
                bm[0][0].is_visible = False
                bm[0] = bm[0][1:]

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:

                while not type(bm[1][0]) == Button:
                    bm[1]=bm[1][1:]
                if window_d < score_range:
                    score += 50
                    print('yes')
                bm[1][0].is_visible = False
                bm[1]=bm[1][1:]

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:

                while not type(bm[2][0]) == Button:
                    bm[2] = bm[2][1:]
                if window_f < score_range:
                    score += 50
                    print('yes')
                bm[2][0].is_visible = False
                bm[2] = bm[2][1:]


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:

                while not type(bm[3][0]) == Button:
                    bm[3] = bm[3][1:]
                if window_s < score_range:
                    score += 50
                    print('yes')
                bm[3][0].is_visible = False
                bm[3] = bm[3][1:]
            
    screen.blit(background_image,back_pos )


    t=Target()
    screen.blit(t.image,(375,700))

    show_buttons(bm)
 
    draw_text(screen, str(score), 18, WIDTH/2, 20)
    
    pygame.display.flip()