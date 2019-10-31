#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   test1.py

@Time    :   2018/7/14 15:00

@Desc    :

'''
import json
import os

import numpy as np


# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     keys = sorted(keywords.keys())
#     for kw in keys:
#         print(kw, ":", keywords[kw])
#
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")

# b=lambda a: a-100 if a==100 else a-50
# print(b(100))

# matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12], ]
# for row in matrix:
#     print(row)
# print([[row[i] for row in matrix] for i in range(4)])
def generateDictionary(rootDir):
    word_dict = dict()
    for lists in os.listdir(rootDir):
        if lists[-3:] == "txt":
            tagName = lists[0:-4]
            print(tagName)
            word_list = list()
            path = os.path.join(rootDir, lists)
            print(path)
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    temp = line.strip()
                    if temp:
                        word_list.append(temp)
            word_dict[tagName] = word_list
    json.dump(word_dict, open("dictionary.json", "w", encoding="utf-8"), ensure_ascii=False)


if __name__ == '__main__':
    print(os.getcwd())
    path = 'E:/kgqca/practice/others/'
    generateDictionary(path)
