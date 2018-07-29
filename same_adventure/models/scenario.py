import pygame
pygame.mixer.init()

class Scenario(object):
    def __init__(self, background, music):
        self.__background = pygame.image.load(background)
        self.__music = pygame.mixer.music.load(music)
    
    @property
    def background(self):
        return self.__background

    def play_music(self):
        pygame.mixer.music.play(-1)

    def stop_music(self): 
        pygame.mixer.music.stop()