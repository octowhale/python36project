#!/usr/bin/env python
# encoding: utf-8
#

"""
@python ver: Python 3.6
@FILE: 验证HTTPS证书有效性.py
@time: 2017/8/19 9:59
"""

import os
import sys
import requests

"""
在 request 请求中， 打开 verify=True ，即可验证 https 证书是否有效。
例如在 12306 请求过程中，就会报错。
而在 baidu 过程中，就没有问题
"""

fakeheader = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"}
# r1 = requests.get('https://kyfw.12306.cn/otn/', verify=True)
# r2 = requests.get('https://www.zhihu.com/', verify=True, headers=fakeheader)
r3 = requests.get('https://www.baidu.com/', verify=True)

print(r3.text)
