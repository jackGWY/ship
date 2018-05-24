import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

#执行API并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Status code:",r.status_code)#200状态码表示请求成功

#将API存储在一个变量中
respose_dict=r.json()
print("totle repositories:",respose_dict['total_count'])

#探索有关数据仓库的信息
repo_dicts=respose_dict['items']
print("Number of items:",len(repo_dicts))
names,plot_dicts=[],[]
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	plot_dict={
	'value':repo_dict['stargazers_count'],
	'label':repo_dict['description'],
	'xlink':repo_dict['html_url'],
	}
	plot_dicts.append(plot_dict)

	#stars.append(repo_dict['stargazers_count'])

#可视化
my_style=LS('#333366',base_style=LCS)
my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.title_font_size=24
my_config.label_font_size=14
my_config.major_label_font_size=18
my_config.truncate_label=15#设置项目名15个字符
my_config.show_y_guides=False#隐藏水平线
my_config.width=1000

chart=pygal.Bar(my_config,style=my_style)
chart.title='Most-Starred Python Projects on GitHub'
chart.x_labels=names

chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')



#print("\nKeys:",len(repo_dict))
#for key in sorted(repo_dict.keys()):
	#print(key)
