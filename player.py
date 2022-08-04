import pygame
from animated_objects import AnimatedObject
from sound import Sound

class Player(AnimatedObject):
    def __init__(self, position, path):
        super().__init__(position, path)
        self.__sound = Sound()
        self.__animations = {'idle' : [], 'run' : [], 'jump' : [], 'fall' : []}
        self.__direction = pygame.math.Vector2(0,1)
        self.__speed = 300
        self.__jump_height = 16
        self.__jumping = False
        self.__on_ground = True
        self.__on_right = True
        self.__status = 'idle'
        self.__max_health = 100
        self.__cur_health = 100
        self.__alive = True
        self.__invincible = False
        self.__invincible_duration = 700
        self.__hurt_time = 0

    @property
    def status(self):
        return self.__status

    @property
    def alive(self):
        return self.__alive

    @property
    def max_health(self):
        return self.__max_health
    
    @property
    def cur_health(self):
        return self.__cur_health

    @property
    def invincible(self):
        return self.__invincible
    
    @property
    def invincible_duration(self):
        return self.__invincible_duration
    
    @property
    def hurt_time(self):
        return self.__hurt_time

    @property
    def speed(self):
        return self.__speed

    @property
    def jump_height(self):
        return self.__jump_height

    @property
    def jumping(self):
        return self.__jumping

    @property
    def direction(self):
        return self.__direction

    @property
    def on_ground(self):
        return self.__on_ground
    
    @alive.setter
    def alive(self, alive):
        self.__alive = alive

    @invincible.setter
    def invincible(self, invincible):
        self.__invincible = invincible

    @hurt_time.setter
    def hurt_time(self, hurt_time):
        self.__hurt_time = hurt_time

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @on_ground.setter
    def on_ground(self, on_ground):
        self.__on_ground = on_ground

    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    @jumping.setter
    def jumping(self, jumping):
        self.__jumping = jumping

    @jump_height.setter
    def jump_height(self, jump_height):
        self.__jump_height = jump_height
    
    @cur_health.setter
    def cur_health(self, cur_health):
        self.__cur_health = cur_health

    def change_health(self, amount):
        if not self.invincible:
            self.cur_health -= amount
            self.invincible = True
            self.hurt_time = pygame.time.get_ticks()
    
    def invincibility_timer(self):
        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.hurt_time >= self.invincible_duration:
                self.invincible = False

    def check_alive(self):
        if self.cur_health <= 0:
            self.cur_health = 0
            self.alive = False

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.__on_right = True
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.__on_right = False
        else:
            self.direction.x = 0

        self.rect.x += self.__direction.x * self.__speed

    def jump(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            if self.__on_ground == True:
                self.__sound.jump_music()
                self.direction.y =  -(self.__jump_height)  
                self.__jumping = True 
                self.on_ground = False
   
    def status_update(self):
        if self.__direction.y < 0 :
            self.__status = 'jump'
            self.__jumping = True
        elif self.__direction.y > 1 :
            self.__status = 'fall'
            self.__on_ground = False
        else:
            if self.__direction.x != 0:
                self.__status = 'run'
            else:
                self.__status = 'idle'

    def character_assets(self):
        character_path = '../Jogo_sprites/Player/'

        for animation in self.__animations.keys():
            animation_path = character_path + animation
            self.__animations[animation] = self.frames = self.import_folder(animation_path)

    def gravity_effect(self):
        self.direction.y += 0.75
        self.rect.y += self.direction.y

    def animate(self):
        animation = self.__animations[self.__status]

        self.frame_index += 0.15
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        image = self.image = animation[int(self.frame_index)]
        if self.__on_right:
            self.image = image
        else:
            self.image = pygame.transform.flip(image, True, False)
        
    def update(self):
        self.check_alive()
        self.animate()
        self.move()
        self.jump()
        self.status_update()
        self.invincibility_timer()
    