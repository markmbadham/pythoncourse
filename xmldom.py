#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:46:55 2019

@author: markbadham
"""

import xml.etree.ElementTree as ET
req = urllib.request.urlopen("http://leadingtraining.co.za/album.xml")
tree=ET.parse(req)
root=tree.getroot()
for child in root:
   print(child.tag, child.attrib)