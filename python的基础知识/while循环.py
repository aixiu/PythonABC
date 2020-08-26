#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 例一

# name = ''

# while name != 'your name':
#     print('Please type your name: ')
#     name = input()

# print('Thank you!')


# 例二
# continue 退出本次循环，进入下次循环

# tick = 0

# while tick < 5:
#     tick += 1
#     if tick == 3:
#         continue
#     print('tick is ', tick)


# 例三 break 直接跳出循环，终止执行

name = ''

while True:
    print('please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')