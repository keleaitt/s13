#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

from lizi.backend.commons import Foo

class YuanFoo(Foo):
    def f1(self):
        print('start')
        super(YuanFoo, self).f1()
        print('stop')




