# /user/bin/python
# -*- coding:utf-8 -*-
import glob
import os
import shutil

def creat_web_dir():
    path = os.path.abspath("android")
    print path
    list_name = glob.glob('*.xmpf')
    file_name = list_name[0]
    print file_name

    file = open(file_name, 'rt')
    line_file = file.readlines()
    site_name = ""
    for line in line_file:
        if line.find("SiteName") != -1:
            site_name = str(line)[12:len(line) -1].decode(encoding='utf-8')
            # site = site_name.decode(encoding='utf-8')
            if os.path.isdir(site_name):
                pass
            else:
                os.mkdir(site_name)

    cap_name = glob.glob('*.cap')
    print cap_name
    for cap in cap_name:
        shutil.copy(cap, site_name)

    if os.path.isdir(site_name + '/result'):
        pass
    else:
        os.makedirs(site_name + '/result/')

    list_cap = glob.glob('*.cap')
    print list_cap

    shutil.rmtree(site_name + '/result')
    for list in list_cap:
        # print list
        list_name = list[:-4]
        os.makedirs(site_name + '/result/' + list_name)


if __name__ == '__main__':
    creat_web_dir()