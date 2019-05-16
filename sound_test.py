import pygame, time

# pygame.mixer.init()

# pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
screen = pygame.display.set_mode((640, 480))

#creates and loads sounds
a = pygame.mixer.Sound("./sounds/a.ogg")
g = pygame.mixer.Sound("./sounds/g.ogg")
f = pygame.mixer.Sound("./sounds/f.ogg")
e = pygame.mixer.Sound("./sounds/e.ogg")
d = pygame.mixer.Sound("./sounds/d.ogg")
c = pygame.mixer.Sound("./sounds/c.ogg")
emp = pygame.mixer.Sound("./sounds/empty.ogg")

#creates beatmap
keys_1 = [c,c,g,g,a,a,g]
keys_2 = [f,f,e,e,d,d,c]
keys_3 = [g,g,f,f,e,e,d]

#plays notes
for note in keys_1:
    note.play()
    time.sleep(.5)
time.sleep(0.5)
for note in keys_2:
    note.play()
    time.sleep(.5)
time.sleep(0.5)
for note in keys_3:
    note.play()
    time.sleep(0.5)
time.sleep(0.5)
for note in keys_3:
    note.play()
    time.sleep(0.5)
time.sleep(0.5)
for note in keys_1:
    note.play()
    time.sleep(.5)
time.sleep(0.5)
for note in keys_2:
    note.play()
    time.sleep(.5)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False