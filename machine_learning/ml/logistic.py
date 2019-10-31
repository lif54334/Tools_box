#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   logistic.py

@Time    :   2018/10/3 19:51

@Desc    :

'''
import pandas as pd
import matplotlib.pyplot as plt
import xlrd

from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.stattools import adfuller
import numpy as np
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot


def test():
    #参数初始化
    discfile = "menori.xlsx"
    forecastnum = 5
    #读取数据，指定日期列为指标，Pandas自动将“日期”列识别为Datetime格式
    data = pd.read_excel(discfile, index_col = u'Time')
    #时序图
    print(data)
    #用来正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']
    #用来正常显示负号
    plt.rcParams['axes.unicode_minus'] = False
    data.plot()
    plt.show()
    plot_acf(data).show()
    print('原始序列的检验结果为：', adfuller(data[u'nums']))
    D_data = data.diff().dropna()
    D_data.columns = [u'差分']
    D_data.plot()  # 画出差分后的时序图
    plt.show()

    plot_acf(D_data) # 画出自相关图
    plt.show()
    # plot_pacf(D_data)  # 画出偏相关图
    # plt.show()
    dta=D_data.diff().dropna()
    dta.plot()  # 画出差分后的时序图
    plt.show()
    plot_acf(dta) # 画出自相关图
    plt.show()
    print(u'差分序列的ADF 检验结果为： ', adfuller(D_data[u'差分']))  # 平稳性检验
    # 差分序列的ADF 检验结果为：  (-3.1560562366723537, 0.022673435440048798, 0, 35, {'1%': -3.6327426647230316,
    # '10%': -2.6130173469387756, '5%': -2.9485102040816327}, 287.5909090780334)
    # 一阶差分后的序列的时序图在均值附近比较平稳的波动， 自相关性有很强的短期相关性， 单位根检验 p值小于 0.05 ，所以说一阶差分后的序列是平稳序列
    # 对一阶差分后的序列做白噪声检验
    from statsmodels.stats.diagnostic import acorr_ljungbox
    print(u'差分序列的白噪声检验结果：', acorr_ljungbox(D_data, lags=1))  # 返回统计量和 p 值
    # 差分序列的白噪声检验结果： (array([11.30402222]), array([0.00077339])) p值为第二项， 远小于 0.05
    # 对模型进行定阶
    model = ARIMA(np.array(data, dtype=np.float), (0, 1, 1)).fit()
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(model.summary2())  # 生成一份模型报告
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(model.forecast(12))  # 为未来5天进行预测， 返回预测结果， 标准误差， 和置信区间

def ma():
    dta = [318, 111, 998, 35, 533, 306, 428, 460, 592, 1795, 816, 1252, 1330, 786, 3318, 847, 1203, 954, 1283, 873, 945,
           2399, 744, 1528, 1116]
    dta = np.array(dta, dtype=np.float)
    dta = pd.Series(dta)
    dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2001', '2025'))
    dta.plot(figsize=(12, 8))

    fig = plt.figure(figsize=(12, 8))
    ax1 = fig.add_subplot(111)
    diff1 = dta.diff(1)
    diff1.plot(ax=ax1)
    dta = dta.diff(1)  # 我们已经知道要使用一阶差分的时间序列，之前判断差分的程序可以注释掉
    dta[0] = 0
    # 进行模型的测试
    # arma_mod70 = sm.tsa.ARMA(dta,(7,0)).fit()
    # arma_mod71 = sm.tsa.ARMA(dta,(7,1)).fit()
    # arma_mod80 = sm.tsa.ARMA(dta,(8,0)).fit()
    arma_mod30 = sm.tsa.ARMA(dta, (0, 1)).fit()
    # 进行模型的评价
    # print(arma_mod70.aic,arma_mod70.bic,arma_mod70.hqic)
    # print(arma_mod30.aic,arma_mod30.bic,arma_mod30.hqic)
    # print(arma_mod71.aic,arma_mod71.bic,arma_mod71.hqic)
    # print(arma_mod80.aic,arma_mod80.bic,arma_mod80.hqic)
    # 进行选定模型的测试
    resid = arma_mod30.resid
    sm.graphics.tsa.plot_acf(resid.values.squeeze())
    sm.graphics.tsa.plot_pacf(resid)
    # plt.show()
    # DW检测
    print(sm.stats.durbin_watson(arma_mod30.resid.values))
    # 进行预测
    predict_dta = arma_mod30.predict('2025', '2035', dynamic=True)
    print(predict_dta)
    fig, ax = plt.subplots(figsize=(12, 8))
    ax = dta.ix['2000':].plot(ax=ax)
    fig = arma_mod30.plot_predict('2025', '2035', dynamic=True, ax=ax, plot_insample=False)
    plt.show()


def picture():
    data = pd.read_excel("menori.xlsx")  # 读取数据，指定“日期”列为索引列
    hang = list(data.columns)
    print(hang)
    # print(hang)
    nums = list(data["nums"])
    x=list(i for i in range(0,len(nums)))
    print(x,nums)
    plt.plot(x,nums)
    plt.show()



def main():
    # test()
    # picture()
    ma()

if __name__ == '__main__':
    main()