#!/usr/bin/env python
#coding=utf8

import os


def split_file(fpath, out_dir, base_num=1000):
    line_lists = [[]] * 1001
    with open(fpath) as file_hd:
        line = file_hd.readline()
        count = 0
        while line:
            tmp_num = int(line)
            line_lists[tmp_num % base_num].append(line)
            if count % 100000 == 0:
                for i in xrange(len(line_lists)):
                    appendToFile(out_dir, str(i)+'sp.txt', ''.join(line_lists[i]))
                print 'now count:',count
            line = file_hd.readline()
    return True


def appendToFile(out_dir, file_name, content):
    f_path = out_dir+'/' + str(file_name)
    fl = open(f_path, 'a')
    fl.write(content)
    fl.close()

if __name__ == '__main__':
    print split_file('visitor2.txt','/html/NginxServer/py-fixbugs-tools/test/vistor/spresult')
