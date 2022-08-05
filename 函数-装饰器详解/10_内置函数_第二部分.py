#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

"""
zip：可以把多个可迭代内容进行合并
sorted：排序
filter：筛选
map： 映射

"""
# zip 函数

# lst1 = ['赵本山', '范伟', '苏有朋']
# lst2 = [40, 38, 42]
# lst3 = ['卖拐', '耳朵大有福', '情深深雨蒙蒙']

# zip 函数模拟

# result = []
# for i in range(len(lst1)):
#     first = lst1[i]
#     second = lst2[i]
#     third = lst3[i]
#     result.append((first, second, third))    
# print(result)

# zip 函数使用

# result = zip(lst1, lst2, lst3)

# 取值方法一
# for item in result:
#     print(item)
 
# 取值方法二 
# lst = list(result)
# print(lst)


# locals 函数

# a = 188
# print(locals())  # 此时 locaals 被写在了全局作用域范围内，此时看到的就是全局作用域中的内容

# def func():
#     a = 336
#     print(locals())  # 此时 locaals 被写在了局部作用域范围内，此时看到的就是局部作用域中的内容
    
# func()

# c = 12
# print(globals())  # globalsl 看到的是全局作用域中的内容

# def func():
#     a = 336
#     print(globals())   # globalsl 看到的是全局作用域中的内容 不管在哪都是全局内容
    
# func()


# sorted 函数详解
# lst = [16, 22, 68, 1, 147, 256, 49]
# s = sorted(lst, reverse=True)  # reverse 翻转
# print(s)

# lst = ['秋', '张二噶', '比克', '卡卡罗特', '超级宇宙无敌大帅B']

# # def func(item):  # item 对应的就是列表中的每一项数据
# #     return len(item)

# # func = lambda x: len(x)

# s = sorted(lst, key=lambda x: len(x))
# print(s)

# sorted 实例

# lst = [
#     {'id': 1, 'name': '周润发', 'age': 18, 'salary': 56000},
#     {'id': 2, 'name': '周星驰', 'age': 35, 'salary': 12000},
#     {'id': 3, 'name': '周伯通', 'age': 47, 'salary': 522000},
# ]

# # 1.根据每个人的年龄排序
# s = sorted(lst, key=lambda x: x['age'])
# print(s)

# # 2.根据工资进行排序，从大到小排序

# s = sorted(lst, key=lambda x: x['salary'], reverse=True)
# print(s)


# filter：筛选 的详解

# lst = ['张无忌', '张三丰', '张翠山', '灭绝小师太', '小狐仙']

# f = filter(lambda x: x.startswith('张'), lst)   # 结果是生成器

# # f = filter(lambda x: not x.startswith('张'), lst)  # 结果是生成器,条件判断 not

# print(list(f))


# map：映射的详解

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [item * item for item in lst]
print(result)