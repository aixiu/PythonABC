#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

import re
# 1.findall方法，返回匹配的结果列表
rs = re.findall('\d+','aixiu12shen34')
print(f'rs:{rs}')

# 2.findall 方法中，flag参数的作用
rs2 = re.findall('a.bc','a\nbc',re.DOTALL)   # re.D .号，可以匹配所有的字符
rs3 = re.findall('a.bc','a\nbc',re.S)  # re.S 多行模式
print(f'rs2:{rs2}')
print(f'rs3:{rs3}')

# 3.findall 方法中分组的使用
rs4 = re.findall('a.+bc','a\nbc',re.S)  #rs4:['a\nbc']
print(f'rs4:{rs4}')

rs5 = re.findall('a(.+)bc','a\nbc',re.S)  #rs5:['\n']
print(f'rs5:{rs5}')