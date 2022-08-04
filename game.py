import pygame, sys
from pygame.locals import *
from screen import Screen
from level import Level
from time import sleep
class Game:
    def __init__(self):
        self.__clock = pygame.time.Clock()
        self.__FPS = 60
        self.__running = True
        self.__screen = Screen().screen
        self.__name = pygame.display.set_caption('Not Mario')
        self.__level = Level(self.__screen).levels[1]
        self.__win = False
        self.__over = False
    @property
    def win(self):
        return self.__win
    @win.setter

    def win(self,win):
        self.__win = win
        
    @property
    def over(self):
        return self.__over

    @over.setter
    def over(self,over):
        self.__over = over
    
    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self,level):
        self.__level = level

    @property
    def running(self):
        return self.__running

    def start_game(self):
        pygame.init()
        bg = pygame.transform.scale(pygame.image.load("images/background2.png"),(1200,700))
        while self.__running:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit() 
                    sys.exit()

            self.__screen.blit(bg, (0, 0))
            #self.__screen.fill((200,200,200))
            self.__level.run() 

            pygame.display.update()
            self.__clock.tick(self.__FPS)
            self.win = self.__level.game_win
            self.over = self.__level.game_over_player
            if self.__level.game_over_player == True or self.__level.game_win == True:
                self.__running = False

