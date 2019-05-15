import pygame.midi, time

a = 81
g = 79
f = 77
e = 76
d = 74
c = 72

# instrument = grand_piano

wait_time = 0.5

pygame.midi.init()
player = pygame.midi.Output(1)
player.get_device_info()
player.set_instrument(1)

keys_1 = [c,c,g,g,a,a,g]
keys_2 = [f,f,e,e,d,d,c]
keys_3 = [g,g,f,f,e,e,d]

for note in keys_1:
    player.note_on(int(note),127)
    time.sleep(wait_time)
    player.note_off(int(note),127)
time.sleep(wait_time)
for note in keys_2:
    player.note_on(int(note),127)
    time.sleep(wait_time)
    player.note_off(int(note),127)
time.sleep(wait_time)
for note in keys_3:
    player.note_on(int(note),127)
    time.sleep(wait_time)
    player.note_off(int(note),127)
time.sleep(wait_time)
for note in keys_3:
    player.note_on(int(note),127)
    time.sleep(wait_time)
    player.note_off(int(note),127)
time.sleep(wait_time)
for note in keys_1:
    player.note_on(int(note),127)
    time.sleep(wait_time)
    player.note_off(int(note),127)
time.sleep(wait_time)
for note in keys_2:
    player.note_on(int(note),127)
    time.sleep(wait_time)
    player.note_off(int(note),127)

# player.note_on(int(c),127)
# time.sleep(wait_time)
# player.note_off(int(c),127)

# player.note_on(int(c),127)
# time.sleep(wait_time)
# player.note_off(int(c),127)

del player #IMPORTANT - The other problem is that you don't delete the midi output object at the end before quitting
pygame.midi.quit()

# import pygame.midi
# import time

# pygame.midi.init()
# player = pygame.midi.Output(0)
# player.set_instrument(0)
# player.note_on(64, 127)
# time.sleep(1)
# player.note_off(64, 127)
# player.note_on(64, 127)
# time.sleep(1)
# player.note_off(64, 127)
# player.note_on(64, 127)
# time.sleep(1)
# player.note_off(64, 127)
# player.note_on(64, 127)
# time.sleep(1)
# player.note_off(64, 127)
# del player

# pygame.midi.quit()
