#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 输入美元数值
dollar = float(input('Enter dollar: '))

# 转换汇率 假如，当前汇率 6.74
CNY = dollar * 6.74

# 输出换算后的结果
print(f'{dollar} dollar equals {CNY:.2f}')
print('{0} dollar equeal {1:.2f}'.format(dollar, CNY))


num1, num2 = input('Enter 2 numbers: ').split()
num1 = int(num1)
num2 = int(num2)

summ = num1 + num2
difference  = num1 - num2
product = num1 * num2
quotient = num1 / num2
product = num1 % num2

print(f'{num1} + {num2} = {summ}')
print(f'{num1} - {num2} = {difference}')
print(f'{num1} * {num2} = {product}')
print(f'{num1} / {num2} = {quotient}')
print(f'{num1} % {num2} = {product}')
