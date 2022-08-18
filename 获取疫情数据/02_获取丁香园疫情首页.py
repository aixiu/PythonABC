#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

# 获取丁香园疫情首页

# 1.导入模块
import requests

# 2.发送请求，获取响应
response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')

# 3.从响应中，获取数据
# print(response.text)  # text 码乱
print(response.content.decode())