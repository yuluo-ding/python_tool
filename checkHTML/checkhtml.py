# /user/bin/python
# -*- coding:utf-8 -*-

import re
import urllib2
import sys

reload(sys)

url = "https://oms.yhjj.com/MS_OMG/Finance/Manage_GCK.aspx?ModuleID=CFF5B1E3-0181-45FA-B28F-6CCDD773A1EE#"


response = urllib2.urlopen(url)
ht = response.read().decode("GBK")
print ht

file = open("test.html")
print file
res = re.search(r'设计业务---设计费</font></td>\s*<td>&nbsp;<font color="BLACK">([^<]*)', ht, re.S)

print res
