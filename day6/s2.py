#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

# import s1
#
# import lib.config
#
# s1.login()
#
# lib.config.config()


#
#
# import json
#
# li = '["bbs","cctv"]'
#
# ret = json.loads(li)
#
# print(ret)
#
#
# import time
#
# # ret = time.strftime("%Y-%m-%d", time.localtime())
# ret = time.mktime(time.strptime("2016-09-07", "%Y-%m-%d"))
#
#
#
#
# print(ret)

import  datetime
import time

ret = datetime.datetime.now()

print(ret.replace(2014,6,12))
