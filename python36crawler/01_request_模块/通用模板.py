#!/usr/bin/env python
# encoding: utf-8

"""
@python_version: python3.6
@file: 通用模板.py
@time: 2017/8/18 9:13
"""

import os
import sys

import requests


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        # 如果状态码不是200 则应发HTTPError异常
        r.raise_for_status()
        # 设置正确的编码方式
        r.encoding = r.apparent_encoding
        return r.text

    except:
        return "Something Wrong!"
