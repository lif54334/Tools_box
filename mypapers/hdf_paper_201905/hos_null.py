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
sql = ("SELECT name,loc,city FROM  %s  " % (table))
cursor.execute(sql)
hos_results = cursor.fetchall()

cursor = db.cursor()
table = "city_level"
sql = ("SELECT city,citylevel FROM  %s  " % (table))
cursor.execute(sql)
loc_results = cursor.fetchall()

i=0
for items in hos_results:
    if items[2] is None:
        for itens in loc_results:
            if str(itens[0]) in str(items[1]):
                print(items[0],items[1],itens[0],itens[1])
                cursor = db.cursor()
                sql_update = "update all_table2 set city = '%s'where  loc='%s'"
                cursor.execute(sql_update % (itens[1], (items[1])))
                continue
            else:
                pass

    else:
        i+=1
        pass
db.commit()
cursor.close()
print(i)