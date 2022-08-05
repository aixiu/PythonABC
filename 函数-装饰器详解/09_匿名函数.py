#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

"""
匿名函数：
    lambda表达式
    语法：
        变量 =  lambda 参数，参数2...: 返回值
"""

# def func():
#     print(123456)
#     return 9999

# ret = func()
# print(ret)

#计算 a+b的结果
# def func(a, b):
#     return a + b
# ret = func(12, 13)
# print(ret)


fn = lambda a, b: a + b
ret = fn(12, 13)
print(ret)