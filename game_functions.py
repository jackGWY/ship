import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien
def check_events(ai_settings,screen,stats,sb,play_buttom,ship,aliens,bullets):
	#响应按键和鼠标事件
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			

			sys.exit()
		elif event.type==pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)

		elif event.type==pygame.KEYUP:
			check_keyup_events(event,ship)
		elif event.type==pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y=pygame.mouse.get_pos()
			check_play_buttom(ai_settings,screen,stats,sb,play_buttom,ship,
				aliens,bullets,mouse_x,mouse_y)
def check_play_buttom(ai_settings,screen,stats,sb,play_buttom,ship,aliens,
	bullets,mouse_x,mouse_y):
	#玩家单击Play按钮开始游戏
	buttom_clicked=play_buttom.rect.collidepoint(mouse_x,mouse_y)
	if buttom_clicked and not stats.game_active:
		#重置settings中的游戏设置
		ai_settings.initialize_dynamic_settings()
		#隐藏光标
		pygame.mouse.set_visible(False)
		#重置游戏统计信息
		stats.reset_stats()
		stats.game_active=True
		#重置分牌图像
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_ships()

		#清空外心人列表和子弹列表
		aliens.empty()
		bullets.empty()
		#创建一群外心人，并让飞船居中
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()


def check_keydown_events(event,ai_settings,screen,ship,bullets):

	if event.key==pygame.K_RIGHT:
		ship.moving_right=True
	elif event.key==pygame.K_LEFT:
		ship.moving_left=True
	elif event.key==pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key==pygame.K_q:

		sys.exit()


def fire_bullet(ai_settings,screen,ship,bullets):
	#创建子弹，并将其加入bullets中
	if len(bullets)<ai_settings.bullets_allowed:
		new_bullet=Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)
		
		
def check_keyup_events(event,ship):
	if event.key==pygame.K_RIGHT:
		ship.moving_right=False
	elif event.key==pygame.K_LEFT:
		ship.moving_left=False	


def update_screen(ai_settings,screen,stats,sb,ship,
	aliens,bullets,play_buttom):
	#更新屏幕上的图像，并切换到新屏幕
	#每次循环都重新绘制图像
	screen.fill(ai_settings.bg_color)

	#在飞船和外星人后面重新绘制所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	#指定位置话飞船
	ship.blitme()
	aliens.draw(screen)
	#显示得分
	sb.show_score()
	#如果游戏处于非活动状态，就绘制play按钮
	if not stats.game_active:
		play_buttom.draw_buttom()

	#让最终绘制的屏幕可见
	pygame.display.flip()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
	#跟新子弹位置，并且消除消失的子弹
	#跟新子弹位置
	bullets.update()

	#删除已经消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)
	#检查是否有子弹击中万星人
	#如果这样，删除子弹和外星人
	check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,
		aliens,bullets)
	
def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,
	aliens,bullets):
#响应子弹和外星人发生的碰撞
	collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
	if collisions:
		for aliens in collisions.values():
			stats.score+=ai_settings.alien_points*len(aliens)
			sb.prep_score()
		check_high_score(stats,sb)
	if len(aliens)==0:
		#如果外星人别消灭就提高一个等级
		#删除现在所有子弹并且新建一群万星人,加快节奏

		bullets.empty()
		ai_settings.increase_speed()
		#提高等级
		stats.level+=1
		sb.prep_level()

		create_fleet(ai_settings,screen,ship,aliens)

def get_number_aliens_x(ai_settings,alien_width):
	#计算可容纳多少外星人
	available_space_x=ai_settings.screen_width -2*alien_width
	number_aliens_x=int(available_space_x/(2*alien_width))
	return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	#创建一个外星人并将其放在当前行
	alien=Alien(ai_settings,screen)
	alien_width=alien.rect.width
	alien.x=alien_width+2*alien_width*alien_number
	alien.rect.x=alien.x
	alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
	aliens.add(alien)


def create_fleet(ai_settings,screen,ship,aliens):
	#创建外星人群
	#创建一个外星人，并计算一行可以容纳多少外星人
	#外星人间距为外星人宽度
	alien=Alien(ai_settings,screen)
	
	number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows=get_number_rows(ai_settings,ship.rect.height,
		alien.rect.height)
	#创建外星人群
	#range()从1数到number_aliens_x
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			#创建一个 外星人并将其加入当前行
			create_alien(ai_settings,screen,aliens,alien_number,row_number)
		


def get_number_rows(ai_settings,ship_height,alien_height):
	#计算屏幕可以容纳多少人
	available_space_y=(ai_settings.screen_height - (3*alien_height) - ship_height)
	number_rows=int(available_space_y/(2*alien_height))
	return number_rows

def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
	#检查是佛有外星人位于屏幕边沿,
	#跟新所有外星人的位置
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
	#检查外星人和飞船之间的碰撞
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
	#检查是否外星人到低端
	check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)

def check_fleet_edges(ai_settings,aliens):
	#有外星人到达边沿就采取相应的措施
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break

def change_fleet_direction(ai_settings,aliens):
	#将外心人下移动，并且改变他们方向
	for alien in aliens.sprites():
		alien.rect.y+=ai_settings.fleet_drop_speed

	ai_settings.fleet_direction*=-1

def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):
    #响应被外星人撞到的飞船
    

    if stats.ship_left>0:
        stats.ship_left-=1
        #跟新积分牌
        sb.prep_ships()
        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        #创建一群外星人，并将飞船放到屏幕低端中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        #暂停
        sleep(2)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets):
	#检查是否有外星人到达屏幕低端
	screen_rect=screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom>=screen_rect.bottom:
			ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets)
			break
def check_high_score(stats,sb):
	#检查是否诞生了最高分
	if stats.score>stats.high_score:
		stats.high_score=stats.score
		#write_high_score(stats.score)
		sb.prep_high_score()
		#知道了最高分还要画出来
def write_high_score(score):
	filename='high_score.txt'
	with open(filename,'w') as f_obj:
		f_obj.write(str(score))




















