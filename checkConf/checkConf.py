# /user/bin/python
# -*- coding:utf-8 -*-

import urllib

from bs4 import BeautifulSoup

file = open("yj_hp_in.conf")


soup = BeautifulSoup(file, 'xml')

des = soup.SITE['DESCRIPTION']
description = urllib.unquote(des.encode("UTF-8"))

print type(description)
print description
print soup.name

