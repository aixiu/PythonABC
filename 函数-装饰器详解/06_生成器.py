#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

"""
生成器(generator)：
    生成器的本质就是迭代器
    
    创建生成器的两种方案：
        1.生成器函数
        2.生成器表达式
    
    生成器函数
        特性
            1.生成器函数中有一个关键字 yield
            2.生成器函数执行的时候，得到的是生成器，
            
    yield:
        作用：
            1.可以返回数据
            2.可以分段的执行函数中的内容，通过 __next__() 可以执行到下一个 yield的位置
"""

# def func():
#     print(123456)
#     yield 999   # yield 也有反回的意思

# ret = func()
# # print(ret)   # <generator object func at 0x0000029EE2D48430>

# ret.__next__()
# print(ret.__next__())   # yield 只有执行到 next的时候才会返回数据


# def func():
#     print(123)
#     yield 666
#     print(456)
#     yield 999
    
# ret = func()
# print(ret.__next__())
# print(ret.__next__())


# 案例
# 去工厂定制 1000 件衣服

# def order():
#     lst = []
#     for i in range(1000):
#         lst.append(f'衣服{i}')
#     return lst

# lst = order()
# print(lst)

def order():
    lst = []
    for i in range(1000):
        lst.append(f'衣服{i+1}')
        if len(lst) == 50:
            yield lst
            lst = []
            
gei = order()
print(gei.__next__())
print(gei.__next__())
