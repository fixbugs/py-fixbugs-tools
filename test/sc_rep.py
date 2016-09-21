#!/usr/bin/env python
#coding=utf-8

from db import DB

db = DB(DB_NAME='venus')

tables = db.query("show tables;")
count = 0
for t in tables:
    nowTableName = t[0]
    if nowTableName == 'vs_log':
        continue
    db = DB(DB_NAME='venus')
    getAllSql = "select * from " + nowTableName + ";"
    print getAllSql
    datas = db.queryNew(str(getAllSql) )
    for d in datas:
        needUpdateSql = 'update ' + nowTableName + "where "
        for k, v in d.items():
            if isinstance(v, unicode):
                v = v.encode("utf-8")
                if '江苏' in v:
                    if '江苏省' in v:
                        continue
                    print v, nowTableName
                    count += 1
            #print k, v
print count

