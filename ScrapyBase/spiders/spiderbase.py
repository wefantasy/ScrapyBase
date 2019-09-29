# coding=UTF-8
'''
@Author: Fantasy
@Date: 2019-06-21 13:03:09
@LastEditors: Fantasy
@LastEditTime: 2019-06-21 13:26:10
@Descripttion: 实例爬虫
@Email: 776474961@qq.com
'''
import scrapy
from PIL import Image
from scrapy import FormRequest, Request
from ScrapyBase.Tool.SpiderUtils import *

class SpiderbaseSpider(scrapy.Spider):
    name = 'spiderbase'
    allowed_domains = ['spiderbase.com']
    start_urls = ['http://spiderbase.com/']
    captcha_url = "http://spiderbase.com/captcha"
    login_url = 'http://spiderbase.com/loginInfo'
    logout_url = "http://spiderbase.com/logout"

    def parse(self, response):
        print(response.body.decode("utf-8","ignore"))

    def start_requests(self):
        yield scrapy.Request(self.login_url, callback=self.login)

    def login(self, response):
        '''
            模拟登录
        '''
        formdata = {}
        formdata["username"] = input("please input username: ")
        formdata["password"] = input("please input password: ")
        loginheaders = {}
        yield scrapy.FormRequest(url=self.captcha_url,
                                 meta={"formdata":formdata}, 
                                 headers=loginheaders, 
                                 callback=self.set_captcha)
    
    def set_captcha(self, response):
        '''
            解析验证码
        '''
        formdata = response.meta.get("formdata", {})
        formdata['CheckCode'] = getImgCheck(response)
        print(formdata)
        yield scrapy.FormRequest(url=self.login_url,
                                 formdata=formdata, 
                                 callback=self.check_login)

    def check_login(self, response):
        '''
            检查登录是否成功
        '''
        if re.findall(r'退出',response.text):
            print("登录成功，开始爬取……")
            for url in self.start_urls:
                yield scrapy.FormRequest(url=url)
            # yield scrapy.FormRequest(url=self.logout_url)
        else:
            print('>>>>>>>>'+response.text)
            print("登陆失败，再次尝试……")
            yield scrapy.Request(self.login_url, callback=self.login, dont_filter=True)