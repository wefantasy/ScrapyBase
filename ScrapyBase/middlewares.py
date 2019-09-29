# coding=UTF-8
'''
@Author: Fantasy
@Date: 2019-06-21 12:51:48
@LastEditors: Fantasy
@LastEditTime: 2019-06-21 13:23:53
@Descripttion: 
@Email: 776474961@qq.com
'''

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import re
import random
from scrapy import signals
from scrapy.conf import settings
from ScrapyBase.Tool.ProxyTool import *

class UserAgentDownloaderMiddleware(object):
    '''
        ??User-agent
    '''
    def process_request(self, request, spider):
        agent = random.choice(settings.get("USER_AGENT"))
        request.headers["User-Agent"] = agent


class ProxyDownloaderMiddleware(object):
    '''
       ???? 
    '''
    def process_request(self, request, spider):
        # request.meta["dont_redirect"] = True
        stats = spider.crawler.stats.get_stats()
        err_count = stats.get("err_count",False)
        if not err_count:
            stats["err_count"] = 1
        if err_count != 0:
            request.meta['proxy'] = "http://"+get_proxy()
            print("use proxy is: "+request.meta['proxy'])
        else:
            stats["err_count"] = err_count + 1
            request.meta.pop('proxy')
            print("use proxy is: localhost")

    def process_exception(self, request, exception, spider):
        proxy = request.meta.get('proxy',"NULL")
        print("error proxy is: "+proxy)
        stats = spider.crawler.stats.get_stats()
        err_count = stats.get("err_count",1)
        print("err_count= ",err_count)
        stats["err_count"] = (err_count + 1) % 5
        return request

class ScrapybaseSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ScrapybaseDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
