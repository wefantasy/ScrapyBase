# coding=UTF-8
'''
@Author: Fantasy
@Date: 2019-06-21 12:59:07
@LastEditors: Fantasy
@LastEditTime: 2019-06-21 13:24:28
@Descripttion: 获取代理相关
@Email: 776474961@qq.com
'''
import time
import random
import requests


def get_proxy():
    proxy = requests.get("http://ip/get/").content.decode()
    # return random.choices(proxys)[0]
    return proxy


print(get_proxy())


def delete_proxy(proxy):
    requests.get("http://ip/delete/?proxy={}".format(proxy))

# your spider code


def getHtml():
    # ....
    retry_count = 5
    proxy = get_proxy()
    while retry_count > 0:
        try:
            html = requests.get('https://www.example.com',
                                proxies={"http": "http://{}".format(proxy)})
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1
    # 出错5次, 删除代理池中代理
    delete_proxy(proxy)
    return None
