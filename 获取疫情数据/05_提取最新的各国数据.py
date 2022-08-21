#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

# 1.导入相关模块
import requests
from bs4 import BeautifulSoup

# 2.发送请求，获取疫情首页内容
response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
home_page = response.content.decode()
# print(home_page)

# 3.使用 BeautifulSoup 提取疫情数据
soup = BeautifulSoup(home_page, 'lxml')
script = soup.find(id='getListByCountryTypeService2true')

# beautifulsoup中，对外接口，没有提供text这个属性，只有string这个属性值；
# beautifulsoup内部才有text这个属性，只供内部使用 –> 如果你想要用text值，应该调用对应的get_text()
# 而你之所有能够直接用soup.text而没报错，应该是和python的class的property没有变成private有关系 –>导致你外部也可以访问到这个，本身是只供内部使用的属性值-> 这个要抽空深究了。
# https://blog.csdn.net/f156207495/article/details/78074240/

# print(type(script))

# text = script.contents

# text = script.text
# text = script.get_text()

text = script.string

# print(type(text))
print(text)
