# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan


# def f1(*args):
#
#     print(args,"Type:",type(args))
#
#
# f1([11,22,33,44])
# f1(*[11,22,33,44])
#
# f1(*"yuan")

# f = open("db","a",encoding="utf-8")
#
# f.write("123")
#
# f.flush()
#


# input("qingshuru:")

# with open("db1","r",encoding="utf-8") as f1 , open("db2","w",encoding="utf-8") as f2:
#     times = 0
#     for line in f1:
#         times += 1
#         new_str = line.replace("Yuan","zhai")
#         if times<=10:
#             f2.write(line)
#         else:
#             break

import  datetime
import  json
import os

# date = datetime.datetime.now().strftime("%y%m%d%H%M%S")
#
# print(date,type(date))
# inp_str = ' {"k1":123, "k2": "wupeiqi"} '  # 正确的输入      切记，内部必须是 双引号 ！！！
#
# inp_list = json.loads(inp_str)
#
# print(inp_list)

# print("请输入要添加的内容：")
# backend = input("backend:")
# server = input("server:")
# weight = input("weight:")
# maxconn = input("maxconn:")
#
# charu_dict = {}
#
# charu_dict["backend"] = backend
# charu_dict["record"] = {}
# charu_dict["record"]["server"] = server
# charu_dict["record"]["weight"] = weight
# charu_dict["record"]["maxconn"] = maxconn
#
# print(charu_dict)
#
#
# name = "1  "
#
# name.strip(name)


with open("ha","r+",encoding="utf-8") as f:
    neirong = f.readlines()
    f.seek(0)
    print(neirong[-1])