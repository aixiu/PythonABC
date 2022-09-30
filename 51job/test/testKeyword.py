#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

from urllib import parse

keyword = parse.quote('大数据')
newKW = parse.quote(keyword)
# print(keyword)
print(newKW)   # %25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE