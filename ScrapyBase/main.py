# coding=UTF-8
'''
@Author: Fantasy
@Date: 2019-06-21 12:58:14
@LastEditors: Fantasy
@LastEditTime: 2019-06-21 13:24:10
@Descripttion: 快速启动类
@Email: 776474961@qq.com
'''
from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute("scrapy crawl district".split(" "))
# execute("scrapy crawl district -s JOBDIR=districtRecord".split(" "))