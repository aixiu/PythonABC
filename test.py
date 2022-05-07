#!/usr/bin/env python
# -*- coding: utf-8 -*-

# with open('test.txt', 'r', encoding='utf-8') as f:
#     for i in f:
#         print(i, end='')


# with open('test.txt',mode='r', encoding='utf-8') as heine:
#     print(heine.readlines())


# with open('test.txt',mode='r', encoding='utf-8') as heine:
#     print(heine.readline())

# with open('test.txt', 'a', encoding='utf-8') as f:
#     f.write('\n猜猜这是第几行？')
    
# with open('test.txt', 'r', encoding='utf-8') as f:
#     for i in f:
#         print(i, end='')


def add(a, b):
    return '计算两个数的和： {} + {} = {}'.format(a, b, a+b)

print(add(30, 40))




nb = 1
while True:
    nb = nb + 1
    print(nb)
    if nb == 100:
        break


# 打印所有 unicode 编码 运行快显示卡顿
for i in range(65536):
    print("{} ".format(chr(i)), end="")
