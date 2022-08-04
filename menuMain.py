from menu import Menu

class menuMain(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.__state = "Start"
        self.__startx, self.__starty = self.mid_w, self.mid_h + 20
        self.__scorex, self.__scorey = self.mid_w, self.mid_h + 60
        self.__creditsx, self.__creditsy = self.mid_w, self.mid_h + 100
        self.cursor_rect.midtop = (self.__startx + self.offset, self.__starty)

    def display_menu(self):
        self.__run_display = True
        while self.__run_display:
            self.game.check_events()
            self.check_input()
            #self.game.display.fill(self.game.WHITE)
            self.game.display.blit(self.game.menu_image, (0, 0))
            self.game.draw_text("Start Game", 35, self.__startx, self.__starty -65)
            self.game.draw_text("Score", 35, self.__scorex, self.__scorey -65)
            self.game.draw_text("Credits", 35, self.__creditsx, self.__creditsy -65)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.__state == 'Start':
                self.cursor_rect.midtop = (self.__scorex + self.offset, self.__scorey)
                self.__state = 'Score'
            elif self.__state == 'Score':
                self.cursor_rect.midtop = (self.__creditsx + self.offset, self.__creditsy)
                self.__state = 'Credits'
            elif self.__state == 'Credits':
                self.cursor_rect.midtop = (self.__startx + self.offset, self.__starty)
                self.__state = 'Start'
        elif self.game.UP_KEY:
            if self.__state == 'Start':
                self.cursor_rect.midtop = (self.__creditsx + self.offset, self.__creditsy)
                self.__state = 'Credits'
            elif self.__state == 'Score':
                self.cursor_rect.midtop = (self.__startx + self.offset, self.__starty)
                self.__state = 'Start'
            elif self.__state == 'Credits':
                self.cursor_rect.midtop = (self.__scorex + self.offset, self.__scorey)
                self.__state = 'Score'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.__state == 'Start':
                self.game.playing = True
            elif self.__state == 'Score':
                self.game.curr_menu = self.game.score
            elif self.__state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.__run_display = False