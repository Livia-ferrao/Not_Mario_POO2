from csv import reader
import pygame

class ImportFile:
    def __init__(self):
        self.__file_size = 64

    @property
    def size(self):
        return self.__file_size

    def import_csv_layout(self, path):
        level_map = []
        with open(path) as map:
            level = reader(map, delimiter= ',')
            for line in level:
                level_map.append(list(line))
            return level_map

    def import_graphics(self, path):
        image = pygame.image.load(path).convert_alpha()
        sprite_x = int(image.get_size()[0] / self.__file_size)
        sprite_y = int(image.get_size()[1] / self.__file_size)

        image_list = []
        for line in range(sprite_y):
            for colum in range(sprite_x):
                x = colum * self.__file_size
                y = line * self.__file_size
                new_image = pygame.Surface((self.__file_size, self.__file_size), flags = pygame.SRCALPHA)
                new_image.blit(image, (0,0), pygame.Rect(x,y,self.__file_size,self.__file_size))
                image_list.append(new_image)
        return image_list

