#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

"""
global：在局部，引入全局变量
nonlocal：在局部，引入外层的局部变量

"""

# 案例一
# a = 10

# def func():
#     # print(a)
#     # 此时我就想在函数内部修改全局的变量 a
#     global a  # 把外面的全局变量引入到局部
#     a = 20 # 创建一个局部变量，并没有去改变全局变量中的 a
    
# func()
# print(a)


# 案例二
def func():
    a = 10
    def func2():
        nonlocal a  # 赂外找一层，看看有没有该变量，如果有就引入，没果没有，就继续向外一层，直到全局（但不包括全局）
        a = 20
    func2()
    print(a)
    
func()