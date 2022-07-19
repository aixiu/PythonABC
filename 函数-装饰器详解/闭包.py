#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

"""

"""

def func():
    a = 10
    def inner():
        print(a)
        return a
    return(inner)

ret = func()

# inner => ret => 什么是时候执行

ret()