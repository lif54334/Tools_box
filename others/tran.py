#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   tran.py

@Time    :   2018/11/28 9:43

@Desc    :

'''

# -*- coding: utf-8 -*-
from imp import reload

"""
百度翻译api，先读入pdf的内容，再调用百度翻译的api来得到翻译后的内容
"""

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator
import os
import http.client
import hashlib
import urllib
import random
import json
import re
from urllib import parse



def translate_txt(paper):
    appid = '20181128000240330'  # 你的appid
    secretKey = 'lFWmeUYpWxKjwYVs25UV'  # 你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'

    q = paper
    # q = 'apple'
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)

    sign = appid + q + str(salt) + secretKey
    m1 = hashlib.md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        web_code = response.read()
        param = json.loads(web_code, encoding='utf-8')
        print(param['trans_result'][0]['dst'])
        return param['trans_result'][0]['dst']

    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()


def readpdf2txt(fp):
    # 来创建一个pdf文档分析器
    parser = PDFParser(fp)
    # 创建一个PDF文档对象存储文档结构
    document = PDFDocument(parser)
    # 检查文件是否允许文本提取
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建一个PDF资源管理器对象来存储共赏资源
        rsrcmgr = PDFResourceManager()
        # 设定参数进行分析
        laparams = LAParams()
        # 创建一个PDF设备对象
        # device=PDFDevice(rsrcmgr)
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # 处理每一页
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open('output.txt', 'a') as f:
                        f.write(x.get_text())
                        # raw_paper = x.get_text()
                        # rel = translate_txt(raw_paper)
                        # f.write(str(rel) + '\n')
                        print('lalala')


if __name__ == '__main__':
    '''''
     解析pdf 文本，保存到txt文件中
    '''
    print('start')
    path = 'C:/Users/lif/Desktop/文档/课程作业/知识管理/英文文献/Review_Knowledgemanagement.pdf'  # 文档的位置

    pdfFile = open(path, 'rb')
    readpdf2txt(pdfFile)
    print('done')
    pdfFile.close()