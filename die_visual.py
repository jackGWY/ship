from die import Die
import pygal

die=Die()
results=[]
for roll_num in range(100):
	result=die.roll()
	results.append(result)

#分析结果
frequencies=[]#装的出现次数
for value in range(1,die.num_sides+1):
	frequency=results.count(value)
	#count用来统计
	frequencies.append(frequency)
#对结果可视化
hist=pygal.Bar()
hist.title="Results of rolling ine D6 1000 times"
hist.x_labels=['1','2','3','4','5','6']
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')
#print(frequencies)
