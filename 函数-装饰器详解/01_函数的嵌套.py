#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

# def func():
#     def inner():
#         print(123)
#     print(inner)   # <function func.<locals>.inner at 0x00000190FE026290>
#     return inner
#     # 函数内部的东西，只有 return 才能被外边访，内部函数可当成变量一样返回。
    
# b1 = func()   # b1 是函数 func 的内部函数 inner

# #此时 如果想执行内部  inner函数 就可以写成 b1()
# print(b1)  # <function func.<locals>.inner at 0x00000190FE026290>
# # b1的内存地址和 上边 inner内存地址是相同的，也就是 b1 就是 inner
# b1()


# def an():
#     print(123)
    
# an()
# bn = an
# bn()
# # 以上结论 函数就可以当成一个变量来看待


# 代理模式
def func(an):  # 如果 an收到的是一个函数
    # print(an)
    an()  # 可以函数名 + () 执行这个函数
    
def target():
    print('我是target')
    
# c = 456
# func(c)

func(target)  # 实参可以是函数


# 综上结论： 
# 1、函数可以作为返回值进行返回
# 2、函数可以作为参数进行互相传递
# 函数名实际上就是一个变量，都表示一个内存地址

