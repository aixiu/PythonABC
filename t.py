#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import fibo

# print(fibo.fib2(10))
# print(fibo.__name__)


# print('python基础知识')


lists = [1, 5, 6, 0, 7, 4, 9, 3]
num = [0, 1, 2, 3, 4, 0, 5, 1, 2, 6, 7]

string_tel = []    
newlist = []
for i in num:
    string_tel.append(lists[i])

print('联系方式：{}'.format("".join(map(str,string_tel))))
