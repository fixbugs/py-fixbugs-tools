#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
环境需求:python2.7 + php 5.3+
功能：查找leju.com 框架类APP类中的所有文件的翻译对比，输出合并完成的新翻译文件
对应目录结构：

'''

import time
import os
import os.path
import re
import json
import subprocess

TARGET_TRANLATE_DIR = '/root/work/translate-mac/tranfiles/'
NEED_TRANLATE_DIR = '/root/work/lm-front-svn/trunk/app'
DOMAIN = "news.leju.com"


def walk_dir(dir_path):
    result = []
    for parent, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            if re.search('\.svn', filename):
                continue
            result.append(os.path.join(parent, filename))
            pass
        pass
    res = []
    for s in result:
        if re.search('\.svn', s):
            continue
        #elif re.search('helper', s):
        #    continue
        elif re.search('template', s):
            continue
        res.append(s)
    return res


def readFile(file_path):
    result = []
    try:
        f = open(file_path, 'r')
        result = f.readlines()
    finally:
        f.close()
    return result


def getTContent(file_path):
    f_content = readFile(file_path)
    result = []
    if f_content:
        for fc in f_content:
            #need_translate_str = re.findall(r"T\([\'\"](.+?)[\'\"]", fc)
            #只匹配以T('或T("开发，到对应'或"结束的中间字段，不考虑各种特殊写法
            need_translate_str = re.findall(r'T\(?((?=")(["](.+?)["])|([\'](.+?)[\']))[\),]?', fc)
            # T\(?((?=")(["](.+?)["])|(['](.+?)[']))[\),]?
            #replease content between '' and "" start with T(
            #need_translate_str = re.findall(r"T\((\'(.+)?\'|\"(.+)?\")",fc)
            #fix bug with double quote ' used for one T()
            #need_translate_str = re.findall(r"T\((\'([^']+)?\'|\"([^']+)?\")", fc)
            if not need_translate_str:
                continue
            tmp_translate_str = need_translate_str[0][2]
            if not tmp_translate_str:
                tmp_translate_str = need_translate_str[0][-1]
            #print need_translate_str[0]
            result.append(tmp_translate_str)
            #result.append(need_translate_str[0])
            #result.append(need_translate_str[0][1])
            pass
        pass
    result = list(set(result))
    result.sort()
    return result


def saveTConent(t_contents, st_type, app_name, file_name, source_file_name):
    content = createFileOrSave(TARGET_TRANLATE_DIR+app_name+"_"+st_type+"_" + file_name, t_contents, source_file_name, st_type, app_name, file_name)
    writeFile(file_name, content)
    pass


def createFileOrSave(file_name, t_content, source_file_name, st_type='model', ap_name='app', f_name='need'):
    old_tranlast_file_name = getOldTranslateFile(source_file_name)
    if old_tranlast_file_name:
        old_tran_content = analsisTranlateFile(old_tranlast_file_name)
    else:
        old_tran_content = []
    content = "<?php\n/**\n"
    content += " * create on server time " + str(time.strftime('%Y-%m-%d %H:%M:%S')) +"\n"
    content += " * " + str(ap_name) + " " + str(f_name[:-4]) + "的语言包\n"
    content += """ * @category    Pub
 * @package     %(domain)s
 * @copyright   %(domain)s Content System
 * @license     %(domain)s Content System license
 * @author      fuxin@leju.com
 */\n""" % dict(domain=DOMAIN)
    content += "return array(\n"
    #controller
    content += " "*4 + "'controller'=>array(\n"
    if st_type == 'controller':
        for t in t_content:
            if old_tran_content and old_tran_content.has_key('controller') and old_tran_content['controller']:
                if old_tran_content['controller'].has_key(t):
                    content += " "*8 + "'" + str(t) + "' => '" + old_tran_content['controller'][t].encode('utf-8') + "',\n"
                else:
                    content += " "*8 + "'" + str(t) + "' => '" + englishToChinese(t)  + "',\n"
            else:
                content += " "*8 + "'" + str(t) + "' => '" + englishToChinese(t) + "',\n"
            pass
        pass
    content += " "*4 +"),\n"
    #model
    content += " "*4 + "'model'=>array(\n"
    if st_type == 'model':
        for t in t_content:
            if old_tran_content and old_tran_content.has_key('model') and old_tran_content['model']:
                if old_tran_content['model'].has_key(t):
                    content += " "*8 + "'" + str(t) + "' => '" + old_tran_content['model'][t].encode('utf-8') + "',\n"
                else:
                    content += " "*8 + "'" + str(t) +"' => '" + englishToChinese(t) + "',\n"
            else:
                content += " "*8 + "'" + str(t) + "' => '" + englishToChinese(t) + "',\n"
            pass
        pass
    content += " "*4 + "),\n"
    #template
    content += " "*4 + "'template'=>array(\n"
    if st_type == 'template':
        for t in t_content:
            if old_tran_content and old_tran_content.has_key('template') and old_tran_content['template']:
                if old_tran_content['template'].has_key(t):
                    content += " "*8 + "'" + str(t) + "' => '" + old_tran_content['template'][t].encode('utf-8') + "',\n"
                else:
                    content += " "*8 + "'" + str(t) + "' => '',\n"
            else:
                content += " "*8 + "'" + str(t) + "' => '',\n"
            pass
        pass
    content += " "*4 + ")\n"

    content += ");\n"
    return content


def writeFile(file_path, content):
    try:
        f = open(file_path, 'w')
        f.write(str(content))
    finally:
        f.close()

'''
根据文件路径获取翻译文件内容(PHP array)
@param file_path string 翻译文件路径
@return False or Dict 返回翻译数组或者False
'''
def analsisTranlateFile(file_path):
    if not os.path.exists(file_path):
        return False
    p = subprocess.Popen(['php', '-r', 'echo json_encode(include "' + str(file_path) + '");'], stdout=subprocess.PIPE)
    config = p.stdout.read().decode('utf8')
    config = json.loads(config)
    return config

'''
根据文件路径获取文件内容
@param file_path string 文件路径
@return False or Dict 返回文件内容数组或者False
'''
def getFileContent(file_path):
    if not os.path.exists(file_path):
        return False
    result = []
    try:
        f = open(file_path, 'r')
        result = f.readlines()
    finally:
        f.close()
    return result


def getOldTranslateFile(file_path):
    split_names = file_path.split("/")
    if isinstance(split_names, list):
        return ''
    sp_len =  split_names.index("app")
    split_res_pre = split_names[0:sp_len]
    split_res = split_names[sp_len:]
    if split_res[0] == "app":
        result = "/".join(split_res_pre)+"/app/_language/zh-cn/"+split_names[sp_len+1]+"/"+split_names[-1]
    else:
        result = "/".join(split_res_pre)+"/_language/zh-cn/"+split_names[sp_len+1]+"/"+split_names[-1]
    return result


def englishToChinese(content):
    if not content:
        return ''
    from tranlate import Tranlate
    appid = '20160724000025705'
    secretKey = 'sLxLk0lYnHPL1wZ_e5_x'
    tcls = Tranlate(appid, secretKey)
    tcls.setQueryString(str(content))
    tranlate_result = tcls.getResult()
    if not tranlate_result:
        return ''
    return tranlate_result.encode('utf-8')


def main():
    files = walk_dir(NEED_TRANLATE_DIR)
    for f in files:
        if re.search('\_', f):
            continue
        if f.endswith('application.php'):
            continue
        split_names =  f.split("/")
        S_LEN = split_names.index("app")
        if(S_LEN < 0):
            continue
        #need change choose for split_names
        if split_names[S_LEN] == "app":
            split_res = split_names[S_LEN:]
            pass
        if len(split_res) == 3:
            st_type = 'controller'
            pass
        elif len(split_res) == 4:
            st_type = 'model'
            pass
        else:
            continue
        st_name = split_res[1]
        t_contents = getTContent(f)
        if not t_contents:
            continue
        if st_type == 'model':
            saveTConent(t_contents, st_type, st_name, split_res[3], f)
        else:
            saveTConent(t_contents, st_type, st_name, split_res[2], f)


def oneFileMain(source_file_name):
    print source_file_name
    analysis_result = getTContent(source_file_name)
    print analysis_result
    content = createFileOrSave('', analysis_result, source_file_name)
    print content


if __name__ == "__main__":
#    createFileOrSave("test.php","1")
    #main()
    #print time.strftime('%Y-%m-%d %H:%M:%S')
    file_path_3 = 'test.php'
    oneFileMain(file_path_3)
    #print analsisTranlateFile(file_path_1)
