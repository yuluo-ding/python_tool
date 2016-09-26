# /user/bin/python
# -*- coding:utf-8 -*-
import glob
import os

def creat_web_dir():
    path = os.path.abspath("/android")
    print path
    file_name = glob.glob("./android/")
    print file_name

def creat_file_dir():
    if os.path.isdir('./result'):
        pass
    else:
        os.mkdir('result')

if __name__ == '__main__':
    creat_web_dir()