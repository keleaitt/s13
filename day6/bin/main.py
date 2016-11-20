#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan
"""
主函数，往系统加入path
"""

import os

import  sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import jisuan as src_jisuan

if __name__ == "__main__" :
    src_jisuan.run()