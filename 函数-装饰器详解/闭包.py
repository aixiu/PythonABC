#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

"""
闭包：
    1、可以让一个变量常驻于内存
"""

def func():
    a = 10
    def inner():
        nonlocal a
        a += 1
        return a
    return inner

ret = func()

# inner => ret => 什么是时候执行

r1 = ret()
print(r1)
r2 = ret()
print(r2)
