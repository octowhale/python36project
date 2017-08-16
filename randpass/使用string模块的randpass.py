#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python2.7
@python_version: python3.6
@file: 使用string模块的randpass.py
@time: 2017/8/16 11:43
"""

import os
import sys
import string
import random

# print(string.ascii_letters)  # 所有字母
# print(string.ascii_lowercase)  # 小写字母
# print(string.ascii_uppercase)  # 大写字母
# print(string.digits)  # 数字
# print(string.hexdigits)  # 16进制符号（大写）
# print(string.octdigits)  # 8进制符号
# print("whitespace: ", string.whitespace)  # 空白字符，含换行符
# print("punctuation: ", string.punctuation)  # 符号
#
# print("printable: ", string.printable, " : end")  # 上面的所有的并集


def randpass(size=20, chars="", upper=False, lower=False, digit=False, punc=False):
    if upper is True:
        chars += string.ascii_uppercase

    if lower is True:
        chars += string.ascii_lowercase

    if digit is True:
        chars += string.digits

    if punc is True:
        chars += string.punctuation

    return ''.join([random.choice(chars) for _ in range(size)])


if __name__ == '__main__':

    print("x"*20)
    print(randpass(chars='iloveyou'))
