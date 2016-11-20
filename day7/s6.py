# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

class F1:
    def show(self):
        print("show")

    def foo(self):
        print(self.name)


class F2(F1):  # F2 继承F1

    def __init__(self, name):
        self.name = name

    def look(self):
        print("look")


obj  = F2("yuan")

obj.foo()
