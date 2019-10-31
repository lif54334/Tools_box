#!/usr/bin/env python
#coding:utf-8

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   man_time_car.py

@Time    :   2019/9/19 14:47

@Desc    :

'''
import pymysql
import json  # 导入模块
import pandas as pd

flag=[]
car_warns_list=list()
db = pymysql.connect("localhost", "root", "1234", "gps")
cursor = db.cursor()
car_list=['沪EF8828', '沪DQ4682', '沪BS3269', '沪D39495', '沪DC7467', '沪D48935', '沪DS5889', '沪EB3908', '沪EB3061', '沪DC2702', '沪D39318', '沪DP7337', '沪D48768', '沪EA3087', '沪D39349', '沪EB9237', '沪DD0291', '沪DQ4662', '沪EA7351', '沪DG4323', '沪DC6878', '沪DC2590', '沪EE3915', '沪DC7448', '沪DP2058', '沪DQ4653', '沪D39321', '沪EL2565', '沪EF8811', '沪D48755', '沪D27226', '沪DC9216', '沪EB2761', '沪EA5383', '沪FD6220', '沪DS8371', '沪DA9105', '沪DC8560', '沪D39145', '沪DD1040', '沪EH9108', '沪D48756', '沪EG6150', '沪DQ4796', '沪D08301', '沪FD6117', '沪D39319', '沪DD5066', '沪DD5023', '沪D48701', '沪D48770', '沪EF2329', '沪D47045', '沪DQ6530', '1004048', '沪BQ9683', '沪D48769', '沪D48663', '沪D41173', '沪DQ4666', '沪D74203', '沪DQ4661', '沪DD5083', '沪DD4295', '沪DC9223', '沪DP7261', '沪DQ4768', '沪D43247', '沪EG9275', '沪DD5063', '沪D40547', '沪BE1403', '沪DD5110', '沪DC9179', '沪DD1406', '沪ED2537', '沪D41393', '沪ET1796', '沪DG4292', '沪DQ4812', '沪EC6736', '沪DJ4587', '沪DF2543', '沪D39342', '沪D41389', '沪DA6660', '沪DD8363', '沪DC9420', '沪EK0219', '沪D48766', '沪EH9165', '沪DQ6520', '沪EQ1178', '冀A7746V', '沪DQ4643', '沪D72580', '沪D08249', '沪D48765', '沪D68672', '沪D48720', '沪DD4436', '沪BL9197', '沪D48752', '沪DC8608', '沪EK8817', '沪BT0883', '沪DC9227', '沪ED6077', '沪D48715', '沪D44843', '沪EA7898', '沪BL8479', '沪DS7938', '沪DD8396', '沪EA5177', '沪DF7232', '沪DD8395', '沪ET9217', '沪D39247', '沪DQ6357', '沪DA9068', '沪D82720', '沪DC9238', '沪DC6829', '沪DC9258', '沪DS1526', '沪D27170', '沪DE3850', '沪DD5019', '沪EP6827', '沪DP7185', '沪EA9873', '沪D48757', '沪DC6817', '沪EF1731', '沪D48718', '沪DD5065', '沪BQ9675', '沪DD5018', '沪DD5082', '沪DD5008', '沪EL2759', '沪FB2931', '沪DD1476', '沪DP7339', '沪EL6386', '沪DD5012', '沪DP7286', '沪EK0297', '沪EA7752', '沪BQ9699', '沪DD1410', '沪DP7331', '沪DD5037', '沪DF2573', '沪D77658', '沪DD1459', '沪DJ4619', '沪EH9109', '沪D48705', '沪DD5055', '沪DC9220', '沪DC9215', '沪ED6098', '沪D27249', '沪DQ4678', '沪DD5042', '沪DE3949', '沪DQ6148', '沪DQ4680', '沪ES5952', '沪DP7268', '沪D48590', '沪EE0575', '沪D41055', '沪BQ9677', '沪EB2706', '沪DD5072', '沪DC7447', '沪DS7961', '沪DC9229', '沪DS2959', '沪EF8579', '沪DP7265', '沪DD5011', '沪EG3229', '沪DA9108', '沪DP2019', '沪DD5003', '沪DD5062', '沪DD5043', '沪BT0897', '沪DC6858', '沪DD1141', '冀A9715V', '沪DD5015', '沪DA6659', '沪BQ9593', '沪DD5033', '沪DL9082', '沪BG9748', '沪DC9189', '沪EH7800', '沪DD5058', '沪DE3908', '冀A8343V', '沪EB5795', '沪DC8588', '沪DA9040', '沪BQ9625', '沪DD5020', '沪DD5039', '沪D48780', '沪D41309', '沪EL5538', '沪DA9069', '沪D39343', '沪DD5017', '沪DC9341', '沪DA9056', '沪DL9090', '沪DD5089', '沪DD5090', '沪DF3839', '沪DD1005', '沪D27142', '沪D99425', '沪D77615', '沪DD5030', '沪DC6827', '沪DD5022', '沪D27248', '沪DD5021', '沪ER8561', '沪D27262', '沪DD1401', '沪DD1442', '沪D27276', '沪D48775', '沪DE3927', '沪DD5059', '沪DA5976', '沪EK2009', '沪EL3681', '沪BG7281', '沪ED7931', '沪EF2333', '沪EB5758', '沪DD4419', '沪D47043', '沪D27031', '沪DD5002', '沪DS5949', '沪D68638', '沪D48732', '沪EB2071', '沪DP2540', '沪DD9530', '沪BQ9686', '沪EE6739', '沪EA5399', '沪DD4410', '沪EQ7733', '沪FA5120', '沪EC3678', '沪DT6697', '沪DC6852', '沪DC8605', '沪D39308', '沪D27176', '沪D5925', '沪EG5167', '沪DF7286', '沪EB5782', '沪D24577', '沪DA6662', '沪BQ9612', '沪EE5892', '沪EC1568', '沪DS5223', '沪DS9010', '沪EJ2952', '沪D41005', '沪DD4377', '沪DD8382', '沪BS5098', '沪EL7208']
def man_time(sql):
    man_time_dict = dict()
    try:
        cursor.execute(sql)
        db.commit()
        results = cursor.fetchall()
        for item in results:
            car_time=str(item[1])+str(item[0])
            car_time=car_time.replace(' ','')
            man_time_dict[car_time]=(item[2])
    except Exception as e:
        print(e)
        print("Error: unable to fetch data")
        pass
    db.close()
    return man_time_dict
def find_warns(car_sql,man_time):
    # try:
    car_warns2=[]
    cursor.execute(car_sql)
    db.commit()
    results = cursor.fetchall()
    for item in results:
        car_warns = {}
        car_warns["id"]=item[0][:7]
        car_warns["org"]=item[1]
        car_warns["level"]=item[2]
        car_warns["class"]=item[3]
        car_warns["name"]=item[4]
        car_warns["speed"]=item[5]
        car_warns["time"]=item[6]
        car_warns["jpg"]=item[7]
        car_warns["jing"]=item[8]
        car_warns["wei"]=item[9]
        car_warns["loc"]=item[10]
        no_time=str(item[6][:11])+str(item[0][:7])
        no_time=no_time.replace(' ', '')
        if str(no_time) in man_time.keys():
            user=str(man_time[no_time])
            car_warns["user"]=user
        else:
            car_warns["user"]='无'
        # car_warns["user"]=man_time[no_time]
    # except Exception as e:
    #     print(e)
    #     print("Error: unable to fetch data")
    #     flag.append(car_sql[-10:])
    #     pass
        car_warns2.append(car_warns)
    return car_warns2,flag


def write_json(name,data):
    json_str=json.dumps(data,ensure_ascii=False,indent=4)
    with open(name, 'w',encoding='utf8') as file:  # test.json文本，只能写入状态 如果没有就创建
        file.write(json_str)  # data转换为json数据格式并写入文件
    file.close()  # 关闭文件

def read_json():
    with open('man_time.json', 'r',encoding='utf8') as fileR:
        R = json.load(fileR)
        fileR.close()
    return R

def process():
    man_time_sql = 'SELECT * from  cm'
    man_time_dict = man_time(man_time_sql)
    name='man_time.json'
    write_json(name,man_time_dict)

def main():
    # process()
    man_time=read_json()
    car_warns_list=warns_search(man_time)
    car_warns_list2=[]
    for item in car_warns_list:
        for j in item:
            car_warns_list2.append(j)
    df = pd.DataFrame(car_warns_list2)
    df.to_csv("output.csv",encoding='utf_8_sig')
    # for item in car_warns_list:
    #     insert_sql(item)
    # warns_car()
    # name='carwarns.json'
    # write_json(name, carwarns)
def warns_search(man_time):
    for item in car_list:
        car_sql="SELECT * from  warnsall where id REGEXP '{0}'".format(str(item))
        carwarns,flag=find_warns(car_sql,man_time)
        # print(len(flag))
        car_warns_list.append(carwarns)
    return car_warns_list

def warns_car():
    warns_car_list = list()
    try:
        cursor.execute('SELECT distinct RIGHT(id,7) from warnsall')
        db.commit()
        results = cursor.fetchall()
        for item in results:
            warns_car_list.append(item[0])
    except Exception as e:
        print(e)
        print("Error: unable to fetch data")
    db.close()
    print(warns_car_list)
def insert_sql(cw_dict):
    db = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='gps')
    print(cw_dict)
    # SQL 插入语句里面的数据类型要对应
    table = 'all'
    keys = ', '.join(cw_dict.keys())
    values = ', '.join(['%s'] * len(cw_dict))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    # try:
    cursor.execute(sql, tuple(cw_dict.values()))
    print('Successful')
    db.commit()
    # except:
    #     print('Failed')
    #     db.rollback()
    cursor.close()
    db.close()









if __name__ == '__main__':
    main()
