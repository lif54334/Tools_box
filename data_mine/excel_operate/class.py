#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   class.py

@Time    :   2019/4/10 14:24

@Desc    :

'''
import pandas as pd
import collections
import matplotlib.pyplot as plt
import numpy as np
import math
import pymysql
from sklearn.cluster import KMeans
import scipy.signal as signal

db = pymysql.connect("localhost", "root", "1234", "data_sci")
cursor = db.cursor()


def main():
    data=getdata()
    # # all_distri_line(data)
    # # all_distri_scatter(data)
    table_name = "oa"
    name_name = "BAD虚拟物料"
    most_distri(table_name, name_name,num=4)




def all_distri_line(series):
    x = np.arange(1, len(series) + 1)
    y = series
    print('x轴长度:{0}    y轴长度:{1}'.format(len(x), len(y)))
    plt.plot(x, y)
    plt.show()


def all_distri_scatter(series):
    x = np.arange(1, len(series) + 1)
    y = series
    print('x轴长度:{0}    y轴长度:{1}'.format(len(x), len(y)))
    plt.scatter(x, y)
    plt.show()


def most_distri(table, name,num):
    sql = ("SELECT re,name FROM  %s  where name='%s'" % (table, name))
    cursor.execute(sql)
    results = cursor.fetchall()
    time_list = [list(item)[0] for item in results]
    time_list = counter(time_list)
    # all_distri_line(time_list)
    # all_distri_scatter(time_list)
    # # two_clusters(time_list,num=num)
    # signale(time_list)

def one_clusters(data):
    y = data.reshape(-1, 1)
    km = KMeans(n_clusters=4)
    km.fit(y)
    label_pred = km.labels_
    centroids = km.cluster_centers_
    inertia = km.inertia_
    print(label_pred, centroids)


def two_clusters(data,num):
    x = np.arange(1, len(data) + 1)
    y = data
    data_list = np.array(list(zip(x, y))).reshape(len(x), 2)
    kmeans = KMeans(n_clusters=num)  # n_clusters:number of cluster
    kmeans.fit(data_list)
    print(kmeans.labels_,kmeans.cluster_centers_)
    plt.figure(figsize=(8, 10))
    colors = ['b', 'g', 'r','w']
    markers = ['o', 's', 'D','x']
    for i, l in enumerate(kmeans.labels_):
        plt.plot(x[i], y[i], color=colors[l], marker=markers[l], ls='None')
    plt.show()

def signale(data):
    plt.figure(figsize=(16, 4))
    aix= np.arange(1, len(data) + 1)
    plt.plot(aix, data)
    print(data[signal.argrelextrema(data, np.greater)])
    print(signal.argrelextrema(data, np.greater))

    print("极小值：{}".format(data[signal.argrelextrema(-data, np.greater)]))
    plt.plot(signal.argrelextrema(data, np.greater)[0], data[signal.argrelextrema(data, np.greater)], 'o')
    plt.plot(signal.argrelextrema(-data, np.greater)[0], data[signal.argrelextrema(-data, np.greater)], '+')
    # plt.plot(peakutils.index(-x),x[peakutils.index(-x)],'*')
    plt.show()

def getdata():
    path = "oa.xlsx"
    df = pd.read_excel(path, sheet_name=0)

    time = df["re"].values
    time_list = counter(time)
    print(time_list)
    return time_list


def counter(data):
    tc = collections.Counter((data))
    tc_max = max(tc.keys())
    data_list = np.zeros(tc_max)
    for i in range(tc_max):
        if i in tc:
            data_list[i] = tc.get(i)
    print(list(data_list))
    return data_list

def persent(data):
    print(np.percentile(data, 5))


if __name__ == '__main__':
    main()
