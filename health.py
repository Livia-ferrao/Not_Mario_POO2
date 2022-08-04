import pygame

class Health:
    def __init__(self, surface):
        self.__surface = surface
        self.__health_bar = pygame.image.load('../Jogo_sprites/Health/health_bar.png')
        self.__health_bar_topleft = (54,39)
        self.__bar_max_width = 152
        self.__bar_height = 4
    
    @property
    def health_bar(self):
        return self.__health_bar

    @property
    def health_bar_topleft(self):
        return self.__health_bar_topleft
    
    @property
    def bar_max_width(self):
        return self.__bar_max_width
    
    @property
    def bar_height(self):
        return self.__bar_height

    @property
    def surface(self):
        return self.__surface

    def show_health(self, current, full):
        self.__surface.blit(self.__health_bar,(20,10))
        current_health_ratio = current / full
        current_bar_width = self.__bar_max_width * current_health_ratio
        health_bar_rect = pygame.Rect(self.__health_bar_topleft,(current_bar_width, self.__bar_height))
        pygame.draw.rect(self.__surface, '#dc4949', health_bar_rect)
