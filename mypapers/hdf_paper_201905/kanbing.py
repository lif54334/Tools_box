#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   kanbing.py

@Time    :   2019/9/29 13:21

@Desc    :

'''
import json
import random
import re
import time
from collections import Counter

import pkuseg

import pymysql
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# db = pymysql.connect("localhost", "root", "1234", "hdf")
# cursor = db.cursor()
# content_dict=dict()
# try:
#     cursor.execute('SELECT type,disease_tag,content from kb where type="不孕不育"')
#     db.commit()
#     results = cursor.fetchall()
#     for item in results:
#         type=item[0]
#         tag=item[1]
#         txt=item[2]
#         if tag in content_dict.keys():
#             content_dict[tag].append(txt)
#         else:
#             content_dict[tag]=[]
# except Exception as e:
#     print(e)
#     print("Error: unable to fetch data")
# db.close()
# print(len(content_dict.keys()))
# json_str = json.dumps(content_dict, ensure_ascii=False, indent=4)
# with open('content_dict.json', 'w', encoding='utf8') as json_file:
#     json_file.write(json_str)

seg_dict=dict()
with open('content_dict.json','r',encoding='utf8') as load_f:
    disease = json.load(load_f)
for key in disease:
    content=disease[key]
    long_content = "".join(content)
    seg = pkuseg.pkuseg(model_name='../doctor/modle/')  # 程序会自动下载所对应的细领域模型
    text = seg.cut(long_content)  # 进行分词
    seg_dict[key]=[Counter(text)]
json_str = json.dumps(seg_dict,ensure_ascii=False,indent=4)
with open('seg_dict.json', 'w',encoding='utf8') as json_file:
    json_file.write(json_str)