#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

#
# while True:
#     num1 = input("num1：")
#     num2 = input("num2：")
#     try:
#         num1 = int(num1)
#         num2 = int(num2)
#         print("num1+num2 = %d" % (num1 + num2))
#
#         # 从上而下捕获错误，如果对某一类错误进行捕获然后记录就用下面的方法。
#
#     except ValueError as  ex:  # 出现ValueError就会报错，其他报错不会报错，代表只捕获一种错误
#         print("出现错误，错误信息：")
#         print(ex)
#     except IndexError as  ex:  # 捕获IndexError
#         print("出现错误，错误信息：")
#         print(ex)
#     except Exception as  ex:  # 捕获Exception  ,就是捕获所有的错误
#         print("出现错误，错误信息：")
#         print(ex)
#
# try:
#     pass
# except ValueError as ex:
#     print(ex)

# try:
#     raise Exception("主动错误一下")  # 创建对象，self.message = "主动错误一下"
#     print("123")
#
# except Exception as ex:
#     print(ex)  # 执行__str__,return self.message


# class YuanException(Exception):
#
#     def __init__(self,msg):
#
#         self.msg = msg
#
#     def __str__(self):
#
#         return  self.msg
#
# try:
#     raise  YuanException("yuan自定义异常")
#
# except YuanException as Yex:
#
#
#     print(Yex)

assert  1==1