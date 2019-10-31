#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   ciyun.py

@Time    :   2018/9/27 18:23

@Desc    :

'''

"""
@author:FLY
@software:PyCharm
@time:2017/08/24
"""
import pickle
from os import path
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
text = ''
stpwds=list()
with open("stopwords.txt","r",encoding='utf-8') as fstp:
    print("读取禁用词")
    for line in fstp.readlines():
        line = line.strip('\n')
        stpwds.append(line)
with open('jiakang.txt', 'r', encoding='utf8') as fin:
    for line in fin.readlines():
        line = line.strip('\n')
# sep’.join（seq）以sep作为分隔符，将seq所有的元素合并成一个新的字符串
text += ' '.join(jieba.cut(line))
backgroud_Image = plt.imread('ciyun3.jpg')
print('加载图片成功！')
'''设置词云样式'''
wc = WordCloud(
    stopwords=stpwds,
    background_color='white',# 设置背景颜色
    mask=backgroud_Image,# 设置背景图片
    font_path='C:\Windows\Fonts\STZHONGS.TTF',  # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
    max_words=50, # 设置最大现实的字数
    max_font_size=150,# 设置字体最大值
    random_state=5# 设置有多少种随机生成状态，即有多少种配色方案
)
wc.generate_from_text(text)
print('开始加载文本')
#改变字体颜色
img_colors = ImageColorGenerator(backgroud_Image)
#字体颜色为背景图片的颜色
wc.recolor(color_func=img_colors)
# 显示词云图
plt.imshow(wc)
# 是否显示x轴、y轴下标
plt.axis('off')
plt.show()
# 获得模块所在的路径的
# d = path.dirname(__file__)
# # os.path.join()：  将多个路径组合后返回
# wc.to_file(path.join(d, "h11.jpg"))
print('生成词云成功!')

