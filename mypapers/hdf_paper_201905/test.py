#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   test.py

@Time    :   2019/9/25 16:25

@Desc    :

'''
import re

url='http://www.haodf.com/zhuanjiaguandian/wsheyan_7958220582.htm'
com_id = re.match(".*(\_\\d+)", url)
print(com_id.group(1)[1:])