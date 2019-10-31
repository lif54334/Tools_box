#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader

def pdfmerge2(inpath,pdfpage,outpath):
    for parent, dirnames, filenames in os.walk(inpath):
        for filename in filenames:
            pdfout = PdfFileWriter()
            file_path = os.path.join(parent, filename)
            (shotname, extension) = os.path.splitext(filename)
            print('文件名全称：%s' % filename)
            #print('文件名：%s' % shotname)
            # print('文件完整路径：%s\n' % file_path)
            pdf1 = PdfFileReader(open(file_path, 'rb'),strict=False)
            numPages = pdf1.getNumPages()
            for index in range(0, numPages):
                pageObj = pdf1.getPage(index)
                pdfout.addPage(pageObj)
            pdf2 = PdfFileReader(open(pdfpage, 'rb'),strict=False)
            pageObj = pdf2.getPage(0)
            pdfout.addPage(pageObj)
            outname = outpath + filename
            # 最后,统一写入到输出文件中
            pdfout.write(open(outname, 'wb'))

def pdfmergeall(inpath,outpath,mergenums):
    filelist=list()
    for parent, dirnames, filenames in os.walk(inpath):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            (shotname, extension) = os.path.splitext(filename)
            #print('文件名全称：%s' % filename)
            #print('文件名：%s' % shotname)
            # print('文件完整路径：%s\n' % file_path)
            filelist.append(file_path)
    print(len(filelist))
    segnums=len(filelist)//mergenums
    # for file in filelist:
    #     print(file)
    for i in range(0,segnums):
        for file in filelist[(i*mergenums):((i+1)*mergenums)]:
            print(file)
        print("###########")




if __name__=='__main__':
    pdfpage = "F:/pdf/PDF/seg.pdf"
    inpath = "F:/pdf/PDFnoab"
    outpath1 = "F:/pdf/PDFmerge2/"
    outpath2="F:/pdf/PDFmergeall/"
    mergenums=2
    pdfmerge2(pdfpage,inpath,outpath1)
    #pdfmergeall(inpath,outpath2,mergenums)