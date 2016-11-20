#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan


import time

import sys

def jindutiao(jindu,zonge):

    ret = (jindu/zonge)*100

    r = "\r%s%d%%"%("="*jindu,ret)
    sys.stdout.write(r)
    sys.stdout.flush()


if __name__ =="__main__":
    for i in range(101):
        time.sleep(0.1)
        jindutiao(i,100)

