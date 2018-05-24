
import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats 
from buttom import Buttom 
from scoreboard import Scoreboard 

def run_game():
	#初始化游戏并且创建一个屏幕对象
	pygame.init()
	ai_settings=Settings()

	screen=pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))

	pygame.display.set_caption("Alien Invation")
	#创建play按钮
	play_buttom=Buttom(ai_settings,screen,"Play")

	#创建一个用于存储统计信息的实例,并且创建积分牌

	stats=GameStats(ai_settings)
	sb=Scoreboard(ai_settings,screen,stats)

	#创建一艘飞船
	ship=Ship(ai_settings,screen)

	#创建一个用于存储子弹的编组
	bullets=Group()
	#外星人编组
	aliens=Group()
	#创建一个外星人
	#alien=Alien(ai_settings,screen)

	#创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)

	#开始游戏主循环
	while True:
		#监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,stats,sb,play_buttom,ship,
			aliens,bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,
				aliens,bullets)
			gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
			
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_buttom)

run_game() 



