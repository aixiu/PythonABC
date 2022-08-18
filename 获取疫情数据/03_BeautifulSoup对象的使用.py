#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

             
'''
Beautiful Soup 介绍和安装
pip install beautifulsoup4  安装bs4 方法一
pip install bs4  安装bs4 方法二
pip install lxml  安装解析器  lxml
'''

# 1.导入模块
from bs4 import BeautifulSoup

# 2.创建 Beautifullsoup 对象
soup = BeautifulSoup('<html>data</html>', 'lxml')
#soup = BeautifulSoup('<html>data</html>',"html.parser")
print(soup)