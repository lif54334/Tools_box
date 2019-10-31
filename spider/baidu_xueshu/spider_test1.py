import re

i="0.13μm IC产品MM模式ESD失效机理"
j={"title": "0.13μm IC产品MM模式ESD失效机理", "author": "吴峰霞/申俊亮/蔡斌", "abstract": "对静电放电(ESD)测试所得到的失效样品进行了物理失效分析,采用塑封体背面研磨、光发射显微镜(EMMI)从背面抓取热点的方法进行异常现象定位,通过剥层技术查找发生在...", "urls": "http://xueshu.baidu.com/usercenter/paper/show?paperid=64a540e84fa39b7a4005ecfa86603a30&site=xueshu_se", "time": ["2013年"], "publish": ["《半导体技术》"]}
print(re.findall(str(i),str(j["title"])))