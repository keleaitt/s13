# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

class  C1:
    def __init__(self,name,obj):
        self.name = name
        self.obj = obj


class C2:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def addage(self):
        self.age += 1

class C3:
    def __init__(self,name,obj):
        self.name = name
        self.obj = obj


c2_obj = C2("Yuan",18)

c1_obj = C1("Zhai",c2_obj)  # 可以把一个对象封装到另外一个对象中

c3_obj = C3("SUN",c1_obj)


c1_obj.obj.addage()   #可以看出这里用c1_obj可以访问C2类对象c2_obj的age 并执行c2_obj的方法

#通过c3_obj访问addage方法

c3_obj.obj.obj.addage()

print(c3_obj.obj.obj.age)
