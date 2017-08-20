#!/usr/bin/env python
# encoding: utf-8
#

"""
@python ver: Python 3.6
@FILE: zimuvu_crawler.py
@time: 2017/8/19 16:00
"""

import os
import sys
import requests
import json

fakeheader = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
    # 'X-Forwarded-For': '8.8.8.8',  # 伪装IP地址
    'Accept': 'image/webp,image/*,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, sdch',  # 使用后压缩结果
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Content-Type': 'application/html',
}


def login(url):
    """
    登录
    :param url:
    :return: s
    """
    s = requests.Session()

    # login_url = '${}/user/login'.format(url)
    """
    字母组的登录页面并不是真正的登录页面。如果使用 /user/login 去尝试登录，会一直提示页面不存在
    这种情况下，可以使用 fiddle 抓取浏览器登录的链接。获取真相的登录 url = /User/Login/ajaxLogin
    """
    login_url = '{}/User/Login/ajaxLogin'.format(url)
    # login_url = 'http://www.zimuzu.tv/user/sign'
    userinfo = json.load(open('user.json'))
    # print(userinfo)

    r = s.post(login_url, data=userinfo, headers=headers)
    # r = s.post(login_url, data=userinfo)

    # print(r.headers)
    # r = s.get(login_url, timeout=3, headers=headers)
    r.raise_for_status()

    result = json.loads(r.text)
    # for k in result:
    #     print(k, result[k])

    return s


def get_today(s):
    # s = login(url)
    today_url = '{}/today'.format(url)

    r = s.get(today_url)
    r.raise_for_status()

    r.encoding = r.apparent_encoding

    print(r.text)


if __name__ == "__main__":
    url = 'http://www.zimuzu.tv'
    s = login(url)

    get_today(s)
