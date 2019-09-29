# coding=UTF-8
'''
@Author: Fantasy
@Date: 2019-06-21 13:05:15
@LastEditors: Fantasy
@LastEditTime: 2019-06-21 13:25:05
@Descripttion: 爬虫解析相关
@Email: 776474961@qq.com
'''
import re
import os
import random
import requests
import pytesseract
from PIL import Image
from io import BytesIO
from lxml import etree
from PIL import ImageEnhance

def getImgCheck(response):
    img = Image.open(BytesIO(response.body)).convert("L")
    img=ImageEnhance.Contrast(img)
    img=img.enhance(3)
    imgstr = pytesseract.image_to_string(img)
    img.show()
    imgstr = imgstr.replace(" ","")
    imgstr = imgstr.replace(".","")
    return imgstr

def cookieToDict(cookie):
    itemDict = {}
    items = cookie.split(';')
    for item in items:
        key = item.split('=')[0].replace(' ', '')
        value = item.split('=')[1]
        itemDict[key] = value
    return itemDict


class AspUtil(object):

    @staticmethod
    def extract(htmlstr):
        data = {}
        html = etree.HTML(htmlstr)
        if html.xpath("//input[@id='__VIEWSTATE']/@value"):
            data['__VIEWSTATE'] = html.xpath(
                "//input[@id='__VIEWSTATE']/@value")[0]
        if html.xpath("//input[@id='__VIEWSTATEGENERATOR']/@value"):
            data['__VIEWSTATEGENERATOR'] = html.xpath(
                "//input[@id='__VIEWSTATEGENERATOR']/@value")[0]
        if html.xpath("//input[@id='__VIEWSTATEENCRYPTED']/@value"):
            data['__VIEWSTATEENCRYPTED'] = html.xpath(
                "//input[@id='__VIEWSTATEENCRYPTED']/@value")[0]
        if html.xpath("//input[@id='__EVENTVALIDATION']/@value"):
            data['__EVENTVALIDATION'] = html.xpath(
                "//input[@id='__EVENTVALIDATION']/@value")[0]
        if html.xpath("//input[@id='Is_IsSubmit']/@value"):
            data['Is_IsSubmit'] = html.xpath(
                "//input[@id='Is_IsSubmit']/@value")[0]
        if html.xpath("//input[@id='Is_IsCheck']/@value"):
            data['Is_IsCheck'] = html.xpath(
                "//input[@id='Is_IsCheck']/@value")[0]
        if html.xpath("//input[@id='Is_IsStop']/@value"):
            data['Is_IsStop'] = html.xpath(
                "//input[@id='Is_IsStop']/@value")[0]
        return data
