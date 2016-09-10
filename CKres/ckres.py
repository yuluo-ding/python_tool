# /user/bin/python
# -*- coding:utf-8 -*-

import os
import glob
import shutil

if os.path.isdir('result'):
    pass
else:
    os.mkdir('result/')

name = glob.glob('*.cap')
print name

shutil.rmtree(r'result')
for list in name:
    print type(list)
    os.makedirs('result/'+list)


