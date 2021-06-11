#!/usr/bin/python 
# -*- coding: utf-8 -*-

import os
start = input('input simulator name')

if start == 'linux':
    os.system('start linux.exe')
    pass
else:
    print('Error:Invalid Name')
    os.system('pause')
    pass
