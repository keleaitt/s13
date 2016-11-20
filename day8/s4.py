#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan


#
# class Foo:
#     pass
#
# class Bar(Foo):
#     pass
#
#
# obj = Bar()
#
# ret = isinstance(obj,Foo)
#
# # ret = issubclass(Bar,Foo)
#
# print(ret)


class C1:
    def f1(self):
        print("C1.f1")


class C2(C1):
    def f1(self):
        super(C2,self).f1()

        print("C2.f1")


obj = C2()

obj.f1()


