#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   pdf_txt_sort.py

@Time    :   2018/7/7 10:58

@Desc    :

'''
import os
import re
import shutil


def sortbytxt(txtpath, pdfab, pdfnoab,pdfore):
    for parent, dirnames, filenames in os.walk(txtpath):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            (shotname, extension) = os.path.splitext(filename)
            # print('文件名全称：%s' % filename)
            print('文件名：%s' % shotname)
            # print('文件完整路径：%s\n' % file_path)
            with open(file_path, "r", encoding="utf-8") as ft:
                lines = ft.readlines()
                for line in lines:
                    result = re.search(r'摘要|摘　要|要：|要:|文 摘', line)
                    # print(result)
            try:
                if result:
                    os.renames(pdfore + shotname + ".pdf", pdfab + shotname + ".pdf")
                else:
                    os.renames(pdfore + shotname + ".pdf", pdfnoab + shotname + ".pdf")
            except FileNotFoundError:
                pass
            continue


if __name__ == '__main__':
    p1 = "F:/txt/txtdb/resu/"  # 放置txt文件的地址
    p2 = "F:/pdf/PDFab/"  # 放置带摘要的pdf文件地址
    p3 = "F:/pdf/PDFnoab/"  # 放置不带摘要pdf文件地址
    p4 = "F:/pdf/PDFdb/"  # 放置原始pdf文件地址
    sortbytxt(p1, p2, p3,p4)
