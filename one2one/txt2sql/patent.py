#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   patent.py

@Time    :   2019/3/18 15:36

@Desc    :

'''
import re

import pymysql


def read(path):
    with open(path,'r',encoding='utf8')as f:
        lines=f.readlines()
        nums=len(lines)
        print(nums)
        # print(re.search(r'(\d+)、(.*)', line))
        contents=list()
        for i in range(0,nums,4):
            content = []
            title=lines[i].strip('\n').split('、')[1]
            abs=lines[i+1].strip('\n').split('：')[1]
            time=lines[i+2].strip('\n').split('：')[1]
            person=lines[i+3].strip('\n').split('：')[1]
            content.append(title)
            content.append(abs[0:14000])
            content.append(time[0:4])
            content.append(person[0:100])
            contents.append(content)
    # print(contents)
    return (contents)

def creat(name):
    db = pymysql.connect("localhost", "root", "1234", "xian")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    table_name = name
    sql = "show tables;"
    cursor.execute(sql)
    tables = [cursor.fetchall()]
    table_list = re.findall('(\'.*?\')',str(tables))
    table_list = [re.sub("'",'',each) for each in table_list]
    if table_name in table_list:
        print("已存在")        #存在返回1
    else:
        print("未存在")
        cursor.execute("CREATE TABLE %s(title varchar(2000),abs varchar (14000),time int(10),person varchar (100))" % table_name)


def insert(data,name):
    table_name=name
    values=[]
    for items in data:
        values.append((items[0],items[1],items[2],items[3]))
        # print(values)
    # print(values)
    print(len(values))
    db = pymysql.connect("localhost", "root", "1234", "xian")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    cursor.executemany("INSERT INTO %s values(%%s,%%s,%%s,%%s)"%(table_name),values)
    db.commit()
    cursor.close()


if __name__ == '__main__':
    name='zl_light'
    path="light2.txt"
    list=read(path)
    creat(name)
    insert(list,name)