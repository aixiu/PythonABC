#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

# !/usr/bin/env python
# -*- encoding: utf-8 -*-
 
import os
 
img_path = 'E:\QQ皮肤'
img_list=os.listdir(img_path)
print('img_list: ',img_list)
 
with open('testImagelist.txt','w') as f:
    for img_name in img_list:
        f.write(img_name+'\n')