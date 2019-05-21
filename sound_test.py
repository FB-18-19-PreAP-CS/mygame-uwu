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
c4 = pygame.mixer.Sound("./sounds/c4.ogg")
emp = pygame.mixer.Sound("./sounds/empty.ogg")

b3 = pygame.mixer.Sound("./sounds/b3.ogg")
g3 = pygame.mixer.Sound("./sounds/g3.ogg")
a3 = pygame.mixer.Sound("./sounds/a3.ogg")
f3 = pygame.mixer.Sound("./sounds/f3.ogg")

a2 = pygame.mixer.Sound("./sounds/a2.ogg")
g2 = pygame.mixer.Sound("./sounds/g2.ogg")
e2 = pygame.mixer.Sound("./sounds/e2.ogg")
f2 = pygame.mixer.Sound("./sounds/f2.ogg")

solin = [b3,c4,c4,b3]
solin2 = [b3,g3,g3,a3]
solin3 = [b3,c4,c4,b3]
solin4 = [b3,g3,g3,f3]

bass1 = [a2,a2,g2,g2]
bass2 = [g2,e2,e2,f2]
#plays notes
for note,b in zip(solin,bass1):
    note.play()
    b.play()
    time.sleep(.5)
time.sleep(1)
for note,b in zip(solin2,bass2):
    note.play()
    b.play()
    time.sleep(.5)
time.sleep(1)
for note,b in zip(solin3,bass1):
    note.play()
    b.play()
    time.sleep(0.5)
time.sleep(1)
for note,b in zip(solin4,bass2):
    note.play()
    b.play()
    time.sleep(0.5)


running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False