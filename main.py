# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption("Asteroids Game")
	pygame.time.Clock()
	dt = 0
	player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running= False
		player.rotate(dt)
		screen.fill((0, 0, 0))
		pygame.display.flip()
		player.draw(screen)
	pygame.time.Clock.tick(60)
	dt = pygame.time.Clock.tick(60) / 1000
	pygame.quit()

if __name__ == "__main__":
	main()

