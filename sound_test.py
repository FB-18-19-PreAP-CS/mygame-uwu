import pygame, time

# pygame.mixer.init()

# pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
screen = pygame.display.set_mode((640, 480))


a = pygame.mixer.Sound("./sounds/a.ogg")
g = pygame.mixer.Sound("./sounds/g.ogg")
f = pygame.mixer.Sound("./sounds/f.ogg")
e = pygame.mixer.Sound("./sounds/e.ogg")
d = pygame.mixer.Sound("./sounds/d.ogg")
c = pygame.mixer.Sound("./sounds/c.ogg")

keys_1 = [c,c,g,g,a,a,g]
keys_2 = [f,f,e,e,d,d,c]
keys_3 = [g,g,f,f,e,e,d]

def a():
    pygame.mixer.music.load('./sounds/a.ogg')
    pygame.mixer.music.play()

def g():
    pygame.mixer.music.load('./sounds/g.ogg')
    pygame.mixer.music.play()

def f():
    pygame.mixer.music.load('./sounds/f.ogg')
    pygame.mixer.music.play()

def e():
    pygame.mixer.music.load('./sounds/e.ogg')
    pygame.mixer.music.play()

def d():
    pygame.mixer.music.load('./sounds/d.ogg')
    pygame.mixer.music.play()

def c():
    pygame.mixer.music.load('./sounds/c.ogg')
    pygame.mixer.music.play()

c()
time.sleep(.5)
c()
time.sleep(.5)
g()
time.sleep(.65)
g()


running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

# pygame.mixer.init()  # Initialize the mixer module.
# sound1 = pygame.mixer.Sound('./sounds/c.ogg')  # Load a sound.

# while True:
#     inpt = input('Press enter to play the sound: ')
#     sound1.play()  # Play the sound.
#     print('Playing sound')