#!/usr/bin/env python
# encoding: utf-8
#

"""
@python ver: Python 3.6
@FILE: 使用header.py
@time: 2017/8/19 10:08
"""

import os
import sys

import requests
import time

"""
有些网站禁止爬虫登录。比如知乎。

因此，可以自己创建 User-Agent 模拟流浪其登录
"""

fakeheader = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"}

"""使用了 User-Agent"""
r2 = requests.get('https://www.zhihu.com/', verify=True, headers=fakeheader)
print(r2.text)

time.sleep(3)

""" 没使用 User-Agent """
r3 = requests.get('https://www.zhihu.com/', verify=True)
print(r3.text)
