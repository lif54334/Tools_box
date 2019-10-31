#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   txt_seg.py

@Time    :   2018/7/7 13:05

@Desc    :

'''

import os
import re

def seg(inpath):
    p2="F:/txt/txtafter/"
    i=0
    for parent, dirnames, filenames in os.walk(inpath):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            (shotname, extension) = os.path.splitext(filename)
            #print('文件名全称：%s' % filename)
            print('文件名：%s'% shotname)
            #print('文件完整路径：%s\n' % file_path)
            with open(file_path,"r",encoding="utf-8") as ft:
                lines=ft.readlines()
                for line in lines:
                    #print(line)
                    result = re.search(r'#################################################################', line)
                    if  not result:
                        with open(p2+"Failure_Analysis_paper"+str(i)+".txt", "a",encoding="utf-8") as ftn:
                            ftn.write(line)
                    else:
                        i+=1
                        with open(p2+"Failure_Analysis_paper"+str(i)+".txt", "a",encoding="utf-8") as ftn:
                            ftn.write(line)
                        continue


if __name__ == '__main__':
    p1="F:/txt/ore/"
    seg(p1)