import pygame
pygame.font.init()

class Draw:
    def __init__(self):
        self.__text_font = pygame.font.SysFont('Bauhaus 93', 40)

    def draw(self, object, surface):
        object.draw(surface)

    def score_ui(self, image, amount, surface, position):
        surface.blit(image, position)
        coin_amount = self.__text_font.render('x' + str(amount), False, 'black')
        coin_amount_rect = coin_amount.get_rect(midleft = (position[0] + 40,position[1] + 18 ))
        surface.blit(coin_amount, coin_amount_rect)
        
