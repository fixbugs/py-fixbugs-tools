#/usr/bin/env python
#coding=utf-8

from pypinyin import lazy_pinyin
import os


def getStringPinYin(chineseString):
    chineseString = unicode(chineseString, 'utf-8')
    print chineseString, lazy_pinyin(chineseString)
    pinYinString = ''.join(lazy_pinyin(chineseString))
    return pinYinString


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


def repleaceEndString(fileContent):
    result = list()
    for f in fileContent:
        result.append(f[0:-2])
    return result


def main():
    wordStringArray = repleaceEndString(getFileContent('pinyin.txt'))
    tranlateResult = list()
    pinyinList = list()
    for word in wordStringArray:
        tmpDict = dict()
        tmpDict['word'] = word
        tmpPinYinResult = getStringPinYin(word)
        if word == '银行发行股票':
            tmpPinYinResult = 'yinhangfaxinggupiao'
        elif word == '巴西汽车市场衰退通用或将重新考虑新投资':
            tmpPinYinResult = 'baxiqicheshichangshuaituitongyonghuojiangchongxinkaolvxintouzi'
        elif word == '大虾被称分离器':
            tmpPinYinResult = 'daxiabeichenfenliqi'
        elif word == '小沈阳退出喜剧人':
            tmpPinYinResult = 'xiaoshenyangtuichuxijuren'
        tmpDict['pinyin'] = tmpPinYinResult
        tranlateResult.append(tmpDict)
        pinyinList.append(tmpPinYinResult)
    #print '-'.join(pinyinList)
    return tranlateResult

if __name__ == '__main__':
    main()
    #print getStringPinYin('傻子')
