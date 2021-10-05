#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

# 安装  pip install bs4

# 1、拿到主页面的源代码，然后提取子页面的链接地址，href
# 2、通过href 拿 到子页面的内容，从子页面中找到图片的下载地址  img -> src
# 3、下载图片


import requests
from bs4 import BeautifulSoup
import time  # 为了防止不停的访问服务器，引起屏蔽

url = "https://www.umei.cc/bizhitupian/weimeibizhi"
indexurl = "https://www.umei.cc"

resp = requests.get(url)
resp.encoding = "utf-8"  # 处理乱码
# print(resp.text)

# 把源代码交给 bs4

main_page = BeautifulSoup(resp.text, 'html.parser')
alist = main_page.find("div", class_="TypeList").find_all("a")

# print(alist)
for a in alist:
    href = a.get('href')  # 直接通过 get 就可以拿到属性的值
    child_href = indexurl + href
    # 拿 到子页面的源代码
    child_page_resp = requests.get(child_href)
    child_page_resp.encoding = "utf-8"
    child_page_text = child_page_resp.text
    # 从子页面中拿 到图片的下载路径
    child_apge = BeautifulSoup(child_page_text, "html.parser")
    # img = child_apge.find("div", class_="ImageBody").find("img")   # 找 div 标签方法
    img = child_apge.find("p", align="center").find("img")  # 找 p 标签方法
    src = img.get("src")
    # print(src) #测试

    # 下载图片
    img_resp = requests.get(src)
    # img_resp.content  # 这里拿 到的是字节 因为下载的是图片

    # resp.text返回的是Unicode型的数据。
    # resp.content返回的是bytes型也就是二进制的数据。

    img_name = src.split("/")[-1]
    with open("img/"+img_name, mode="wb") as f:
        f.write(img_resp.content)  # 图片内容写入文件

    print("下载已完成", img_name)
    time.sleep(1)

print("全部下载完毕!!!")