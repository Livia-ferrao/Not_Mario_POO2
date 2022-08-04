from map_settings import *

class Map:
    def __init__(self):
        self.__maps = [map1, map2, map3]
    @property
    def maps(self):
        return self.__maps



