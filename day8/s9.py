#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan


import re
text = "has dfggeegsergerg"
r = re.match("h(\w+)",text)  #只要匹配到了就做分组
print(r.group())
print(r.groups())
print(r.groupdict())


text = "has dfggeegsergerg"
r = re.match("h(?P<name>\w+)",text)  #给分组搞成字典样式
print(r.group())
print(r.groups())
print(r.groupdict())