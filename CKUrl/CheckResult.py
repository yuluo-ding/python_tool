# !/usr/bin/python
# -*- coding:utf-8 -*-

class CheckResult(object):
    result = {}

    # def __init__(self, result):
    #     self.result = result
    #
    # def check(self, result):
    #     for key in result.keys:
    #         if key

    def __init__(self):
        self.result = {}

    def __add__(self, added = None):
        for key in added.result.keys():
            if key in self.result:
                self.result[key].union(added.result[key])
                self.result[key] = self.result[key].union(added.result[key])
            else:
                self.result[key] = added.result[key]
        return self

    def output(self):
        print self.result
