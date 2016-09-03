#/usr/bin/env python
#coding=utf-8

from pypinyin import lazy_pinyin
import os


def getStringPinYin(chineseString):
    chineseString = unicode(chineseString, 'utf-8')
    #print chineseString, lazy_pinyin(chineseString)
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
        #卡戴珊姐妹曝隐私
        #我们俩
        #美人鱼曝纪录片
        if '传' in word:
            if word == '射雕英雄传之东成西就':
                tmpPinYinResult = 'shediaoyingxiongzhuanzhidongchengxijiu'
            elif '正传' in word:
                tmpPinYinResult.replace('zhengchuan', 'zhengzhuan')
            elif '莫扎特传' in word:
                tmpPinYinResult = 'mozhatezhuan'
            print word, tmpPinYinResult
        if '曝' in word:
            #pu 3+
            tmpPinYinResult = tmpPinYinResult.replace('pu', 'bao')
        if '沈' in word:
            tmpPinYinResult = tmpPinYinResult.replace('chen', 'shen')
        if '银行' in word:
            #3+
            tmpPinYinResult = tmpPinYinResult.replace('yinxing', 'yinhang')
        if '重新' in word:
            tmpPinYinResult = tmpPinYinResult.replace('zhongxin', 'chongxin')
        if word == '报告称城镇学校教师职业倦怠比乡村教师更严重':
            tmpPinYinResult = 'baogaochenchengzhenxuexiaojiaoshizhiyejuandaibixiangcunjiaoshigengyanzhong'
        #elif word == '小沈阳退出喜剧人':
        #    print tmpPinYinResult, word
        #    tmpPinYinResult = 'xiaoshenyangtuichuxijuren'
        #elif word == '中国光大银行九江分行盛大开业':
        #    tmpPinYinResult = 'zhongguoguangdayinhangjiujiangfenhangshengdakaiye'
        tmpDict['pinyin'] = tmpPinYinResult
        tranlateResult.append(tmpDict)
        pinyinList.append(tmpPinYinResult)
    print '-'.join(pinyinList)
    return tranlateResult

if __name__ == '__main__':
    main()
    #print getStringPinYin('傻子')
