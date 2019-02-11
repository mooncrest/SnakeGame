import pygame
import sys
import random
from collections import deque
import itertools
import time

class Snake(object):
	def __init__(self):
		self.pos = [500, 500]
		self.body = deque([[500, 500],[500,500],[500, 500]])
		self.dir = 'RIGHT'


	def Change(self, direc):
		if direc == 'RIGHT' and not self.dir == 'LEFT':
			self.dir = 'RIGHT'
		elif direc == 'LEFT' and not self.dir == 'RIGHT':
			self.dir = 'LEFT'
		elif direc == 'UP' and not self.dir == 'DOWN':
			self.dir = 'UP'
		elif direc == 'DOWN' and not self.dir == 'UP':
			self.dir = 'DOWN'


	def Move(self, food):
		if self.dir == 'RIGHT':
			self.pos[0] += 20
		elif self.dir == 'LEFT':
			self.pos[0] -= 20
		elif self.dir == 'UP':
			self.pos[1] -= 20
		elif self.dir == 'DOWN':
			self.pos[1] += 20

		self.body.appendleft(self.pos[:])

		if self.pos == food:
			return True

		self.body.pop()
		return False


	def Check(self):
		if self.pos[0] > 1000 or self.pos[0] < 0:
			return True

		elif self.pos[1] > 1000 or self.pos[1] < 0:
			return True

		return any(map(lambda x: x == self.pos, itertools.islice(self.body, 4, None)))



class Food(object):
	def __init__(self):
		self.pos = [random.randrange(1,50) * 20, random.randrange(1, 50) * 20]
		self.food = True


	def SpawnFood(self):
		if not self.food:
			self.pos =  [random.randrange(1,50) * 20, random.randrange(1, 50) * 20]
			self.food = True

		return self.pos

class Game():
	# game engine
	def start_screen(self):
		pass
	
	
	def gameover_screen(self):
		pass


	def auto_play(self):
		pass


	def Play(self):
		window = pygame.display.set_mode((1000,1000))
		fps = pygame.time.Clock()
		pygame.display.set_caption('SNEK')
		score, snake, food = 0, Snake(), Food()
		time.sleep(.5)
		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT and snake.dir != 'RIGHT':
						snake.Change('RIGHT')
					elif event.key == pygame.K_LEFT and snake.dir != 'LEFT':
						snake.Change('LEFT')
					elif event.key == pygame.K_UP and snake.dir != 'UP':
						snake.Change('UP')
					elif event.key == pygame.K_DOWN and snake.dir != 'DOWN':
						snake.Change('DOWN')
					else:
						continue
					break
			foodpos = food.SpawnFood()

			if snake.Move(foodpos):
				score += 1
				food.food = False


			if snake.Check():
				self.GameOver(score)

			window.fill(pygame.Color(0,0,0))
			pygame.draw.rect(window, pygame.Color(255,0,0), pygame.Rect(food.pos[0],food.pos[1],20,20))

			for pos in snake.body:
				pygame.draw.rect(window, pygame.Color(0,255,0), pygame.Rect(pos[0],pos[1],20,20))

			pygame.display.flip()
			fps.tick(15 + score // 2)

	def GameOver(self, score):
		print(score)
		pygame.quit()
		sys.exit()

if __name__ == '__main__':
	Game().Play()

