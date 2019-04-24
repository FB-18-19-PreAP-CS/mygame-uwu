import pygame

WIDTH = 1000
HEIGHT = 1000
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
done = False
while not done:
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_a]:
        print('a')
    pygame.display.flip()

pygame.event.

        
