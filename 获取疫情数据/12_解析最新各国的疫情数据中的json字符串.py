#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

# 1. 导入相关模块
import requests
from bs4 import BeautifulSoup
import re
import json

# 2. 发送相关请求，获取疫情首页内容
response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
home_page = response.content.decode()

# 3. 使用BeautidulSoup提取疫情数据
soup = BeautifulSoup(home_page, 'lxml')
script = soup.find(id='getListByCountryTypeService2true')

text = script.string
# print(text)

#4. 使用正则表达式，提取json字符串
json_str = re.findall(r'\[.+\]', text)[0]   # ['[{"id":19223181,"createTime":1660983491000,"modifyTime":1660983491000"}]'] 获取列表第1项内容
# print(json_str)  # <class 'str'>

# 5.把JSON字符串转化为Python类型的数据
last_day_corona_virus = json.loads(json_str)
print(last_day_corona_virus)  # <class 'list'>


"""
关于load()和dump()的区别：

    loads： 是将 string 转换为 dict
    dumps： 是将 dict 转换为 string
    
    load： 是将 json格式字符串转化为 dict，读取文件
    dump： 是将 dict类型转换为 json格式字符串，存入文件
    
其他更详细的方面，参考该文章：https://www.cnblogs.com/bigtreei/p/10466518.html
"""
