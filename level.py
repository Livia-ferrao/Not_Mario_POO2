from level_controller import LevelController
from map import Map
from screen import Screen

class Level:
    def __init__(self, screen):
        self.__map = Map()
        self.__levels = [LevelController(self.__map.maps[0], screen),
                         LevelController(self.__map.maps[1], screen),
                         LevelController(self.__map.maps[2], screen)
                        ]


    @property
    def levels(self):
        return self.__levels