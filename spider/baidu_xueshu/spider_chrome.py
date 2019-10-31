#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   spider_chrome.py

@Time    :   2018/7/11 11:09

@Desc    :

'''

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')