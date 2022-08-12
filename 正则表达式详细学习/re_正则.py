#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

import re

'''
正则表达式
    一，字符串的匹配
'''
# 普通字符
    # 大多数字母和字符都可以进行自身匹配
    
# a = 'abc123+-*'
# b = re.findall('abc', a)
# print(b)  # ['abc']

# 元字符
    # 元字符指的是. ^ $ ? + {} \ []之类的特殊字符，通过它们我们可以对目标字符串进行个性化检索，返回我们要的结果。
    
    # 1. [] 的使用方法有以下三种：
        # a.常用来指定一个字符集
        
# s = 'a123456b'
# rule = 'a[0-9][1-6][1-6][1-6][1-6][1-6]b'
# l = re.findall(rule, s)
# print(l)  # ['a123456b']

        # b.可以表示一个范围        
        # 例如要在字符串"abcabcaccaac"中选出abc元素：

s = 'abcabcaccaac'
rule = 'a[a, b, c]c'  # rule = 'a[a-z0-9][a-z0-9][a-z0-9][a-z0-9]c'
l = re.findall(rule, s)
print(l)

    

