#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

def pringNum(n):
    print(n)
    if n == 1:
        return
    pringNum(n-1)
    
pringNum(5)