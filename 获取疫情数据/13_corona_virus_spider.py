#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

"""
思路
    1. 发送请求,获取疫情首页
    2. 从疫情首页中提取最近一日各国疫情字符串
    3. 从最近一日各国疫情字符串中,提取json格式字符串
    4. 把json格式字符串，转换为Python类型
    5. 把Python类型的数据,以json格式存入文件中
"""

import requests
from bs4 import BeautifulSoup
import re
import json

# 1. 发送请求,获取疫情首页
response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
home_page = response.content.decode()

# 2. 从疫情首页中提取最近一日各国疫情字符串
soup = BeautifulSoup(home_page, 'lxml')
script = soup.find(id='getListByCountryTypeService2true')
# text = script.text
text = script.string
# print(text)

# 3. 从最近一日各国疫情字符串中,提取json格式字符串
json_str = re.findall(r'\[.+\]', text)[0]
# print(json_str)

# 4. 把json格式字符串，转换为Python类型
last_day_corona_virus = json.loads(json_str)
# print(last_day_corona_virus)

# 5. 把Python类型的数据,以json格式存入文件中
with open('data/last_day_corona_virus.json', mode='w', encoding='utf-8') as fp:
    json.dump(last_day_corona_virus, fp, ensure_ascii=False)