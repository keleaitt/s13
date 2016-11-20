# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

import subprocess


#三通道原理
obj = subprocess.Popen(["python"],
                       stdin = subprocess.PIPE,  # 命令输入通道
                       stdout=subprocess.PIPE,  # 输出结果通道
                       stderr=subprocess.PIPE, #输出错误通道
                       universal_newlines=True)

obj.stdin.write("print(1)\n")  #把命令输入进去
obj.stdin.write("print(2)")


#下面的写法很啰嗦，Popen提供了更好的写法
# obj.stdin.close()
#
# cmd_out = obj.stdout.read()
#
# obj.stdout.close()
#
# cmd_error = obj.stderr.read()
#
# obj.stderr.close()
#
#
#
# print(cmd_out)
#
# print(cmd_error)

out_err_list = obj.communicate()  #如果命令只有一行或者很简单，直接在communicate 中加入命令连上面两行也省去了

print(out_err_list)