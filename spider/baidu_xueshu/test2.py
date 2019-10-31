#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   test2.py

@Time    :   2019/5/24 14:26

@Desc    :

'''
import json
import re

import demjson
import simplejson

i="Solution-Processed and High-Performance Organic Solar Cells Using Small Molecules with a Benzodithiophene Unit"
j={"title": "Solution-Processed and High-Performance Organic Solar Cells Using Small Molecules with a Benzodithiophene Unit", "author": "J Zhou/Y Zuo/X Wan", "abstract": "Three small molecules named DR3TBDTT, DR3TBDTT-HD, and DR3TBD2T with a benzo[1,2-b:4,5-b]dithiophene (BDT) unit as the central building block have been...", "urls": "http://xueshu.baidu.com/usercenter/paper/show?paperid=ebbacfd494ea2e306737c9433fc8f275&site=xueshu_se", "time": "2013年", "publish": "《Journal of the American Chemical Society》"}

j=str(j)
m=re.sub('\'','\"',j)
m=re.sub('\n','\\n',m)
print(m)
n=simplejson.loads(m)
# print(m)
if str(i) == str(n["title"]):
    print("yes")