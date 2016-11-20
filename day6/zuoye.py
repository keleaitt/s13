#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

import re


#
# suanshi = "8*12+(6-(5*6-2)/77+2)*(3-7)+8"
#
# qiankuohao = re.search(r"\(",suanshi)
#
# houkuohao = re.search(r"\)",suanshi)
# print(qiankuohao.span())
# print(houkuohao.span())
#
#
# print(eval(suanshi))

import  time
#
# def fenge(suanshi):
#     while True:
#         qiankuohao = re.search(r"\(", suanshi)
#
#         houkuohao = re.search(r"\)", suanshi)
#
#
#         if "(" in suanshi[qiankuohao.span()[1]:houkuohao.span()[1]]:
#             suanshi = suanshi[qiankuohao.span()[1]:houkuohao.span()[1]]
#             print("fenge")
#             print(suanshi)
#
#         else:
#             time.sleep(2)
#             suanshi = suanshi[qiankuohao.span()[1]:houkuohao.span()[0]]
#             print(suanshi)

def jisuan(args):

    ret = eval(args)

    return  str(ret)


def  fenge():    suanshi = "8*12+(6-(5*6-2)/77+2)*(3-7)+8"

    while True:
        if "(" in suanshi:
            ret = re.split(r"(\(([\w\+\-\*\/]*)\))",suanshi)
            jieguo = jisuan(ret[2])
            print(ret[1])
            suanshi = suanshi.replace(ret[1],jieguo)
            print(suanshi)
        else:
            jieguo = jisuan(suanshi)
            return jieguo




jieguo = fenge()

print(jieguo)