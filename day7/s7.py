# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

class S0:
    def f2(self):
        print("S0")

class S1(S0):
    def f1(self):
        self.f2()


class S2:
    def f3(self):
        self.f1()

    def f2(self):
        print("S2")


class S3(S1,S2):
    def f3(self):
        pass


obj = S3()

obj.f2()