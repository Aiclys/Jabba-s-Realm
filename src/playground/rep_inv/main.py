#!/usr/bin/env python3

import pygame, sys
from settings import WIDTH, HEIGHT, NAV_THICKNESS
from world import World

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT + NAV_THICKNESS))
pygame.display.set_caption("Republic Invader")

class Main:
	def __init__(self, screen):
		self.screen = screen
		self.FPS = pygame.time.Clock()

	def main(self):
		world = World(self.screen)
		while True:
			self.screen.fill("black")

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						world.player_move(attack = True)

			world.player_move()
			world.update()
			pygame.display.update()
			self.FPS.tick(30)


if __name__ == "__main__":
	play = Main(screen)
	play.main()
