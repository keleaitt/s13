#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

import  pickle

yonghu_dict = {"li": 8000, "zhai": 9999}  # 用户表记录用户及初始金额，后期用pickle读取

yonghu_shijian_dict = {}  # 以时间为键，记录用户购买商品后的时间

gouwujilu_dict = {}  # 以时间为键，记录该时间购买的商品

shangpindalei_list = ["食品类", "洗护类", "电子类", "汽车类"]  # 商品大类

shangpin_list = [
    [("酸奶", 8), ("火龙果", 20), ("海参", 3000)],
    [("海飞丝", 30), ("洗洁精", 6), ("肥皂", 5)],
    [("xiaomi", 4999), ("Apple", 10000), ("联想", 3999)],
    [("骐达", 129000), ("欧蓝德", 220000), ("奥迪", 500000)]
]  # 商品小类

cunruyonghu = open("yonghu.pkl","wb")
cunrushuju = open("shuju.pkl","wb")
pickle.dump(yonghu_dict,cunruyonghu)
pickle.dump(yonghu_shijian_dict,cunruyonghu)
pickle.dump(gouwujilu_dict,cunrushuju)
pickle.dump(shangpindalei_list,cunrushuju)
pickle.dump(shangpin_list,cunrushuju)

cunruyonghu.close()
cunrushuju.close()