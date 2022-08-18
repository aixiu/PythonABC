#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu


# 贪婪模式和非贪婪模式
'''
    相关正则符号
    '*'，*前面的字符匹配0次或多次（贪婪模式）

    '+'，+前面的字符匹配1次或多次（贪婪模式）

    '?'，?前面的字符匹配0次或1次（贪婪模式）

    '*?,+?,??'，上面三个的非贪婪模式

    '{m,n}'，前面的字符匹配m-n次（贪婪模式）

    '{m,n}?'，上面的非贪婪模式
'''
# 硬核Python进阶篇
#     - https://www.bilibili.com/video/BV1zK4y1Z75d?p=2&vd_source=20f7c1f5f32f90ae92d9428e45039d9b

import re

# level1 - 固定的字符串
    # 要求：确定字符串中是否有123456
text = '麦叔身高:178，体重：168，学号：123456，密码:9527'
print(re.findall(r'123456', text))

# level2 - 某一类字符
#     要求：找出所有的单个的数字
print(re.findall(r'5*', text))