#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {lif54334}

@Software:   PyCharm

@File    :   linecut.py

@Time    :   2018/9/28 21:34

@Desc    :

'''
import re


def cut():
    with open("cutlines.txt", "w", encoding="utf-8")as f:
        print("start")
        with open("lines.txt", 'r', encoding='utf-8')as fls:
            try:
                # print("start")
                line = fls.readline().strip('\n')
                # print(len(line))
                if len(line)>150:
                    # print(line)
                    # print("yes")
                    linelist = line.split('。')
                    # print(linelist)
                    for element in linelist:
                        print("start======================")
                        print(element+"\n")
                        f.write(str(element) + "\n")

                else:
                    f.write(line + "\n")
                while line:
                    line = fls.readline().strip('\n')
                    # print(len(line))
                    # print("yes")
                    if len(line)>150:
                        # print(line)
                        linelist = line.split('。')
                        # print(linelist)
                        for element in linelist:
                            # print("start======================")
                            # print(element + "\n")
                            if element=='':
                                pass
                            else:
                                f.write(str(element) + "\n")
                    else:
                        f.write(line + "\n")
            except:
                pass
    print("over")
    print("start2")
    with open("cutlines.txt", "r", encoding="utf-8")as f2:
        with open("cutlines_over.txt", "w", encoding="utf-8")as f3:
            line = f2.readline().strip('\n')
            if len(line) <= 150:
                f3.write(str(line) + "\n")
            else:
                pass
            while line:
                line = f2.readline().strip('\n')
                if len(line) <= 150:
                    f3.write(str(line) + "\n")
                else:
                    pass

    print("over2")



def main():
    cut()


if __name__ == '__main__':
    main()
