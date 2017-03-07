# !/usr/bin/python
# -*- coding:utf-8 -*-
import re


class CUrlCategories(object):
    out = {}

    def __init__(self, path):
        self.path = path

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
        out = url_dict
        return out

    # 完成 url 检查，并输出最终的字典
    def CheckUrlCategories(self, inUrl, out):
        if out.has_key(inUrl):
            a = out[inUrl]
            print a
        else:
            return "not has this url"



def test():
    testUrlCate = CUrlCategories("test")
    out = testUrlCate.ReadToMemory()
    testUrlCate.CheckUrlCategories("www.sina.com", out)


if __name__ == '__main__':
    test()
