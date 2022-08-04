import pygame
from abc import ABC, abstractmethod
from os import walk

class AnimatedObject(pygame.sprite.Sprite, ABC):
    @abstractmethod
    def __init__(self, position, path):
        super().__init__()
        self.__frames = self.import_folder(path)
        self.__frame_index = 0
        self.__image = self.__frames[self.__frame_index]
        self.__rect = self.__image.get_rect(topleft = position)
        
    @property
    def image(self):
        return self.__image

    @property
    def frame_index(self):
        return self.__frame_index
    
    @property
    def frames(self):
        return self.__frames
    
    @property
    def rect(self):
        return self.__rect

    @frame_index.setter
    def frame_index(self, frame_index):
        self.__frame_index = frame_index

    @frames.setter
    def frames(self, frames):
        self.__frames = frames

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    @image.setter
    def image(self, image):
        self.__image = image

    def import_folder(self, path, size=(64,75)):
        image_list = []
        for _,_,image_files in walk(path):
            for image in image_files:
                full_path = path + '/' + image
                image_surf = pygame.image.load(full_path).convert_alpha()
                final_image = pygame.transform.scale(image_surf, size)
                image_list.append(final_image)

        return image_list
        
    def animate(self):
        self.__frame_index += 0.20
        if self.__frame_index >= len(self.__frames):
            self.__frame_index = 0
        self.__image = self.__frames[int(self.__frame_index)]

    def update(self,level_shift):
        self.animate()
        self.rect.x += level_shift
    

