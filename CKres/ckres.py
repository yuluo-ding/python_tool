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
    print file_name

    shutil.rmtree(r'result')
    for list in file_name:
        print type(list)
        os.makedirs('result/' + list)



class Site:
    _web_dir = ""
    _name = ""
    _xx_type = ""
    _input_output = ""

    def __init__(self, web_dir, name, xx_type, input_output):
        self._dir = web_dir
        self._name = name
        self._xx_type = xx_type
        self._input_output = input_output

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


if __name__ == '__main__':
    creat_file_dir()
