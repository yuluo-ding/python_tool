# /user/bin/python
# -*- coding:utf-8 -*-

import os
import glob
import shutil


def creat_file_dir():
    if os.path.isdir('result'):
        pass
    else:
        os.mkdir('result/')

    file_name = glob.glob('*.cap')
    # print file_name

    shutil.rmtree(r'result')
    for list in file_name:
        # print list
        list_name = list[:-4]
        os.makedirs('result/' + list_name)


def count_file():
    file_name = [name for name in os.listdir('result/') if os.path.isdir(os.path.join('result/', name))]
    print file_name
    print type(file_name)


class Site:
    __web_dir = ""
    __name = ""
    __xx_type = ""
    __input_output = ""

    def __init__(self, web_dir, name, xx_type, input_output):
        self.__dir = web_dir
        self.__name = name
        self.__xx_type = xx_type
        self.__input_output = input_output

    def set_web_dir(self, web_dir):
        self._web_dir = web_dir

    def get_web_dir(self):
        return self._web_dir

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_xx_type(self, xx_type):
        self._xx_type = xx_type

    def get_xx_type(self):
        return self._xx_type

    def set_input_output(self, input_output):
        self._input_output = input_output

    def get_input_output(self):
        return self._input_output


def generator():
    json_file = Site.get_web_dir() + Site.get_name() + ".json"
    file = open(json_file, "w")
    content = Site.get_input_output()
    number = len(content)
    print "Num: " + number

    con = "{\"" + Site.get_name() + "\":\n"
    con += "{\n"
    con += "\"bin\":\n"
    con += "[\"device:/com/roles/front/app/yjhp/yj_hp\",\"snspro:/com/roles/snspro/httpextractor/yj_snp\"],\n"
    con += "[\"config\":\n"
    con += "[\"device:/com/cfg/yj_hp_in.conf\",\n"
    con += "\"device:/com/cfg/yj_hp_output.conf\",\n"
    con += "\"device:/com/cfg/yj_snp_extract.conf\",\n"
    con += "\"device:/com/cfg/yj_snp_output.conf\",\n"
    con += "\"input_outputs\":"
    if number != None:
        con += "[\n"
    counter = 0
    http_content = ""
    ttk_flag = ""
    ttk_info = ""
    for i in content:
        for c in content[i]:
            print c

def check_typ(site_type):
    if site_type.find("HTTPSHOP") != 0:
        return "HTTPSHOP"
    else:
        return "Unknow"

def main():
    name = ""
    input_output = {}
    input = ""
    file_content = []
    file_content_list = ""
    files = {}
    site_type = ""
    client_ip = brand = platform = version = action = ''

    directories = [name for name in os.listdir('result/') if os.path.isdir(os.path.join('result/', name))]
    capture_names = []
    counter = 0
    # 列出
    for d in directories:
        sub = 'result/' + directories[counter] + '/'
        # result目录下每个文件夹的名字
        file_name_list = directories[counter]
        # 打印出result目录下每个目录的名称
        print sub
        capture_names = [name for name in os.listdir(sub) if os.path.isdir(os.path.join(sub))]
        # 打印出每个目录下的文件名称的列表
        # print capture_names

        capture_count = 0
        for c in capture_names:
            sheet_file_dir = sub + capture_names[capture_count]
            print sheet_file_dir
            sheet_file = open(sheet_file_dir, "rt")

            sheet_content = sheet_file.readlines()
            line_counter = 0
            for line in sheet_content:
                if line.find("Protocol") != -1:
                    protocol = str(line)[0:len(str(line))-1]
                    print line
                elif line.find("Domain") != -1:
                    domain = str(line)[0:len(str(line))-1]
                elif line.find("XX-Type") != -1:
                    action_type = str(line)[0:len(str(line))-1]
                    site_type = action_type[8:]
                line_counter += 1

            file_content_list = protocol + " " + domain + " " + action_type
            file_content.append(file_content_list)

            capture_count += 1

        for i in file_content:
            if file_content.count(i) > 0:
                files[i] = file_content.count(i)
        input_output[input] = files
        file_content = []
        files = {}


        name_counter = 0
        name_divider = 0
        for b in file_name_list:
            if file_name_list[name_counter] == '_':
                name_divider += 1
            if file_name_list[name_counter] != '_':
                if name_divider == 0:
                    client_ip += file_name_list[name_counter]
                elif name_divider == 1:
                    brand += file_name_list[name_counter]
                    xx_name = brand
                elif name_divider == 2:
                    platform += file_name_list[name_counter]
                elif name_divider == 3:
                    version += file_name_list[name_counter]
                else:
                    action += file_name_list[name_counter]
            name_counter += 1

            # platform & version to be read in
        print("\n\tIP:\t" + client_ip)
        print("\tBrand:\t" + brand)
        print("\tType:\t" + brand)
        print("\tPlatform:\t" + platform)
        print("\tVersion:\t" + version)
        print("\tAction:\t" + action)

        client_ip = brand = platform = version = action = ''
        capture_count += 1

    xx_type = ""
    site_type_counter = 0
    for s in site_type:
        if site_type[site_type_counter] != '_':
            xx_type += site_type[site_type_counter]
        else:
            break
        site_type_counter += 1

    web_dir = './'
    website = Site(web_dir, xx_name, xx_type, input_output)
    generator(website)
    input_output.clear()

    counter += 1

if __name__ == '__main__':
    # creat_file_dir()
    main()