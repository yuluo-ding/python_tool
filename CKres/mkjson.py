# /user/bin/python
# -*- coding:utf-8 -*-
import glob
import os
import shutil
from collections import Counter


class Site:

    def __init__(self, web_dir, name, xx_type, input_output):
        self.__web_dir = web_dir
        self.__name = name
        self.__xx_type = xx_type
        self.__input_output = input_output

    def set_web_dir(self, web_dir):
        self.__web_dir = web_dir

    def get_web_dir(self):
        return self.__web_dir

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_xx_type(self, xx_type):
        self.__xx_type = xx_type

    def get_xx_type(self):
        return self.__xx_type

    def set_input_output(self, input_output):
        self.__input_output = input_output

    def get_input_output(self):
        return self.__input_output

def type_check(site_type):
    if site_type.find("BBS") != 0:
        return "BBS"
    else:
        return "Unknown Type"


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


def generator(website):
    json_file = website.get_web_dir() + ".json"
    file = open(json_file, "w")
    i_o_content_before = website.get_input_output()
    print  i_o_content_before
    number = len(i_o_content_before)
    # print number

    value_lists = []
    i_o_content = {}

    for i in i_o_content_before:
        n = Counter(i_o_content_before[i]).items()
        # print n
        for k,v in n:
            sm = {}
            sm[k] = v
            value_lists.append(sm)
        # print value_lists
        i_o_content[i] = value_lists
        value_lists = []
    print i_o_content

    content = "{\"" + website.get_name() + "\":\n"
    content += "{\n"
    content += "\"bin\":\n"
    content += "[\"device:/com/roles/front/app/yjhp/yj_hp\",\"snspro:/com/roles/snspro/httpextractor/yj_snp\"],\n"
    content += "\"config\":\n"
    content += "[\"device:/com/cfg/yj_hp_in.conf\",\n"
    content += "\"device:/com/cfg/yj_hp_output.conf\",\n"
    content += "\"snspro:/com/cfg/yj_snp_extract.conf\",\n"
    content += "\"snspro:/com/cfg/yj_snp_output.conf\"],\n"
    content += "\"input_outputs\":"
    if number > 1:
        content += "[\n"
    counter = 0
    http_content = ""
    ttk_terminal_flag_content = ""
    ttk_device_info_content = ""

    for i in i_o_content_before:
        print i
        for c in i_o_content_before[i]:
            print c
            print i_o_content_before[i][c]
            if c.find("TTKTERMINALFLAG") != -1:
                if ttk_terminal_flag_content == "":
                    ttk_terminal_flag_content += "{\"" + c + "\":" + str(i_o_content_before[i][c]) + "}"
                else:
                    ttk_terminal_flag_content += ",{\"" + c + "\":" + str(i_o_content_before[i][c]) + "}"
            elif c.find("TTKDEVICEINFO") != -1:
                if ttk_device_info_content == "":
                    ttk_device_info_content += "{\"" + c + "\":" + str(i_o_content_before[i][c]) + "}"
                else:
                    ttk_device_info_content += ",{\"" + c + "\":" + str(i_o_content_before[i][c]) + "}"
            else:
                if http_content == "":
                    http_content += "{\"" + c + "\":" + str(i_o_content_before[i][c]) + "}"
                else:
                    http_content += ",{\"" + c + "\":" + str(i_o_content_before[i][c]) + "}"


        counter += 1
        if counter == number:
            content += "{\n\"input\":\n[\"" + i + \
                       ".cap\"],\n\"output\":[{\n\"dir\":\"snspro:/ramdisk/front/output/yj_snp\",\n\"files\":[" \
                       + http_content + "]\n}\n"
            if ttk_terminal_flag_content != "":
                content += ",{\n\"dir\":\"snspro:/ramdisk/front/output/or_ttk_flag\",\n\"files\":[" \
                           + ttk_terminal_flag_content + "]\n}\n"
            if ttk_device_info_content != "":
                content += ",{\n\"dir\":\"snspro:/ramdisk/front/output/or_ttk_info\",\n\"files\":[" \
                           + ttk_device_info_content + "]\n}\n"
            content += "]\n}\n"
        else:
            content += "{\n\"input\":\n[\"" + i + \
                       ".cap\"],\n\"output\":[{\n\"dir\":\"snspro:/ramdisk/front/output/yj_snp\",\n\"files\":[" \
                       + http_content + "]\n}\n"
            if ttk_terminal_flag_content != "":
                content += ",{\n\"dir\":\"snspro:/ramdisk/front/output/or_ttk_flag\",\n\"files\":[" \
                           + ttk_terminal_flag_content + "]\n}\n"
            if ttk_device_info_content != "":
                content += ",{\n\"dir\":\"snspro:/ramdisk/front/output/or_ttk_info\",\n\"files\":[" \
                           + ttk_device_info_content + "]\n}\n"
            content += "]\n},\n"

        http_content = ""
        ttk_terminal_flag_content = ""
        ttk_device_info_content = ""

    if number > 1:
        content += "]\n"
    content += "}\n}"

    file.write(content)
    file.close()

    return 0


def find_msg():
    name = ""
    input_output = {}
    input = ""
    file_content = []
    file_content_list = ""
    files = {}
    client_ip = brand = platform = version = action = ''
    result_lists = []
    site_type = ""

    directories = [name for name in os.listdir('./') if os.path.isdir(os.path.join('./' + name))]
    # print directories


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

            for k, v in n.items():
                sm = {}
                sm[k] = v
                result_lists.append(sm)
            # print result_lists

            result_lists = []
            # file_content = []

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
                    elif name_divider == 1:
                        brand += name[name_counter]
                        xx_name = brand
                    elif name_divider == 2:
                        platform += name[name_counter]
                    elif name_divider == 3:
                        version += name[name_counter]
                    else:
                        action += name[name_counter]
                name_counter += 1

            capture_counter += 1

        xx_type = ""
        site_type_counter = 0
        for s in site_type:
            if site_type[site_type_counter] != '_':
                xx_type += site_type[site_type_counter]
            else:
                break
            site_type_counter += 1
        print xx_type
        # print xx_name

        web_dir = './' + directories[counter] + '/'
        website = Site(web_dir, name, xx_type, input_output)
        generator(website)
        input_output.clear()

        counter += 1



if __name__ == '__main__':
    # creat_web_dir()
    find_msg()
