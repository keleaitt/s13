# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

# class Sheng:
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod  # 静态方法
#     def f1():
#         print("这是静态字段")
#
#     @classmethod  # 类方法，至少要有一个参数cls，类方法通过类调用
#     def f2(cls):
#         cls()  # cls是类名，可以调用静态方法
#
#
# # Sheng.f1()
#
# Sheng.f2()


class Pager:

    def __init__(self,all_count):
        self.all_count = all_count

    def f1(self):
        return  123
    def f2(self,value):
        pass
    def f3(self):
        pass

    foo = property(fget=f1,fset=f2,fdel=f3)






p = Pager(101)

# result = p.all_paper()
#
# print(result)

# p.all_pager = 1111
#
# ret = p.all_pager
#
# del p.all_pager
#
# print(ret)

ret = p.foo


print(ret)