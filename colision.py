from player import Player
from enemy import Enemy


class Colision:
    def __init__(self):
        pass

    def ground_horizontal_colison(self, ground, sprite):
        for ground_sprite in ground:
                if sprite.rect.colliderect(ground_sprite.rect):
                    if sprite.direction.x < 0:
                        sprite.rect.left = ground_sprite.rect.right
                    elif sprite.direction.x > 0:
                        sprite.rect.right = ground_sprite.rect.left
                        
    def ground_vertical_colison(self, ground, sprite):
        if isinstance(sprite, Player):
            sprite.gravity_effect()
            for ground_sprite in ground:
                    if sprite.rect.colliderect(ground_sprite.rect):
                        if sprite.direction.y < 0:
                            sprite.rect.top = ground_sprite.rect.bottom
                            sprite.direction.y = 0
                        elif sprite.direction.y > 0.5:
                                sprite.rect.bottom = ground_sprite.rect.top
                                sprite.direction.y = 0
                                sprite.on_ground = True
                                sprite.jumping = False
        elif isinstance (sprite, Enemy):
            for enemy in sprite:
                enemy.gravity_effect()
                for ground_sprite in ground:
                    if sprite.rect.colliderect(ground_sprite.rect):
                        sprite.rect.bottom = ground_sprite.rect.top

    def player_enemy_colision(self, enemy, player):
        for enemy_sprite in enemy:
            if player.rect.colliderect(enemy_sprite.rect):
                if enemy_sprite.rect.top < player.rect.bottom < enemy_sprite.rect.centery and player.status == "fall":
                    player.direction.y = -player.jump_height
                    enemy_sprite.dead = True
                else:
                    player.change_health(enemy_sprite.power)

    def enemy_limiter_colision(self, limiter, enemy):
        for limiter_sprite in limiter:
            for enemy_sprite in enemy:
                if enemy_sprite.rect.colliderect(limiter_sprite.rect):
                    enemy_sprite.reverse_side()

    def player_coin_colision(self, coin, player):
        for coin_sprite in coin:
            if player.rect.colliderect(coin_sprite.rect):
                coin_sprite.collected = True
    
    def player_powerup_colision(self, powerup, player):
        for powerup_sprite in powerup:
            if player.rect.colliderect(powerup_sprite.rect):
                powerup_sprite.effect(player)
                powerup_sprite.kill()

    def player_flag_colision(self, flag, player):
        for flag_sprite in flag:
            if player.rect.colliderect(flag_sprite.rect):
                flag_sprite.collected = True
                
