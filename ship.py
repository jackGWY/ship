import pygame
from pygame.sprite import Sprite 

class Ship(Sprite):
	def __init__(self,ai_settings,screen):
		#初始化飞船并设置初试位置
		super(Ship,self).__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		#加载飞船图像并且获取他的外界矩形
		self.image=pygame.image.load('images/ship_new.jpg')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()

		#将每艘飞船放在屏幕底部中央
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom

		#在飞船属性center中存储小数值
		self.center=float(self.rect.centerx)


		#移动标志
		self.moving_right=False
		self.moving_left=False
	def update(self):
		#根据移动标志移动飞船位置
		#更新飞船的center值，而不是rect
		if self.moving_right and self.rect.right<self.screen_rect.right:
			#self.rect.centerx+=1
			self.center+=self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left>0:
			#self.rect.centerx-=1
			self.center-=self.ai_settings.ship_speed_factor
		#根据self.center的值跟新rect对象
		#self.rect.centerx 将只存储self.center 的整数部分，
		# 但对显示飞船而言， 这问题不大
		self.rect.centerx=self.center

	def blitme(self):
		#在指定位置绘制飞船
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		#让飞船在屏幕中居中
		self.center=self.screen_rect.centerx


		