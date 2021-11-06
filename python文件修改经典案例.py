import os
import time

# 案例文本原始内容

'''第一行
第二行
第三行
第四行
猜猜这是第几行？
猜猜这是第几行？
张观博
张欣竹
张欣阳
张刚军

李扬阳
李靖阳
李熙阳'''

# 文件修改   把文件中的  李 -> 汪

with open("./test.txt", mode="r", encoding="utf-8") as f1, \
    open("test_副本.txt", mode="w", encoding="utf-8") as f2:
    for line in f1:
        line = line.strip()
        if line.startswith("李"):
            line = line.replace("李", "汪")

        f2.write("\n".join(line))
             
         

# 删除源文件
os.remove("./test.txt")
os.rename("test_副本.txt", "./test.txt")