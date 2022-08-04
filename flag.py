from static_objects import StaticObject

class Flag(StaticObject):
    def __init__(self, position, image):
        super().__init__(position, image)
        self.__collected = False

    @property
    def collected(self):
        return self.__collected

    @collected.setter
    def collected(self, collected):
        self.__collected = collected