#!/usr/bin/env python
#coding=utf-8

import MySQLdb

class DB():
    def __init__(self, DB_HOST='localhost', DB_USER='root', DB_PWD='123456', DB_NAME='data_tizi'):
        self.DB_HOST = DB_HOST
        self.DB_USER = DB_USER
        self.DB_PWD = DB_PWD
        self.DB_NAME = DB_NAME

        self.conn = self.getConnection()

    def getConnection(self):
        return MySQLdb.Connect(
            host = self.DB_HOST,
            user = self.DB_USER,
            passwd = self.DB_PWD,
            db = self.DB_NAME,
            charset ='utf8'
        )

    def query(self, sqlString):
        cursor=self.conn.cursor()
        cursor.execute(sqlString)
        returnData=cursor.fetchall()
        cursor.close()
        self.conn.close()
        return returnData

    def update(self, sqlString):
        cursor=self.conn.cursor()
        cursor.execute(sqlString)
        self.conn.commit()
        cursor.close()
        self.conn.close()

    def insert_many(self, sqlString, datalist):
        cursor=self.conn.cursor()
        cursor.executemany(sqlString, datalist)
        self.conn.commit()
        cursor.close()
        self.conn.close()

    def insert(self,sqlString):
        cursor = self.conn.cursor()
        cursor.execute(sqlString)
        returnData = cursor.lastrowid
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return returnData
