#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   myfeatyres.py

@Time    :   2018/10/3 14:41

@Desc    :

'''
import sys
from imp import reload

from feature_selector import FeatureSelector
import pandas as pd
import numpy as np
import xlrd
import scipy.stats as stats
import xlsxwriter



def test():
    train = pd.read_excel('../data/menori.xlsx')
    train_labels = train["nums"]
    print(train.head())
    train = train.drop(columns=["nums"])
    fs = FeatureSelector(data=train, labels=train_labels)
    fs.identify_collinear(correlation_threshold=0.98)
    correlated_features = fs.ops['collinear']
    print(correlated_features)

def pearson():
    workbook = xlsxwriter.Workbook("men.xlsx")
    worksheet = workbook.add_worksheet()
    zimu=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    names=list()
    data = pd.read_excel("../data/menori.xlsx")  # 读取数据，指定“日期”列为索引列
    hang=list(data.columns)
    # print(hang)
    y=data["nums"]
    try:
        for name in hang:
            x=data[name]
            r, p = stats.pearsonr(x, y)
            if (float(abs(r)))>=0.90 and float(p)<=0.05:
                print("数量和 %s的相关系数是%.4f,显著性水平是%.4f"%(name,r,p))
                names.append(name)
            else:
                pass
    except:
        pass




def main():
    # test()
    pearson()

if __name__ == '__main__':
    main()