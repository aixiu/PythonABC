#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

# 1. 导入相关模块
import requests
from bs4 import BeautifulSoup
import re

# 2. 发送相关请求，获取疫情首页内容
response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
home_page = response.content.decode()

# 3. 使用BeautidulSoup提取疫情数据
soup = BeautifulSoup(home_page, 'lxml')
script = soup.find(id='getListByCountryTypeService2true')

text = script.string
# print(text)

# 4. 使用正则表达式，提取json字符串
json_str = re.findall(r'\[.+\]', text)[0]
print(json_str)
