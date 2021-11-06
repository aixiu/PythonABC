#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu


import os  # 和操作系统相关的模块
import time # 和时间相关的模块

import pathlib

# 案例文本原始内容

'''第一行
第二行
第三行
第四行
猜猜这是第几行？
猜猜这是第几行？
张观博
张欣竹
张欣阳
张刚军

李扬阳
李靖阳
李熙阳'''

# 文件修改   把文件中的  李 -> 汪

with open("./test.txt", mode="r", encoding="utf-8") as f1, \
    open("test_副本.txt", mode="w", encoding="utf-8") as f2:
    for line in f1:
        # 由于字符串为不可变类型，不能直接修改，此用，重新赋值给原字符串方式达到目地。
        line = line.strip()   
        if line.startswith("李"):   # 第一个字符  startwith
            line = line.replace("李", "汪")  # 同理，字符串不可修改。  replace 替换

        f2.write(line)
        f2.write("\n")
             
         
time.sleep(2)
# 删除源文件
os.remove("./test.txt")
time.sleep(2)
# 把副本文件重命名为源文件名
os.rename("test_副本.txt", "./test.txt")