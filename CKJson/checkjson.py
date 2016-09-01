# /user/bin/python
# -*- coding:utf-8 -*-

import glob
import json
import os
import time
import re

path = []

p = r"D:\\xuexi\Python\CKJson\测试\*.json"
f = glob.iglob(p.decode('utf-8').encode('gbk'))
os.remove('cap.txt')
exists = os.path.isfile('error.txt')
if exists is True:
    os.remove('error.txt')
print f

for p in f:
    path.append(p)
    json_file = file(p)
    try:
        data = json.load(json_file)

        st = json.dumps(data, sort_keys=True)
        result = re.findall('"[\S]*.cap', st)
        print result
        cap_data = open('cap.txt', 'a')
        for i in result:
            cap_data.write(i)
            cap_data.write('\n')
        cap_data.close()

    except Exception, e:
        with open('error.txt','w') as f:
            current_time = time.strftime('%m-%d: %H:%M:%S',time.localtime(time.time()))
            counter = str(e)
            f.seek(0)
            f.write(p +'  ' + str(current_time) + '\n' + '  ' + counter + '\n')
        print e

print path


