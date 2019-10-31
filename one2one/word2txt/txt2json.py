#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   txt2json.py

@Time    :   2018/9/22 9:36

@Desc    :

'''
import json
import re
import numpy as np
import copy
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def static():
    nums = [0]
    nums = nums * 1000
    with open("cutlines.txt", "r", encoding="utf-8") as f:
        try:
            line = f.readline().strip('\n')
            # line = re.findall(r"'string': '(.+?)', 'entities'", line)
            # print(type(line))
            num = len(line)
            # print(line, num)
            nums[num] = nums[num] + 1
            while True:
                line = f.readline().strip('\n')
                # line = re.findall(r"'string': '(.+?)', 'entities'", line)
                num = len(line)
                # print(line, num)
                nums[num] = nums[num] + 1
        except:
            pass
    # print(nums)
    print("==========================")
    nums2 = copy.deepcopy(nums)
    for i in range(len(nums) - 1, -1, -1):
        if int(nums[i]) <=10:
            nums2.pop(i)
            # print("remove-----------------------------evomer")
        else:
            break
    # for n in nums[::-1]:
    #     if int(n) == 0:
    #         nums2.remove(n)
    #         # print("remove")
    #     else:
    #         break
    # print(nums2)
    with open("nums2.txt","w",encoding="utf-8")as fn:
        fn.write(str(nums2))
    print(sum(nums2[:200])/sum(nums2),sum(nums2[:250])/sum(nums2),sum(nums2[:300])/sum(nums2))
    return nums2, len(nums2)


def plot(ydata, nums):
    # print(ydata)
    print("开始绘制文本长度分布图")
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.hist(data, bins=nums)
    # plt.title('文本长度分布')
    # plt.xlabel('长度')
    # plt.ylabel('频率')
    # plt.show()
    xdata = [i for i in range(0, nums)]
    # print(xdata)

    fig = plt.figure()
    plt.bar(xdata, ydata, width=0.8, color="green")
    plt.xlabel("长度")
    plt.ylabel("频率")
    plt.title("文本长度分布")
    plt.show()

def main():
    ydata = list()
    ydata, nums = static()
    print(ydata)
    print(len(ydata))
    plot(ydata, nums)


if __name__ == '__main__':
    main()
