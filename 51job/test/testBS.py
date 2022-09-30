#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

from bs4 import BeautifulSoup
import re  # 正则表达式，进行文字匹配

html = open("./jobList.html", mode="r", encoding="gbk")
bs = BeautifulSoup(html, "html.parser")

# 详情链接规则
findLink = re.compile(r'"job_href":"(.*?)",', re.S)
resultList = re.findall(findLink, str(bs))