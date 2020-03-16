# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:15:57 2020

@author: xzhu
"""

from win32_setctime import setctime
import time
import os
filenames=os.listdir()
for filename in filenames:
    # check whether it has the form VID_....mp4
    filename=filename.strip()
    if filename.startswith('VID') and filename.endswith('.mp4'):
       print(filename)
       pattern='VID_%Y%m%d_%H%M%S.mp4'
       newtime=time.strptime(filename,pattern)
       newtime_stamp=time.mktime(newtime)
       setctime(filename,newtime_stamp)
       os.utime(filename,(newtime_stamp,newtime_stamp))