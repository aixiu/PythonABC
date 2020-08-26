#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 本金和利率的一个小例子

# 本金
money = input('输入本金: ')
# 利率
interest_rate = input('输入利率(整数): ')

# 转换成浮点数
money = float(money)
interest_rate = float(interest_rate) * .01

# 10年后，本金+利息一共有
for i in range(10):
    money = money + money * interest_rate

print(f'10年后共有: {money:.2f}')
