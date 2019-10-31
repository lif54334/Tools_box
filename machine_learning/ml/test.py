#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   oa_data.py

@Time    :   2018/11/23 17:59

@Desc    :

'''
import numpy as np

def rank(x):
    y = sorted(x)
    num = list()
    for i in y:
        out = x.index(i) + 1
        print(out)
        num.append(out)
    print(num)
    return num

x = [2, 1, 4, 5, 7, 3, 6]
result = rank(x)