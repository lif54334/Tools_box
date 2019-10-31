#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
author:Herish
datetime:2019/3/11 17:23
software: PyCharm
description: 在百度学术网站下载论文参考文献
后续学习可以参考：https://blog.csdn.net/llh_1178/article/details/80558274
'''
import random
import time

import requests, os, re
from collections import namedtuple
from urllib.parse import urlencode
from urllib import parse
from bs4 import BeautifulSoup
import json
from fake_useragent import UserAgent


def get_page(title, offset):
    head = {}
    head['User-Agent'] = UserAgent().random
    params = {
        'wd': title,
        'pn': offset,
        'tn': 'SE_baiduxueshu_c1gjeupa',
        'ie': 'utf-8',
        'sc_hit': '1'
    }
    url = "http://xueshu.baidu.com/s?" + urlencode(params)
    # proxy_list = [
    # {"http" : "http://117.90.252.143:9000"},
    # {"http" : "http://180.118.247.233:9999"},
    # {"http" : "http://183.129.244.16:11006"},
    # {"http" : "http://121.232.194.21:9000"},
    # {"http" : "http://60.13.42.31:9999"},
    # {"http" : "http://125.110.120.214:9000"},
    # {"http" : "http://120.234.138.102:53779"},
    # {"http" : "http://1.197.203.27:9999"},
    # {"http" : "http://125.123.141.70:9999"},
    # {"http" : "http://39.106.127.234:80"}
    # ]
    # proxys = random.choice(proxy_list)
    #
    # print(proxys)
    try:
        response = requests.get(url, headers=head)
        if response.status_code == 200:
            return response.text
    except requests.ConnectionError:
        return None


# 对于每页的文献信息（每页基本包含10篇文献），提取所有的文献主题、作者、摘要、文献详细地址
def get_urls(text):
    all_titles = []  # 主题
    all_abstracts = []  # 摘要
    all_authors = []  # 作者
    all_paper_urls = []  # 论文初步网址
    all_publish = []  # 论文来源
    all_time = []  # 论文时间

    soup = BeautifulSoup(text, 'lxml')

    title_datas = soup.select('div.sc_content > h3 > a')  # select返回值类型为<class 'list'>

    author_datas = soup.find_all('div', 'sc_info')  # find_all返回值类型为<class 'bs4.element.ResultSet'>

    abstract_datas = soup.find_all('div', 'c_abstract')

    publish_datas = soup.find_all('div', 'sc_info')

    time_datas = soup.find_all('div', 'sc_info')
    for item in title_datas:
        result = {
            'title': item.get_text(),
            'href': item.get('href')  # 关于论文的详细网址，经过观察发现需要提取部分内容
            # http://xueshu.baidu.com/usercenter/paper/show?paperid=389ef371e5dae36e3a05b187f7eb2a95&site=xueshu_se
            # /s?wd=paperuri%3A%28389ef371e5dae36e3a05b187f7eb2a95%29&filter=sc_long_sign&sc_ks_para=q%3D%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E7%A0%94%E7%A9%B6%E7%BB%BC%E8%BF%B0&sc_us=11073893925633194305&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8
        }
        all_titles.append(item.get_text())
        wd = str(parse.urlparse(item.get('href')).query).split('&')[0]
        paperid = wd.split('%')[2][2:]
        params = {
            'paperid': paperid,
            'site': 'xueshu_se'
        }
        url = 'http://xueshu.baidu.com/usercenter/paper/show?' + urlencode(params)
        all_paper_urls.append(url)
        # print(url)
        # print(result)

    for abs in abstract_datas:  # abs类型是<class 'bs4.element.Tag'>
        str_list = []
        for l in abs.contents:  # l的类型是<class 'bs4.element.NavigableString'>
            if str(l).replace('\n', '').strip():
                str_list.append(str(l).replace('\n', '').strip())
            else:
                str_list.append("unknown")
        # print("".join(str_list).replace('<em>','').replace('</em>',''))
        all_abstracts.append("".join(str_list).replace('<em>', '').replace('</em>', ''))

    for authors in author_datas:  # authors类型为<class 'bs4.element.Tag'>
        for span in authors.find_all('span', limit=1):  # 此时span类型为<class 'bs4.element.Tag'>
            each_authors = []
            for alist in span.find_all('a'):
                if alist.string is None:
                    each_authors.append("unknown")
                else:
                    each_authors.append(alist.string)
            all_authors.append(each_authors)

    for publish in publish_datas:  # authors类型为<class 'bs4.element.Tag'>
        each_publish = []
        spans = publish.find_all('span')  # 此时span类型为<class 'bs4.element.Tag'>
        spans = str(spans)
        try:
            publish_name = re.search(r'《.*》', spans)
            publish_name = publish_name.group()
        except:
            publish_name = "unknown"

        each_publish.append(publish_name)
        all_publish.append(each_publish)

    for time in time_datas:  # authors类型为<class 'bs4.element.Tag'>
        each_time = []
        for span in time.find_all('span', {"class": "sc_time"}):  # 此时span类型为<class 'bs4.element.Tag'>
            time_name = "unknown"
            for alist in span:
                try:
                    alist.string = ((alist.string).strip())
                    time_name=alist.string
                except:
                    time_name="unknown"
            each_time.append(time_name)
        all_time.append(each_time)

    return all_titles, all_authors, all_abstracts, all_paper_urls, all_publish, all_time


paper = namedtuple('paper', ['title', 'author', 'abstract', 'download_urls', 'publish', 'time'])


# namedtuple()是产生具有命名字段的元组的工厂函数。命名元组赋予元组中每个位置的意义，并更易读、代码更易维护。
# 它们可以使用在通常元组使用的地方，并添加了通过名称访问字段的能力，而不是位置索引
def set_paper(all_titles, all_authors, all_abstracts, all_paper_urls, all_publish, all_time):
    print(len(all_titles), len(all_authors), len(all_abstracts), len(all_paper_urls), len(all_publish), len(all_time))
    papers = [paper(all_titles[i], all_authors[i], all_abstracts[i], all_paper_urls[i], all_publish[i], all_time[i]) for
              i in range(len(all_titles))]
    return papers


# 获取每个文献页面的详细信息
def get_download(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.ConnectionError:
        return None


# 对于每个文献页面爬取的详细页面内容进行提取，找出所有可免费下载的地址
def get_download_urls(text):
    download_urls = []

    pattern = re.compile('<a.*?class="dl_item".*?href="(.*?)".*?<span.*?class="dl_lib">(.*?)</span>', re.S)
    results = re.findall(pattern, text)
    for item in results:
        each_data = {
            'url': item[0],
            'download': item[1]
        }
        if "免费" in each_data.get('download'):
            download_urls.append(each_data.get('url'))
            # print(each_data)
    return download_urls


# 将文献主题、作者、摘要、下载路径转换成字典保存，使用json进行存储
def save_data(papers):
    json_papers = []
    for paper in papers:
        each_data = {
            'title': paper[0],
            'author': "/".join(paper[1]),
            'abstract': paper[2],
            'urls': paper[3],
            'time': paper[5],
            'publish': paper[4]

        }
        json_papers.append(each_data)

    with open('baidu_xueshu.txt', 'a', encoding='utf-8') as f:
        for paper in json_papers:
            f.write(json.dumps(paper, ensure_ascii=False) + '\n')


def read():
    with open("paper_title.txt", "r", encoding="utf8")as f:
        titles = f.readlines()
    return titles


def main():
    # # -------- 程序入口处 ------------------
    # titles=read()
    # for title in titles:
    #     # print(random.random() * 10)
    #     time.sleep(random.random() * 10)
    title = "12.9级内六角圆柱螺栓断裂失效分析"
    # # keywords = str(input("请输入在百度学术网站需要查询的关键词：\n"))
    print("开始爬取百度学术网站关于“{}”关键词的相关内容".format(title))
    for i in range(1):
        print("开始爬取第{}页的内容".format(str(i + 1)))
        offset = i * 10
        text = get_page(title, offset)
        all_titles, all_authors, all_abstracts, all_paper_urls, all_publish, all_time = get_urls(text)
        papers = set_paper(all_titles, all_authors, all_abstracts, all_paper_urls, all_publish, all_time)
        save_data(papers)

    print("保存成功！")


if __name__ == '__main__':
    main()
