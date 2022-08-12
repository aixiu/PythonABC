#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

"""
常量即表示不可更改的变量，一般用于做标记。

re模块中有9个常量，常量的值都是int类型！
"""
import re

# 一常量

# def regexFlag():
#     """
#     演示re模块常量的使用
#     """
    
#     # 1 re.IGNORECASE
#     # 语法： re.IGNORECASE 或简写为 re.I
#     # 作用： 进行忽略大小写匹配。
    
#     text = '猪哥大帅b'
#     pattern = r'猪哥大帅B'
#     print('默认模式：', re.findall(pattern, text))
#     print('忽略大小写 模式：', re.findall(pattern, text, re.IGNORECASE))
    
#     # 在默认匹配模式下大写字母B无法匹配小写字母b，而在 忽略大小写 模式下是可以的。
    
# def regexFlag():
#     """
#     演示re模块常量的使用
#     """
    
#     # 2 re.ASCII
#     # 语法： re.ASCII 或简写为 re.A
#     # 作用： 顾名思义，ASCII表示ASCII码的意思，让 \w, \W, \b, \B, \d, \D, \s 和 \S 只匹配ASCII，而不是Unicode。
    
#     text = 'a猪哥b最帅c'
#     pattern = r'\w+'
#     print('Unicode：', re.findall(pattern, text))
#     print('ASCII：', re.findall(pattern, text, re.ASCII))
    
#     # 在默认匹配模式下\w+匹配到了所有字符串，而在ASCII模式下，只匹配到了a、b、c（ASCII编码支持的字符）。
#     # 注意：这只对字符串匹配模式有效，对字节匹配模式无效。
    
# def regexFlag():
#     """
#     演示re模块常量的使用
#     """
    
#     # 3 re.DOTALL
#     # 语法： re.DOTALL 或简写为 re.S
#     # 作用： DOT表示.，ALL表示所有，连起来就是.匹配所有，包括换行符\n。默认模式下.是不能匹配行符\n的。
    
#     text = '猪哥\n最帅'
#     pattern = r'.*'
#     print('默认模式：', re.findall(pattern, text))
#     print('.匹配所有模式：', re.findall(pattern, text, re.DOTALL))
    
#     # 在默认匹配模式下.并没有匹配换行符\n，而是将字符串分开匹配；而在re.DOTALL模式下，换行符\n与字符串一起被匹配到。
#     # 注意：默认匹配模式下.并不会匹配换行符\n。
    
# def regexFlag():
#     """
#     演示re模块常量的使用
#     """
    
#     # 4 re.MULTILINE
#     # 语法： re.MULTILINE 或简写为 re.M
#     # 作用： 多行模式，当某字符串中有换行符\n，默认模式下是不支持换行符特性的，比如：行开头 和 行结尾，而多行模式下是支持匹配行开头的。表示.，ALL表示所有，连起来就是.匹配所有，包括换行符\n。默认模式下.是不能匹配行符\n的。
    
#     text = '猪哥\n最帅'
#     pattern = r'^最帅'
#     print('默认模式：', re.findall(pattern, text))
#     print('多行模式：', re.findall(pattern, text, re.MULTILINE))
    
#     # 在默认匹配模式下.并没有匹配换行符\n，而是将字符串分开匹配；而在re.DOTALL模式下，换行符\n与字符串一起被匹配到。
#     # 注意：默认匹配模式下.并不会匹配换行符\n。

# def regexFlag():
#     """
#     演示re模块常量的使用
#     """
    
#     # 5 re.VERBOSE
#     # 语法： re.VERBOSE 或简写为 re.X
#     # 作用： 详细模式，可以在正则表达式中加注解！
    
#     text = '猪哥最帅'
#     pattern = r"""^猪哥  #人物
#                    最师  #形容词
#                """
#     print('默认模式：', re.findall(pattern, text))
#     print('详细模式：', re.findall(pattern, text, re.VERBOSE))
    
#     # 默认模式下并不能识别正则表达式中的注释，而详细模式是可以识别的。

#     # 当一个正则表达式十分复杂的时候，详细模式或许能为你提供另一种注释方式，但它不应该成为炫技的手段，建议谨慎考虑后使用！
    
    
    
# regexFlag()