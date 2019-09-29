# coding=UTF-8
'''
@Author: Fantasy
@Date: 2019-06-21 12:59:07
@LastEditors: Fantasy
@LastEditTime: 2019-06-21 13:24:21
@Descripttion: 数据库相关工具
@Email: 776474961@qq.com
'''

import pymysql


class MySqlTool(object):

    def __init__(self, host="localhost", username="root", password="root", dbname=""):
        self.db = pymysql.connect(host, username, password, dbname)
        self.cursor = self.db.cursor()

    def insertData(self, insertSql, params):
        try:
            self.cursor.execute(insertSql, params)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            raise Exception

    def deleteData(self, deleteSql, params):
        try:
            self.cursor.execute(deleteSql, params)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            raise Exception

    def updateData(self, updateSql, params):
        try:
            self.cursor.execute(updateSql, params)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            raise Exception

    def selectDate(self, selectSql, params):
        try:
            self.cursor.execute(selectSql, params)
            results = self.cursor.fetchall()
            self.db.commit()
            return results
        except Exception:
            self.db.rollback()
            raise Exception