#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   factor2.py

@Time    :   2018/11/22 9:21

@Desc    :

'''

import numpy as np #导入numpy库
import pandas as pd #导入pandas库
from math import sqrt #导入求根函数sqrt
from sklearn.decomposition import FactorAnalysis
import numpy.linalg as nlg #导入nlg函数，linalg=linear+algebra
from numpy import *

def Find():
    inputfile='../ml/data/content2.xlsx' #原始数据文件
    outputfile="cite_out.xlsx" #输出文件
    data=pd.read_excel(inputfile, index_col='id') #以city为索引列读取原文件
    A=mat(data)
    print(A.I)
    C=data.corr()
    eig_value,eig_vector=nlg.eig(C) #计算特征值和特征向量
    eig=pd.DataFrame() #利用变量名和特征值建立一个数据框
    eig['names']=data.columns#列名
    eig['eig_value']=eig_value#特征值
    #
    print("特征值特征矩阵")
    print(eig)
    variance=list()
    result=list()
    for k in range(1,7): #确定公共因子个数
        # print(eig['eig_value'][k-1].sum())
        v_val=(eig['eig_value'][k-1] / eig['eig_value'][0:7].sum())
        print("第%s个变量的方差贡献为%.2f" % (k, v_val))
        variance.append(v_val)
        if eig['eig_value'][:k].sum()/eig['eig_value'].sum()>=0.99: #如果解释度达到99%, 结束循环
            break

    fa = FactorAnalysis(n_components=5)
    data_dim=fa.fit_transform(data)
    # print(variance)
    print("旋转后因子得分")
    print(data_dim)
    Y=mat(data_dim)
    X=(A.I)*Y
    print("因子载荷矩阵")
    print(X)
    for idata in data_dim:
        scores=0
        for i in range(0,4):
            score=idata[i]*variance[i]
            # print("第%s个因子得分为%s"%(i,score))
            scores+=score
            if i==3:
                # print(scores)
                result.append(scores)
    print("因子综合得分")
    print(result)

    """
    网站运营商资质（l1）
    网站运营商信誉度（l2）
    网站运营商类型（机构或个体）（l3）
    内容公开政策声明的明确性（l4）
    站点实体信息披露程度（l5）
    广告/商业性信息内容量（l6）
    第三方/权威方背书（l7）
    信息安全保障程度（l8）
    
    权重值
    5.98
    5.55
    6.04
    5.53
    5.44
    5.19
    5.88
    5.38
    
    最小二乘解
    x1	=	1.4846e+01   14.85
    x2	=	2.2722e+00   2.27
    x3	=	6.6161e-02   0.066
    x4	=	5.6746e-01   0.57
    
    """
    # fac_mat=mat(data_dim)
    # fac_coef=mat([[14.85],[2.27],[0.066],[0.57]])
    # fac_result=fac_mat*fac_coef
    # print("因子分析")
    # print(fac_result)
    # print("加权平均")
    # wei_coef=mat([[5.98],[5.55],[6.04],[5.53],[5.44],[5.19],[5.88],[5.38]])
    # wei_mat=mat(data)
    # wei_result=wei_mat*wei_coef
    # print(wei_result)
    # def rank(x):
    #     X=list()
    #     for h in x:
    #         X.append(h)
    #     y = sorted(X)
    #     num = list()
    #     for i in y:
    #         out = X.index(i) + 1
    #         # print(out)
    #         num.append(out)
    #     # print(num)
    #     return num
    # print(rank(fac_result))
    # print(rank(wei_result))

    """
    内容的逻辑性（f15）  
    精确性（f16）
    完整性（f17）
    实时性（f18）
    情感倾向词使用频率（f19）
    情感倾向词强度（f20）
    字符错误率（f21）
    5.15
    5.05
    5.32
    5.55
    5.99
    6.15
    6.09
    
    x1	=	-15.39
    x2	=	3.55
    x3	=	4.23
    x4	=	3.49
    x5	=	-5.66
    
    """
    fac_mat=mat(data_dim)
    fac_coef=mat([[-15.39],[3.55],[4.23],[3.49],[-5.66]])
    fac_result=fac_mat*fac_coef
    print("因子分析")
    print(fac_result)
    print("加权平均")
    wei_coef=mat([[5.15],[5.05],[5.32],[5.55],[5.99],[6.15],[6.09]])
    wei_mat=mat(data)
    wei_result=wei_mat*wei_coef
    print(wei_result)
    def rank(x):
        X=list()
        for h in x:
            X.append(h)
        y = sorted(X,reverse=True)
        num = list()
        for i in y:
            out = X.index(i) + 1
            # print(out)
            num.append(out)
        # print(num)
        return num
    print(rank(fac_result))
    print(rank(wei_result))