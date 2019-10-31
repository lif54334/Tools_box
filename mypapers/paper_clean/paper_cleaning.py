import re
import os

def clean(name):

 fp= open('F:/txt/txtdb/ore/'+name+".txt",'r',encoding="utf-8")
 fo=open('F:/txt/txtdb/resu/'+name+".txt",'w',encoding="utf-8")
 for line in fp.readlines():  # 对每一行先删除空格，\n等无用的字符，再检查此行是否长度为0
    line = str(line).replace(" ", "").replace("\t", "").strip()
    if len(line) > 1:
        a = re.findall('[[\d+]([\d\D]{1,35})[[A-Z]]([\d\D]{1,35})', line)  # 参考文献
        b = re.findall('([\d\D]{1,6})期|([\d\D]{1,6})卷', line)
        c = re.findall('参考文献', line)
        d = re.findall('作者|邮箱|地址|杂志|期刊|报刊|文章编号|备注|收稿|接收日期|基金|附图|中图|文献标识码|DOI|电话|邮政编码|单位|学报|大学|编辑|編辑|下转|上接|本刊', line)
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
        o = re.findall('^[A-Za-z0-9\一\二\三\四\五\六\七\八\九\十\,\，\丄\、\。\．\，\」\•\〜\£\♦\⑴\.\?\□\？\!\！\+\-\△\:\：\~\#\%\^\&\*\(\§\（\)\）\—\=\}\{\[\]\;\；\一\'\‘\’\"\“\_\°\”\<\《\》\>\|\/\【\】\■\±\〇]{1,}$', line)  # 只有字母和标点
        p = re.findall('^[[\d+]([\d\D]{1,60})\d{4}([\d\D]{1,20})$', line)  # 参考文献补充
        q = re.findall('^[0-9]+([.]{1}[0-9]+){0,1}±[0-9]+([.]{1}[0-9]+){0,1}$', line)  # 单位
        r = re.findall('\n\s*\r', line)  # 空行
        s = re.findall('^表|图\d+$', line)
        t = re.findall('^表|图\d+$', line)
        u = re.findall('(辽宁|吉林|黑龙江|河北|山西|陕西|甘肃|青海|山东|安徽|江苏|浙江|河南|湖北|湖南|江西|台湾|福建|云南|海南|四川|贵州|广东|内蒙古|新疆|广西|西藏|宁夏|北京|上海|天津|重庆|香港|澳门 )([\d\D]{0,40})', line)
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
                                                                                        if len(u) == 0:fo.write(line+'\n')


 fp.close()
 fo.close()

if __name__ == '__main__':
    inpath="F:/txt/txtdb/ore"   #放置需要处理的txt文件的地址
    fs = os.listdir(inpath)
    for f in fs:
        if (f[0] == '~' or f[0] == '.'):
            continue
        fname=os.path.splitext(f)[0]
        print("transform:"+fname)
        clean(fname)
