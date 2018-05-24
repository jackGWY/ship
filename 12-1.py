import sys
import pygame

def run_game():
	pygame.init()
	screen=pygame.display.set_mode((1000,600))

	#开始游戏主循环
	bg_color=(0,0,230)
	while True:
		#监视视频事件和鼠标事件
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
		screen.fill(bg_color)

		pygame.display.flip()

run_game()

