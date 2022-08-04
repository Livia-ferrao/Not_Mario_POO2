import pygame

class Node(pygame.sprite.Sprite):
	def __init__(self,pos,status,icon_speed):
		super().__init__()
		self.__image = pygame.transform.scale(pygame.image.load('images_overworld/ilha2.png'),(400,300))
		self.__rect = self.image.get_rect(center = pos)
		self.__detection_zone = pygame.Rect(self.rect.centerx-(icon_speed/2),self.rect.centery-(icon_speed/2),icon_speed,icon_speed)

	@property
	def image(self):
		return self.__image

	@image.setter
	def image(self,image):
		self.__image = image

	@property
	def rect(self):
		return self.__rect

	@rect.setter
	def rect(self,rect):
		self.__rect = rect

	@property
	def detection_zone(self):
		return self.__detection_zone

	@detection_zone.setter
	def detection_zone(self,detection_zone):
		self.__detection_zone = detection_zone
	