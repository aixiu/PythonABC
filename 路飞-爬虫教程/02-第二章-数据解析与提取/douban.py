#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

# 拿到页面源代码
# 提取和解析数据

import requests
from lxml import etree

url = "https://movie.douban.com/subject/35505100/?from=showing"
resp = requests.get(url)
print(resp.text)

# html = etree.HTML(resp.text)  # 直接处理拿到的源码

# # 拿到每一个服务商的div
# divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")
# for div in divs:
#     try:
#         price = div.xpath("./div/div/a[2]/div[2]/div[1]/span[1]/text()")[0].strip("¥")
#         amount = div.xpath("./div/div/a[2]/div[2]/div[1]/span[2]/text()")[0]
#         title =  "saas".join(div.xpath("./div/div/a[2]/div[2]/div[2]/p/text()"))
#         com_name = div.xpath("./div/div/a[1]/div[1]/p/text()")[1]
#         location = div.xpath("./div/div/a[1]/div[1]/div/span/text()")[0]
#         print(price)
#         print(amount)
#         print(title)
#         print(com_name)
#         print(location)
#     except Exception:
#         pass