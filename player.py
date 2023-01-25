import pygame
class Player(pygame.sprite.Sprite):
	def __init__(self, blocks):
		super().__init__()
		self.image = pygame.image.load("assets/hunter.png")
		self.image = pygame.transform.scale(self.image, (80, 80))
		self.ogimage = self.image
		self.rect = self.image.get_rect()
		self.blocks = blocks
		self.facingx = 0
		self.facingy = 0
		self.speed = 5
		self.health = 100
		self.enemies = []

	def setHealth(self, health):
		self.health = health

	def setEnemies(self, enemies):
		self.enemies = enemies


	def get_input(self):
		key = pygame.key.get_pressed()
		if key[pygame.K_w]:
			self.image = self.ogimage
			self.facingy = -1
			if self.rect.y > 0:
				self.rect.y += self.facingy*self.speed
				for sprite in self.blocks.sprites():
					if self.rect.colliderect(sprite.rect):
						self.rect.top = sprite.rect.bottom
		elif key[pygame.K_s]:
			self.image = pygame.transform.rotozoom(self.ogimage, 180, 1)
			self.facingy = 1
			if self.rect.y + self.rect.h < 690:
				self.rect.y += self.facingy*self.speed
				for sprite in self.blocks.sprites():
					if self.rect.colliderect(sprite.rect):
						self.rect.bottom = sprite.rect.top
		elif key[pygame.K_a]:
			self.image = pygame.transform.rotozoom(self.ogimage, 90, 1)
			self.facingx = -1
			if self.rect.x > 0:
				self.rect.x += self.facingx*self.speed
				for sprite in self.blocks.sprites():
					if self.rect.colliderect(sprite.rect):
						self.rect.left = sprite.rect.right
		elif key[pygame.K_d]:
			self.image = pygame.transform.rotozoom(self.ogimage, -90, 1)
			self.facingx = 1
			if self.rect.x < 1120:
				self.rect.x += self.facingx*self.speed
				for sprite in self.blocks.sprites():
					if self.rect.colliderect(sprite.rect):
						self.rect.right = sprite.rect.left

		elif key[pygame.K_f]:
			for enemy in self.enemies.sprites():
				if enemy.rect.colliderect(self.rect):
					enemy.kill()
	def update(self):
		self.get_input()

class Bullet(pygame.sprite.Sprite):
	def __init__(self, player, posx, posy, facing):
		super().__init__()
		self.image = pygame.image.load("assets/bullet.png")
		self.image = pygame.transform.scale(self.image, (20, 40))
		self.ogimage = self.image
		self.rect = self.image.get_rect()
		self.player = player
		self.facing = facing
		self.rect.x = posx-5
		self.rect.y = posy+50
		self.speed = 10

	def update(self):
		if self.facing == 'down':
			self.image = pygame.transform.rotozoom(self.ogimage, -90, 1)
			self.rect.y += self.speed
		elif self.facing == 'up':
			self.image = pygame.transform.rotozoom(self.ogimage, 90, 1)
			self.rect.y -= self.speed
		if self.rect.colliderect(self.player.rect):
			newhealth = self.player.health-5
			self.player.setHealth(newhealth)
			if self.player.health < 0:
				self.player.kill()
			print(self.player.health)
		if (self.rect.y == 0 or self.rect.y == 660):
			self.kill()

class Enemy(Player):
	def __init__(self, col, blocks, player):
		super().__init__(blocks)
		self.image = pygame.image.load("assets/enemy.png")
		self.image = pygame.transform.scale(self.image, (100, 100))
		self.ogimage = self.image
		self.rect = self.image.get_rect()
		self.rect.y = 0
		self.rect.x = col*100
		self.player = player
		self.up = False
		self.speed = 1
		self.cooldown = 0
		self.bulletGroup = pygame.sprite.Group()

	def shoot(self):
		if self.cooldown > 20:
			self.cooldown = 0
			if self.up == True:
				bullet = Bullet(self.player, self.rect.x+25, self.rect.y, 'up')
				self.bulletGroup.add(bullet)
			elif self.up == False:
				bullet = Bullet(self.player, self.rect.x+25, self.rect.y, 'down')
				self.bulletGroup.add(bullet)
		else:
			self.cooldown += 1

	def update(self, surf):
		if self.up:
			self.line = pygame.draw.line(surf, (255, 255, 255), (self.rect.x+50, self.rect.y+50), (self.rect.x+50, 0), 1)
		elif self.up == False:
			self.line = pygame.draw.line(surf, (255, 255, 255), (self.rect.x+50, self.rect.y+50), (self.rect.x+50, 700), 1)
		if self.rect.y == 0:
			self.image = pygame.transform.rotozoom(self.ogimage, 180, 1)
			self.up = False
		elif self.rect.y == 600:
			self.image = self.ogimage
			self.up = True
		if self.up:
			self.rect.y -= self.speed
		elif not self.up:
			self.rect.y += self.speed
		self.bulletGroup.draw(surf)
		self.bulletGroup.update()
		if self.player.rect.colliderect(self.line):
			self.shoot()