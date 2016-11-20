# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

import json
import datetime
import os
import time

YONGHU_DIC = {}  # 登录用户的信息
YONGHU_LIST = []  # 存储所有用户的name值


def panduanyonghu_zsq(func):
    """
    装饰器
    1.主要完成判断用户是否存在的功能。
    2.根据权限判断是否使用判断用户功能

    :param func:
    :return:
    """

    def panduanyonghu():
        while True:
            xingming = input("请输入您要修改的用户名：")
            if xingming in YONGHU_LIST:  # 姓名在全局变量列表的话，将姓名传递到func
                func(xingming)
                break
            else:
                print("您输入的用户名不存在，请重新输入")

    return panduanyonghu


def zidonghuankuan_zsq(func):
    """
    自动还款的装饰器，到了还款日，强制用户还款。
    :param func:
    :return:
    """

    def zidonghuankuan():
        date = datetime.datetime.now().strftime("%d")  # 取当前时间的日，与字典中还款日对照
        while True:
            if YONGHU_LIST == []:
                break
            elif date == YONGHU_DIC["huankuanri"] and int(YONGHU_DIC["xiaofei"]) > 0:
                print("今天是您的还款日，请还款！本月需要还%s 元" % YONGHU_DIC["xiaofei"])
                cunkuan(YONGHU_DIC["name"])
                continue

            else:
                func()

    return zidonghuankuan


@zidonghuankuan_zsq
def guanliyuan():
    """
    管理员菜单，感觉写的很不好，应该考虑用其他办法实现
    :return:
    """
    while True:
        print("""
        1.账户管理
        2.现金管理
        3.重新登录
        4.退出程序

        """)
        n1 = input("请输入您的选择：")

        if n1 == "1":
            print("""
            1.添加账户
            2.指定用户最大透支额度
            3.指定用户还款日
            4.冻结用户
            5.修改用户密码
            6.删除账户
            7.返回上层菜单

            """)
            n2 = input("请输入您的选择：")
            if n2 == "1":
                tianjiazhanghu()
            if n2 == "2":
                zhidingedu()
            if n2 == "3":
                huankuanri()
            if n2 == "4":
                dongjieyonghu()
            if n2 == "5":
                xiugaimima()
            if n2 == "6":
                shanchuyonghu()
            if n2 == "7":
                break

        if n1 == "2":
            print("""
            1.取款
            2.存款
            3.用户转账
            4.返回上层菜单

            """)
            n3 = input("请输入您的选择：")
            if n3 == "1":
                qukuan(YONGHU_DIC["name"])
            if n3 == "2":
                cunkuan(YONGHU_DIC["name"])
            if n3 == "3":
                yonghuzhuanzhang(YONGHU_DIC["name"])
            if n3 == "4":
                break
        if n1 == "3":
            """
            global  YONGHU_DIC
            YONGHU_DIC = {}
            这里以前的处理方式是上面的语句，但是加上后报错，但不影响程序运行，不知道为什么。下为报错信息
            SyntaxWarning: name 'YONGHU_DIC' is used prior to global declaration
            global  YONGHU_DIC

            """
            YONGHU_DIC.clear()
            del YONGHU_LIST[:]
            break
        if n1 == "4":
            exit("欢迎再次使用！")


@zidonghuankuan_zsq
def putongyonghu():
    """
    普通用户的菜单，同管理员菜单一样，实现办法不好
    :return:
    """
    while True:
        print("""
        1.取款
        2.存款
        3.用户转账
        4.修改密码
        5.重新登录
        6.退出系统

        """)
        n1 = input("请输入您的选择：")
        if n1 == "1":
            qukuan(YONGHU_DIC["name"])
        if n1 == "2":
            cunkuan(YONGHU_DIC["name"])
        if n1 == "3":
            yonghuzhuanzhang(YONGHU_DIC["name"])
        if n1 == "4":
            putongxiugaimima(YONGHU_DIC["name"])
        if n1 == "5":
            YONGHU_DIC.clear()
            del YONGHU_LIST[:]
            break
        if n1 == "6":
            exit("欢迎再次使用！")


def yonghuzhuanzhang(name):
    """
    实现用户转账功能，感觉应该能调用其他函数实现，并且等待1秒不是很好的解决办法。
    :param name:
    :return:
    """
    while True:
        shoukuanren = input("请输入收款人：")
        if shoukuanren in YONGHU_LIST:
            while True:

                xiaofei = input("请输入您的转账金额:")
                v = panduanjine(name, xiaofei)
                if v:
                    xiaofeigengxin(name, xiaofei)
                    print("已经成功转账！")

                    """
                    这里之所以等待1秒，是因为执行两次xiaofeigengxin.
                    都牵扯到变更名字问题，如果不等待一秒，那么会因为重命名时因为文件名相同而报错。
                    （重命名用的日期到秒的方式）

                    """
                    time.sleep(1)
                    xiaofeigengxin(shoukuanren, xiaofei=str(-int(xiaofei)))
                    break
                else:
                    print("您的金额已经超过限额，请重新输入！")
            break
        else:
            print("您输入的收款人不存在，请重新输入")


@panduanyonghu_zsq
def zhidingedu(name):
    """
    给用户指定额度的函数
    :param name: panduanyonghu_zsq 传进参数name
    :return:
    """
    touzhi = input("请输入该用户最大透支额度：")
    xiugaiyonghu(name=name, touzhi=touzhi)


@panduanyonghu_zsq
def huankuanri(name):
    """
    给用户指定还款日
    :param name: panduanyonghu_zsq 传进参数name
    :return:
    """
    huankuanri = input("请输入用户的还款日（1-28）：")
    xiugaiyonghu(name=name, huankuanri=huankuanri)


@panduanyonghu_zsq
def dongjieyonghu(name):
    """
    冻结用户
    :param name: panduanyonghu_zsq 传进参数name
    :return:
    """
    zhuangtai = input("是否要 冻结/解冻 该用户（0 解冻/1 冻结）:")
    xiugaiyonghu(name=name, zhuangtai=zhuangtai)


@panduanyonghu_zsq
def xiugaimima(name):
    """
    修改密码
    :param name:
    :return:
    """
    pwd = input("请输入您要修改的密码：")
    xiugaiyonghu(name=name, pwd=pwd)


@panduanyonghu_zsq
def shanchuyonghu(name):
    """
    删除用户
    :param name:
    :return:
        """
    date = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    os.renames("xinxi", date)
    with open("xinxi", "w+", encoding="utf-8") as new, open(date, "r+", encoding="utf-8") as old:
        for lines in old:
            dic = json.loads(lines)
            if dic["name"] == name:
                print("已经删除该用户！")
            else:
                new.write(lines)


def putongxiugaimima(name):
    """
    一般用户的修改密码函数，本来想统一用xiugaimima函数实现。但是调试许久失败了，所以重写一个函数。
    :param name:
    :return:
    """
    pwd = input("请输入您要修改的密码：")
    xiugaiyonghu(name=name, pwd=pwd)


def qukuan(name):
    """
    取款的函数
    :param name:
    :return:
    """

    while True:
        xiaofei = input("请输入您要取款数额：")
        v = panduanjine(name=name, xiaofei=xiaofei)

        if v:
            xiaofeigengxin(name=name, xiaofei=xiaofei)
            break
        else:
            print("您的金额已经超过限额，请重新输入！")


def cunkuan(name):
    """
    用户存款函数
    :param name:
    :return:
    """
    xiaofei = input("请输入您本次要存入的金额:")
    v = panduanjine(name=name, xiaofei=str(-int(xiaofei)))
    if v:

        xiaofeigengxin(name=name, xiaofei=str(-int(xiaofei)))
    else:
        print("您的金额已经超过限额，请重新输入！")


def panduanjine(name, xiaofei):
    """
    判断用户金额是否超过限额
    :param name:
    :param xiaofei:
    :return:  超过返回False  没超返回True
    """
    """

    :param name: 传递进来的当前用户
    :param xiaofei: 本次消费金额
    :return: 超过限额 False 不超限额True
    """
    with open("xinxi", "r", encoding="utf-8") as f1:
        for lines in f1:
            dic = json.loads(lines)
            if dic["name"] == name:
                if int(dic["touzhi"]) >= int(dic["xiaofei"]) + int(xiaofei):
                    return True
                else:
                    return False


def xiaofeigengxin(name, xiaofei):
    """
    完成消费更新
    :param name:  传递进来的用户名
    :param xiaofei: 传递进来的本次消费金额
    :return: None
    """
    date = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    os.renames("xinxi", date)
    with open("xinxi", "w+", encoding="utf-8") as new, open(date, "r+", encoding="utf-8") as old:
        for lines in old:
            dic = json.loads(lines)
            if dic["name"] == name:
                dic["xiaofei"] = str(int(dic["xiaofei"]) + int(xiaofei))
                if dic["name"] == YONGHU_DIC["name"]:
                    YONGHU_DIC["xiaofei"] = dic["xiaofei"]
                v = json.dumps(dic)
                new.write(v)
                new.write("\n")
                if dic["name"] == YONGHU_DIC["name"]:
                    YONGHU_DIC["xiaofei"] = dic["xiaofei"]
                    print("""
                        当前用户信息为：
                        用户名 ： %s
                        密码：%s
                        透支额度： %s
                        已消费： %s
                        还款日为每月 %s 日

                        """ % (
                        dic["name"], dic["pwd"], dic["touzhi"], dic["xiaofei"], dic["huankuanri"]))
                    continue
            else:
                new.write(lines)


def tianjiazhanghu():
    """
    添加账户，因为这是第一个写的功能，所以实现起来较为简单。
    :return:
    """
    while True:

        name = input("请输入要添加的用户名：")
        if name in YONGHU_LIST:
            print("您输入的用户已经存在，请重新输入！")
        else:
            pwd = input("请输入用户密码：")
            quanxian = input("请输入用户权限0（管理员）/ 1(普通用户）：")
            touzhi = input("请输入该用户透支额度：")
            huankuanri = input("请输入还款日：")
            tianjia_dic = dict(name=name, pwd=pwd, quanxian=quanxian, touzhi=touzhi, huankuanri=huankuanri,
                               zhuangtai="0",
                               xiaofei="0")
            date = datetime.datetime.now().strftime("%y%m%d%H%M%S")
            os.renames("xinxi", date)
            with open("xinxi", "w+", encoding="utf-8") as new, open(date, "r+", encoding="utf-8") as old:
                for lines in old:
                    if lines == "\n":  # 这里加上这句是在添加用户的时候如果出现空行  有时候会报错
                        continue
                    else:
                        new.write(lines)
                new.write("\n")
                v = json.dumps(tianjia_dic)
                new.write(v)
                YONGHU_LIST.append(name)
                print("添加用户成功")
            break


def xiugaiyonghu(**kwargs):
    """
    完成修改用户数据的功能
    :param kwargs: 接收一个字典，然后用字典update主字典
    :return:
    """
    date = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    os.renames("xinxi", date)
    with open("xinxi", "w+", encoding="utf-8") as new, open(date, "r+", encoding="utf-8") as old:
        for lines in old:
            dic = json.loads(lines)

            if dic["name"] == kwargs["name"]:
                dic.update(kwargs)
                v = json.dumps(dic)
                new.write(v)
                new.write("\n")
                quanxian = "普通用户" if dic["quanxian"] == "1" else "管理用户"
                zhuangtai = "正常" if dic["zhuangtai"] == "0" else "冻结用户"
                print("""
                修改后的用户信息为：
                %s 用户为 %s
                该用户状态为：%s
                密码：%s
                透支额度： %s
                已消费：%s
                还款日为每月 %s 日

                """ % (dic["name"], quanxian, zhuangtai, dic["pwd"], dic["touzhi"], dic["xiaofei"], dic["huankuanri"]))
            else:
                new.write(lines)


def main():
    """
    主函数
    :return:
    """
    print("""
    欢迎进入ATM系统，请登录
    """)
    while True:

        name = input("请输入您的用户名：")
        pwd = input("请输入您的密码：")

        with open("xinxi", "r+", encoding="utf-8") as xinxi:
            for lines in xinxi:
                xunhuanyonghu_dict = json.loads(lines)
                YONGHU_LIST.append(xunhuanyonghu_dict["name"])
                # print(YONGHU_LIST)
                if xunhuanyonghu_dict["name"] == name and xunhuanyonghu_dict["pwd"] == pwd:
                    global YONGHU_DIC
                    YONGHU_DIC = json.loads(lines)

                    # if dic["quanxian"] == "1":
                    #     putongyonghu()

            if YONGHU_DIC == {}:
                print("您的输入有误请重新输入！")
                del YONGHU_LIST[:]
        if "quanxian" in YONGHU_DIC and YONGHU_DIC["quanxian"] == "0" and YONGHU_DIC["zhuangtai"] == "0":
            guanliyuan()
        elif "zhuangtai" in YONGHU_DIC and YONGHU_DIC["zhuangtai"] == "1":
            print("您的账户已冻结，请重新登录")
            del YONGHU_LIST[:]
        elif "quanxian" in YONGHU_DIC and YONGHU_DIC["quanxian"] == "1" and YONGHU_DIC["zhuangtai"] == "0":
            putongyonghu()


main()
