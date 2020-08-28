#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 英文输入比如：HIDE
# 加密成 Unicode 字符。用 ord() 函数
# 最后再反向操作还原出原文 用 chr() 函数

# 要加密的字符串
message = input('输入要加密的字符串>>> ')

secmessage = ''

for i in message:
    if i.isalpha():   # 如果是字母
        secmessage += str(ord(i) - 23)
    elif i.isspace():  # 如果是空格
        secmessage += str(ord(i))

print('加密后的信息为>>> ',secmessage)

normmessage = ''

for i in range(0, len(secmessage)-1, 2):
    charCode = secmessage[i] + secmessage[i + 1]
    # print(charCode)
    if charCode != '32':  # 空格的 ord() = 32
        normmessage += chr(int(charCode) + 23)
    else:
        normmessage += chr(int(charCode))

print('还原码为>>> ',normmessage)
    
