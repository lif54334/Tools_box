#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   csv_calibrate.py

@Time    :   2018/7/4 14:56

@Desc    :

'''

import os
import csv
import numpy

def calibrate(path):

    files = os.listdir(path)
    for file in files:
        print(file)
        with open (path+file,"r") as csvf:
            reader1 = csv.reader(csvf,delimiter=',')
            print(reader1)
            # rows = [row for row in reader]
            # hnum=len((rows[0]))
            # print(hnum)
            for i, r in enumerate(reader1):
                if i == 0:
                    line = r
                    print(line)
        with open(path + file, "r") as csvf:
            reader2 = csv.DictReader(csvf, delimiter=',')
            for i in range(4):
                str =  line[i]
                print(str)
                rows = [row[str] for row in reader2 ]
                print(rows)




if __name__ == '__main__':
    path="F:/sql/fsqca/test/"
    calibrate(path)