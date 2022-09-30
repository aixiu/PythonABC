#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

'''
制作流程
    1.爬取数据   spider.py
        爬取列表
        爬取详情
    2.数据保存   51job.db
        保存列表
        保存详情
    3.搭建框架  app.py：路由  templates：页面  static：素材（图片，CSS,JS）
        前端页面
        列表显示
        表单制作
    4.制作图表
        Echarts
            - 柱形图
            - 饼状图
        WordCloud
'''

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import sqlite3  #  进行SQLite数据库操作
from urllib import parse

# 搜索页面路径：https://search.51job.com/list/090200,000000,0000,00,9,99,python,2,1.html

KW = input("请输入你要搜索的岗位关键字： ")
keyword = parse.quote(parse.quote(KW))
pageNum = 1

#主流程
def main():
    baseurl = f"https://search.51job.com/list/090200,000000,0000,00,9,99,{keyword},2,{pageNum}.html"  # 基础 URL
    # 1.爬取网页
    # datalist = getData(baseurl)
    # savepath = f"./豆瓣电影Top250.xls"
    
    # 3.保存数据到 excel
    # saveData(datalist, savepath)
    
    html = askURL(baseurl)
    # print(html)


# 获取到所有工作岗位链接 
def getLink():
    return []    
  
# 得到指定一个 url 的网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("gbk")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):   # hasattr() 函数用于判断对象是否包含对应的属性。
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
            
    return html




if __name__ == '__main__':
    main()
