#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   json_w_txt.py

@Time    :   2018/7/23 22:02

@Desc    :

'''

import os
import json

def json2txt_1_0():
    with open("data.txt", 'w', encoding='utf8')as f:
        truedict = json.load(open('true_all_814.json', 'r', encoding="utf-8"))
        keys = list(set(truedict.keys()))
        for key in keys:
            words1 = truedict[key]
            for word in words1:
                if word==' ':
                    print("发现空白")
                    continue
                else:
                    text = word + ' ' + '1' + '\n'
                    f.write(text)
        wrongdict = json.load(open('wrong_all_814.json', 'r', encoding="utf-8"))
        keys = list(set(wrongdict.keys()))
        for key in keys:
            words2 = wrongdict[key]
            for word in words2:
                if word==' ':
                    print("发现空白")
                    continue
                else:
                    text = word + ' ' + '0' + '\n'
                    f.write(text)
def json2txt(inname,outname):
    infile=inname+'.json'
    outfile=outname+'.txt'
    with open(outfile, 'w', encoding='utf-8')as f:
        dict = json.load(open(infile, 'r', encoding="utf-8"))
        keys = list(set(dict.keys()))
        for key in keys:
            words = dict[key]
            for word in words:
                if word==' ':
                    print("发现空白")
                    continue
                else:
                    text = word+'\n'
                    f.write(text)

if __name__=="__main__":
    inname="dictionary_third"
    outname="test"
    #json2txt(inname,outname)
    json2txt_1_0()