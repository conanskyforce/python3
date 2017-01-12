# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 23:28:08 2017

@author: conan
"""
import os

dirs = os.listdir()
i=0
for a in dirs:
    if os.path.isdir(a):
        if os.path.exists(str(i)):
            continue
        os.rename(a,str(i))
        i = i+1
print(dirs)