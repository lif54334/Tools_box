from itertools import chain

from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
import numpy as np
import collections
import pymysql

db = pymysql.connect("localhost", "root", "1234", "cy")
cursor = db.cursor()
table = "all_table2"
sql = ("SELECT name,hospital FROM  %s  " % (table))
cursor.execute(sql)
hos_results = cursor.fetchall()


cursor = db.cursor()
table = "all_hospital"
sql = ("SELECT shengfen,shi,mingc FROM  %s  " % (table))
cursor.execute(sql)
loc_results = cursor.fetchall()

print(hos_results)
print(loc_results)
unknow=[]
for items in hos_results:
    hos=items[1]
    for itens in loc_results:
        if str(hos) in str(itens[2]) or  str(itens[2]) in str(hos):
            # print(items,itens)
            cursor = db.cursor()
            sql_update = "update all_table2 set loc = '%s'where name = '%s' and hospital='%s'"
            cursor.execute(sql_update % (itens[1],items[0],items[1]))
            continue
        else:
            # unknow.append(hos)
            pass
db.commit()
cursor.close()
# print(set(unknow))
# cursor = db.cursor()
# sql_update="update all_table2 set loc = '%s'where name = '%s' and hospital='%s'"
# for i in range(0,len(data)):
#     cursor.execute(sql_update % (data[i],i+1))
# # cursor.executemany(sql_update,data)
# db.commit()
# cursor.close()