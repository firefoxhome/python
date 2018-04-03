#coding=utf-8
#sudo apt-get install python-pygame

#4-2        Building interface
#4-3 12:03  Detection keyboard
#4-3 14:30  Control my plane to move around
#4-3 16:03  Aircraft launching bullets

import pygame
from pygame.locals import *

class HeroPlane(object):

	def __init__(self,screen):
		self.x = 230
		self.y = 600

		self.screen = screen

		self.imageName = "./hero.gif"
		self.image = pygame.image.load(self.imageName).convert()

		self.bulletList = []

	def display(self):
		self.screen.blit(self.image,(self.x,self.y))

		for bullet in self.bulletList:
			bullet.display()
			bullet.move()

	def moveLeft(self):
		self.x -= 10

	def moveRight(self):
		self.x += 10

	def sheBullet(self):
		newBullet = Bullet(self.x,self.y,self.screen)
		self.bulletList.append(newBullet)

class Bullet(object):
	def __init__(self,x,y,screen):
		self.x = x+40
		self.y = y-20
		self.screen = screen
		self.image = pygame.image.load("./bullet-3.png").convert()

	def move(self):
		self.y -= 2

	def display(self):
		self.screen.blit(self.image,(self.x,self.y))


if __name__ =="__main__":
	screen = pygame.display.set_mode((480,800),0,32)

	background = pygame.image.load("./background.png").convert()

	heroPlane = HeroPlane(screen)

	#hero = pygame.image.load("./hero.gif").convert()

	#x=0
	#y=0

	while True:
		screen.blit(background,(0,0))

		heroPlane.display()

		#screen.blit(hero,(x,y))

		for event in pygame.event.get():
			if event.type == QUIT:
				print("exit")
				exit()
			elif event.type == KEYDOWN:
				if event.key == K_a or event.key == K_LEFT:
					print('left')
					heroPlane.moveLeft()
					#x-=5
				elif event.key == K_d or event.key == K_RIGHT:
					print('right')
					heroPlane.moveRight()
					#x+=5
				elif event.key == K_SPACE:
					print('space')
					heroPlane.sheBullet()

		pygame.display.update()