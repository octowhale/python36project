#!/usr/bin/env python
# encoding: utf-8
#

"""
@python ver: Python 3.6
@FILE: sspancel_crawler.py
@time: 2017/8/19 8:22
@os: 
"""



import requests
import json
from random import randint

fakeheader = [
    'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36']

lenfhd = len(fakeheader)

headers = {'User-Agent': fakeheader[lenfhd - 1]}

setting = json.load(open('user.json', 'r'))

userinfo = {
    "email": setting['email'],
    "passwd": setting['passwd'],
    "code": "",
    "remember_me": "week",
    "headers": headers
}

site_url = setting['site_url']


def login(url):
    """
    模拟登录，返回登录 cookie
    :param url:
    :return:
    """

    r = requests.post(url, data=userinfo)

    # print(r.cookies)

    login_cookie = r.cookies
    return login_cookie


def get_html(url):
    cookies = login(login_url)
    # r = requests.get(url, fakeheader[0], cookies=cookies)

    print(headers)

    """使用 cookie 登录"""
    r = requests.post(url, cookies=cookies)

    """返回网页访问状态，如果有错则报错退出，如果无错继续执行"""
    r.raise_for_status()

    """
    r.encoding : 系统字符集
    r.apparent_encoding : 网站字符集
    
    调试的时候可以先打印 r.apparent_encoding 的值，并为 r.encoding 直接赋值。
    """
    # print(r.encoding, r.apparent_encoding)
    # r.encoding = r.apparent_encoding    #utf-8
    r.encoding = 'utf-8'
    return r.text


if __name__ == "__main__":

    login_url = '{}/auth/login'.format(site_url)
    user_url = '{}/user'.format(site_url)
    checkin_url = '{}/user/checkin'.format(site_url)

    result = json.loads(get_html(checkin_url))
    for k in result:
        print(result[k])
