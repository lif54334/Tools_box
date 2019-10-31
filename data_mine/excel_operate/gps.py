#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   gps.py

@Time    :   2019/10/21 23:00

@Desc    :

'''
import pandas as pd
import numpy as np

test_dict = {'licese':[0],'nums':[0],'time':[0]}
nulldata = pd.DataFrame(test_dict)

df=pd.read_excel('gps2.xlsx')#这个会直接默认读取到这个Excel的第一个表单
print(df)
df=df[:500]
df_group = df.groupby('time')

for item in df_group:
    print("start")
    items=item[1]
    nums=items["nums"]
    nums=list(nums)
    mean = np.mean(nums)
    std = np.std(nums, ddof=1)
    max=np.max(nums)
    min=np.min(nums)
    up=mean+2*std
    down=mean-2*std
    select=['1']*len(nums)
    for i in range(0,len(nums)):
        if nums[i] >=up or nums[i]<=down:
            select[i]='0'
    items["out"]=select
    nulldata=nulldata.append(items,ignore_index=True)

nulldata.to_excel("gps3.xlsx")
