#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   oa_data.py

@Time    :   2018/11/16 12:26

@Desc    :

'''
import datetime
import random
import re
import string

import fool
import jieba
import pymysql
import requests
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from snownlp import SnowNLP
import lxml
import xlrd


app = Flask(__name__)
bootstrap = Bootstrap(app)
dresult = dict()
lresult = list()
conn = pymysql.connect(host='localhost', user='root', password='1234', db='web', charset='utf8')
cur = conn.cursor()
sql = "SELECT * FROM text"
cur.execute(sql)
u = cur.fetchall()


def main():
    for indata in u:
    # indata=u[5]
        Txtmine(indata)

def DtCalc(stTime, edTime):
    st=datetime.datetime.strptime(stTime, "%Y-%m-%d")
    ed=datetime.datetime.strptime(edTime, "%Y-%m-%d")
    rtn = ed -st
    rtn=re.findall(r"(.+?) days", str(rtn))
    return int(rtn[0])

def Txtmine(indata):
    result=dict()
    data = indata[6]
    title = indata[2]
    result["id"]=indata[0]
    # 内容的逻辑性（f15）
    count_en = count_dg = count_sp = count_zh = count_pu = 0
    s_len = len(data)
    for c in data:
        if c in string.ascii_letters:
            count_en += 1
        elif c.isdigit():
            count_dg += 1
        elif c.isspace():
            count_sp += 1
        elif c.isalpha():
            count_zh += 1
        else:
            count_pu += 1
    logic=round((100*count_pu/s_len),2)
    result["logic"]=logic

    # 完整性（f17）
    b61list=["当量","尺寸","距离","半径","杀伤","重量","小当量","弹头","核打击","B61","威力","精确度"]
    seg_list = jieba.cut(data)
    # seg_list=", ".join(seg_list)
    # print(seg_list)
    num=0
    for word in seg_list:
        # print(word)
        for target in b61list:
            # print(target)
            if word==target:
                num=num+1
            else:
                continue
    result["complete"]=num
    # 实时性（f18）
    puttime = indata[4]
    today="2018-12-01"
    rtn=DtCalc(puttime,today)
    result["time"]=rtn
    # 情感倾向词使用频率（f19）
    counts=data.count("！")+data.count("？")+data.count("?")+data.count("!")+data.count("—")+data.count("非")+data.count("极")+data.count("慑")+data.count("恐")
    # print(counts)
    result["e_counts"]=counts
    # 情感倾向词强度（f20）
    s = SnowNLP(data)
    senums=len(s.sentences)
    scores=0
    for sentence in s.sentences:
        snow=SnowNLP(sentence)
        scores=scores+snow.sentiments
        # intense=round(s.sentiments,4)
    # print(round(scores/senums,3))
    intense=round(scores/senums,3)
    if intense<=0.02:
        intense=0.842
    elif intense<=0.05:
        intense=0.765
    elif intense<=0.1:
        intense=0.644
    result["e_intense"]=intense
    # 字符错误率（f21）
    wrong=data.count("#")+data.count("&")+data.count("##")+data.count("&&")
    result["wrong"]=wrong
    # 精确性（f16）
    words, ners = fool.analysis(data)
    result["acc"]=len(ners[0])
    return result
    print(result)
if __name__ == '__main__':
    main()