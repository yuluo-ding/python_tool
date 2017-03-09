# !/usr/bin/python
# -*- coding:utf-8 -*-
import os

from CK_Url import CUrlCategories


class Checkblacklist(object):
    domain = []

    def __init__(self, path, str, lib):
        self.path = path
        self.str = str
        self.lib = lib

    def list_file(self):
        list_dir = os.walk(self.path)
        for root, dirs, files in list_dir:
            for file_name in files:
                if file_name == self.str:
                    tmp_path = os.path.join(root, file_name)
                    with open(tmp_path, 'r+') as f:
                        f = f.readlines()
                        for line in f:
                            self.domain.append(line)
                else:
                    pass

    def merge(self, result, out):
        for key in out.keys():
            if key in result:
                a = result[key] + out[key]
                result[key] = a
            else:
                result[key] = out[key]

    def get_res(self, outCategories):
        # 调用 CK_Url 的方法
        result = {}
        res = CUrlCategories(self.lib)
        res.ReadToMemory()
        tmp_out = {}
        for d in self.domain:
            d = d.strip('\n')
            res.CheckUrlCategories(d, tmp_out)
            self.merge(result, tmp_out)
        for key in result.keys():
            result[key] = set(result[key])
            outCategories[key] = set(result[key])


def test():
    # 传入的参数分别为，目标文件夹，目标文件名，库名
    a = Checkblacklist("blacklist", "domains", "test")
    a.list_file()
    outCategories = {}
    a.get_res(outCategories)
    print outCategories


if __name__ == '__main__':
    test()
