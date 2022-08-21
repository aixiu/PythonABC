#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

import json

# 1.把PYTHON类型的数据转化为JSON字符串
# 1.1 PYTHON类型的数据
json_str = '''[{"cityName":"陕西","currentConfirmedCount":1231,"confirmedCount":2812},
               {"cityName":"西安","currentConfirmedCount":1499,"confirmedCount":2173},
               {"cityName":"海东","currentConfirmedCount":0,"confirmedCount":1}]'''

rs = json.loads(json_str)
# 1.2 转化
json_str = json.dumps(rs, ensure_ascii=False) #1.不要取名为json,会冲突2.多一个属性ensure_ascii=False可以不使用ascii码（ 即常说的乱码如：\u9655\u897f）
print(f'json_str:\n{json_str}')

# 2.把PYTHON以JOSN格式存储到文件中
# 2.1 构建要写入的文件对象
with open('data/test1.json', mode='w', encoding='utf-8') as fp:
    # 2.2 储存到文件中
    json.dump(rs, fp, ensure_ascii=False)