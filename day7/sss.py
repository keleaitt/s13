#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yuan

from xml.etree import  ElementTree as ET

tree = ET.parse("xxoo.xml")

root = tree.getroot()

for child in root:
    print(child.tag,child.attrib)
    for i  in child:
        print(i.tag,i.attrib,i.text)