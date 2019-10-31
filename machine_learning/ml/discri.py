#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   discri.py

@Time    :   2018/11/16 19:01

@Desc    :

'''
import pandas as pd
import numpy as np
from numpy import *


def main():
    data = pd.read_excel("../ml/data/gecao.xlsx")
    results=list()
    for i in data.index.values:  # 获取行号的索引，并对其进行遍历：
        # 根据i来获取每一行指定的数据 并利用to_dict转成字典
        row_data = data.ix[i]
        input=[[row_data[0]],[row_data[1]]]
        result=distance(input)
        results.append(result)
    print(results)
    # x =mat([[100.0],[18.0]])
    # distance(x)


def distance(x):
    data = pd.read_excel("../ml/data/gecao.xlsx")
    # print(data.head)
    X1 = list()
    X2 = list()
    # print(data["revenue"])
    X1 = [list(data["revenue"][0:12]), list(data["size"][0:12])]
    X2 = [list(data["revenue"][12:]), list(data["size"][12:])]
    # print("===X1====")
    # print(X1)
    # print("===X2====")
    # print(X2)
    X1=np.array(X1)
    X2=np.array(X2)
    u1=mat([[110.225],[20.26666667]])
    u2=mat([[87.4],[17.63333333]])

    m1=np.cov(X1)
    m2=np.cov(X2)
    # print("====m1,m2====")
    # print(m1,m2)
    m1=mat(m1)
    m2=mat(m2)
    n1=m1.I
    n2=m2.I
    n1=mat(n1)
    n2=mat(n2)
    # print("===n1,n2=====")
    # print(n1,n2)
    # print("===mat(x-u2)).T=====")
    # print((mat(x-u2)).T)
    # print("====(mat(x-u2)).T)*n2*(mat(x-u2))====")
    # print(((mat(x-u2)).T)*n2*(mat(x-u2)))
    # print("====((mat(x-u1)).T)*n1*(mat(x-u1))======")
    # print(((mat(x-u1)).T)*n1*(mat(x-u1)))
    model=((mat(x-u2)).T)*n2*(mat(x-u2))-((mat(x-u1)).T)*n1*(mat(x-u1))
    # print("最终输出结果%s" %model)
    if model[0][0]<=0:
        rtn=0
    else:
        rtn=1
    return rtn
if __name__ == '__main__':
    main()
