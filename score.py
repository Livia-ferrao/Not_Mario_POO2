import pygame

class Score:
    def __init__(self):
        self.__score = 0
        self.__image = pygame.image.load("../Jogo_sprites/Score_UI/coin_ui.png")

    @property 
    def score(self):
        return self.__score
    
    @property 
    def image(self):
        return self.__image

    @score.setter
    def score(self, score):
        self.__score = score

    def update(self):
        self.__score += 1
