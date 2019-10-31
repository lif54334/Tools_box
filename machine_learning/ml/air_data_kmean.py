#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   air_data_kmean.py

@Time    :   2019/5/16 14:21

@Desc    :

'''
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def read_data():
    datafile= r'air_data.csv' #航空原始数据,第一行为属性标签
    resultfile = r'test.xls' #数据探索结果表
    data = pd.read_csv(datafile, encoding = 'utf-8') #读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）
    explore = data.describe(percentiles = [], include = 'all').T #包括对数据的基本描述，percentiles参数是指定计算多少的分位数表（如1/4分位数、中位数等）；T是转置，转置后更方便查阅
    explore['null'] = len(data)-explore['count'] #describe()函数自动计算非空值数，需要手动计算空值数
    explore = explore[['null', 'max', 'min']]
    explore.columns = [u'空值数', u'最大值', u'最小值'] #表头重命名
    print(explore)

def clean_data():
    datafile= r'air_data.csv' #航空原始数据,第一行为属性标签
    cleanedfile = 'air_clean.csv' #数据清洗后保存的文件
    data = pd.read_csv(datafile,encoding='utf-8') #读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）
    data = data[data['SUM_YR_1'].notnull() & data['SUM_YR_2'].notnull()] #票价非空值才保留
    #只保留票价非零的，或者平均折扣率与总飞行公里数同时为0的记录。
    index1 = data['SUM_YR_1'] != 0
    index2 = data['SUM_YR_2'] != 0
    index3 = (data['SEG_KM_SUM'] == 0) & (data['avg_discount'] == 0) #该规则是“与”,书上给的代码无法正常运行，修改'*'为'&'
    cleandata = data[index1 | index2 | index3] #该规则是“或”
    # data.to_excel(cleanedfile) #导出结果
    return cleandata

def feature(data):
    data = data[['LOAD_TIME', 'FFP_DATE', 'LAST_TO_END', 'FLIGHT_COUNT', 'SEG_KM_SUM', 'avg_discount']]
    # data['L']=pd.datetime(data['LOAD_TIME'])-pd.datetime(data['FFP_DATE'])
    # data['L']=int(((parse(data['LOAD_TIME'])-parse(data['FFP_ADTE'])).days)/30)
    d_ffp = pd.to_datetime(data['FFP_DATE'])
    d_load = pd.to_datetime(data['LOAD_TIME'])
    res = d_load - d_ffp
    data2=data.copy()
    data2['L'] = res.map(lambda x: x / np.timedelta64(30 * 24 * 60, 'm'))
    data2['R'] = data['LAST_TO_END']
    data2['F'] = data['FLIGHT_COUNT']
    data2['M'] = data['SEG_KM_SUM']
    data2['C'] = data['avg_discount']
    data3 = data2[['L', 'R', 'F', 'M', 'C']]
    data4 = (data3 - data3.mean(axis=0)) / data3.std(axis=0)
    data4.columns = ['Z' + i for i in data4.columns]
    return data4

def k_mean(data):
    for i in range(3,8):
        kmodel = KMeans(n_clusters=i,max_iter=50)
        kmodel.fit(data)
        # 简单打印结果
        r1 = pd.Series(kmodel.labels_).value_counts()  # 统计各个类别的数目
        r2 = pd.DataFrame(kmodel.cluster_centers_)  # 找出聚类中心
        # 所有簇中心坐标值中最大值和最小值
        max = r2.values.max()
        min = r2.values.min()
        r = pd.concat([r2, r1], axis=1)  # 横向连接（0是纵向），得到聚类中心对应的类别下的数目
        r.columns = list(data.columns) + [u'类别数目']  # 重命名表头
        print(r)
        # 绘图
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, polar=True)
        center_num = r.values
        feature = ["L", "R", "F", "M", "C"]
        N = len(feature)
        for i, v in enumerate(center_num):
            # 设置雷达图的角度，用于平分切开一个圆面
            angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
            # 为了使雷达图一圈封闭起来，需要下面的步骤
            center = np.concatenate((v[:-1], [v[0]]))
            angles = np.concatenate((angles, [angles[0]]))
            # 绘制折线图
            ax.plot(angles, center, 'o-', linewidth=2, label="第%d簇人群,%d人" % (i + 1, v[-1]))
            # 填充颜色
            ax.fill(angles, center, alpha=0.25)
            # 添加每个特征的标签
            ax.set_thetagrids(angles * 180 / np.pi, feature, fontsize=15)
            # 设置雷达图的范围
            ax.set_ylim(min - 0.1, max + 0.1)
            # 添加标题
            plt.title('客户群特征分析图', fontsize=20)
            # 添加网格线
            ax.grid(True)
            # 设置图例
            plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0), ncol=1, fancybox=True, shadow=True)

        plt.show()


def main():
    read_data()
    cleandata=clean_data()
    std_data=feature(cleandata)
    print(std_data)
    k_mean(std_data)



if __name__ == '__main__':
    main()
