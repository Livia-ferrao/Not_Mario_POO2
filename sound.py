import pygame

class Sound:
    def __init__(self):
        pass

    def coin_music(self):
        music = pygame.mixer.Sound('sound/smw_coin.wav')
        music.play()

    def jump_music(self):
        music = pygame.mixer.Sound('sound/smw_jump.wav')
        music.play()
    
    def move_cursor_music(self):
        music = pygame.mixer.Sound('sound/smw_kick.wav')
        music.play()

