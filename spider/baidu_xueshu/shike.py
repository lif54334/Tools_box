#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   shike.py

@Time    :   2019/5/28 13:23

@Desc    :

'''
import re
import simplejson
import csv

with open('test1.csv','a',newline='')as csv_file:
    # 获取一个csv对象进行内容写入
    writer=csv.writer(csv_file)
    writer.writerow(['车次','车站','时间1','时间2'])
    with open("shike.txt", "r", encoding="utf8")as f:
        lines = f.readlines()
        for line in lines:
            line2 = re.sub('\n', '\\n', line)
            p = simplejson.loads(line2)
            text=p["y"]
            for item in text:
                csv_text=list()
                number=item["CC"]
                station=item["ZM"]
                time1=item["TIMEA"]
                time2=item["TIMEB"]
                csv_text=[number,station,time1,time2]
                writer.writerow(csv_text)
