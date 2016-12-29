# /user/bin/python
# -*- coding: utf-8 -*-
import re
from os import listdir
from os.path import isfile, join
import shutil

path = 'D:\\xuexi\\Python\\python_tool\\CKout\\test'
dst = "dst"


def list_dir(path):
    file_list = (f for f in listdir(path) if isfile(join(path, f)))

    for f in file_list:
        print f
        file_path = join(path, f)
        check_user_agent(file_path)
        # print type(f)


def check_user_agent(file):

    with open(file, 'r') as f:
        data = f.read()
        pattern = r"UserAgent:([^\s]*)"
        match = re.search(pattern, data)
        # result = match.group()
        if match:
            shutil.copy(file, dst)
        else:
            pass


list_dir(path)
