#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   sentiment.py

@Time    :   2019/7/3 8:39

@Desc    :

'''
import csv
import json
import jieba
import pandas as pd
import numpy as np

def read():
    big_dict={}
    with open("result.txt","r",encoding="utf8")as fr:
        lines=fr.readlines()
        for line in lines:
            num_list=[]
            line2=eval(line)
            word=(line2["Word"])
            fre=line2["Frequency"]
            Valence_Mean=line2["Valence_Mean"]
            Valence_SD=line2["Valence_SD"]
            Arousal_Mean=line2["Arousal_Mean"]
            Arousal_SD=line2["Arousal_SD"]
            num_list=[fre,Valence_Mean,Valence_SD,Arousal_Mean,Arousal_SD]
            big_dict[word]=num_list
    big_dict["不错"]=['686', '6.3', '0.447', '4.4', '0.894']
    return big_dict
def txt_emotions(big_dict):
    with open('test1.csv', 'a', newline='',encoding="utf_8_sig")as csv_file:
        # 获取一个csv对象进行内容写入
        writer = csv.writer(csv_file)
        writer.writerow(['文本', '情感词出现次数', 'Frequency', 'Valence_SD','Valence_SD','Arousal_Mean','Arousal_SD'])
        df=pd.read_excel("review.xls", sheet_name='Sheet1',)
        items=df.ix[:,[0]].values
        for item in items:
            txt=item[0]
            seg_list = jieba.cut(txt)
            num_lists=[]
            for seg in seg_list:
                try:
                    if big_dict[seg]:
                        num_list=big_dict[seg]
                        num_lists.append(num_list)
                except:
                    pass
            if len(num_lists)>0:
                num=np.zeros(5,dtype=np.float64)
                for i in num_lists:
                    nums=np.array(i,dtype=np.float64)
                    num=num+nums
                numlist_result=list((num/len(num_lists)))
                numlist_num=len(num_lists)
            else:
                numlist_result=list((np.zeros(5,dtype=np.float64)))
                numlist_num=0
            csv_text=[txt,numlist_num,numlist_result[0],numlist_result[1],numlist_result[2],numlist_result[3],numlist_result[4]]
            writer.writerow(csv_text)
def main():
    # big_dict={"不错":[1,1,1,1,1]}
    big_dict=read()
    print(big_dict)
    txt_emotions(big_dict)
if __name__ == '__main__':
    main()