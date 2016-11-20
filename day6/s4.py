#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

# import re
#
# ret = re.findall(r"yd[a-z]an\b","ydean fhakfnykdddknyuhiwufh")
#
# print(ret)

# import re
#
# a =re.split("\d+","one1tow2three3four4")
#
# print(a)

# import re
#
# text = "hello  handsome boy,koot balabala bool "
#
# regex = re.compile(r"\woo\w*")
#
# print (regex.findall(text))

# import re
#
# a = re.search(r"\\com","www.run\comoob").group()
#
# print(a)

# import re
#
# text = "hasfdfddf  halfdfd  hadfdfd dfggeegsergerg"
#
# r = re.split("(h(a)l)",text)
#
# print(r)

# print(r.group())
# print(r.groups())
# print(r.groupdict())

suanshi = "8*12+(6-(5*6-2)/77+2)*(3-7)+8"

print(eval(suanshi))