import pygame, sys
from menuCredits import menuCredits
from menuMain import menuMain
from menuScore import menuScore
from main import Main
from screen import Screen
from sound import Sound


class Play():
    def __init__(self):
        pygame.init()

        self.__sound = Sound()
        pygame.mixer.music.load("./sound/BoxCat-Games-CPU-Talk.ogg")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
    
        self.__game = Main()
        self.__screen = Screen()
        self.__running, self.__playing = True, False

        self.__display = pygame.Surface((self.__screen.width, self.__screen.height))
        self.__window = pygame.display.set_mode(((self.__screen.width,self.__screen.height)))

        self.__UP_KEY, self.__DOWN_KEY, self.__START_KEY, self.__BACK_KEY = False, False, False, False

        self.__main_menu = menuMain(self)
        self.__score = menuScore(self)
        self.__credits = menuCredits(self)
        self.__curr_menu = self.__main_menu

        self.__imageMenu = pygame.image.load('images/mainMenu.png')
        self.__menu_image = pygame.transform.scale(self.__imageMenu, (self.__screen.width ,self.__screen.height))
        self.__imageCreditos = pygame.image.load('images/creditsMenu.png')
        self.__creditos_image = pygame.transform.scale(self.__imageCreditos, (self.__screen.width, self.__screen.height ))
        self.__imageScore = pygame.image.load('images/scoreMenu.png')
        self.__score_image = pygame.transform.scale(self.__imageScore, (self.__screen.width, self.__screen.height ))
    
    @property
    def display(self):
        return self.__display

    @property
    def running(self):
        return self.__running

    @property
    def playing(self):
        return self.__playing

    @property
    def screen(self):
        return self.__screen

    @property
    def menu_image(self):
        return self.__menu_image
    
    @property
    def creditos_image(self):
        return self.__creditos_image
    
    @property
    def score_image(self):
        return self.__score_image

    @property
    def window(self):
        return self.__window
    
    @property
    def UP_KEY(self):
        return self.__UP_KEY

    @property
    def DOWN_KEY(self):
        return self.__DOWN_KEY

    @property
    def START_KEY(self):
        return self.__START_KEY

    @property
    def BACK_KEY(self):
        return self.__BACK_KEY

    @property
    def main_menu(self):
        return self.__main_menu
    
    @property
    def score(self):
        return self.__score

    @property
    def credits(self):
        return self.__credits

    @property
    def curr_menu(self):
        return self.__curr_menu

    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, sound):
        self.__sound = sound

    @curr_menu.setter
    def curr_menu(self, curr_menu):
        self.__curr_menu = curr_menu

    @playing.setter
    def playing(self, playing):
        self.__playing = playing

    @menu_image.setter
    def menu_image(self, menu_image):
        self.__image_image = menu_image
    
    @creditos_image.setter
    def creditos_image(self, creditos_image):
        self.__creditos_image = creditos_image

    @score_image.setter
    def score_image(self, score_image):
        self.__score_image = score_image
    
    @window.setter
    def window(self, window):
        self.__window = window

    @UP_KEY.setter
    def UP_KEY(self, UP_KEY):
        self.__UP_KEY = UP_KEY

    @DOWN_KEY.setter
    def DOWN_KEY(self, DOWN_KEY):
        self.__DOWN_KEY = DOWN_KEY

    @START_KEY.setter
    def START_KEY(self, START_KEY):
        self.__START_KEY = START_KEY
    
    @BACK_KEY.setter
    def BACK_KEY(self, BACK_KEY):
        self.__BACK_KEY = BACK_KEY
    
    @main_menu.setter
    def main_menu(self, main_menu):
        self.__main_menu = main_menu

    @score.setter
    def score(self, score):
        self.__score = score

    @credits.setter
    def credits(self, credits):
        self.__credits = credits


    def game_loop(self):
        while self.__playing:
            self.check_events()
            if self.__BACK_KEY:
                self.__playing= False
            self.__game.start()

            pygame.display.update()
            self.reset_keys()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running, self.__playing = False, False
                self.__curr_menu.__run_display = False
                pygame.quit() 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.__START_KEY = True
                    self.__game.running = True
                if event.key == pygame.K_BACKSPACE:
                    self.__BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.__DOWN_KEY = True
                    self.__sound.move_cursor_music()
                if event.key == pygame.K_UP:
                    self.__UP_KEY = True
                    self.__sound.move_cursor_music()

    def reset_keys(self):
        self.__UP_KEY, self.__DOWN_KEY, self.__START_KEY, self.__BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font('font/8-BIT WONDER.TTF',size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.__display.blit(text_surface,text_rect)

    def start_not_mario(self):
        g = Play()

        while g.running:
            g.curr_menu.display_menu()
            g.game_loop()
            g.reset_keys()