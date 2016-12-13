#!/usr/bin/env python
#coding=utf8

kb_mp = dict()

kb_mp['1'] = [' ','.','!']  #空格
kb_mp['2'] = ['q','b','x']
kb_mp['3'] = ['z','u','v']
kb_mp['4'] = ['g','h','j']
kb_mp['5'] = ['m','p','l']
kb_mp['6'] = ['f','c','y','t']
kb_mp['7'] = ['k','n','r']
kb_mp['8'] = ['a','e','w']
kb_mp['9'] = ['i','d','o','s']


unSecStr = "648159969691164817828591164816793258587879116481793791584919716481923878149589116481978918491988164974919966878765611648618781796169791961735891187916486148381791789586616971648196863912391169316871239681648511999847881896416485114597966197139596616485118293616481975616497416931687179619919919479781648511286839816486164874816497491164861539416481435871786816978879118791849581995815861988164851891648167836197891188198814879391128683981648158955818491878167836187934416916497716486168716487481648189759187816481978918491991"

wordsPath = '/usr/share/dict/words'

def getFileContent(file_path):
    import os
    if not os.path.exists(file_path):
        return False
    result = []
    try:
        f = open(file_path, 'r')
        for l in f.readlines():
            l = l.strip("\r\n")
            result.append(l)
    finally:
        f.close()
    return result

allWords = getFileContent(wordsPath)
import itertools
hasResultKey = dict()

def findWord(numStr):
    if numStr in hasResultKey:
        return hasResultKey[numStr]
    res = list()
    for i in range(len(numStr)):
        res.append(kb_mp[numStr[i]])
    res = str(res)
    result = list()
    for iw in itertools.product(*eval(res)):
        tword = ''.join(iw)
        if tword in allWords:
            result.append(tword)
    hasResultKey[numStr] = result
    print numStr
    print result
    print "=============="
    return result

unSecArr = unSecStr.split(str('11'))
lastWord = list()
for us in unSecArr:
    wordArr = us.split(str('1'))
    for w in wordArr:
        lastWord.append(findWord(w))

print lastWord
