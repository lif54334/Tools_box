#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   doctor_paper.py

@Time    :   2019/9/22 16:34

@Desc    :

'''
import json
import random
import re
import time

import pymysql
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

db = pymysql.connect("localhost", "root", "1234", "hdf")
cursor = db.cursor()
papers_dict = dict()


def get_url():
    url_dict=dict()
    try:
        cursor.execute('SELECT art_cate_href,title,paper_id from paper_hdf')
        db.commit()
        results = cursor.fetchall()
        for item in results[:10]:
            id=item[2]
            url_dict[id]=item[0]
    except Exception as e:
        print(e)
        print("Error: unable to fetch data")
    db.close()
    return url_dict

def get_page(url):
    head = {}
    head['User-Agent'] = UserAgent().random
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
        print("error")
        return None

def craw_list(url,text):
    paper_text=[]
    id=re.match(".*(\_\\d+)", url)
    id=id.group(1)[1:]
    soup = BeautifulSoup(text, 'lxml')
    page_txt=soup.select('body > div.content_2.clearfix > div.article_l > div.bg_w.mb20 > div > div.pb20.article_detail > p')
    for item in page_txt:
        paper_txt=str(item.get_text())
        # print(len(paper_txt))
        paper_txt=paper_txt.strip('\n')
        paper_txt=paper_txt.replace(u'\xa0', u' ')
        paper_text.append(paper_txt)
    paper_str="".join(paper_text)
    papers_dict[id]=paper_str
    return papers_dict

def search_url(id,url):
    paper_urls=[]
    text=get_page(url)
    soup = BeautifulSoup(text,'lxml')
    div=soup.select('body > div.content_2.clearfix > div.article_l > div.doc_article.fs > ul > li> div>p>a.art_t')

    for item in div:
        paper_url='http:'+str(item.get('href'))
        print(paper_url)
        paper_urls.append(paper_url)
    return paper_urls



def paper_spider(urls):
    for key in urls:
        time.sleep(random.random() * 10)
        print(key,urls[key])
        urls2=search_url(key,urls[key])
        for url in urls2:
            text=get_page(url)
            papers_dict=craw_list(url,text)
    # print(papers_dict)
    json_str = json.dumps(papers_dict,ensure_ascii=False,indent=4)
    with open('doctor.json', 'w',encoding='utf8') as json_file:
        json_file.write(json_str)

def main():
    urls=get_url()
    paper_spider(urls)
if __name__ == '__main__':
    main()
