import operator
from itertools import chain

from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
import numpy as np
import collections
import pymysql


def classfication(id):
    db = pymysql.connect("localhost", "root", "1234", "data_sci")
    cursor = db.cursor()
    table = "oa"
    sql = ("SELECT re,id,name FROM  %s  where id='%s'" % (table, id))
    cursor.execute(sql)
    results = cursor.fetchall()
    some_time_list = [list(item)[0] for item in results]
    tc = collections.Counter(some_time_list)
    tc_max = max(tc.keys())
    data_list = np.zeros(tc_max)
    for i in range(tc_max):
        j=i+1
        if j in tc:
            data_list[i] = tc.get(j)
    y = data_list
    # y=[27.0, 130.0, 163.0, 221.0, 175.0, 145.0, 138.0, 146.0, 133.0, 102.0, 61.0, 70.0, 37.0, 71.0, 52.0, 44.0, 30.0, 48.0, 26.0, 26.0, 16.0, 34.0, 35.0, 29.0, 13.0, 15.0, 16.0, 15.0, 31.0, 17.0, 20.0, 29.0, 30.0, 7.0, 18.0, 31.0, 25.0, 11.0, 15.0, 13.0, 15.0, 9.0, 8.0, 22.0, 4.0, 12.0, 4.0, 3.0, 7.0, 16.0, 27.0, 10.0, 31.0, 3.0, 3.0, 9.0, 4.0, 10.0, 8.0, 17.0, 4.0, 1.0, 14.0, 11.0, 7.0, 5.0, 2.0, 4.0, 5.0, 4.0, 3.0, 4.0, 6.0, 15.0, 5.0, 1.0, 10.0, 2.0, 3.0, 0.0, 2.0, 5.0, 0.0, 2.0, 21.0, 0.0, 2.0, 2.0, 4.0, 0.0, 7.0, 17.0, 2.0, 5.0, 3.0, 4.0, 2.0, 3.0, 4.0, 8.0, 0.0, 1.0, 1.0, 0.0, 3.0, 1.0, 1.0, 1.0, 5.0, 2.0, 0.0, 0.0, 3.0, 2.0, 2.0, 2.0, 1.0, 1.0, 0.0, 1.0, 5.0, 1.0, 2.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 2.0, 5.0, 0.0, 2.0, 1.0, 0.0, 1.0, 0.0, 2.0, 1.0, 2.0, 4.0, 0.0, 0.0, 0.0, 5.0, 0.0, 1.0, 0.0, 3.0, 1.0, 1.0, 2.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 3.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    x = np.arange(1, len(y) + 1)
    y = np.array(y)
    z = np.dstack((x, y))[0]
    y_sum = sum(y)
    n_components = np.arange(1, 5)
    models = [GaussianMixture(n, covariance_type='full', random_state=0).fit(z)
              for n in n_components]

    numlist = list()
    for i in models:
        bic = i.bic(z)
        aic = i.aic(z)
        numlist.append(aic)
    # print("list:{}    min:{}".format(min(numlist), numlist.index(min(numlist)) + 1))
    # plt.plot(n_components, [m.bic(z) for m in models], label='BIC')
    # plt.plot(n_components, [m.aic(z) for m in models], label='AIC')
    # plt.legend(loc='best')
    # plt.xlabel('n_components')
    # plt.show()

    gmm = GaussianMixture(n_components=numlist.index(min(numlist)) + 1, max_iter=200).fit(z)

    labels = gmm.predict(z)
    # plt.scatter(z[:, 0], z[:, 1], c=labels, s=40, cmap='viridis')
    # plt.show()

    time_list = gmm.predict(z)
    time_counter = collections.Counter(gmm.predict(z))
    # print("clusters_list:{}   list_counter:{}".format(time_list, time_counter))

    time_counter_key = list(time_counter.keys())

    return time_counter_key, time_list, y, y_sum


def predict(time_counter_key, time_list, y, x):
    time_dict_list = []
    for i in time_counter_key:

        y_key = [m for m, n in enumerate(time_list) if n == i]
        # print("y_key_nums:{}   zero_nums:{}".format(len(y_key), max(y_key) - min(y_key) + 1 - len(y_key)))
        y_list = []
        # y_list.append([0] * (max(y_key) - min(y_key) + 1 - len(y_key)))
        y_list_sum = 0
        for j in y_key:
            y_list_sum += int(y[j])
            y_list.append([j + 1] * int(y[j]))
        y_list = list(chain.from_iterable(y_list))
        if len(y_list) == 0:
            pass
        else:
            y_array = np.array(y_list)
            time_dict = dict()
            time_dict["class"] = i
            if x >= (min(y_key)) and x <= (max(y_key)):
                time_dict["predict"] = ((np.sum(y_array <= x)) / len(y_list)).round(3)
            else:
                time_dict["predict"] = 0
            time_dict_list.append(time_dict)
    return time_dict_list


def model(time_counter_key, time_list, y, y_sum):
    time_dict_list = []
    for i in time_counter_key:

        y_key = [m for m, n in enumerate(time_list) if n == i]
        # print("y_key_nums:{}   zero_nums:{}".format(len(y_key), max(y_key) - min(y_key) + 1 - len(y_key)))
        y_list = []
        # y_list.append([0] * (max(y_key) - min(y_key) + 1 - len(y_key)))
        y_list_sum = 0
        for j in y_key:
            y_list_sum += int(y[j])
            y_list.append([j + 1] * int(y[j]))
        y_list = list(chain.from_iterable(y_list))
        if len(y_list) == 0:
            pass
        else:
            time_dict = dict()
            time_dict["class"] = i
            time_dict["start"] = min(y_key)
            time_dict["stop"] = max(y_key)
            time_dict["y_list_weight"] = (y_list_sum / y_sum).round(3)
            time_dict["y_list_mean"] = np.mean(y_list)
            time_dict["y_list_std"] = np.std(y_list)
            time_dict["confidence interval"] = [(np.mean(y_list) - np.std(y_list)).round(3),
                                                (np.mean(y_list).round(3) + np.std(y_list)).round(3)]
            # time_dict["y_list_20%"] = np.percentile(y_list, 20)
            # time_dict["y_list_50%"] = np.percentile(y_list, 50)
            # time_dict["y_list_80%"] = np.percentile(y_list, 80)
            time_dict_list.append(time_dict)
    sorted_list = sorted(time_dict_list, key=operator.itemgetter('y_list_mean'))
    return sorted_list


def haveid():
    db = pymysql.connect("localhost", "root", "1234", "data_sci")
    cursor = db.cursor()
    sql = ("SELECT distinct id,name FROM oa")
    cursor.execute(sql)
    results = cursor.fetchall()
    id_list = [[list(item)[0], list(item)[1]] for item in results]

    return id_list


def insert(id, name, data):
    db = pymysql.connect("localhost", "root", "1234", "data_sci")
    cursor = db.cursor()
    class1_mean = None
    class1_interval_up = None
    class1_interval_down = None

    class1_weight = None
    class2_mean = None
    class2_interval_up = None
    class2_interval_down = None

    class2_weight = None
    class3_mean = None
    class3_interval_up = None
    class3_interval_down = None

    class3_weight = None
    class4_mean = None
    class4_interval_up = None
    class4_interval_down = None

    class4_weight = None
    plus = None
    for i in range(0, len(data)):
        if i == 0:
            item = data[0]
            qujian = item["confidence interval"]
            class1_mean = item["y_list_mean"]
            if qujian[0]<0:
                class1_interval_up = 0
            else:
                class1_interval_up=qujian[0]
            class1_interval_down = qujian[1]
            class1_weight = item["y_list_weight"]
        elif i == 1:
            item = data[1]
            qujian = item["confidence interval"]
            class2_mean = item["y_list_mean"]
            if qujian[0]<0:
                class1_interval_up = 0
            else:
                class1_interval_up=qujian[0]
            class2_interval_down = qujian[1]
            class2_weight = item["y_list_weight"]
        elif i == 2:
            item = data[2]
            qujian = item["confidence interval"]
            class3_mean = item["y_list_mean"]
            if qujian[0]<0:
                class1_interval_up = 0
            else:
                class1_interval_up=qujian[0]
            class3_interval_down = qujian[1]
            class3_weight = item["y_list_weight"]
        elif i == 3:
            item = data[3]
            qujian = item["confidence interval"]
            class4_mean = item["y_list_mean"]
            if qujian[0]<0:
                class1_interval_up = 0
            else:
                class1_interval_up=qujian[0]
            class4_interval_down = qujian[1]
            class4_weight = item["y_list_weight"]
        else:
            pass

    id = int(id)
    name = str(name)
    sql_insert = "insert into oa_ao_copy1(id, name, class1_mean,class1_interval_up,class1_interval_down,class1_weight,class2_mean,class2_interval_up,class2_interval_down,class2_weight,class3_mean,class3_interval_up,class3_interval_down,class3_weight,class4_mean,class4_interval_up,class4_interval_down,class4_weight,plus) values(%s,'%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % (
    id, name or 'NULL', class1_mean or 'NULL', class1_interval_up or 'NULL',class1_interval_down or 'NULL', class1_weight or 'NULL',
    class2_mean or 'NULL', class2_interval_up or 'NULL',class2_interval_down or 'NULL', class2_weight or 'NULL', class3_mean or 'NULL',
    class3_interval_up or 'NULL',class3_interval_down or 'NULL', class3_weight or 'NULL', class4_mean or 'NULL', class4_interval_up or 'NULL',
    class4_interval_down or 'NULL',class4_weight or 'NULL', plus or 'NULL')
    # print(value_list)

    cursor.execute(sql_insert)
    db.commit()
    # sql_update = "update oa_ao_copy1 set id = '%s',name='%s',class1_mean='%s',class1_interval='%s',class1_weight='%s',class2_mean='%s',class2_interval='%s',class2_weight='%s',class3_mean='%s',class3_interval='%s',class3_weight='%s',class4_mean='%s',class4_interval='%s',class4_weight='%s'  where id = '%s'"
    # cursor.execute(sql_update % (id, name, class1_mean,class1_interval,class1_weight,class2_mean,class2_interval,class2_weight,class3_mean,class3_interval,class3_weight,class4_mean,class4_interval,class4_weight))


def main():
    ids=haveid()
    for item in ids:
        id = item[0]
        name = item[1]
    #     id="132002884"
    #     name="McCoy's 5a Medium/500ML(Invitrogen,12330"
        print(id)
        name=name.replace("'","”")
        try:
            print("true")
            time_counter_key, time_list, y, y_sum = classfication(id)
            out = model(time_counter_key, time_list, y, y_sum)
            insert(id, name, out)
        except:
            try:
                out=[]
                print("wrong")
                insert(id, name, out)
            except:
                pass


    # x=50
    # pre=predict(time_counter_key,time_list,y,x)
    # print(pre)


if __name__ == '__main__':
    main()
