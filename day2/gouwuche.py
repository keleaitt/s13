# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan
import datetime
import pickle

duquyonghu = open("yonghu.pkl", "rb")
duqushuju = open("shuju.pkl", "rb")

yonghu_dict = pickle.load(duquyonghu)  # 用户表记录用户及初始金额，后期用pickle读取

yonghu_shijian_dict = pickle.load(duquyonghu)  # 以用户为键，用列表记录用户购买商品后的时间

gouwujilu_dict = pickle.load(duqushuju)  # 以时间为键，记录该时间购买的商品

shangpindalei_list = pickle.load(duqushuju)  # 商品大类

shangpin_list = pickle.load(duqushuju)  # 商品明细

bencigouwu_dict = {}  # 本次购物

duquyonghu.close()
duqushuju.close()

user = input("请输入您的用户名：")

yue = yonghu_dict.setdefault(user, 0)  # 如果没有这个用户在用户字典里加入记录

print("欢迎光临".center(50, "-"))
while True:
    print('''
    请选择功能清单：

    1.查询历史消费记录

    2.充值后购买商品


    ''')
    gongnengxuanze = input("请输入您的选择")

    if gongnengxuanze.isdigit() and int(gongnengxuanze) == 1:
        if user not in yonghu_shijian_dict:
            print("您是第一次购物，未有您的购物记录。")
        else:

            for index_ls, shijian in enumerate(yonghu_shijian_dict[user]):
                print(index_ls + 1, ":", shijian)
            xuanzejilu = input("请选择您需要查看历史记录的序号(返回请按b)：")
            if xuanzejilu.isdigit() and int(xuanzejilu) <= len(yonghu_shijian_dict[user]):
                for xuhao, shuju in enumerate(gouwujilu_dict[yonghu_shijian_dict[user][int(xuanzejilu) - 1]]):
                    print(xuhao + 1, ":", shuju,
                          gouwujilu_dict[yonghu_shijian_dict[user][int(xuanzejilu) - 1]][shuju][0],
                          gouwujilu_dict[yonghu_shijian_dict[user][int(xuanzejilu) - 1]][shuju][1])
            elif xuanzejilu == "b":
                continue

    elif gongnengxuanze.isdigit() and int(gongnengxuanze) == 2:
        while True:
            chongzhi = input("请输入您要充值的金额：")  # 充值金额
            if chongzhi.isdigit():
                yue += int(chongzhi)
                print("您现在的余额是【%s】" % yue)

                while True:
                    for index_dalei, i in enumerate(shangpindalei_list):  # 列出商品大类列表
                        print(index_dalei + 1, ":", i)
                    xuanzedalei = input("请选择您需要商品的大类：")
                    if xuanzedalei.isdigit() and int(xuanzedalei) < len(shangpindalei_list) + 1:  # 判断是数字且小于


                        while True:
                            for index_mx, (sp_ming, sp_jia) in enumerate(
                                    shangpin_list[int(xuanzedalei) - 1]):  # 根据选择列出商品明细列表
                                print(index_mx + 1, ":", sp_ming, sp_jia)
                            xuanzemingxi = input("请输入您需要购买商品的序号(返回上一层菜单请输入b)：")
                            if xuanzemingxi.isdigit() and int(xuanzemingxi) < len(shangpin_list[index_dalei]) + 1:
                                while True:
                                    shuliang = input("请输入您要购买的数量：")
                                    if shuliang.isdigit():
                                        zongjine = int(
                                            shangpin_list[int(xuanzedalei) - 1][int(xuanzemingxi) - 1][1]) * int(
                                            shuliang)
                                        if zongjine > yue:
                                            print("您的余额不足!")
                                            break
                                        else:
                                            yue -= zongjine
                                            if shangpin_list[int(xuanzedalei) - 1][int(xuanzemingxi) - 1][
                                                0] in bencigouwu_dict:
                                                bencigouwu_dict[
                                                    shangpin_list[int(xuanzedalei) - 1][int(xuanzemingxi) - 1][0]][
                                                    0] += int(shuliang)
                                                bencigouwu_dict[
                                                    shangpin_list[int(xuanzedalei) - 1][int(xuanzemingxi) - 1][0]][
                                                    1] += int(zongjine)
                                            else:
                                                bencigouwu_dict.setdefault(
                                                    shangpin_list[int(xuanzedalei) - 1][int(xuanzemingxi) - 1][0],
                                                    [int(shuliang), zongjine])
                                            print("您现在的余额是%s" % yue)

                                            jixugouwu = input("您是否继续购物？（y--继续，n--退出）")

                                            if jixugouwu == "y":
                                                break
                                            else:

                                                print("序号  货物名称   数量    金额")
                                                for xuhao, shuju in enumerate(bencigouwu_dict):
                                                    print(xuhao + 1, "    ", shuju, "    ", bencigouwu_dict[shuju][0],
                                                          "    ",
                                                          bencigouwu_dict[shuju][1])
                                                # 更新各个字典
                                                date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                                if user in yonghu_shijian_dict:
                                                    yonghu_shijian_dict[user].append(date)
                                                else:
                                                    yonghu_shijian_dict[user] = [date]
                                                gouwujilu_dict[date] = bencigouwu_dict
                                                yonghu_dict[user] = yue

                                                # 保存各个字典

                                                cunruyonghu = open("yonghu.pkl", "wb")
                                                cunrushuju = open("shuju.pkl", "wb")
                                                pickle.dump(yonghu_dict, cunruyonghu)
                                                pickle.dump(yonghu_shijian_dict, cunruyonghu)
                                                pickle.dump(gouwujilu_dict, cunrushuju)
                                                pickle.dump(shangpindalei_list, cunrushuju)
                                                pickle.dump(shangpin_list, cunrushuju)

                                                cunruyonghu.close()
                                                cunrushuju.close()

                                                '''print(yonghu_shijian_dict, "++++用户时间", gouwujilu_dict, "+++购物记录",
                                                      yonghu_dict, "+++用户余额",
                                                      gouwujilu_dict, "+++购物记录",
                                                      )'''

                                            print("您现在的余额是%s" % yue)

                                            exit("欢迎您的再次光临！！")


                                    else:
                                        print("您的输入有误，请重新输入")
                            elif xuanzemingxi == "b":

                                break



                            else:
                                print("您输入错误，请重新输入！")
                    else:
                        print("您输入错误!请重新输入 ")


            else:
                print("您的输入金额有误请重新输入")
    else:
        print("您的输入有误，请重新输入！")
