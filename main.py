import pygame
import pygame.font
import math
from player import Player
from player import Enemy
from utils import Map
pygame.init()

win = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()
pygame.display.set_caption("Hunter Assassin")



level1 = [
	[0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
	[0, 1, 2, 0, 1, 1, 0, 0, 0, 0, 0, 1],
	[0, 2, 2, 0, 1, 1, 0, 0, 0, 0, 0, 2],
	[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
	[0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 1],
	[0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 3]
]

map1 = Map(level1)
blockGroup = Map.drawMap(map1)

player = Player(blockGroup)
playerGroup = pygame.sprite.Group()
playerGroup.add(player)

backImage = pygame.image.load("assets/back.jpg")
bulletGroup = pygame.sprite.Group()
enemy = Enemy(7, blockGroup, player)
enemyGroup = pygame.sprite.Group()
enemyGroup.add(enemy)

while True:
	clock.tick(60)
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()


	win.fill((0, 0, 0))
	playerGroup.draw(win)
	playerGroup.update()
	blockGroup.update(win)
	enemyGroup.draw(win)
	enemyGroup.update(win)
	pygame.display.update()