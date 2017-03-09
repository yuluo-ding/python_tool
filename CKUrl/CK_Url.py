# !/usr/bin/python
# -*- coding:utf-8 -*-
import re

from CCategoryBase import CCategoryBase
from CheckResult import CheckResult


class CUrlCategories(CCategoryBase):
    out = {}

    # 将输入文件读取内存中,返回字典
    def ReadToMemory(self):
        url_dict = {}
        pattern_url = re.compile("url:([^ ]*)")
        pattern_path = re.compile("path:([^\s]*)")
        try:
            with open(self.path, 'r+') as f:
                lines = f.readlines()
                for line in lines:
                    re_url = re.search(pattern_url, line)
                    re_path = re.search(pattern_path, line)
                    if re_url and re_path:
                        url_li = [re_url.group(1), re_path.group(1)]

                        if url_dict.has_key(url_li[0]):
                            url_dict[url_li[0]] = [url_li[1]] + url_dict[url_li[0]]
                        else:
                            url_dict[url_li[0]] = [url_li[1]]
                    else:
                        pass

        except BaseException as e:
            print e
        self.out = url_dict

    # 完成 url 检查，并输出最终的字典
    def CheckUrlCategories(self, inUrl, outCategories):
        # print self.out
        if self.out.has_key(inUrl):
            a = self.out[inUrl]
            outCategories[self.path] = a
        else:
            # print "not has this url"
            pass


def test():
    testUrlCate = CUrlCategories("test1")
    testUrlCate.ReadToMemory()
    outCategories = {}
    testUrlCate.CheckUrlCategories("0-money.us", outCategories)
    print outCategories


if __name__ == '__main__':
    test()
