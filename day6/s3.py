#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

#  菜单处理

#
# def chuangjianyonghu():
#     print("创建用户！")
#
# def shanchuyonghu():
#     print("删除用户！")
#
# def dongjieyonghu():
#     print("冻结用户！")
#
# def chaxunyonghu():
#     print("查询用户！")
#
# menu ="""
#    1.创建用户
#    2.删除用户
#    3.冻结用户
#    4.查询账户
#
# """
#
# print(menu)
#
# menu_dic = {
#     "1": chuangjianyonghu,
#     "2": shanchuyonghu,
#     "3": dongjieyonghu,
#     "4": chaxunyonghu
# }
#
# while True:
#     user_option = input(">>:").strip()
#     if user_option in menu_dic:
#         menu_dic[user_option]()
#     else:
#         print("此选项不存在！")


def fun(num):
    if num == 1:
        return  1
    else:
        return  num*fun(num-1)

print(fun(6))