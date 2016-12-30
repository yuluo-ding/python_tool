# /user/bin/python
# -*- coding: utf-8 -*-
import os
import re
from os import listdir
from os.path import isfile, join
import shutil

path = 'D:\\xuexi\\Python\\python_tool\\CKout\\test'
dst = "dst"

def list_dir(path):
    file_list = (f for f in listdir(path) if isfile(join(path, f)))
    if file_list == None:
        print 'no file \n'
    else:
        print 'is checking...'

    for f in file_list:
        print f
        file_path = join(path, f)
        check_user_agent(file_path)
        os.remove(file_path)
        print file_path


def check_user_agent(file):

    with open(file, 'r') as f:
        data = f.read()
        pattern = r"XX-UserAgent:([^\n]*)"
        match = re.search(pattern, data)
        print match

        isExists = os.path.exists(dst)
        if not isExists:
            os.mkdir(dst)
            return
        else:
            pass

        if match:
            a = match.group()
            a = a.split(r"\r\n")[0]
            b = a.split(":")[1]

            if b == 'out':
                shutil.copy(file, dst)
        else:
            pass

list_dir(path)
