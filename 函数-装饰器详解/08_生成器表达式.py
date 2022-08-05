#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

"""
生成器表达式  -> 一次性的，用完一次再取值就为空
    语法：(数据 for循环 if判断)
"""

gen = (i**2 for i in range(10))
# print(next(gen))
# print(gen.__next__())


for item in gen:
    print(item)
    
lst = list(gen)
print(lst)

# s = list('周杰伦')   # list()  => for循环  => next()
# print(s)
