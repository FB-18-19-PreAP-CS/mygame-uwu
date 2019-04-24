import pygame, time

pygame.mixer.init()
pygame.init()

screen = pygame.display.set_mode((1000,1000))
song = pygame.mixer.Sound("./sounds/8bit_twinkle_star.wav")

song.play()
time.sleep(30) #sleep allows the song to play