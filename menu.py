import re
import pygame
from screen import Screen

class Menu():
    def __init__(self, game):
        self.__game = game
        self.__mid_w, self.__mid_h = self.__game.screen.width / 2, self.__game.screen.height / 2
        self.__run_display = True
        self.__cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.__offset = - 100

    @property
    def game(self):
        return self.__game

    @property
    def cursor_rect(self):
        return self.__cursor_rect
    
    @property
    def offset(self):
        return self.__offset
    
    @property
    def mid_w(self):
        return self.__mid_w

    @property
    def mid_h(self):
        return self.__mid_h
    
    @property
    def run_display(self):
        return self.__run_display

    @game.setter
    def game(self, game):
        self.__game = game

    @run_display.setter
    def run_display(self, run_display):
        self.__run_display = run_display
    
    @mid_h.setter
    def mid_h(self, mid_h):
        self.__mid_h = mid_h
    
    @mid_w.setter
    def mid_w(self, mid_w):
        self.__mid_w = mid_w

    @offset.setter
    def offset(self, offset):
        self.__offset = offset
    
    @cursor_rect.setter
    def cursor_rect(self, cursor_rect):
        self.__cursor_rect = cursor_rect
    
    @run_display.setter
    def run_display(self, run_display):
        self.__run_display = run_display

    def draw_cursor(self):
        self.__game.draw_text('*', 15, self.__cursor_rect.x -100, self.__cursor_rect.y -60) 

    def blit_screen(self):
        self.__game.window.blit(self.__game.display, (0, 0))
        pygame.display.update()
        self.__game.reset_keys()
