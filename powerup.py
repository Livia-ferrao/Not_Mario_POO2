from random import randint
from animated_objects import AnimatedObject
from player import Player

class Powerup(AnimatedObject):
    def __init__(self, position, path):
        super().__init__(position, path)
        self.__size = 64
        self.__rect = self.image.get_rect(center = ((position[0] + int(self.__size/2)), (position[1] + int(self.__size/2))))
        self.__collected = False

    @property
    def rect(self):
        return self.__rect
    
    def drop_powerup(self, powerup):
            return powerup

    @property
    def collected(self):
        return self.__collected
    
    @collected.setter
    def collected(self, collected):
        self.__collected = collected

    def effect(self, player):
        x = randint(0,2)
        if x == 0:
            player.speed = 20
        elif x == 1:
            if player.max_health - player.cur_health >= 20:
                player.cur_health += 20
            else:
                player.cur_health = player.max_health
        else:
            player.jump_height = 22

