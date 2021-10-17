#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

# 1. 找到未加密的参数                       # window.arsea(参数, xxxx,xxx,xxx)
# 2. 想办法把参数进行加密(必须参考网易的逻辑), params  => encText, encSecKey => encSecKey
# 3. 请求到网易. 拿到评论信息

# 需要安装pycrypto:   pip install pycrypto
from Crypto.Cipher import AES
from base64 import b64encode
import requests
import json


url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

# 请求方式是POST