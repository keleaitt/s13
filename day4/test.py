#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

# def dakai_zsq(func):
#     def dakai():
#         with open("xinxi","r+",encoding="utf-8") as f1:
#             func()
#             f1.seek(0,2)
#             f1.write(tianjia_dic)
#     return dakai
#
#
#
# @dakai_zsq
# def tianjiazhanghu():
#     name = input("请输入用户名：")
#     pwd = input("请输入用户密码：")
#     quanxian = input("请输入用户权限0（管理员）/ 1(普通用户）：")
#     touzhi = input("请输入该用户透支额度：")
#     huankuanri = input("请输入还款日：")
#     tianjia_dic = {"name": name, "pwd": pwd, "quanxian": quanxian, "touzhi": touzhi, "huankuanri": huankuanri,
#                    "zhuangtai": "0"}
#
# tianjiazhanghu()
import json
import  datetime
import os

def zhidingedu():
    name = input("请输入修改的用户名：")
    touzhi = input("请输入该用户最大透支额度：")
    xiugaiyonghu(name = name ,touzhi = touzhi)

def xiugaiyonghu(**kwargs):
    date = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    os.renames("xinxi",date)
    with open("xinxi", "w+", encoding="utf-8") as new,open(date,"r+",encoding="utf-8") as old:
        for lines in old:
            dic = json.loads(lines)

            if dic["name"] == kwargs["name"]:
                dic.update(kwargs)
                v = json.dumps(dic)
                new.write(v)
                new.write("\n")
            else:
                new.write(lines)

zhidingedu()