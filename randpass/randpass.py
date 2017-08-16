#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python2.7
@python_version: python3.6
@file: randpass.py
@time: 2017/8/16 10:56
"""

import os
import sys
import random


def randpass(length=10, alpha_lower=True, alpha_upper=True, digit=True, symbal=False):
    alpha_lower_pool = 'abcdefghijklmnopqrstuvwxyz'
    alpha_upper_pool = alpha_lower_pool.upper()
    digit_pool = '0123456789'
    symbal_pool = '!#$%^&*()'

    pool = ''

    if alpha_lower is True:
        pool += alpha_lower_pool
    if alpha_upper is True:
        pool += alpha_upper_pool
    if digit is True:
        pool += digit_pool
    if symbal is True:
        pool += symbal_pool

    rel = ''
    for i in range(length):
        rel += random.choice(pool)
    print(rel)


    """
    生成器表达式
    在开始介绍生成器表达式之前，先看看我们比较熟悉的列表解析( List comprehensions)，列表解析一般都是下面的形式。
    [expr for iter_var in iterable if cond_expr]

    ex: [i for i in range(50) if i%2]
    """

    print(''.join([random.choice(pool) for x in range(length)]))


if __name__ == '__main__':
    randpass(length=20, symbal=True)
