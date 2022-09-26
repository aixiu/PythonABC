#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行 excel 文件写入操作   Excel的写插件  安装命令：pip install xlwt；  Excel的读取插件  安装命令：pip install xlrd
import sqlite3  #  进行SQLite数据库操作

def main():
    baseurl = "https://movie.douban.com/top250?start={}"  # 基础 URL
    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = f"./豆瓣电影Top250.xls"
    
    # 3.保存数据
    saveData(savepath)
    
    # askURL("https://movie.douban.com/top250?start=0")

# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数，10次
        url = baseurl.format(str(i * 25))
        html = askURL(url)  # 保存获取到的网页源码
        
        # 2.逐一解析数据
        
    return datalist

# 得到指定一个 url 的网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):   # hasattr() 函数用于判断对象是否包含对应的属性。
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
            
    return html

# 保存数据
def saveData(savepath):
    pass
    
if __name__ == '__main__':  # 当程序执行时
    # 调用函数
    main()
    getData()