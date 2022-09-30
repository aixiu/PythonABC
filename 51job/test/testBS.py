#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

from bs4 import BeautifulSoup
import re  # 正则表达式，进行文字匹配

html = open("./jobList.html")
bs = BeautifulSoup(html, "html.parser")

# 影片详情链接的规则
findLink = re.compile(r'<div class="e_icons ick.*?href="(.*?)" target="_blank" class="el">', re.S) 

imgSrc = re.findall(findLink, bs)[0]

print(imgSrc)
