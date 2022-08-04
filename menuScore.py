from menu import Menu
from scoreDAO import ScoreDAO
import pygame

class menuScore(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()    
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.blit(self.game.score_image, (0, 0))
      
            self.game.draw_text('Score', 40, self.game.screen.width / 2, 150)
            self.showScore()
            self.blit_screen()

    def showScore(self):
        self.__scoreDAO = ScoreDAO()
        plus = 0
        count = 0    
        for data, score in self.__scoreDAO.get_all():
            self.draw_score(data, 20, 450, 250 + plus)
            self.draw_score("---------------", 20, 675, 250 + plus)
            self.draw_score(str(score), 20, 750, 250 + plus)
            plus += 50
            count += 1
            if count >= 7:
                break

    def draw_score(self, text, size, x, y):
        font = pygame.font.Font("freesansbold.ttf",size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.game.display.blit(text_surface,text_rect)
