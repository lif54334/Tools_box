#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   txt_re_bom.py

@Time    :   2018/8/9 16:16

@Desc    :

'''
import os


def removeBom(file):
    '''移除UTF-8文件的BOM字节'''
    BOM = b'\xef\xbb\xbf'
    existBom = lambda s: True if s == BOM else False

    f = open(file, 'rb')
    if existBom(f.read(3)):
        fbody = f.read()
        # f.close()
        with open(file, 'wb') as f:
            f.write(fbody)


if __name__ == '__main__':
    path="F:/txt/txtbom"
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.find(".txt") != -1:
                print(file)
                removeBom(os.path.join(root, file))
