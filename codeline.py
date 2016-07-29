# coding=utf-8
import os
import time
basedir = '/html/NginxServer/py-fixbugs-tools'
filelists = []
# 指定想要统计的文件类型
whitelist = ['php', 'py']
explainSkipList = ['#']


#遍历文件, 递归遍历文件夹中的所有
def getFile(basedir):
        global filelists
        for parent, dirnames, filenames in os.walk(basedir):
            for dirname in dirnames:
                getFile(os.path.join(parent, dirname))
                #递归
            for filename in filenames:
                if os.path.join(parent, filename) in filelists:
                    continue
                ext = filename.split('.')[-1]
                #只统计指定的文件类型，略过一些log和cache文件
                if ext in whitelist:
                    filelists.append(os.path.join(parent, filename))


#统计一个文件的行数
def countLine(fname):
    count = 0
    with_out_explains = 0
    for file_line in open(fname).xreadlines():
        if file_line != '' and file_line != '\n':
            #过滤掉空行
            count += 1
            file_line = file_line.lstrip()
            if file_line[0] in explainSkipList:
                continue
            with_out_explains += 1
    print fname + '----', count
    print with_out_explains
    result = dict()
    result['count'] = count
    result['with_out_explains'] = with_out_explains
    return result


def main():
    global filelists
    startTime = time.clock()
    getFile(basedir)
    totalline = 0
    total_line_without_explains = 0
    for filelist in filelists:
        count_res = countLine(filelist)
        totalline = totalline + count_res['count']
        total_line_without_explains = total_line_without_explains + count_res['with_out_explains']
        print 'total lines:', totalline
        print 'total lines with out explains', total_line_without_explains
        print 'Done! Cost Time: %0.2f second' % (time.clock() - startTime)

if __name__ == '__main__':
    main()
