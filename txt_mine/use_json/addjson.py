# -*- coding: utf-8 -*-
"""
@software: PyCharm
@file: addjson.py
@time: 2018/6/23 16:30 
"""
import logging.handlers
import os
import json

# def log():
#     logger = logging.getLogger()
#     logger.setLevel(logging.INFO)
#     fmt = logging.Formatter('%(filename)s-%(asctime)s---：%(message)s')
#     fh = logging.FileHandler('log.txt', encoding='utf-8')
# 
#     sh = logging.StreamHandler()
#     sh.setFormatter(fmt)
#     fh.setFormatter(fmt)
#     logger.addHandler(fh)
#     logger.addHandler(sh)
#     return logger

#     lg = log()
#     lg.info("日志模板")

def jsonmerge(path1,path2):
    file1 = open(path1, "rb")
    file2 = open(path2, "rb")
    json1 = json.load(file1)
    json2 = json.load(file2)
    print("json1: ", json1)
    print("json2: ", json2)
    merge = dict(json2, **json1)
    print("merge: ", merge)
    json.dump(merge, open("true_dictionary_sss.json", "w", encoding="utf-8"), ensure_ascii=False)

if __name__ == "__main__":
    p1=r"true_dictionary1.json"
    p2=r"true_dictionary2.json"
    jsonmerge(p1,p2)


