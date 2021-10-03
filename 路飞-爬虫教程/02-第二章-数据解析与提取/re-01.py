import re

# findall: 匹配字符串中所有的符合正则的内容
lst = re.findall(r"\d+", "我的电话号码是：10086，你的电话是：10010")
print(lst)

# finditer: 匹 配字符串中所有的内容[返回的是迭代器],从迭代器中拿到内容需要.group()

it = re.finditer(r"\d+", "我的电话号码是：10086，你的电话是：10010")
for i in it:
    print(i.group())


# search 找到一个结果就返回，返回的结果是match对象,从迭代器中拿到内容需要.group()
s = re.search(r"\d+", "我的电话号码是：10086，你的电话是：10010")
print(s.group())

# match 是从头开始匹配
s = re.match(r"\d+", "10086，你的电话是：10010")
print(s.group())

# 预加载正则表达式
obj  = re.compile(r"\d+")

ret = obj.finditer("我的电话号码是：10086，你的电话是：10010")
for i in ret:
    print(i.group())


ret = obj.findall("测试其它的数字，比如：124578962")
print(ret)



s = """
<div class='jay'><span id='1'>老猫</span></div>
<div class='jj'><span id='2'>宋铁</span></div>
<div class='tom'><span id='3'>联通</span></div>
<div class='aixiu'><span id='4'>移动</span></div>
"""

# obj = re.compile(r"<div class='.*?'><span id='.*?'>.*?</span></div>", re.S)  # re.S 让.能匹配换行
obj = re.compile(r"<div class='.*?'><span id='(?P<id>.*?)'>(?P<name>.*?)</span></div>", re.S)  # re.S 让.能匹配换行

result = obj.finditer(s)
for it in result:
    # print(it.group())
    print(it.group("name"))
    print(it.group("id"))

# 注：(?P<分组名>正则) 可以单独从正则匹配的内容中进一步提取内容