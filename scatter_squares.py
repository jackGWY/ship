import matplotlib.pyplot as plt

x_values=list(range(1,101))
y_values=[x**2 for x in x_values]
#plt.scatter(x_values,y_values,c='red',edgecolor='none',s=40)#s是点的大小
#plt.scatter(x_values,y_values,c=(0,0,0.8),edgecolor='none',s=40)#s是点的大小,c配置为淡蓝色
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)
#坐标越大颜色越深

#设置图标标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记大小
plt.tick_params(axis='both',which='major',labelsize=14)
#设置每个坐标的取值范围
#plt.axis(0, 1100, 0, 1100000)

#自动保存图标到文件，并且减除空白区域
plt.savefig('squares_plot.png',bbox_inches='tight')
plt.show()