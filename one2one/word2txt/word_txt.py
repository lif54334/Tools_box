# coding=UTF-8
import docx2txt
import os,sys


def Translate(inpath,outpath):
    global all_FileNum
    fs=os.listdir(inpath)

    for f in fs:
        if (f[0] == '~' or f[0] == '.'):
            continue
        os.chdir(inpath)
        text = docx2txt.process(f)
        os.chdir(outpath)
        fname=os.path.splitext(f)[0]
        print("start transform:"+fname)
        with open(fname+".txt","w",encoding='utf-8') as f:
            for i in text:
                f.write(i)
            flag=1
            if(flag==1):
              print("transform ok")
            else:
              print("fail")
        all_FileNum = all_FileNum + 1

if __name__ == '__main__':

    docxpath = 'E:/kgqca/practice/word2txt/docx' #docx文件地址
    txtpath = 'E:/kgqca/practice/word2txt/txt' #txt文件地址
    all_FileNum = 0
    flag = 0
    Translate(docxpath, txtpath)
    print('转换文件总数 = ', all_FileNum)
