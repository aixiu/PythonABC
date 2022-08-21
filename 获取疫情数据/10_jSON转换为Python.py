#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

#导入模块
import json

# 1 把JSON字符串，转换为Python数据
# 1.1 准备JSON字符串
json_str = '''[{"cityName":"陕西","currentConfirmedCount":1231,"confirmedCount":2812},
               {"cityName":"西安","currentConfirmedCount":1499,"confirmedCount":2173},
               {"cityName":"海东","currentConfirmedCount":0,"confirmedCount":1}]'''

# 1.2 把JSON字符串，转换为Python类型数据
rs = json.loads(json_str)
#print(f'rs:{rs}')
#print(type(rs)) #<class 'list'> 数组转换为列表
#print(type(rs[0])) #<class 'dict'> 数组转换为字典

# 2 把JSON格式文件，转换为Python类型数据
# 2.1 构建指向该文件的文件对象
with open('data/test.json', mode='r', encoding='utf8') as fp:
    # 2.2 加载该文件对象，转换问JSON类型的数据
    python_list = json.load(fp)
    print(f'python_list:{python_list}')
    print(type(python_list))  # <class 'list'> 数组转换为列表
    print(type(python_list[0])) #<class 'dict'> 数组转换为字典