#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   ip_spider.py

@Time    :   2018/7/12 21:03

@Desc    :  Crawl free ip

'''
import random
from time import sleep

import pymysql
import requests
from pyquery import PyQuery as pq
import os
import re
import json
from ip_pool.config import MONGO, MYSQL, TXT_STORE, ips, ipshttp, ipshttps, maxp, base_url, test_url, headers,ip_storege
from pymongo import MongoClient as Client


def load_txt():
    proxy_https = list()
    proxy_http = list()
    with open("https.txt", 'r')as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            proxy_https.append(line)
    with open("http.txt", 'r')as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            proxy_http.append(line)
    return proxy_http, proxy_https


def remove_file(name, suffix):
    fullname = name + suffix
    if os.path.exists(fullname):
        # 删除文件，可使用以下两种方法。
        os.remove(fullname)
        # os.unlink(my_file)
        print('have deleted')
    else:
        print('no such file:%s' % fullname)


def check_ip_in_array(ip_array):
    for test_data in ip_array:
        test_ip = str(test_data['ip']) + ":" + str(test_data['port'])
        test_result = requests.get(test_url, headers=headers, proxies=test_ip, timeout=0.1)
        if test_result:
            print("有效Ip")
        else:
            print("无效Ip")
            ip_array.remove(test_data)
    return ip_array


def check_ip_only(ip, port):
    ipstrange = str(ip) + ":" + str(port)
    print(ipstrange)
    proxies_test = {'proxies': ipstrange}
    try:
        test_result = requests.get(test_url, headers=headers, proxies=proxies_test, timeout=1)
        if test_result:
            print("可以用")
            return True
        else:
            print("不能用")
            return False
    except:
        print("挂掉了")
        return False


def check_in_mongo(name):
    client = Client(host=MONGO['uri'], port=MONGO['port'])
    db = client['ipsite']
    coll = db[name]
    for i in coll.find():
        i_result = check_ip_only(i['ip'], i['port'])
        if not i_result:
            print("delete i")
            coll.delete_one(i)


def sto_txt(ip_label, port_label, hp_label):
    new_ip = (str(ip_label) + ":" + str(port_label))
    if hp_label == "HTTPS":
        with open("https.txt", 'a', encoding='utf-8')as https_file:
            https_file.write(str(new_ip) + "\n")
    else:
        with open('http.txt', 'a', encoding="utf-8")as http_file:
            http_file.write(str(new_ip) + "\n")


def sto_json(dt1, dt2):

    print("https")
    ip_storege["HTTPS"]=dt1
    ip_storege["HTTP"]=dt2
    json.dump(ip_storege,open("https.json", 'a', encoding='utf-8'))
    # with open("https.json", 'a', encoding='utf-8')as https_file:
    #     json.dump(dt1, https_file, indent=4, ensure_ascii=False)
    # print("http")
    # with open("http.json", 'a', encoding='utf-8')as http_file:
    #     json.dump(dt2, http_file, indent=4, ensure_ascii=False)



def ips_seg(ips):
    for ipentry in ips:
        if ipentry['type'] == 'HTTPS':
            ipshttps.append(ipentry)
            # print(ipentry['ip'])
            # json.dump(ipentry,https_file,indent=4,ensure_ascii=False)
        if ipentry['type'] == 'HTTP':
            ipshttp.append(ipentry)
        else:
            continue
    return ipshttp, ipshttps


def load_json(select):
    if select == True:
        with open("https.json", 'r')as sf:
            https_data = json.load(sf)
            return https_data

        # with open("http.json", 'r')as f:
        #     http_data = json.load(f)
        #     return http_data
    else:
        return None


def add_ip(https_data, http_data):
    proxytps=list()
    proxytp=list()
    for data in https_data:
        new_https = str(data['ip']) + ":" + str(data['port'])
        proxytps.append(new_https)

    for data in http_data:
        new_http = str(data['ip']) + ":" + str(data['port'])
        proxytp.append(new_http)


def sto_mongo(array):
    name = array[5]['type']
    client = Client(host=MONGO['uri'], port=MONGO['port'])
    db = client[MONGO['db']]
    coll = db[name]
    # 先检测，再写入，防止重复
    for ip in array:
        if coll.find({'ip': ip['ip']}).count() == 0:
            coll.insert_one(ip)
    client.close()

def sto_mysql(array):
    db = pymysql.connect(host=MYSQL['host'], port=MYSQL['port'], user=MYSQL['user'], password=MYSQL['passwd'], db=MYSQL['db'])
    for data in array:
        cursor = db.cursor()
        ip=data['ip']
        port=data['port']
        type=data['type']
        sql="INSERT INTO IP_STO(IP,PORT,TYPE)VALUES ('%S','%S','%S') "% (ip,port,type)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print("error")
            break
    db.close()



def load_mongo(name):
    ipsto = list()
    client = Client(host=MONGO['uri'], port=MONGO['port'])
    db = client["ipsite"]
    col = db[name]
    for x in col.find():
        # print(x)
        ipsto_ip = str(x['ip']) + ":" + str(x['port'])
        ipsto.append(ipsto_ip)
    return ipsto


def generate_ip(name):
    mongo_array = list()
    client = Client(MONGO['uri'], MONGO['port'])
    db = client['ipsite']
    coll = db[name]
    # count = coll.count()
    # nums = random.randint(0, count)
    # print(nums)
    mongo_ips = coll.find()
    for i in mongo_ips:
        mongo_ip = str(i['ip']) + ":" + str(i['port'])
        mongo_array.append(mongo_ip)
    return mongo_array


def offer_ip(name):
    if name == "HTTPS":
        proxytps = generate_ip(name)
        proxtps = {'proxies': random.choice(proxytps)}
        return proxtps
    else:
        proxytp = generate_ip(name)
        proxtp = {'proxies': random.choice(proxytp)}
        return proxtp


def run(name):

    for page_num in range(1, maxp):
        prox = offer_ip(name)
        url = base_url + str(page_num)
        print(url)
        print(headers, prox)
        html = requests.get(url, headers=headers, proxies=prox).text
        doc = pq(html)
        for data in doc('#ip_list').items('tr'):
            ip_label = data('td').eq(1).text()
            port_label = data('td').eq(2).text()
            hp_label = data('td').eq(5).text()
            new_ip = (str(data('td').eq(1).text()) + ":" + str(data('td').eq(2).text()))
            test_prox = {'proxies': new_ip}
            try:
                test_response = requests.get(test_url, headers=headers, proxies=test_prox, timeout=0.1)
            except:
                continue
            if test_response:
                ips.append({'ip': ip_label, 'port': port_label, 'type': hp_label})
            else:
                continue
        sleep(3)
    return ips

if __name__ == '__main__':
    print("check before")
    check_in_mongo("HTTPS")
    check_in_mongo("HTTP")
    ips = run("HTTP")
    print("over\n")
    # sto_mysql(ips)
    ipshttps, ipshttp = ips_seg(ips)
    # add_ip(ipshttps, ipshttp)
    print("https")
    sto_mongo(ipshttps)
    print("http")
    sto_mongo(ipshttp)
    print("check after")
    check_in_mongo("HTTPS")
    check_in_mongo("HTTP")
    # httpsip=load_mongo("HTTPS")
    # print("https")
    # print(httpsip)
    # httpip=load_mongo("HTTP")
    # print("http")
    # print(httpip)
