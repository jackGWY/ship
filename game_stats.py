class GameStats():
	#跟踪游戏的统计信息
	def __init__(self,ai_settings):
		#初始化统计信息
		self.ai_settings=ai_settings
		self.reset_stats()
		#游戏启动时处于活动状态
		self.game_active=False
		#任何情况不应该重置最高分
		#self.high_score=self.get_high_score()
		self.high_score=0
	def reset_stats(self):
		#初始化在游戏运行期间可能的统计信息
		self.ship_left=self.ai_settings.ship_limit
		self.score=0
		self.level=1

	def get_high_score(self):
		filename='high_score.txt'
		try:
			with open(filename) as f_obj:
				lines=f_obj.readlines()
		except FileNotFoundError:
			msg="sorry,the file "+filename+" does not exitst."
			print(msg)
		else:
			result_string=''
			for line in lines:
				result_string+=line.strip()
			return int(result_string)
