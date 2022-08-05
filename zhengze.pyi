#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

import os
import stat
import shutil

file_path = './test/'

print(os.access(file_path, os.R_OK))	#查看文件是否有读的权限
print(os.access(file_path, os.W_OK))	#查看文件是否有写的权限
print(os.access(file_path, os.X_OK))	#查看文件是否有执行的权限

try:
    shutil.rmtree(file_path)
except PermissionError as e:
    error_file_path = str(e).split(":", 2)[-1]
    if os.path.exists(error_file_path):
        os.chmod(error_file_path, stat.S_IWUSR)    # 假如文件没有写的权限，
        
        

