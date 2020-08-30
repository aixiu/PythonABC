#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, b + a


def fib2(n):
    flist = []
    a, b = 0, 1
    while b < n:
        flist.append(b)
        a, b = b, a + b
    return flist


# 加入以下代码，可以当脚本使用  $ python fibo.py 10
# http://www.pythondoc.com/pythontutorial3/modules.html#id11
if __name__ == '__main__':
    import sys
    fib(int(sys.argv[1]))
    