#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   clean.py

@Time    :   2019/3/18 17:14

@Desc    :

'''

# coding = utf-8
import re


def clearBlankLine():
    file1 = open('light.txt', 'r', encoding='utf-8') # 要去掉空行的文件
    file2 = open('light2.txt', 'w', encoding='utf-8') # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            if re.search(r'(标题（翻译）)：(.*)', line):
                continue
            if re.search(r'(摘要（翻译）)：(.*)', line):
                continue
            if re.search(r'(公开（公告）号)：(.*)', line):
                continue
            if re.search(r'(公开（公告）日)：(.*)', line):
                continue
            if re.search(r'(申请号)：(.*)', line):
                continue
            if re.search(r'(当前法律状态)：(.*)', line):
                continue
            if re.search(r'(描述信息)：(.*)', line):
                continue
            if re.search(r'(法律状态)：(.*)', line):
                continue
            if re.search(r'(法律状态公告日)：(.*)', line):
                continue
            if re.search(r'(状态效果)：(.*)', line):
                continue
            if re.search(r'(状态代码)：(.*)', line):
                continue
            file2.write(line)
    finally:
        file1.close()
        file2.close()


if __name__ == '__main__':
    clearBlankLine()