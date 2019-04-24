import pygame, time

pygame.mixer.init()
pygame.init()

screen = pygame.display.set_mode((1000,1000))
song = pygame.mixer.Sound("./sounds/8bit_twinkle_star.wav")

while True:
    song.play()
    pygame.display.quit()
# time.sleep(5)

# time.sleep(30) #sleep allows the song to play