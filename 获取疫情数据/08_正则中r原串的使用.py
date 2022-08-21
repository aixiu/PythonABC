#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

import re
#1. 在不使用r原串的情况下，遇到转义符
rs = re.findall('a\nbc', 'a\\nbc')
print(f're:{re}')
rs = re.findall('a\\\\nbc','a\\nbc')
print(f're:{rs}')

#r原串在正则表达式中可以消除转移符带来的影响
rs1 = re.findall(r'a\nbc','a\nbc')
print(f'rs1:{rs1}')

rs2 = re.findall(r'a\\nbc','a\\nbc')
print(f'rs2:{rs2}')

# 拓展： 可以解决写正则的时候，不符合PEP8规范的问题
rs3 = re.findall(r'\d','a123')
print(f'rs3:{rs3}')