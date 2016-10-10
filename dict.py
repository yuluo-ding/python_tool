#!/usr/bin/python
# -*- coding:utf8 -*-

import os
dict = {'a' :{'b' :1, 'c' :2}, 'd':{'e':3, 'f':4}}

for i in dict:
    print i
    for c in dict[i]:
        print c
        print dict[i][c]