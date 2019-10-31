#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   huigui.py

@Time    :   2018/10/4 19:27

@Desc    :

'''

import pandas as pd
from math import sqrt
import matplotlib
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
from sklearn.linear_model import LinearRegression


def amira():
    data = pd.read_excel("unisexori.xlsx")
    dta = data["nums"]
    # dta=[318, 111, 998, 35, 533, 306, 428, 460, 592, 1795, 816, 1252, 1330, 786, 3318, 847, 1203, 954, 1283, 873, 945,
    #            2399, 744, 1528, 1116]
    dta = np.array(dta, dtype=np.float)

    dta = pd.Series(dta)
    dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2001', '2025'))
    dta.plot(figsize=(12, 8))
    plt.show()

    fig = plt.figure(figsize=(12, 8))
    ax1 = fig.add_subplot(111)
    diff1 = dta.diff(1)
    diff1.plot(ax=ax1)

    fig = plt.figure(figsize=(12, 8))
    ax2 = fig.add_subplot(111)
    diff2 = dta.diff(2)
    diff2.plot(ax=ax2)

    plt.show()
    dta = dta.diff(1)  # 我们已经知道要使用一阶差分的时间序列，之前判断差分的程序可以注释掉 //原文有错误应该是diff1= dta.diff(1)，而非dta= dta.diff(1)
    dta[0] = 0
    print(dta)
    mse1 = dta["2021":"2025"]
    print(mse1)
    fig = plt.figure(figsize=(12, 8))
    ax1 = fig.add_subplot(211)
    fig = sm.graphics.tsa.plot_acf(dta, lags=20, ax=ax1)
    ax2 = fig.add_subplot(212)
    fig = sm.graphics.tsa.plot_pacf(dta, lags=20, ax=ax2)
    plt.show()

    arma_mod = sm.tsa.ARMA(dta, (6, 2)).fit()
    print("求解最优值：=============", (arma_mod.aic, arma_mod.bic, arma_mod.hqic))
    resid = arma_mod.resid
    fig = plt.figure(figsize=(12, 8))
    ax1 = fig.add_subplot(211)
    fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=20, ax=ax1)
    ax2 = fig.add_subplot(212)
    fig = sm.graphics.tsa.plot_pacf(resid, lags=20, ax=ax2)
    plt.show()

    predict_dta = arma_mod.predict('2021', '2031', dynamic=True)
    print(predict_dta)
    mse2 = predict_dta["2021":"2025"]
    fig, ax = plt.subplots(figsize=(12, 8))
    ax = dta.ix['2000':].plot(ax=ax)
    fig = arma_mod.plot_predict('2021', '2031', dynamic=True, ax=ax, plot_insample=False)
    plt.show()
    print(mse1, mse2)
    math(mse1, mse2)


def multi():
    data = pd.read_excel("E:\\practice\\ml\\data\\test2.xlsx")
    font = {
        'family': 'SimHei'
    }
    matplotlib.rc('font', **font)

    pd.plotting.scatter_matrix(data[["nums", "x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11", "x12"]],
                   figsize=(10, 10), diagonal='kid')
    # data[["nums", "cost", "pep1","pep2","pebd"]].corr()
    x = data[["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11", "x12"]]
    y = data[["nums"]]
    lrModel = LinearRegression()
    # 训练模型
    lrModel.fit(x, y)
    # 预测
    result = list()
    for i in range(0, len(data["nums"])):
        indata = [
            [data["x1"][i], data["x2"][i], data["x3"][i], data["x4"][i], data["x5"][i], data["x6"][i], data["x7"][i],
             data["x8"][i], data["x9"][i], data["x10"][i], data["x11"][i], data["x12"][i]]]
        # print(indata)
        out = lrModel.predict(indata)[0][0]
        # print(out)
        result.append(out)
    # print(lrModel.predict([[624626.03,0.27,0.16,0.2]]))
    # 查看参数
    print(result)
    print(lrModel.coef_)
    # 查看截距
    print(lrModel.intercept_)
    print(lrModel.score(x, y))
    plt.title('回归')
    plt.plot(data["time"], data["nums"], color='red', label='真实值')
    plt.plot(data["time"], result, color='green', label='预测值')

    plt.legend()  # 显示图例
    plt.xlabel("时间")
    plt.ylabel("数值")
    plt.show()


def math(ma1, ma2):
    target = ma1
    prediction = ma2

    error = []
    for i in range(len(target)):
        error.append(target[i] - prediction[i])

    # print("Errors: ", error)
    # print(error)

    squaredError = []
    absError = []
    for val in error:
        squaredError.append(val * val)  # target-prediction之差平方
        absError.append(abs(val))  # 误差绝对值

    # print("Square Error: ", squaredError)
    print("Absolute Value of Error:  ", absError)

    print("MSE = %.2f" % (sum(squaredError) / len(squaredError)))  # 均方误差MSE

    print("RMSE = %.2f " % (sqrt(sum(squaredError) / len(squaredError))))  # 均方根误差RMSE
    print("MAE = %.2f" % (sum(absError) / len(absError)))  # 平均绝对误差MAE

    targetDeviation = []
    targetMean = sum(target) / len(target)  # target平均值
    for val in target:
        targetDeviation.append((val - targetMean) * (val - targetMean))
    # print("Target Variance = ", sum(targetDeviation) / len(targetDeviation))  # 方差

    # print("Target Standard Deviation = ", sqrt(sum(targetDeviation) / len(targetDeviation)))  # 标准差


def corr():
    excelFile = r'taobao.xlsx'
    df = pd.DataFrame(pd.read_excel(excelFile))
    # print(df)
    inde = (df.index)
    colo = list(df.columns)
    # print(colo)
    for name in colo[2::1]:
        cor, pva = stats.pearsonr(df[name], df["nums"])
        # relat =float(df["nums"].corr(df[name]))
        if cor >= 0.85 and pva <= 0.05:
            print("%s与nums的相关性是%.4f,显著性是%s" % (name, cor, pva))
        else:
            pass


def staml():
    data = pd.read_excel("test2.xlsx")
    x = data[["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11", "x12"]]
    y = data["nums"]
    print(data.head())
    X = sm.add_constant(x)
    res = sm.OLS(y, X).fit()
    print(res.params)
    print(res.summary)


def main():
    # amira()
    multi()
    # corr()
    # staml()


if __name__ == "__main__":
    main()
