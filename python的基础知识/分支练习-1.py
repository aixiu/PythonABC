#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 例一
name = 'Alice'

if name == 'Alice':
    print(f'Hi {name}')

print('Done')

# 例二
password = 'swordfish'

if password == 'swordfish':
    print('Access granted.')
else:
    print('Worng password')

# 例三
name = 'Bob'
age = 3000

if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice, kidoo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie')