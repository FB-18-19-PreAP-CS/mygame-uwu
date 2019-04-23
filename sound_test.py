import pygame, time

pygame.mixer.init()
pygame.init()
song = pygame.mixer.Sound("8bit_twinkle_star.wav")

song.play()
time.sleep(30) #sleep allows the song to play