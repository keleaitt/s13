#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan
#
# def outer(func):
#     def inner(*arg,**kwargs):
#
#         print("start")
#         r =func(*arg,**kwargs)
#         print("end")
#         return  r
#     return  inner
#

# @ + 函数名
#功能 1. 自动执行outer函数并且将其下面的函数名称f1，当做参数传递。
#     2.将outer函数的返回值，重新复制给f1
# @outer
# def f1(*arg,**kwargs):
#     print(arg)
#     print(kwargs)
#     return "小羊"
#
#
# k = f1(123,456,5555,name = "156")
#
# print(k)
#
# dict = {"name":"yuan","pwd":"789","quanxian":"0","touzhi":"100000","huankuanri":"15","zhuangtai":"0","xiaofei":"0"}
#
# print("""
# 当前用户：%s
#
#
# """% (name ="haha" if 1 ==
# dic = {"name":"yuan","pwd":"789","quanxian":"0","touzhi":"100000","huankuanri":"15","zhuangtai":"0","xiaofei":"0"}
#
# quanxian = "普通用户" if dic["quanxian"] == "1" else "管理用户"
# zhuangtai = "正常" if dic["zhuangtai"] == "0" else "冻结用户"
# print("""
# 修改后的用户信息为：
# %s 用户为 %s
# 该用户状态为：%s
# 密码：%s
# 透支额度： %s
# 已消费：%s
# 每月还款日为 %s
#
#
#
#
# """ % ( dic["name"], quanxian, zhuangtai, dic["pwd"], dic["touzhi"], dic["xiaofei"], dic["huankuanri"]) )
import datetime
date = datetime.datetime.now().strftime("%d")
print(date,type(date))