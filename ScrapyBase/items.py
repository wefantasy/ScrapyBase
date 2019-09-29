# coding=UTF-8
'''
@Author: Fantasy
@Date: 2019-06-21 12:51:48
@LastEditors: Fantasy
@LastEditTime: 2019-06-21 13:21:18
@Descripttion: 
@Email: 776474961@qq.com
'''

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapybaseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    def getInsertSql(self):
        '''获取插入数据的sql语句'''
        insertSql = """
            insert into test(a,b,c,d) 
            value(%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE 
            a=VALUES(a),b=VALUES(b)
        """
        params = (self['districtParentCode'],self['districtCode'],self['districtName'],self['districtLevel'])
        return insertSql,params