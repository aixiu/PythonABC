#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 例一
# 输入：Random access memory，输出：RAM
# 输出字符串的首字母大写
strs = input('请输入英文字符串，英文，空格隔开>>> ')

strs = strs.upper()  # 转换为大小

strs_words = strs.split() # 用空格分割后的字符串列表

for i in strs_words:
    print(i[0], end='')

