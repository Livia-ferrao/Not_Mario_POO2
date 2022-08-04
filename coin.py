from animated_objects import AnimatedObject

class Coin(AnimatedObject):
    def __init__(self, position, path):
        super().__init__(position, path)
        self.frames = self.import_folder(path, (32,32))
        self.__rect = self.image.get_rect(center = ((position[0] + 45), (position[1]) + 45))
        self.__collected = False
        
    @property
    def rect(self):
        return self.__rect
        
    @property
    def collected(self):
        return self.__collected

    @collected.setter
    def collected(self, collected):
        self.__collected = collected

    