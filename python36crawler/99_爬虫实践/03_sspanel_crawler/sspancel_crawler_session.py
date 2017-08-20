#!/usr/bin/env python
# encoding: utf-8
#

"""
@python ver: Python 3.6
@FILE: sspancel_crawler_session.py
@time: 2017/8/19 9:35
@os: win10
"""

import os
import sys

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
    "remember_me": "week"
}

site_url = setting['site_url']


def login(url):
    """创建一个会话实例，将所有访问都模拟成为一次访问"""
    s = requests.Session()
    # s.get(login_url)

    """登录"""
    s.post(url, data=userinfo)

    # print(s.cookies)  # 此次会话的 cookie

    return s


def checkin(s, url):
    """使用会话实例进行第二次交互： 签到"""
    r = s.post(url)

    return r.text


if __name__ == "__main__":

    login_url = '{}/auth/login'.format(site_url)
    user_url = '{}/user'.format(site_url)
    checkin_url = '{}/user/checkin'.format(site_url)

    s = login(login_url)
    result = json.loads(checkin(s, checkin_url))

    for k in result:
        print(result[k])
