# /user/bin/python
# -*- coding:utf-8 -*-
import glob
import os
import shutil
from collections import Counter


class Site:
    __site_name = ""

    def __init__(self, site_name):
        self.__site_name = site_name

    def set_name(self, site_name):
        self.set_name = site_name

    def get_name(self, site_name):
        return self.__site_name


def creat_web_dir():
    path = os.path.abspath("android")
    print path
    list_name = glob.glob('*.xmpf')
    file_name = list_name[0]
    print file_name

    file = open(file_name, 'rt')
    line_file = file.readlines()

    for line in line_file:
        if line.find("SiteName") != -1:
            site_name = str(line)[12:len(line) - 1].decode(encoding='utf-8')
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


def find_msg():
    name = ""
    input_output = {}
    input = ""
    file_content = []
    file_content_list = ""
    files = {}
    site_type = ""
    client_ip = brand = platform = version = action = ''

    directories = [name for name in os.listdir('./') if os.path.isdir(os.path.join('./' + name))]
    print directories

    counter = 0
    for d in directories:
        tmp = unicode(directories[counter], 'gb2312')
        subdirectory = './' + tmp + '/result/'
        print subdirectory

        capture_name = [name for name in os.listdir(subdirectory) if os.path.isdir(os.path.join(subdirectory, name))]
        capture_counter = 0
        for c in capture_name:
            name = capture_name[capture_counter]
            input = name
            sheet_directory = './' + tmp + '/result/' + name + '/'
            sheet_names = [name for name in os.listdir(sheet_directory) if os.path.isfile(os.path.join(sheet_directory, name))]
            # print sheet_names

            sheet_counter = 0
            for s in sheet_names:
                sheet_file_dir = sheet_directory + sheet_names[sheet_counter]
                sheet_file = open(sheet_file_dir, 'rt')
                sheet_content = sheet_file.readlines()
                line_counter = 0
                for line in sheet_content:
                    if line.find("Protocol") != -1:
                        protocol = str(line)[0:len(str(line))-1]
                        # print line
                    elif line.find("Domain") != -1:
                        domain = str(line)[0:len(str(line))-1]
                    elif line.find("XX-Type") != -1:
                        action_type = str(line)[0:len(str(line))-1]
                        site_type = action_type[8:]
                    line_counter += 1
                file_content_list = protocol + " " + domain + " " + action_type
                file_content.append(file_content_list)
                sheet_counter += 1

            n = Counter(file_content)
            lists=[]
            for k, v in n.items():
                sm = {}
                sm[k] = v
                lists.append(sm)
            print lists

                # print Counter(file_content)
            for i in file_content:
                if file_content.count(i) > 0:
                    files[i] = file_content.count(i)
                    # print files[i]
            input_output[input] = files
            file_content = []
            files = {}

            name_counter = 0
            name_divider = 0
            for b in name:
                if name[name_counter] == '_':
                    name_divider += 1
                if name[name_counter] != '_':
                    if name_divider == 0:
                        client_ip += name[name_counter]
                        # print client_ip
                    elif name_divider == 1:
                        brand += name[name_counter]
                        xx_name = brand
                    elif name_divider == 2:
                        platform += name[name_counter]
                        print platform
                    elif name_divider == 3:
                        version += name[name_counter]
                    else:
                        action += name[name_counter]
                name_counter += 1

            # print("\n\tIP:\t" + client_ip)
            # print("\tType:\t" + brand)
            # print("\tPlatform:\t" + platform)
            # print("\tVersion:\t" + version)
            # print("\tAction:\t" + action)
            client_ip = brand = platform = version = action = ''
            capture_counter += 1

        xx_type = ""
        site_type_counter = 0
        for s in site_type:
            if site_type[site_type_counter] != '_':
                xx_type += site_type[site_type_counter]
            else:
                break
            site_type_counter += 1

        web_dir = './' + tmp + '/'
        counter += 1


if __name__ == '__main__':
    # creat_web_dir()
    find_msg()
