# !/usr/bin/python
# -*- coding:utf-8 -*-

class CCategoryBase(object):
    def __init__(self, path=''):
        self.path = path

    def Init(self, path):
        self.path = path

    def ReadCategory(self):
        pass

    def CheckUrlCategories(self):
        pass

    def CheckHostCategories(self):
        pass