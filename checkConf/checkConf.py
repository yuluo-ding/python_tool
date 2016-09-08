# /user/bin/python
# -*- coding:utf-8 -*-

import urllib

from bs4 import BeautifulSoup

file = open("yj_hp_in.conf")

soup = BeautifulSoup(file, 'xml')
tags = soup.SITE
print tags.attrs

des_txt = open("description.txt", 'w')
des_txt.close()

for tag in soup.find_all(["SITE"]):

    domain = tag['DOMAIN']
    dos = urllib.unquote(domain.encode("UTF-8"))

    description = tag['DESCRIPTION']
    des = urllib.unquote(description.encode("UTF-8"))
    print dos + " " + des

    des_txt = open("description.txt", 'a')
    des_txt.write( dos + " " + des + "\n")

des_txt.close()