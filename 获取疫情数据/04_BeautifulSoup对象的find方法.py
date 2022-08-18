#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

# 1.导入模块
from bs4 import BeautifulSoup

# 2.准备文档字符串
html = '''
<html>
	<head>
		<title>The Dormouse's story</title>
	</head>
	<body>
		<p class="title" name="dromouse">
			<b>The Dormouse's story</b>
		</p>
		<p class="story">Once upon a time there were three little sisters; and their names were
			<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
			<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
			<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
			and they lived at the bottom of a well.</p>
		<p class="story">...</p>
	</body>
</html>
'''

# 3.创建 BeautifuSoup 对象
soup = BeautifulSoup(html, 'lxml')

# 4.查找 titlel 标签
title = soup.find('title')
print(title)

# 5.查找 a 标签
a = soup.find('a')
print(a)

# 查找所有的 a 标签
a_s = soup.find_all('a')
print(a_s)

# 二、根据属性查找
    #查找 id 为 link1 的标签
    
# 方法一：通过命名参数进行查找    
a = soup.find(id='link1')
print(a)

# 方法二：使用attrs来指定属性字典，进行查找
a = soup.find(attrs={'id': 'link1'})
print(a)

# 三、根据文本查找
# 获取下面文档中文本为 Elsie 的标签文本
text = soup.find(text='Elsie')
print(text)

#Tag对象
print(type(a))  #<class 'bs4.element.Tag'>
print('标签名：', a.name)
print('标签所有属性:', a.attrs)  #输出的class是一个列表，class 一个属性中可以有多个值
print('标签文本内容：', a.text)