# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

# s = "print(123)"
#
# r = compile(s,"<string>","exec")
#
# print(r)
#
# exec(r)
#
# s = "8*8"
#
# r = compile(s,"<string>","exec")
#
# ret = exec(r)
#
# print(ret)
#
# v = eval(s)
#
# print(v)
# print(dir(str))

# n1,n2 = divmod(97,10)
#
# print(n1)
#
# print(n2)'
#
# li = [11, 22, 33, 44, 55, 66]
#
# def f1(i):
#
#     if i > 30:
#         return  True
#
# ret = filter(f1, li)
#
# print(list(ret))

#
# li = [11, 22, 33, 44, 55, 66]
#
# ret = map(lambda a : a+100, li)
#
# print(list(ret))

# NAME = "YUAN"
#
# def  show():
#     a = 123
#     b =345
#     print(locals())
#     print(globals())
#
# show()

# s = "李杰"
#
# for i  in s:
#     print(i)
# print(2 ** 10)
#
# print(pow(2,10)),
# li = [11 ,22, 33, 44, 55]
#
# k = reversed(li)
#
# print(list(k))

# v = round(1.9)
#
# print(v)

# s = "sssssssss"
#
# k  = slice("ss",s)
#
# print(k)
# li1 = ["yuan",11 ,22, 33, 44, 55,10]
#
# li2 = ["is",11, 22, 33, 44,55 ,77, 99]
#
# r = zip(li1,li2)
#
# temp = list(r)[0]
#
# v = " ".join(temp)
#
# print(v)

# import  json
#
# s = '{"yuan":"shuai","zhai":"qian"}'
#
# v = json.loads(s)
#
# print(v,type(v))

# def f1 ():
#     print("123")
#
#
# def  f2(xxx):
#     xxx()
#
# f2(f1)
import  json
with open("xinxi1","r+",encoding="utf-8") as f1:
    for lines in f1:
        YONGHU_DIC = json.loads(lines)
        print(YONGHU_DIC,type(YONGHU_DIC))
