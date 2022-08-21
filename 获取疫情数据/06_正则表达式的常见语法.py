#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

# 导入正则模块
import  re

# 字符匹配  #findall 的参数中 第一个是正则表达式  第二是字符串
rs1 = re.findall('abc','abc') #在字符串里查找和前面正则表达式里与abc匹配的内容
rs2 = re.findall('a.c','abc')
rs3 = re.findall('a.c','a%c')
rs4 = re.findall('a.c','a\nc')   # 无法匹配，‘.’匹配任意字符（除 ‘\n’）
rs5 = re.findall('a\.c','a.c') #单独匹配 a.c

#中括号匹配
rs6 = re.findall('a[bc]d','abd')

#预定义的子字符集
rs7 = re.findall('\d','123')  #\d只能匹配一个字符
rs8 = re.findall('\w','AQD3456cs量子')  #\d只能匹配字母、数字、下划线、中文

#数量词
rs9 = re.findall('\d*','123') # ['123', '']允许匹配空
rs10 = re.findall('a\d*','a123') #['a123'] ，允许 \d 可以出现0次
rs11 = re.findall('a\d+','a1') #['a1']  \d至少出现一次
rs12 = re.findall('a\d?','a16543') #只匹配一次  ['a1']
rs13 = re.findall('a\d{3}','a16543') #{n} n为匹配个数  ['a165']
print(rs8)