#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import random

code = []

code.append(random.choice(string.ascii_lowercase))
code.append(random.choice(string.ascii_uppercase))
code.append(random.choice(string.digits))

while len(code) < 6:
    code.append(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits))

q_code = "".join(code)

print(q_code)