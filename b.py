#!/usr/bin/env python
# -*- coding: utf-8 -*-

count = 0

while count < 3:
    ipw = input('请输入 “白嫖” 或 “红包” >>> ')

    if ipw == "白嫖":
        print('滚！拉黑。')
        break
    elif ipw == "红包":
        print('问题解决')
        break
    else:
        print('输入的什么鬼,看不懂提示吗？')
        count += 1
        if count == 3:
            print('三次机会都输不对，捣乱的吧')