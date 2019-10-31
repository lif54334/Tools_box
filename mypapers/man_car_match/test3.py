#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   test3.py

@Time    :   2019/10/6 14:29

@Desc    :

'''
import json

no_time='2019-06-04沪EF8828'
no_time=str(no_time)
with open('man_time.json', 'r', encoding='utf8') as fileR:
    R = json.load(fileR)
    fileR.close()
if no_time in R.keys():
    print(no_time)
else:
    print("no")