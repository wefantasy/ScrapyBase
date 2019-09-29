# coding=UTF-8
'''
@Author: Fantasy
@Date: 2019-06-21 12:51:48
@LastEditors: Fantasy
@LastEditTime: 2019-06-21 13:22:48
@Descripttion: 
@Email: 776474961@qq.com
'''
import pymysql
from twisted.enterprise import adbapi
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapybasePipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls,settings):
        '''
        @Descripttion: 读取配置，初始化数据库池

        @Param: 

        @Return: 
        '''
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWD"],
            charset="utf8",
            use_unicode=True
        )
        dbpool = adbapi.ConnectionPool("pymysql", **dbparms)
        return cls(dbpool)
    
    def process_item(self,item,spider):
        # query = self.dbpool.runInteraction(self.insert, item)
        # query.addErrback(self.handle_error, item, spider) #处理异常
        # print(item)
        pass

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        print (failure)
    
    def insert(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        insert_sql, params = item.getInsertSql()
        print (insert_sql, params)
        cursor.execute(insert_sql, params)
