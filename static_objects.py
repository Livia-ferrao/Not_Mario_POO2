import pygame
from abc import ABC, abstractmethod

class StaticObject(pygame.sprite.Sprite, ABC):
    @abstractmethod
    def __init__(self, position, image):
        super().__init__()
        self.__image = image
        self.__rect = self.image.get_rect(topleft = position)

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image):
        self.__image = image

    @property
    def rect(self):
        return self.__rect

    def update(self, x_shift):
        self.rect.x += x_shift