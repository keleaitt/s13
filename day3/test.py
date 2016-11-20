# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

#
# old_dict = {
# "#1":8,
# "#2":4,
# "#4":2,
# }
#
# new_dict = {
# "#1":4,
# "#2":4,
# "#3":2,
# }
#
# old_set_key = set(old_dict.keys())
# new_set_key = set(new_dict.keys())
#
# print(old_set_key,new_set_key)
#
# zengjia = new_set_key.difference(old_set_key)
#
# shanchu = old_set_key.difference(new_set_key)
#
# print(zengjia)
# with open("ha","r",encoding="utf-8") as f:
#     shuju = f.read()
#     shuju_list = shuju.split("\n")
#     for  i  in range(len(shuju_list)):
#         if "backend" in shuju_list[i] and "buy.oldboy.org" in shuju_list[i] and i+1 <=len(shuju_list):
#             for a in range(i+1,len(shuju_list)):
#                 if "backend"  in shuju_list[a] or shuju_list[a] == "":
#                     break
#                 else:
#                     print(shuju_list[a].strip())
#
# a = "   a b c"
# print(a.strip())
# import  datetime
#
# date = str(datetime.datetime.now())[:19]
#
# print(date)

import  datetime
import  json
import os
print("请输入要添加的内容：")
backend = input("backend:")
server = input("server:")
weight = input("weight:")
maxconn = input("maxconn:")

# charu_dict = {}
#
# charu_dict["backend"] = backend
# charu_dict["record"] = {}
# charu_dict["record"]["server"] = server
# charu_dict["record"]["weight"] = weight
# charu_dict["record"]["maxconn"] = maxconn

chaxun = "backend "+backend.strip()+"\n"  # 查询的字段

charu   = "        server {0} {1} weight {2} maxconn {3}\n".format(server,server,weight,maxconn)

date = datetime.datetime.now().strftime("%y%m%d%H%M%S")
os.renames("ha", date)
with open("ha", "w+", encoding="utf-8") as f1,  open(date, "r+", encoding = "utf-8") as f2:
    neirong = f2.readlines()
    f2.seek(0)
    hanghao = 0
    tianjia_biaoji = 0 #内容是否已经添加 0 未添加 1 添加
    for line in f2:
        hanghao += 1
        if chaxun == line :
            for i in range(hanghao,len(neirong)):
                if "backend" in neirong[i]:
                    break
                elif server in neirong[i]:
                    num = i
        elif neirong[num] == line :
            f1.write(charu)
            tianjia_biaoji = 1
        elif neirong[-2] == line and tianjia_biaoji == 0: # 取-2是因为发现最后一行往往是个空行。
            f1.write(line)
            f1.write(chaxun)
            f1.write(charu)
            f1.write("\n")
        else:
            f1.write(line)




