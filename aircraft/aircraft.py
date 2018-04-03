#coding=utf-8
#sudo apt-get install python-pygame

import pygame

if __name__ =="__main__":
	screen = pygame.display.set_mode((480,800),0,32)

	background = pygame.image.load("./background.png").convert()

	while True:
		screen.blit(background,(0,0))
		pygame.display.update()