#coding=utf-8
#sudo apt-get install python-pygame


#4-2 Building interface
#4-3 Detection keyboard
import pygame
from pygame.locals import *

if __name__ =="__main__":
	screen = pygame.display.set_mode((480,800),0,32)

	background = pygame.image.load("./background.png").convert()

	while True:
		screen.blit(background,(0,0))

		for event in pygame.event.get():
			if event.type == QUIT:
				print("exit")
				exit()
			elif event.type == KEYDOWN:
				if event.key == K_a or event.key == K_LEFT:
					print('left')
				elif event.key == K_d or event.key == K_RIGHT:
					print('right')
				elif event.key == K_SPACE:
					print('space')

		pygame.display.update()