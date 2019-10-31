#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   nerloss_map.py

@Time    :   2018/8/3 20:34

@Desc    :

'''
import re
import matplotlib.pyplot as plt
import numpy as np


def readlog(inpath):
    with open("train.log",'r',encoding='utf-8')as lf:
        lines=lf.readlines()
        for line in lines:
            flag=re.findall(r"iteration",line)
            if flag:
                try:
                    iteration=re.findall(r"iteration:(.+?) step",line)
                    step=re.findall(r"step:(.+?)/",line)
                    nerloss=re.findall(r"NER loss: (.+)",line)
                    keynum="No."+str(iteration[0])
                    lossnum=nerloss[0]
                    #print(lossnum)
                    losslist.append(lossnum)
                    #print(iteration,step,nerloss)
                except:
                    print("null")
                    continue
            else:
                continue
    #print(losslist)
    #print(losslist)
    return losslist

def map(array):
    nums=len(array)
    print(nums)
    x_values=list(range(0,nums))
    y_values=array
    plt.scatter(x_values, y_values, s=10)
    plt.tick_params(axis='both', which='major', labelsize=14)
    #plt.axis([0,100, 0, 0.2])
    #print(x_values,y_values)
    plt.show()

def test():
    x = list(range(1, 1001))
    y = [x ** 2 for x in x]
    plt.scatter(x, y, s=200)
    # 设置标题并加上轴标签
    plt.title("Squares Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.xlabel("Square of Value", fontsize=14)

    # 设置刻度标记的大小
    plt.tick_params(axis='both', which='major', labelsize=14)

    # 设置每个坐标的取值范围
    plt.axis([0, 1000, 0,0.5])
    plt.show()

if __name__=='__main__':
    workpath='../matlab/'
    losslist=list()
    lossdict=dict()
    llist=readlog(workpath)
    nums=len(llist)%100
    for n in range(0,nums):
        mylist=[]
        mylist=llist[(n*100):((n+1)*100)]
        map(mylist)
    # test()