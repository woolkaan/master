#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

path = 'C:/users/'

for rootdir, dirs, files in os.walk(path):
    for file in files:
        if((file.split('.')[-1])=='txt'):
            currentpath = os.path.join(rootdir, file)
            """print (currentpath)"""
            text = open(currentpath, 'rb')
            link = text.read()
            params = (currentpath, link)
            """print (params)"""