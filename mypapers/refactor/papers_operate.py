#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   papers_operate.py

@Time    :   2018/7/29 13:55

@Desc    :

'''

# !/usr/bin/env python
# -*- encoding: utf-8 -*-
import logging
import os
import random
import re
from datetime import time, datetime
import time
import docx2txt
from PyPDF2 import PdfFileWriter, PdfFileReader

'''
设置一些文件存放位置和其他参数
'''
pdf_seg_page = "F:/pdf/PDF/seg.pdf"  # 用来放置分隔符的pdf文件
source_pdf_path = "F:/pdf/PDFtest"  # 原始pdf文件夹
out_pdf_path1 = "F:/pdf/PDFmerge2/"  # 经过分隔符合并处理后的pdf文件存放处
out_pdf_path2 = "F:/pdf/PDFmergeall/"  # 暂时没用
mergenums = 2  # 暂时没用
docxpath = 'F:/txt/docx'  # docx文件地址
docx2txtpath = 'F:/txt/txtore'  # txt文件地址
all_FileNum = 0
flag = 0
txt_seg_path = "F:/txt/txtore"  # 放置需要分割处理的txt文件
txt_out_seg_path = "F:/txt/txtafter"  # 放置分割处理后的txt文件
txtcleanpath = "F:/txt/txtafter"  # 放置需要清洗处理的txt文件的地址
clean_txt_in = txtcleanpath
clean_txt_out = "F:/txt/txtclean"  # 放置清洗过后的txt文件的地址
rename_txt_path = "F:/txt/txtclean"  # 要进行更名的txt文件地址
t= (time.time())
dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))
print(dt)
'''
log模块(待完善)
'''
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='my.log',
                    filemode='a')
# 定义一个Handler打印INFO及以上级别的日志到sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# 设置日志打印格式
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%H:%M')
console.setFormatter(formatter)
# 将定义好的console日志handler添加到root logger
mylog=logging.getLogger('my.log')
mylog.addHandler(console)
# 设置propagate=0表示继承的源头，不会把log信息传给logging了
mylog.propagate=0
logging.info("ECUST----------ECUST")

'''
将一个文件夹下的pdf文件与我们的分隔符pdf进行合并（用来插入论文分隔符）
'''

def pdfmerge_2(pdfpage, inpath, outpath):
    print(inpath)  # 打印pdf操作文件夹
    for parent, dirnames, filenames in os.walk(inpath):
        print(dirnames)
        for filename in filenames:
            pdfout = PdfFileWriter()
            file_path = os.path.join(parent, filename)
            (shotname, extension) = os.path.splitext(filename)
            # print('文件名全称：%s' % filename)  # 文件名全称example:E公司M产品MOS管失效分析.pdf
            # print('文件后缀：%s' % extension)#文件后缀example：.pdf
            # print('文件名：%s' % shotname)#文件名example：E公司M产品MOS管失效分析
            # print('文件完整路径：%s\n' % file_path)#文件完整路径example：F:/pdf/PDFnoab\E公司M产品MOS管失效分析.pdf
            if extension == ".pdf":
                try:
                    pdf1 = PdfFileReader(open(file_path, 'rb'), strict=False)
                    numPages = pdf1.getNumPages()
                    for index in range(0, numPages):
                        pageObj = pdf1.getPage(index)
                        pdfout.addPage(pageObj)
                    pdf2 = PdfFileReader(open(pdfpage, 'rb'), strict=False)
                    pageObj = pdf2.getPage(0)
                    pdfout.addPage(pageObj)
                    outname = outpath + filename
                    # 最后,统一写入到输出文件中
                    pdfout.write(open(outname, 'wb'))
                except:
                    print("文件：%s 出错"% filename )
            else:
                continue


'''
将一个文件夹下的pdf文件全部合并（暂时没啥用）
'''


def pdfmerge_all(inpath, outpath, mergenums):
    filelist = list()
    for parent, dirnames, filenames in os.walk(inpath):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            (shotname, extension) = os.path.splitext(filename)
            # print('文件名全称：%s' % filename)
            # print('文件名：%s' % shotname)
            # print('文件完整路径：%s\n' % file_path)
            filelist.append(file_path)
    print(len(filelist))
    segnums = len(filelist) // mergenums
    # for file in filelist:
    #     print(file)
    for i in range(0, segnums):
        for file in filelist[(i * mergenums):((i + 1) * mergenums)]:
            print(file)
        print("ECUST保佑nobug")


def Translate(inpath, outpath):
    global all_FileNum
    fs = os.listdir(inpath)
    for f in fs:
        if (f[0] == '~' or f[0] == '.'):
            continue
        os.chdir(inpath)
        text = docx2txt.process(f)
        os.chdir(outpath)
        fname = os.path.splitext(f)[0]
        print("start transform:" + fname)
        with open(fname + ".txt", "w", encoding='utf-8') as f:
            for i in text:
                f.write(i)
            flag = 1
            if (flag == 1):
                print("transform ok")
            else:
                print("fail")
        all_FileNum = all_FileNum + 1
    print('转换文件总数 = ', all_FileNum)


def seg(inpath, outpath):
    p2 = outpath+'/'
    i = 0
    for parent, dirnames, filenames in os.walk(inpath):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            (shotname, extension) = os.path.splitext(filename)
            # print('文件名全称：%s' % filename)
            print('文件名：%s' % shotname)
            # print('文件完整路径：%s\n' % file_path)
            with open(file_path, "r", encoding="utf-8") as ft:
                lines = ft.readlines()
                for line in lines:
                    # print(line)
                    result = re.search(r'#################################################################', line)
                    if not result:
                        with open(p2 + "Failure_Analysis_paper" + str(i) + ".txt", "a", encoding="utf-8") as ftn:
                            ftn.write(line)
                    else:
                        i += 1
                        with open(p2 + "Failure_Analysis_paper" + str(i) + ".txt", "a", encoding="utf-8") as ftn:
                            ftn.write(line)
                        continue


def clean(name, clean_txt_in, clean_txt_out):
    inprocess = open(clean_txt_in + '/' + name + ".txt", 'r', encoding="utf-8")
    outprocess = open(clean_txt_out + '/' + name + ".txt", 'w', encoding="utf-8")
    for line in inprocess.readlines():  # 对每一行先删除空格，\n等无用的字符，再检查此行是否长度为0
        line = str(line).replace(" ", "").replace("\t", "").strip()
        if len(line) > 1:
            a = re.findall('[[\d+]([\d\D]{1,35})[[A-Z]]([\d\D]{1,35})', line)  # 参考文献
            b = re.findall('([\d\D]{1,6})期|([\d\D]{1,6})卷', line)
            c = re.findall('参考文献', line)
            d = re.findall('作者|邮箱|地址|杂志|期刊|报刊|文章编号|备注|收稿|接收日期|基金|附图|中图|文献标识码|DOI|电话|邮政编码|单位|学报|大学|编辑|編辑|下转|上接|本刊|综述', line)
            e = re.findall('([A-Za-z0-9啊-座,.+-]+){14}', line)  # 连续14个字母，数字，标点
            f = re.findall('\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*', line)  # 邮箱
            g = re.findall('[[a-zA-z]+://[^\s]*', line)  # 网址
            h = re.findall('\d{4}-\d{1,2}-\d{1,2}', line)  # 短日期
            i = re.findall('.*省(.+)医院.*', line)  # 地址    if len(f) == 0:    if len(g) == 0:
            j = re.findall('^[-+]\d+$ ', line)  # 只有整数
            k = re.findall('^[-+]?(\d+(\.\d*)?|\.\d+)[dD]?$', line)  # 只有小数
            l = re.findall('^\d{4}年\d{1,2}(月)$', line)  # 只有日期
            m = re.findall('^[A-Za-z0-9]+$', line)  # 只有英文或整数
            n = re.findall('^([A-Za-z0-9啊-座,.+-]+)$', line)  # 只有字母和标点
            o = re.findall(
                '^[A-Za-z0-9\一\二\三\四\五\六\七\八\九\十\,\，\丄\、\。\．\，\」\•\〜\£\♦\⑴\.\?\□\？\!\！\+\-\△\:\：\~\#\%\^\&\*\(\§\（\)\）\—\=\}\{\[\]\;\；\一\'\‘\’\"\“\_\°\”\<\《\》\>\|\/\【\】\■\±\〇]{1,}$',
                line)  # 只有字母和标点
            p = re.findall('^[[\d+]([\d\D]{1,60})\d{4}([\d\D]{1,20})$', line)  # 参考文献补充
            q = re.findall('^[0-9]+([.]{1}[0-9]+){0,1}±[0-9]+([.]{1}[0-9]+){0,1}$', line)  # 单位
            r = re.findall('\n\s*\r', line)  # 空行
            s = re.findall('^表|图\d+$', line)
            t = re.findall('^表|图\d+$', line)
            u = re.findall(
                '(辽宁|吉林|黑龙江|河北|山西|陕西|甘肃|青海|山东|安徽|江苏|浙江|河南|湖北|湖南|江西|台湾|福建|云南|海南|四川|贵州|广东|内蒙古|新疆|广西|西藏|宁夏|北京|上海|天津|重庆|香港|澳门 )([\d\D]{0,40})',
                line)
            v = re.findall('#################################################################', line)
            if len(a) == 0:
                if len(b) == 0:
                    if len(c) == 0:
                        if len(d) == 0:
                            if len(e) == 0:
                                if len(f) == 0:
                                    if len(g) == 0:
                                        if len(h) == 0:
                                            if len(i) == 0:
                                                if len(j) == 0:
                                                    if len(k) == 0:
                                                        if len(l) == 0:
                                                            if len(m) == 0:
                                                                if len(n) == 0:
                                                                    if len(o) == 0:
                                                                        if len(p) == 0:
                                                                            if len(q) == 0:
                                                                                if len(r) == 0:
                                                                                    if len(s) == 0:
                                                                                        if len(t) == 0:
                                                                                            if len(u) == 0:
                                                                                                if len(
                                                                                                        v) == 0: outprocess.write(
                                                                                                    line + '\n')

    inprocess.close()
    outprocess.close()


def txtrename(rename_txt_path):
    i=1
    # oldpath=rename_txt_path+'/'
    num = random.randint(0, 10000)
    for parent, dirnames, filenames in os.walk(rename_txt_path):
        # parent=parent+'/'
        print(parent)
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            (shotname, extension) = os.path.splitext(filename)
            if extension == ".txt":
                # print('文件名全称：%s' % filename)
                # print('文件名：%s' % shotname)
                # print('文件完整路径：%s\n' % file_path)
                with open(file_path, 'r', encoding="utf-8")as f:
                    line = f.readline()
                newline = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", line)
                newline1=''.join(newline)
                newline2=newline1.replace(".","").replace("】","").replace("，","").replace("-","").replace("：","").replace("■","").replace("}","").replace("⑷","").replace("+","").replace("()","").replace("（)","").replace("——","")
                try:
                    name = (newline2[:-1] +str(i)+ ".txt")
                    oname = ''.join(name)
                    #print(type(oname))
                    oname=oname.replace("\\","").replace("\",").replace("//","").replace("»","").replace("\'","").replace("\"","")
                    oname = oname.replace('*', '').replace('◄', '').replace(':', '').replace('"', '').replace("@","").replace("^","").replace("__","").replace("~","").replace("【","").replace("•","").replace("©","").replace("、","")
                    #print(oname)
                    oldname = file_path
                    #print("oldname: %s" % oldname)
                    newname = os.path.join(parent, oname)
                    print("newname: %s" % newname)
                    os.renames(oldname, newname)
                    i=i+1

                except :
                    pass

            else:
                continue


def main():
    # Translate(docxpath, docx2txtpath)  # 进行docx to txt的转换
    # seg(txt_seg_path,txt_out_seg_path)  # 进行txt文件按照分隔符处理分割为小文件
    fs = os.listdir(txtcleanpath)  # 进行txt文件的清理
    for f in fs:
        if (f[0] == '~' or f[0] == '.'):
            continue
        fname = os.path.splitext(f)[0]
        print("clean:" + fname)
        clean(fname, clean_txt_in, clean_txt_out)
    txtrename(rename_txt_path)


if __name__ == '__main__':
    # pdfmerge_2(pdf_seg_page, source_pdf_path, out_pdf_path1)  # 进行分隔符合并处理
    # pdfmerge_all(inpath, outpath2, mergenums)
    # 然后这时利用ABBYY对加入了分隔符的pdf文件进行转换为docx格式
    main()  # 进行docx转txt，txt分割，txt清洗，txt重命名一系列操作
