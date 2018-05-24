import matplotlib.pyplot as plt 
from random_work import RandomWalk
while True:
	rw=RandomWalk(50000)#带参数构造方法
	rw.fill_walk()
	#设置绘制窗口的尺寸,分辨率
	plt.figure(dpi=128,figsize=(10,6))

	point_numbers=list(range(rw.num_points))
	plt.scatter(rw.x_values,rw.y_values,
		c=point_numbers,cmap=plt.cm.Blues,
		edgecolor='none',s=1)#注意可以引用另一个文件的变量
	#突出起点和终点
	plt.scatter(0,0,c='green',edgecolor='none',s=100)
	plt.scatter(rw.x_values[-1],rw.y_values[-1],
		c='red',edgecolor='none',s=100)
	#隐藏坐标轴
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	plt.show()

	keep_running=input("make another walk?(y/n):")
	if keep_running=='n':
		break
