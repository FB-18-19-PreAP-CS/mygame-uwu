import pygame
pygame.init()
pressed = pygame.key.get_pressed()

if pressed[pygame.K_a]:
    print('a')

