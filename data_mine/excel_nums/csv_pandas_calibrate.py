#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   csv_pandas_calibrate.py

@Time    :   2018/7/4 16:12

@Desc    :

'''
import numpy
import os
import pandas as pd
import numpy as np

def calibrate(path):
    files = os.listdir(path)
    for file in files:
        #print(file)
        with open (path+file,"r",encoding="utf-8") as csvf:
            data = pd.read_csv(csvf)
            # cols = data.columns
            # # num=len(cols)
            # # #print(num)
            str=data.ix[:,'usefulre']
            line = ("calibrate(%s,%.4f,%.4f,%.4f)" % ('usefulre', np.percentile(str, 95), np.median(str), np.percentile(str, 5)))
            with open('../num/test.txt',"a+") as txt:
            # print(file + '\n' + line)
                txt.write(file + '\n' + line+'\n')
            # for i in range(num):
            #     name=cols[i]
            #     print(name)
            #     str=data.ix[:, name]
            #     line=("calibrate(%s,%s,%s,%s)"%(name,np.percentile(str, 95),np.median(str),np.percentile(str, 5)))
            #     print(line)
            #     with open('../num/test.txt',"a+") as txt:
            #          txt.write(file+'  '+line+'\n')
def newtxt(dirs):
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    else:
        print("文件存在")

if __name__ == '__main__':
    path="F:/sql/fsqca/data/"
    # dirs="E:/kgqca/practice/num/test.txt"
    # newtxt(dirs)
    calibrate(path)