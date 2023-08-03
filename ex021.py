import pygame

pygame.init()
pygame.mixer.music.load('sound.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print('press enter to close the audio')
input()

