import pygame
import time 
import random
# import pygame_functions
WIDTH = 1000
HEIGHT = 1000
pygame.mixer.init()
a = pygame.mixer.Sound("./sounds/a.ogg")
g = pygame.mixer.Sound("./sounds/g.ogg")
f = pygame.mixer.Sound("./sounds/f.ogg")
e = pygame.mixer.Sound("./sounds/e.ogg")
d = pygame.mixer.Sound("./sounds/d.ogg")
c = pygame.mixer.Sound("./sounds/c.ogg")
wrong = pygame.mixer.Sound("./sounds/wrong.ogg")




pygame.init()
screenRefresh = True

back_pos = [0,0]
countscreen = pygame.display.set_mode((WIDTH,HEIGHT))
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
        self.image = pygame.image.load("target-1.png")
    




#used to create beatmap
column_a = ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','x','-','-','-','-','-','-','-','x','-','-','-','-','-','-','-','-','x','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','x']
column_s = ['-','x','x','-','-','-','-','-','-','-','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','-','x','x','-','-','x','x','-','-','-','-','-','-','-','-','-','-','x','x','-']
column_d = ['-','-','-','x','x','-','-','x','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','x','-','-','-','x','x','-','-','-']
column_f = ['-','-','-','-','-','x','x','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','x','x','-','-','-','-','-','-','-','-','-','-','-','x','x','-','-','x','x','-','-','-','-','-']
#used to play sounds
note_a = [c,d,d,c]
note_s = [c,c,d,d,e,e,e,e,c,c,d,d]
note_d = [g,g,g,e,e,f,f,f,f,g,g,g,e,e]
note_f = [a,a,f,f,g,g,g,g,a,a,f,f]

def beatmap():
    buttons_a = []
    buttons_s = []
    buttons_d = []
    buttons_f = []
    row = 0
    spacing = 80
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



def draw_text(surf,text,size,x,y):
    font = pygame.font.Font('Fipps-Regular.otf',size)
    text_surface = font.render(text,True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface,text_rect)


done_count = False
pygame.event.wait()
start = time.time()
score_med = 30
score_easy = 70
score_hard = 10
score = 0
rclist = ["space_bg_b.png","space_bg_g.png","space_bg_p.png","space_bg_r.png"]
background_image = pygame.image.load(random.choice(rclist))

def count():

    for i in range(3,-2,-1):
        screen.blit(background_image,back_pos )
        if i > 0:
            draw_text(screen, str(i), 40, WIDTH/2, HEIGHT/2)
            time.sleep(.5)
        if i == 0:
            draw_text(screen, 'GO', 40, WIDTH/2, HEIGHT/2)
            time.sleep(.5)
        if i == -1:
            draw_text(screen, '', 40, WIDTH/2, HEIGHT/2)
        time.sleep(1)
        pygame.display.flip()

countdec = True
while not done:
    if countdec:
        count()
        countdec = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if not(len(bm[0]) == 0):
                    try:
                        #deal only with buttons
                        while not type(bm[0][0]) == Button:
                            bm[0] = bm[0][1:]
                    except IndexError:
                        break

                    window_a = abs(bm[0][0].loc[1]- 720)
                    if window_a < score_hard:
                        note_a[0].play()
                        score += 50
                    elif window_a < score_med:
                        note_a[0].play()
                        score += 10
                        
                    elif window_a < score_easy:
                        note_a[0].play()
                        score += 1
                    else:
                        wrong.play()
                    note_a = note_a[1:]
                    bm[0][0].is_visible = False
                 
                    bm[0]=bm[0][1:]

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if not(len(bm[1]) == 0):
                    try:
                        while not type(bm[1][0]) == Button:
                            bm[1] = bm[1][1:]
                    except IndexError:
                        break
                    window_s = abs(bm[1][0].loc[1]- 720)
                    if window_s < score_hard:
                        note_s[0].play()
                        score += 50
                    elif window_s < score_med:
                        note_s[0].play()
                        score += 10
                        
                    elif window_s < score_easy:
                        note_s[0].play()
                        score += 1
                    else:
                        wrong.play()
                    note_s = note_s[1:]
                    
                    bm[1][0].is_visible = False
                 
                    bm[1]=bm[1][1:]


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if not(len(bm[2]) == 0):
                    try:
                        while not type(bm[2][0]) == Button:
                            bm[2] = bm[2][1:]
                    except IndexError:
                        break
                    window_d = abs(bm[2][0].loc[1]- 720)
                    if window_d < score_hard:
                        note_d[0].play()
                        score += 50
                    elif window_d < score_med:
                        note_d[0].play()
                        score += 10
                        
                    elif window_d < score_easy:
                        note_d[0].play()
                        score += 1
                    else:
                        wrong.play()
                    note_d = note_d[1:]
                    bm[2][0].is_visible = False
          
                    bm[2]=bm[2][1:]
              


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if not(len(bm[3]) == 0):
                    try:
                        while not type(bm[3][0]) == Button:
                            bm[3] = bm[3][1:]
                    except IndexError:
                        break
                    window_f = abs(bm[3][0].loc[1]- 720)
                    if window_f < score_hard:
                        note_f[0].play()
                        score += 50
                    elif window_f < score_med:
                        note_f[0].play()
                        score += 10
                        
                    elif window_f < score_easy:
                        note_f[0].play()
                        score += 1
                    else:
                        wrong.play()
                    note_f = note_f[1:]
                    bm[3][0].is_visible = False
          
                    bm[3]=bm[3][1:]

    pygame.display.set_caption('Rhythm Galaxy')      
    screen.blit(background_image,back_pos )


    t=Target()
    screen.blit(t.image,(375,700))

    show_buttons(bm)
 
    draw_text(screen, "SCORE :", 30, 690, 10)
    draw_text(screen, str(score), 30, 850, 10)


    pygame.display.flip()

