#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   test2.py

@Time    :   2019/9/19 17:45

@Desc    :

'''

list1=['沪BE3517', '沪DD4377旧', '沪BK4870']
list2=['沪BE351', '沪DD4377', '沪BK487']
c=[]
for i in list2:
    for j in list1:
        if i in j:
            c.append(i)
        else:
            pass
print(c)