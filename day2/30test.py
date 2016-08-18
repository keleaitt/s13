#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

shangpin_list = [
    ('Iphone',5888),
    ('Mac Air',8000),
    ('Mac Pro',9000),
    ('xiaomi',1999),
    ('Bike',800),
    ('Cloth',200),
    ('Apple',10),

]

#for i in shangpin_list:
    # sp_ming,sp_jiage = i

for index,zu in enumerate(shangpin_list):
    print( index+1,"\033[42;1m：\033[0m",zu)