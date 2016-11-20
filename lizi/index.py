#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

from settings import ClassName
from settings import Path

def execute():

    model = __import__(Path,fromlist=True)

    cls = getattr(model,ClassName)
    obj= cls()
    obj.f1()
    print(ClassName)


if __name__ == "__main__":
    execute()