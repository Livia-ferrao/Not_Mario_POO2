from time import sleep
import pygame, sys
from LevelOverworld import LevelOverworld
from Overworld import Overworld


class Main:
	def __init__(self):
		self.__max_level = 2
		self.__screen = pygame.display.set_mode((1200,700))
		self.__overworld = Overworld(0,self.max_level,self.screen,self.create_level)
		self.__status = 'overworld'
		self.__BACK_KEY = False
		self.__running = True

	@property
	def running(self):
		return self.__running

	@property
	def BACK_KEY(self):
		return self.__BACK_KEY

	@property
	def status(self):
		return self.__status
	
	@property
	def overworld(self):
		return self.__overworld
	
	@property
	def max_level(self):
		return self.__max_level
	
	@property
	def screen(self):
		return self.__screen

	@running.setter
	def running(self, running):
		self.__running = running

	@BACK_KEY.setter
	def BACK_KEY(self, BACK_KEY):
		self.__BACK_KEY = BACK_KEY

	@status.setter
	def status(self, status):
		self.__status = status

	@overworld.setter
	def overworld(self, overworld):
		self.__overworld = overworld
	
	@screen.setter
	def screen(self, screen):
		self.__screen = screen

	@max_level.setter
	def max_level(self, max_level):
		self.__max_level = max_level
	
	

	def create_level(self,current_level):
		self.level = LevelOverworld(current_level,self.screen,self.create_overworld)
		self.status = 'level'

	def create_overworld(self,current_level,new_max_level):
		if new_max_level > self.max_level:
			self.max_level = new_max_level
		self.overworld = LevelOverworld(current_level,self.screen,self.create_level)
		self.status = 'overworld'

	def run(self):
		if self.status == 'overworld':
			self.overworld.run()
		else:
			self.level.run()
			sleep(2)
			self.level.start()
			self.level.game_over()
			sleep(3)
			self.status = 'overworld'

	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE:
					self.BACK_KEY = True
                

	def start(self):
		pygame.init()
		
		clock = pygame.time.Clock()
		bg = pygame.transform.scale(pygame.image.load("images_overworld/background.png"),(1200,700))

		while self.running:
			self.check_events()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				

			self.screen.blit(bg, (0, 0))
			self.run()

			pygame.display.update()
			clock.tick(60)
			if self.BACK_KEY:
				self.running = False
			self.BACK_KEY = False