#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu


# 视频地址 https://www.bilibili.com/video/BV1i54y1h75W

import requests

query = input('输入一个内容：')

# url = f'https://www.sogou.com/web?query={query}'
url = 'https://www.sogou.com/web?query={}'.format(query)
dic = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52"
}

resp = requests.get(url, headers=dic)  # 处理反爬

print(resp)

print(resp.text)  # 拿到页面源码
