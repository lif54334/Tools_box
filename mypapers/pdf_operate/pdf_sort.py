#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   pdf_sort.py

@Time    :   2018/7/7 9:19

@Desc    :

'''
import sys
import os
import re
from unittest import result

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser, PDFDocument


def sortbyab(path):
    abpath="F:/pdf/PDFab/"
    noabpath="F:/pdf/PDFnoab/"
    pattern1 = re.compile(r'摘要|摘　要')
    pattern2 = re.compile(r'\n')
    for parent, dirnames, filenames in os.walk(path):
        for filename in filenames:
            result = []
            file_path = os.path.join(parent, filename)
            print('文件名：%s' % filename)
            print('文件完整路径：%s\n' % file_path)
            with open(file_path,"rb") as fp:
                praser = PDFParser(fp)
                # 创建一个PDF文档
                doc = PDFDocument()
                # 连接分析器 与文档对象
                praser.set_document(doc)
                doc.set_parser(praser)
                # 提供初始化密码
                # 如果没有密码 就创建一个空的字符串
                doc.initialize()
                # 检测文档是否提供txt转换，不提供就忽略
                if not doc.is_extractable:
                    raise PDFTextExtractionNotAllowed
                # 创建PDf 资源管理器 来管理共享资源
                rsrcmgr = PDFResourceManager()
                # 创建一个PDF设备对象
                laparams = LAParams()
                device = PDFPageAggregator(rsrcmgr, laparams=laparams)
                # 创建一个PDF解释器对象
                interpreter = PDFPageInterpreter(rsrcmgr, device)
                pdfStr = ''
                # 循环遍历列表，每次处理一个page的内容
                for page in doc.get_pages():  # doc.get_pages() 获取page列表
                    interpreter.process_page(page)
                    # 接受该页面的LTPage对象
                    layout = device.get_result()
                    for x in layout:
                        if hasattr(x, "get_text"):
                            # print x.get_text()
                            result.append(x.get_text())
                result.replace('\n','')
                print(result)

if __name__ == '__main__':
    path="F:/pdf/PDF/"
    sortbyab(path)