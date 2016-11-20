# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

import re


def jisuan(args):
    """
    传入无括号的算式进行计算
    :param args: 传入无括号的算式
    :return: 返回计算结果
    """

    ret = eval(args)

    return str(ret)


def fenge(suanshi):
    """
    传入算式，利用re，将计算算式最近的（）分割分组，然后按照需求，进行相关计算替换，最终替换成没有括号的算式进行计算
    :param suanshi:
    :return:返回计算结果
    """
    while True:
        if "(" in suanshi:
            ret = re.split(r"(\(([\w\+\-\*\/]*)\))", suanshi)  # 利用re规则split成一个分组后的列表
            jieguo = jisuan(ret[2])  # 计算相关内容
            # print(ret[1])
            # 这里本来想用re.sub 进行替换但是发现，替换公式中含有加减乘数，不知道怎么处理，所以用了replace
            suanshi = suanshi.replace(ret[1], jieguo)
            # print(suanshi)
        else:
            jieguo = jisuan(suanshi)  #在算式无括号后，直接计算得出结果，返回结果
            return jieguo


def run():
    """
    运行函数
    :return:
    """
    suanshi = input("请您输入计算算式：")
    jieguo = fenge(suanshi)

    print("该算式计算结果为：" + jieguo)
