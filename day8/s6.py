#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

class Foo:

    instance = False

    def __init__(self,name):
        self.name = name

    @classmethod
    def get_instance(cls):  # 创建一个类方法
        #cls是类名

        if cls.instance:

            return cls.instance

        else:

            obj = cls("Yuan")

            cls.instance = obj

            return  obj

obj1 = Foo.get_instance()
obj2 = Foo.get_instance()

print(obj1)
print(obj2)

