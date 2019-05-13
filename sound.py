import pygame.midi, time

a = 440
g = 392
f = 349.23
e = 329.63	
d = 293.66
c = 261.63

# instrument = grand_piano

wait_time = 0.5

pygame.midi.init()

# pygame.midi.Output()
print(pygame.midi.get_device_info(1))
print(pygame.midi.get_default_output_id())


pygame.midi.Output.set_instrument(22)

pygame.midi.Output.note_on(c,127)
time.sleep(wait_time)
pygame.midi.Output.note_off(c,127)

pygame.midi.Output.note_on(c,127)
time.sleep(wait_time)
pygame.midi.Output.note_off(c,127)

pygame.midi.quit()

