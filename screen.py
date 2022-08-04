import pygame

class Screen():
    def __init__(self):
        self.__width = 1200
        self.__height = 700
        self.__screen = pygame.display.set_mode((self.__width, self.__height))

    @property
    def screen(self):
        return self.__screen

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height