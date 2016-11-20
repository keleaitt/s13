#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

import  re

suanshi = "8*12+(6-(5*6-2)/77+2)*(3-7)+8"

suanshi = re.sub(r"\(\5\*\6\-\2\)","28",suanshi)

print(suanshi)