# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

shuju = {'2016-08-17 20:48:38': {'海参': [1, 3000], '酸奶': [20, 160]}, '2016-08-17 20:52:05': {'海飞丝': [20, 600], '肥皂': [4, 20]}}

for index,zhi in enumerate(shuju['2016-08-17 20:48:38']):


    print(index+1,zhi,shuju["2016-08-17 20:48:38"][zhi][0],shuju["2016-08-17 20:48:38"][zhi][1])

