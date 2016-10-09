#!/usr/bin/python
# -*- coding:utf8 -*-

import os

allFileNum = 0
def printPath(level, path):
    global allFileNum
    '''''
        打印一个目录下的所有文件夹和文件
        '''
    # 所有文件夹，第一个字段是次目录的级别
    dirList = []
    # 所有文件
    fileList = []
    # 返回一个列表
    files = os.listdir(path)
    # 添加目录级别
    dirList.append(str(level))
    for f in files:
        if(os.path.isdir(path + '/' + f)):
            if(f[0] == "."):
                pass
            else:
                # 添加非隐藏文件夹
                dirList.append(f)
        if(os.path.isfile(path + '/' + f)):
            fileList.append(f)

    # 当一个标志使用，文件夹列表第一个级别不打印
    i_dl = 0
    for dl in dirList:
        if (i_dl == 0):
            i_dl += 1
        else:
            # 打印至控制台，不是第一个的目录
            print '-' * (int(dirList[0])), dl
            # 打印目录下的所有文件夹和文件，目录级别+1
            printPath((int(dirList[0]) + 1), path + '/' + dl)
    for fl in fileList:
        print '-' * (int(dirList[0])), fl
        allFileNum = allFileNum + 1


if __name__ == '__main__':
    printPath(1, 'D:\python\python_tool')
    print "总文件数 = ", allFileNum