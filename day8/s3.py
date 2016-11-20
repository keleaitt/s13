#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan


# class Foo:
#
#     def __init__(self,name):
#
#         self.__name = name  # 变成私有的 加上两个__
#
#     def f1(self):
#
#         print(self.__name)
#
# obj = Foo("abc")
#
# print(obj.__name)
#
# obj.f1()


class Foo:

    __cc = 123
    def __init__(self,name):

        self.name = name

    def f1(self):
        print(Foo.__cc)

    def f2():
        print(Foo.__cc)


obj = Foo("aaa")

print(_Foo__f2())  # 这样就可以访问了，一种万不得已才用的方法

