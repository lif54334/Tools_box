#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   nums.py

@Time    :   2018/11/4 19:34

@Desc    :

'''

import re

import fool
import jieba
import numpy
import pymysql
import pandas as pd
import requests
from snownlp import SnowNLP

dresult=list()
# excelFile = r'text.xlsx'
# df = pd.DataFrame(pd.read_excel(excelFile))
# print(df["content"])
conn = pymysql.connect(host='localhost', user='root', password='1234', db='wwweb', charset='utf8')
cur = conn.cursor()
sql = "SELECT * FROM text"
cur.execute(sql)
u = cur.fetchall()
data = list(u)
data = [list(i) for i in data]
data = pd.DataFrame(data)
maxnum=list()
loclist=list()
peolist=list()
orglist=list()
for idta in data[6]:
    results = re.findall("(?isu)(https\://[a-zA-Z0-9\.\?/&\=\:]+)", idta)
    maxnum.append(len(results))
print(maxnum)
# print(max(loclist),max(orglist),max(peolist))
def Txtmine(indata):
    data = indata[6]
    title=indata[2]
    dresult["title"] = title
    dresult["article"] = data
    mylen = len(data)
    line_num = data.count("\n")
    """字数行数"""
    dresult["wordnums"] = mylen
    dresult["linenums"] = line_num
    """词频"""
    words = jieba.lcut(data)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        elif word.isdigit():
            continue
        else:
            rword = word
        counts[rword] = counts.get(rword, 0) + 1

    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    dresult["words"] = items[0:3]

    """情感"""
    s = SnowNLP(data)
    dresult["sentiments"] = s.sentiments
    """摘要"""
    s = SnowNLP(data.replace("不", ""))
    # print(s.keywords())
    swords = list()
    for word in s.keywords():
        if len(word) < 2:
            continue
        else:
            swords.append(word)
    dresult["keywords"] = swords
    summary = list(set(s.summary()))[:3:1]
    # print(summary)
    lines = ""
    for line in summary:
        # print(line)
        lines = lines + line + " //// "
    dresult["summary"] = lines
    """特征值"""
    values = [i for i in indata[7:]]
    dresult["val"] = values

    """超链接数目"""
    results = re.findall("(?isu)(https\://[a-zA-Z0-9\.\?/&\=\:]+)", data)
    dresult["urlnums"] = len(results)

    """错字检测"""
    r = requests.post("http://www.cuobiezi.net/api/v1/zh_spellcheck/json",
                      data={'content': '我最喜欢的就是元啊节吃汤圆。 ', 'check_mode': 'advanced', 'action': 'show'})

    """"""
    loc = 0
    org = 0
    peo = 0
    words, ners = fool.analysis(data)
    for ner in ners[0]:
        if ner[2] == "location":
            loc += 1
        elif ner[2] == "org":
            org += 1
        elif ner[2] == "person":
            peo += 1
        else:
            continue
    dresult["loc"] = loc
    dresult["org"] = org
    dresult["peo"] = peo

    # print(dresult)

    return dresult