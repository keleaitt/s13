#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

class Foo():

    #字段（静态字段）
    CC = 234
    def __init__(self):

        #字段（普通字段）
        self.name = "Yuan"


    def show(self):
        print(self.name)