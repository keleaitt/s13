# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan
"""
1.这次作业并不完美，测试多次后有两次出现问题，后多次测试没出问题，不知道是否是程序问题还是因为自己操作问题导致

2.因为全程是输入的信息，导致可能用户会输错。很多地方没有对输入信息进行校验。也许按照题目要求直接要求用户输入字典，反而省去很多麻烦。

3.程序有很多可优化的地方，感觉函数还是分的不够细，重复代码还是比较多。

4.因为获取与增加、删除是分开写的，导致一些变量的名字本该统一，却分成多个变量名。
"""

import  datetime
import  json
import os

def huoqu():
    """
    获取ha记录
    :return: 无
    """
    shuru = input("请输入backend：")  # 用户需要查询的backend
    chaxun_wangzhi = "backend " + shuru.strip()+"\n"  # 组合成需要查询的字符串
    with open("ha", "r", encoding="utf-8") as f:
        shuju = f.readlines()
        f.seek(0)
        hanghao = 0
        if chaxun_wangzhi in shuju:  # 判断不存在 直接弹出没有查询到记录
            for line in f:
                hanghao += 1
                if chaxun_wangzhi == line:  # 查询网址记录下行号
                    for a in range(hanghao, len(shuju)):  # 开始从记录行号的开始for循环
                        if "backend" in shuju[a] :  # 循环到backend 跳出循环
                            break
                        else:
                            print(shuju[a].strip())  # strip 只能去除开头结尾的换行 空格，中间的不能去
        else:
            print("您输入的backend没有查询到记录。")


def zengjia():
    """
    增加backend记录
    :return:
    """
    print("请输入要添加的内容：")
    backend = input("backend:")
    server = input("server:")
    weight = input("weight:")
    maxconn = input("maxconn:")


    chaxun = "backend " + backend.strip() + "\n"  # 查询的字段

    charu = "        server {0} {1} weight {2} maxconn {3}\n".format(server, server, weight, maxconn)

    date = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    os.renames("ha", date)
    with open("ha", "w+", encoding="utf-8") as f1, open(date, "r+", encoding="utf-8") as f2:
        neirong = f2.readlines()
        f2.seek(0)
        hanghao = 0
        tianjia_biaoji = 0  # 内容是否已经添加 0 未添加 1 添加
        genggai = "待更改"  # 标记作用，判断是新增一行还是更改原来行
        for line in f2:
            hanghao += 1
            if chaxun == line:
                f1.write(line)
                for i in range(hanghao, len(neirong)):
                    if "backend" in neirong[i]:
                        break
                    elif server in neirong[i]:
                        genggai = server
                if genggai != server:
                    f1.write(charu)
                    tianjia_biaoji = 1
                    print("已经插入backend记录")
            elif genggai in line and tianjia_biaoji == 0:
                f1.write(charu)
                tianjia_biaoji = 1
                print("已经更改backend记录")

            elif hanghao == len(neirong) and tianjia_biaoji == 0:  # 取最后一行。
                f1.write(line)
                f1.write(chaxun)
                f1.write(charu)
                f1.write("\n")
                print("已经增加backend记录")
            else:
                f1.write(line)

def shanchu():
    """
    删除backend记录
    :return:
    """
    print("请输入要删除的内容：")
    backend = input("backend:")
    server = input("server:")
    # weight = input("weight:")
    # maxconn = input("maxconn:")

    chaxun = "backend " + backend.strip() + "\n"  # 查询的字段

    # charu = "        server {0} {1} weight {2} maxconn {3}\n".format(server, server, weight, maxconn)
    date = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    os.renames("ha", date)

    with open("ha", "w+", encoding="utf-8") as f1, open(date, "r+", encoding="utf-8") as f2:
        neirong = f2.readlines()
        f2.seek(0)
        hanghao = 0
        shanchu_biaoji = 0  # 内容是否已经删除 0 未删除 1 已删除
        shanchu = "待删除"
        backend_flag = 0  # backend标记，做为是否删除backend的标记
        for line in f2:
            hanghao += 1
            if chaxun == line:
                for i in range(hanghao, len(neirong)):
                    # print(neirong[hanghao])
                    if "backend" in neirong[i]:
                        break
                    elif server in neirong[i]:
                        shanchu = server
                    elif i > hanghao + 1 and backend_flag == 0:  # 这个操作是判断是否需要把backend删除
                        f1.write(chaxun)
                        backend_flag = 1
                if shanchu != server:
                    print("未找到您需要删除的记录")
            elif shanchu in line and shanchu_biaoji == 0:
                print("已经删除您需要删除的记录")
                shanchu_biaoji == 1

            else:
                f1.write(line)


def main():
    while True:
        print("""
        1.获取ha记录
        2.增加ha记录
        3.删除ha记录
        4.退出

        """)

        num = input("请输入操作序号:")
        if num.isdigit() and int(num) <= 4:
            if int(num) == 1:
                huoqu()
            elif int(num) == 2:
                zengjia()
            elif int(num) == 3:
                shanchu()
            elif int(num) == 4:
                exit("欢迎您再次使用此系统！")
        else:
            print("您的输入有误，请重新输入")


main()
