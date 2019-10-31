# -*- coding: utf-8 -*-
"""
@software: PyCharm
@file: addjson2.py
@time: 2018/6/23 17:05 
"""
import logging.handlers
import os
import json
from collections import Counter

# def log():
#     logger = logging.getLogger()
#     logger.setLevel(logging.INFO)
#     fmt = logging.Formatter('%(filename)s-%(asctime)s---：%(message)s')
#     fh = logging.FileHandler('log.txt', encoding='utf-8')
#     sh = logging.StreamHandler()
#     sh.setFormatter(fmt)
#     fh.setFormatter(fmt)
#     logger.addHandler(fh)
#     logger.addHandler(sh)
#     return logger

#     lg = log()
#     lg.info("日志模板")

def jsonmerge(path1,path2):
    file1 = open(path1, "r",encoding='utf8')
    file2 = open(path2, "r",encoding='utf8')
    json1 = json.load(file1)
    json2 = json.load(file2)
    print("json1: ", json1)
    print("json2: ", json2)
    dict = {}
    for key in json1.keys():
        dict[key] = list(json1[key])
    for key in json2.keys():
        if key in dict:
    # append
            for v in json2[key]:
              if not v in dict[key]:
                 dict[key].append(v)
        else:
          dict[key] = list(json2[key])

    print(dict)
    json.dump(dict, open("true3.json", "w", encoding="utf-8"), ensure_ascii=False)

if __name__ == "__main__":
    p1=r"true1.json"
    p2=r"true2.json"
    jsonmerge(p1,p2)
