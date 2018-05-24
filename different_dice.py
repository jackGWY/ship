from die import Die
import pygal
#创建D6和D10
die_1=Die()
die_2=Die(10)

results=[]
for roll_num in range(50000):
	result=die_1.roll()+die_2.roll()
	results.append(result)

#分析结果
frequencies=[]#装的出现次数
max_result=die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):
	frequency=results.count(value)
	#count用来统计
	frequencies.append(frequency)
#对结果可视化
hist=pygal.Bar()
hist.title="Results of rolling D6+D10 50000 times"
hist.x_labels=[]
for i in range(2,17):
	hist.x_labels.append(str(i))


hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add('D6+D10',frequencies)
hist.render_to_file('different_dice.svg')
#print(frequencies)
