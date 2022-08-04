from score import Score
from sprites import Sprites
from draw import Draw
from colision import Colision
from health import Health
from random import randint, random
from powerup import Powerup
from coin import Coin
import pygame
from scoreDAO import ScoreDAO
from datetime import datetime
from sound import Sound

class LevelController:
    def __init__(self, current_level, surface):
        self.__sound = Sound()
        self.__scoreDAO = ScoreDAO()
        self.__draw = Draw()
        self.__sprite = Sprites()
        self.__score = Score()
        self.__colision = Colision()
        self.__date = datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')
        self.__health = Health(surface)
        self.__display_surface = surface
        self.__level_shift = 0
        self.__level = current_level
        self.__ground = self.__sprite.setup_sprite(self.__level, 'ground')
        self.__coins = self.__sprite.setup_sprite(self.__level, 'coins')
        self.__enemys = self.__sprite.setup_sprite(self.__level, 'enemys')
        self.__limiter = self.__sprite.setup_sprite(self.__level, 'limiter')
        self.__player = self.__sprite.setup_sprite(self.__level, 'player')
        self.__flag = self.__sprite.setup_sprite(self.__level, 'flag')
        self.__powerup = pygame.sprite.Group()
        self.__game_over_player = False
        self.__game_win = False
    
    @property
    def game_over_player(self):
        return self.__game_over_player

    @game_over_player.setter
    def game_over(self,game_over_player):
        self.__game_over_player = game_over_player

    @property
    def game_win(self):
        return self.__game_win

    @game_win.setter
    def game_over(self,game_win):
        self.__game_win = game_win


    def mapa_limiter(self):
        player = self.__player.sprite
        player_x = player.rect.centerx
        player_y = player.rect.centery
        direction_x = player.direction.x
        
        if player_x < 300 and direction_x < 0:
            self.__level_shift = 4
            player.speed = 0
        elif player_x > 600 and direction_x > 0:
            self.__level_shift = -4
            player.speed = 0
        else:
            self.__level_shift = 0
            player.speed = 4
        
        if player_y >= 1150:
            self.__game_over_player = True


    def colision_control(self):
        self.__colision.ground_horizontal_colison(self.__ground.sprites(), self.__player.sprite)
        self.__colision.ground_vertical_colison(self.__ground.sprites(), self.__player.sprite)
        self.__colision.ground_vertical_colison(self.__ground.sprites(), self.__enemys.sprites())
        self.__colision.player_enemy_colision(self.__enemys.sprites(), self.__player.sprite)
        self.__colision.player_coin_colision(self.__coins.sprites(), self.__player.sprite)
        self.__colision.enemy_limiter_colision(self.__limiter.sprites(), self.__enemys.sprites())
        self.__colision.player_powerup_colision(self.__powerup.sprites(), self.__player.sprite)
        self.__colision.player_flag_colision(self.__flag.sprites(), self.__player.sprite)
                    
    def draw_control(self):
        self.__draw.draw(self.__ground, self.__display_surface)
        self.__draw.draw(self.__player, self.__display_surface)
        self.__draw.draw(self.__enemys, self.__display_surface)
        self.__draw.draw(self.__coins, self.__display_surface)
        self.__draw.score_ui(self.__score.image, self.__score.score, self.__display_surface, (50, 60))
        self.__health.show_health(self.__player.sprite.cur_health, self.__player.sprite.max_health)
        self.__draw.draw(self.__powerup, self.__display_surface)
        self.__draw.draw(self.__flag, self.__display_surface)

    def update(self):
        self.__ground.update(self.__level_shift)
        self.__coins.update(self.__level_shift)
        self.__enemys.update(self.__level_shift)
        self.__limiter.update(self.__level_shift)
        self.__player.update()
        self.__powerup.update(self.__level_shift)
        self.__flag.update(self.__level_shift)

    def check_state(self):
        for sprite in self.__enemys.sprites():
            if sprite.dead == True:
                posicao = sprite.rect.topleft
                if randint(0,1) == 0 or 1:
                    self.__powerup.add((Powerup(posicao, "../Jogo_sprites/Powerup")))
                sprite.kill()

        for sprite in self.__coins.sprites():
            if sprite.collected == True:
                sprite.kill()

    def score(self):
        for sprite in self.__coins.sprites():
            if sprite.collected == True:
                self.__score.update()
                self.__sound.coin_music()
    
    def game_over(self):
        if self.__player.sprite.alive == False or self.__game_over_player == True:
            self.__scoreDAO.add(self.__date, self.__score)
            self.__player.sprite.alive = True
            self.__game_over_player = True

    def win(self):
        for flag in self.__flag:
            if flag.collected == True:
                self.__scoreDAO.add(self.__date, self.__score)
                self.__game_win = True
                flag.kill()


    def run(self):
        self.draw_control()
        self.update()
        self.mapa_limiter() 
        self.colision_control()
        self.score()
        self.game_over()
        self.win()
        self.check_state()

