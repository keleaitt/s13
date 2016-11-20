#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

class RenWu:
    def __init__(self,name,age,xingbie,renzhong,guoji,techang,cunkuan,fang,che,jingli=0):
        self.name = name
        self.age = age
        self.xingbie = xingbie
        self.renzhong = renzhong
        self.guoji =guoji
        self.techang = techang
        self.cunkuan = cunkuan
        self.fang = fang
        self.che =che
        self.jingli = jingli

class Work(RenWu):
    pass

class GuanXi(RenWu):
    pass

class DuiHua(GuanXi):
    pass



