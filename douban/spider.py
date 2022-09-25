#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行 excel 文件写入操作   Excel的写插件  安装命令：pip install xlwt；  Excel的读取插件  安装命令：pip install xlrd
import sqlite3  #  进行SQLite数据库操作

def main():
    baseurl = "https://movie.douban.com/top250?start="  # 基础 URL
    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = f"./豆瓣电影Top250.xls"
    
    # 3.保存数据
    saveData(savepath)

# 爬取网页
def getData(baseurl):
    datalist = []
    # 2.逐一解析数据
    return datalist

# 保存数据
def saveData(savepath):
    pass
    
if __name__ == '__main__':  # 当程序执行时
    # 调用函数
    main()