#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

import requests

url = "https://movie.douban.com/j/chart/top_list"

# 重新封装参数
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.37"
}

resp = requests.get(url, params=param, headers=headers)

# print(resp.request.url)

print(resp.json())
resp.close()  # 关掉 resp