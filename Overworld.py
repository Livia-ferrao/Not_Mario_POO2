import pygame 
from node_overworld import Node
from icon_overworld import Icon



class Overworld:
	def __init__(self,start_level,max_level,surface,new_level):
		self.__display_surface = surface 
		self.__max_level = max_level
		self.__current_level = start_level
		self.__new_level = new_level
		self.__moving = False
		self.__move_direction = pygame.math.Vector2(0,0)
		self.__speed = 10
		self.__levels = [
		{'node_pos':(300,450), 'content': 'this is level 1','unlock':1},
		{'node_pos':(600,300), 'content': 'this is level 2','unlock':2},
		{'node_pos':(900,450), 'content': 'this is level 3', 'unlock':2}]
		self.setup_nodes()
		self.setup_icon()

	@property
	def display_surface(self):
		return self.__display_surface

	@property
	def current_level(self):
		return self.__current_level
	
	@property
	def levels(self):
		return self.__levels

	@property
	def max_level(self):
		return self.__max_level

	@property
	def new_level(self):
		return self.__new_level
	
	@property
	def moving(self):
		return self.__moving
	
	@property
	def move_direction(self):
		return self.__move_direction

	@property
	def speed(self):
		return self.__speed

	@move_direction.setter
	def move_direction(self):
		self.__move_direction = self.__move_direction
	
	@current_level.setter
	def current_level(self, current_level):
		self.__current_level = current_level

	@moving.setter
	def moving(self,moving):
		self.__moving = moving

	@move_direction.setter
	def move_direction(self, direction):
		self.__move_direction = direction

	def setup_nodes(self):
		self.nodes = pygame.sprite.Group()

		for index, node_data in enumerate(self.levels):
			if index <= self.max_level:
				node_sprite = Node(node_data['node_pos'],'available',self.speed)
			else:
				node_sprite = Node(node_data['node_pos'],'locked',self.speed)
			self.nodes.add(node_sprite)

	def draw_paths(self):
		points = [node['node_pos'] for index,node in enumerate(self.levels) if index <= self.max_level]
		pygame.draw.lines(self.display_surface,'grey',False,points,10)

	def setup_icon(self):
		self.icon = pygame.sprite.GroupSingle()
		icon_sprite = Icon(self.nodes.sprites()[self.current_level].rect.center)
		self.icon.add(icon_sprite)

	def input(self):
		keys = pygame.key.get_pressed()

		if not self.moving:
			if keys[pygame.K_RIGHT] and self.current_level < self.max_level:
				self.move_direction = self.get_movement_data('next')
				self.current_level += 1
				self.moving = True
			elif keys[pygame.K_LEFT] and self.current_level > 0:
				self.move_direction = self.get_movement_data('previous')
				self.current_level -= 1
				self.moving = True
			elif keys[pygame.K_SPACE]:
				self.new_level(self.current_level)

	def get_movement_data(self,target):
		start = pygame.math.Vector2(self.nodes.sprites()[self.current_level].rect.center)
		
		if target == 'next': 
			end = pygame.math.Vector2(self.nodes.sprites()[self.current_level + 1].rect.center)
		else:
			end = pygame.math.Vector2(self.nodes.sprites()[self.current_level - 1].rect.center)

		return (end - start).normalize()

	def update_icon_pos(self):
		if self.moving and self.move_direction:
			self.icon.sprite.pos += self.move_direction * self.speed
			target_node = self.nodes.sprites()[self.current_level]
			if target_node.detection_zone.collidepoint(self.icon.sprite.pos):
				self.moving = False
				self.move_direction = pygame.math.Vector2(0,0)


	def run(self):
		self.input()
		self.update_icon_pos()
		self.icon.update()
		self.draw_paths()
		self.nodes.draw(self.display_surface)
		self.icon.draw(self.display_surface)