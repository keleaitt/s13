#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

class Ren:

    workdict={"厨师":[3000,10],"维修电脑":[2000,5],"运维工程师":[8000,20],"SAP开发":[30000,50],"Python大牛":[50000,30]}

    xuexidict = {"烤肉串":[500,10],"新东方厨师":[8000,20],"SAP培新":[50000,50],"老男孩Python":[5800,50]}

    fangzidict = {"北三环60平米":50000,"南三环50平米":40000,"东三环40平米":20000}

    chedict = {"吉利":50000,"卡罗拉":100000,"斯巴鲁":200000,"特斯拉":1000000}



    def __init__(self,xingbie,nianling,gongzuo,cunkuan,jingli=100,fangzi=0,che=0):

        self.xingbie = xingbie
        self.nianling = nianling
        self.gongzuo = gongzuo
        self.cunkuan = cunkuan
        self.fangzi = fangzi
        self.che = che
        self.jingli = jingli


    def  work(self):



