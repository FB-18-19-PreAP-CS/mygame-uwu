import pygame.midi, time

a = 440
g = 392
f = 349.23
e = 329.63	
d = 293.66
c = 261.63

wait_time = 0.5

pygame.midi.init()

player = pygame.midi.get_default_output_id()

player.set_instrument(1)

player.note_on(c)
time.sleep(wait_time)
player.note_off(c)

player.note_on(c)
time.sleep(wait_time)
player.note_off(c)