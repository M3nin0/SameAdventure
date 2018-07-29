import pygame
from same_adventure.models.character import Player, Orc
from same_adventure.models.weapon import Projectile

class Window(object):
    """Main window class
    """

    def __init__(self, caption, display, clock, scenario):
        pygame.display.set_caption(caption)
        self.__display = pygame.display.set_mode(display)
        self.__font = pygame.font.SysFont('comicsans', 30, True)
        self.__clock = clock
        self.__scenario = scenario
    
    def redraw_game_window(self, objects):
        self.__display.blit(self.__scenario.background, (0, 0))

        for obj in objects:            
            if type(obj).__name__ == 'Player':
                self.__display.blit(self.__font.render('Score: {}'.format(obj.score), 1, (0, 0, 0)), (45, 10))

            obj.draw(self.__display)
            pygame.display.update()

    @property
    def clock(self):
        return self.__clock

    @property
    def display(self):
        return self.__display

    @property
    def scenario(self):
        return self.__scenario
