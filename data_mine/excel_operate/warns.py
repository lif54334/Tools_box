import os
import pandas as pd


# 将文件读取出来放一个列表里面

pwd = 'F:\\文档\\论文\\小论文3\\单据与车辆\\mancar\\' # 获取文件目录

# 新建列表，存放文件名
file_list = []

# 新建列表存放每个文件数据(依次读取多个相同结构的Excel文件并创建DataFrame)
dfs = []

for root,dirs,files in os.walk(pwd): # 第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件。
  for file in files:
    file_path = os.path.join(root, file)
    file_list.append(file_path) # 使用os.path.join(dirpath, name)得到全路径
    df = pd.read_excel(file_path) # 将excel转换成DataFrame
    dfs.append(df)

# 将多个DataFrame合并为一个
df = pd.concat(dfs)

# 写入excel文件，不包含索引数据
df.to_excel('F:\\文档\\论文\\小论文3\\单据与车辆\\test\\mancar.xlsx', index=False)
