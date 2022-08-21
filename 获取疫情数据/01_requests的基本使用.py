#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

# 视频地址：https://www.bilibili.com/video/BV1464y1c7Eq?p=1
# requests安装
    # 安装命令：pip install requests
    
# requests基本使用
    # 1.导入模块
    # 2.发送get请求，获取响应
    # 3.从响应中获取数据
    
import requests

response = requests.get('http://www.baidu.com')   # 一定要加http或https请求协议
print(response)  # 打印响应
print(response.encoding)   # 查看当前返回用于解码response.content的编码。  ISO-8859-1
# response.encoding = 'utf-8'  #设置编码（中文不乱码）
# print(response.text)  # 打印响应内容 按 encoding 指定的编码进行解码
# print(response.content) # 响应体bytes类型

print(response.content.decode()) # 根据对应的编码进行解析  .decode() 解码 .content的二进制内容

'''
知识点：
    text和content方法的区别
    
    r.text 　　　　str 　　　#字符串方式的响应体，会自动根据响应头部的 字符编码进行解码
    r.content 　　 bytes　　#字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩

    requests对象的get和post方法都会返回一个Response对象，这个对象里面存的是服务器返回的所有信息，包括响应头，响应状态码等。其中返回的网页部分会存在.content和.text两个对象中。

    两者区别在于，content中间存的是字节码，而text中存的是Beautifulsoup根据猜测的编码方式将content内容编码成字符串。

    直接输出content，会发现前面存在b'这样的标志，这是字节字符串的标志，而text是，没有前面的b,对于纯ascii码，这两个可以说一模一样，对于其他的文字，需要正确编码才能正常显示。大部分情况建议使用.text，因为显示的是汉字，但有时会显示乱码，这时需要用.content.decode('utf-8')，中文常用utf-8和GBK，GB2312等。这样可以手工选择文字编码方式。

    所以简而言之，.text是现成的字符串，.content还要编码，但是.text不是所有时候显示都正常，这是就需要用.content进行手动编码。
'''