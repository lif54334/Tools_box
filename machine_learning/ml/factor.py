#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   factor.py

@Time    :   2018/11/22 8:24

@Desc    :

'''

import numpy as np #导入numpy库
import pandas as pd #导入pandas库
from math import sqrt #导入求根函数sqrt
inputfile='../ml/data/site2.xlsx' #原始数据文件
outputfile="cite_out.xlsx" #输出文件
X=pd.read_excel(inputfile, index_col='id') #以city为索引列读取原文件
X1=(X-X.mean())/X.std() # 0均值规范化
print("0均值规范矩阵")
print(X1)
print("相关系数矩阵")
C=X1.corr()
print(C)

import numpy.linalg as nlg #导入nlg函数，linalg=linear+algebra
eig_value,eig_vector=nlg.eig(C) #计算特征值和特征向量
eig=pd.DataFrame() #利用变量名和特征值建立一个数据框
eig['names']=X.columns#列名
eig['eig_value']=eig_value#特征值

print("特征值特征矩阵")
print(eig)
for k in range(1,8): #确定公共因子个数
    # print(eig['eig_value'][k-1].sum())
    print("第%s个数的值为%.2f" % (k, eig['eig_value'][k-1] / eig['eig_value'][0:4].sum()))
    if eig['eig_value'][:k].sum()/eig['eig_value'].sum()>=0.99: #如果解释度达到99%, 结束循环
        print(k)
        break
col0=list(sqrt(eig_value[0])*eig_vector[:,0]) #因子载荷矩阵第1列
col1=list(sqrt(eig_value[1])*eig_vector[:,1]) #因子载荷矩阵第2列
col2=list(sqrt(eig_value[2])*eig_vector[:,2]) #因子载荷矩阵第3列
col3=list(sqrt(eig_value[3])*eig_vector[:,3]) #因子载荷矩阵第4列
A=pd.DataFrame([col0,col1,col2,col3]).T #构造因子载荷矩阵A
A.columns=['ll1','ll2','ll3','ll4'] #因子载荷矩阵A的公共因子
print("因子载荷矩阵")
print(A)
h=np.zeros(8) #变量共同度，反映变量对共同因子的依赖程度，越接近1，说明公共因子解释程度越高，因子分析效果越好
D=np.mat(np.eye(8))#特殊因子方差，因子的方差贡献度 ，反映公共因子对变量的贡献，衡量公共因子的相对重要性
# print("方差贡献")
# print(D)
A=np.mat(A) #将因子载荷阵A矩阵化
for i in range(8):
    a=A[i,:]*A[i,:].T #A的元的行平方和
    h[i]=a[0,0] #计算变量X共同度,描述全部公共因子F对变量X_i的总方差所做的贡献，及变量X_i方差中能够被全体因子解释的部分
    # print(h)
    D[i,i]=1-a[0,0] #因为自变量矩阵已经标准化后的方差为1，即Var(X_i)=第i个共同度h_i + 第i个特殊因子方差

from numpy import eye, asarray, dot, sum, diag #导入eye,asarray,dot,sum,diag 函数
from numpy.linalg import svd #导入奇异值分解函数
def varimax(Phi, gamma = 1.0, q =20, tol = 1e-6): #定义方差最大旋转函数
    p,k = Phi.shape #给出矩阵Phi的总行数，总列数
    R = eye(k) #给定一个k*k的单位矩阵
    d=0
    for i in range(q):
        d_old = d
        Lambda = dot(Phi, R)#矩阵乘法
        u,s,vh = svd(dot(Phi.T,asarray(Lambda)**3 - (gamma/p) * dot(Lambda, diag(diag(dot(Lambda.T,Lambda)))))) #奇异值分解svd
        R = dot(u,vh)#构造正交矩阵R
        d = sum(s)#奇异值求和
        if d_old!=0 and d/d_old < 1 + tol:
            break
    return dot(Phi, R)#返回旋转矩阵Phi*R

rotation_mat=varimax(A)#调用方差最大旋转函数
rotation_mat=pd.DataFrame(rotation_mat)#数据框化
print(rotation_mat)

X1=np.mat(X1) #矩阵化处理
factor_score=(X1).dot(A) #计算因子得分
factor_score=pd.DataFrame(factor_score)#数据框化
factor_score.columns=['f1','f2','f3','f4'] #对因子变量进行命名
# factor_score.to_excel(outputfile)#打印输出因子得分矩阵
print(factor_score)
