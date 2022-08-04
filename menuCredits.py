from menu import Menu

class menuCredits(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False

            self.game.display.blit(self.game.creditos_image, (0, 0))
            self.game.draw_text('Credits', 45, self.game.screen.width / 2, self.game.screen.height / 2 - 90)
            self.game.draw_text('Game made by', 30, self.game.screen.width / 2, self.game.screen.height / 2 -30)
            self.game.draw_text('Eduardo', 30, self.game.screen.width / 2, self.game.screen.height / 2 + 30)
            self.game.draw_text('Fillipi', 30, self.game.screen.width / 2, self.game.screen.height / 2 + 70)
            self.game.draw_text('Livia', 30, self.game.screen.width / 2, self.game.screen.height / 2 + 110)
            self.game.draw_text('Lucas', 30, self.game.screen.width / 2, self.game.screen.height / 2 + 150)
            self.blit_screen()