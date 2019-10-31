#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   config.py

@Time    :   2018/7/13 17:15

@Desc    :

'''

from fake_useragent import UserAgent
import random

maxp = 3

MONGO = {
    'uri': 'localhost',
    'db': 'ipsite',
    'port': 27017
}

MYSQL = {
    'host': 'localhost',
    'db': 'ipsite',
    'port': 3306,
    'user': 'root',
    'passwd': 1234
}

TXT_STORE = ''
ips = list()
ipshttps = list()
ipshttp = list()
ip_storege=dict()
base_url = "http://www.xicidaili.com/nn/"
test_url = "http://www.sogou.com/"
ua = UserAgent()
headers = {'User-Agent': ua.random}
