import re
import os
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np


def remove_non_alpha_chars(string):
    pattern = r'[^a-zA-Z]'
    return re.sub(pattern, '', string)


def get_file_paths(folder_path):
    txt_file_paths = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder_path)
                txt_file_paths.append('OMIGA-helper/'+relative_path)

    return txt_file_paths

all_letters = ['a', 'o', 'e', 'i', 'u', 'v', 'ang', 'ong', 'eng', 'ing', 'ung', 'vng', \
    'ka', 'ko', 'ke', 'ki', 'ku', 'kv', 'kang', 'kong', 'keng', 'king', 'kung', 'kvng', \
    'da', 'do', 'de', 'di', 'du', 'dv', 'dang', 'dong', 'deng', 'ding', 'dung', 'dvng', \
    'ta', 'to', 'te', 'ti', 'tsu', 'tv', 'tang', 'tong', 'teng', 'ting', 'tung', 'tvng', \
    'za', 'zo', 'ze', 'zi', 'zu', 'zv', 'zang', 'zong', 'zeng', 'zing', 'zung', 'zvng', \
    'sa', 'so', 'se', 'si', 'su', 'sv', 'sang', 'song', 'seng', 'sing', 'sung', 'svng', \
    'ga', 'go', 'ge', 'gi', 'gu', 'gv', 'gang', 'gong', 'geng', 'ging', 'gung', 'gvng', \
    'na', 'no', 'ne', 'ni', 'nu', 'nv', 'nang', 'nong', 'neng', 'ning', 'nung', 'nvng', \
    'ma', 'mo', 'me', 'mi', 'mu', 'mv', 'mang', 'mong', 'meng', 'ming', 'mung', 'mvng', \
    'ba', 'bo', 'be', 'bi', 'bu', 'bv', 'bang', 'bong', 'beng', 'bing', 'bung', 'bvng', \
    'pa', 'po', 'pe', 'pi', 'pu', 'pv', 'pang', 'pong', 'peng', 'ping', 'pung', 'pvng', \
    'ra', 'ro', 're', 'ri', 'ru', 'rv', 'rang', 'rong', 'reng', 'ring', 'rung', \
    'ya', 'yo', 'ye', 'yi', 'yang', 'yong', 'ying', \
    'wa', 'we', 'wi', 'wang', 'weng', \
    'ha', 'ho', 'he', 'hi', 'hu', 'hv', 'hang', 'hong', 'heng', 'hing', 'hung', 'hvng', \
    'la', 'lo', 'le', 'li', 'lu', 'lv', 'lang', 'long', 'leng', 'ling', 'lung', 'lvng']

reading = ''
index = 0
i = ''
list = []
stats = {}
file_list = []
folder_path = "/Users/yuan/Documents/python/OMIGA-helper"
paths = get_file_paths(folder_path)
for passages in paths:
    with open('{0}'.format(passages), "r") as file:
        text = file.read()
        text = remove_non_alpha_chars(text)
        text = text.lower()
        while index < len(text):
            i = text[index]
            reading = reading + i
            if reading in all_letters:
                try:
                    if text[index+1] + text[index+2] == 'ng':
                        reading = reading + text[index+1] + text[index+2] 
                        list.append(reading)
                        reading = ''
                        index += 2
                    else:
                        list.append(reading)
                        reading = ''
                except:
                    list.append(reading)
                    reading = ''
            if reading not in all_letters and len(reading) > 4:
                reading = ''
            index += 1
        print('Reading: {0}'.format(passages))

for k in all_letters:
    count = list.count(k)
    stats[k] = round(count / len(list) * 100,2)

stats_list = []

for m in stats:
    stats_list.append(stats[m])
    print('{0} : {1}%'.format(m, stats[m]))

print(stats_list)
# 创建柱状图
fig, ax = plt.subplots(figsize=(12, 8))  # 设置图形大小

# 计算柱子的位置
bar_positions = np.arange(len(all_letters))

ax.bar(bar_positions, stats_list, color='b')

'''
for i, value in enumerate(stats_list):
    ax.text(i, value + 1, str(value), ha='center')
'''

# 设置坐标轴标签和标题
ax.set_xlabel('Letters')
ax.set_ylabel('Percentage')
ax.set_title('OMIGA Letters Stats')

ax.set_ylim(bottom=0)

ax.set_xticks(bar_positions)
ax.set_xticklabels(all_letters, rotation=90)

ax.tick_params(axis='x', labelrotation=90, labelsize=5)
ax.tick_params(axis='y', labelsize=5)

# 显示图形
plt.show()