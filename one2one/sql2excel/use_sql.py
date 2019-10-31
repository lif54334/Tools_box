#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   use_sql.py

@Time    :   2019/3/19 20:21

@Desc    :

'''

import itertools

import numpy
from pyecharts import Line
from pypinyin import lazy_pinyin, pinyin
import pymysql
import re

def use_data(sql):
    db = pymysql.connect("localhost", "root", "1234", "xian")
    cursor = db.cursor()
    values = list()
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            value = dict()
            value["nums"] = list(row)[0]
            value["time"] = list(row)[1]
            value["theme"] = list(row)[2]
            values.append(value)
    except Exception as e:
        print(e)
        print("Error: unable to fetch data")
    return values
    db.close()

def use_dict(data):
    time=list()
    theme=list()
    for items in data:
        time.append(items["time"])
        theme.append(items["theme"])
    time=(list(set(time)))
    time.sort()
    time_nums=len(time)
    theme=(list(set(theme)))
    theme.sort()
    theme_nums=len(theme)

    nums = numpy.zeros((theme_nums, time_nums)).astype('int64')
    for items in data:
        nums[theme.index(items["theme"]),time.index(items["time"])]=items["nums"]
    return time,nums

def picture(table,time,data):
    # print(time)
    attr = time
    line = Line(str(table+"发展趋势"),background_color = 'white')
    # print("theme shape %s"%(data.shape[0]))
    for i in range(0,data.shape[0]):
        line.add("第%s主题"%(i), attr, data[i].tolist(),is_random=True, is_label_show=True,is_smooth=False)
        # print(data[i].tolist())
    line.use_theme("vintage")
    path=table+".html"
    line.render(path)

def main():
    table="light"
    sql=("SELECT COUNT(theme) as nums,time,theme  FROM  %s  GROUP BY theme,time"%(table))
    data=use_data(sql)
    time,nums=use_dict(data)
    picture(table,time,nums)


if __name__ == '__main__':
    main()