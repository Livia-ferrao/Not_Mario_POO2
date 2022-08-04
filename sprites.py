import pygame
from flag import Flag
from player import Player
from ground import Ground
from coin import Coin
from enemy import Enemy
from limiter import Limiter
from import_file import ImportFile

class Sprites:
    def __init__(self):
        self.__files = ImportFile()
        self.__import_sprite = self.__files.import_graphics
        self.__sprites = {'ground' : ('../Jogo_sprites/Ground/ground_sprite.png', Ground),
                          'flag' : ('../Jogo_sprites/Flag/flag.png', Flag),
                          'coins' : ('../Jogo_sprites/Coins/animation', Coin),
                          'enemys' : ('../Jogo_sprites/Enemy/Run', Enemy),
                          'limiter' : ('../Jogo_sprites/Limiter/limiter_sprite.png', Limiter),
                          'player' : ('../Jogo_sprites/Player/idle', Player)
                            }
        self.__layout = self.__files.import_csv_layout

    def create_sprite_group(self,layout,type):
        size = self.__files.size
        sprite_group = pygame.sprite.Group()

        for line_index, line in enumerate(layout):
            for colum_index,val in enumerate(line):
                    if val != '-1':
                        x = colum_index * size
                        y = line_index * size

                        if type == 'ground' or type == 'limiter' or type == 'flag' :
                            image_list = self.__import_sprite(self.__sprites[type][0])
                            image = image_list[int(val)]
                            sprite = self.__sprites[type][1]((x,y), image)
                        
                        elif type == 'player':
                            sprite_group = pygame.sprite.GroupSingle()
                            sprite = self.__sprites[type][1]((x,y), self.__sprites[type][0])
                            sprite.character_assets()

                        else: 
                            sprite = self.__sprites[type][1]((x,y), self.__sprites[type][0])

                        sprite_group.add(sprite)

        return sprite_group

    def setup_sprite(self, level, group):
        setup = self.__layout(level[group])
        sprites = self.create_sprite_group(setup, group)
        return sprites