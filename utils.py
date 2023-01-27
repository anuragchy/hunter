import pygame

class Block(pygame.sprite.Sprite):
	def __init__(self, type, posx, posy):
		super().__init__()
		if type == 'wood1':
			self.image = pygame.image.load("assets/woodblock.jpeg")
		elif type == 'wood2':
			self.image = pygame.image.load("assets/woodblock2.jpeg")
		elif type == 'start':
			self.image = pygame.Surface([100, 100])
			self.type = 'start'

		self.image = pygame.transform.scale(self.image, (100, 100))
		self.rect = self.image.get_rect()
		self.rect.x = posx
		self.rect.y = posy


	def update(self, surface):
		surface.blit(self.image, (self.rect.x, self.rect.y))

class Map:
	def __init__(self, levelmap):
		self.levelmap = levelmap

	@staticmethod
	def drawMap(m):
		blockGroup = pygame.sprite.Group()
		levelmap = m.levelmap
		for i in range(len(levelmap)):
			for j in range(len(levelmap[0])):
				if(levelmap[i][j] == 1):
					wb = Block('wood1', j*100, i*100)
					blockGroup.add(wb)
				elif (levelmap[i][j] == 2):
					wb = Block('wood2', j*100, i*100)
					blockGroup.add(wb)
				elif(levelmap[i][j] == 3):
					wb = Block('start', j, i)

		return blockGroup

	@staticmethod
	def updateEnemies(levelmap, enemies):
		for i in range(len(levelmap)):
			for j in range(len(levelmap[0])):
				if levelmap[i][j] == 4:
					enemy = Enemy()
