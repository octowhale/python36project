#!/usr/bin/env python
# encoding: utf-8

"""
@python_version: python3.6
@file: 01_html解析ailice.py
@time: 2017/8/18 9:14
"""

import os
import sys
from bs4 import BeautifulSoup

#
# with open('alice.html', 'r') as fobj:
#     html = fobj.read()

html = open('alice2.html', 'r').read()
# print(html)


soup = BeautifulSoup(html, 'html.parser')

# 格式化整个html
# print(soup.prettify())


####
# 可以简单的说，每个标签都是 soup 的子节点。通过 . 引用。
# 可以简单的作为字典操作
####

print(type(soup))  # <class 'bs4.BeautifulSoup'>

# # 找到文档的 title
# print(soup.title)
# # titile 的 name 值
# print(soup.title.name)
# # title 中的字符串 string
# print(soup.title.string)
#
# # title 的父节点
# print(soup.title.parent)
# # title 的父节点 name 属性
# print(soup.title.parent.name)
#
# print(soup.head)
#
# print('\n# 文档的第一个段落\n')#
# print(soup.p)
# print(soup.find('p'))  # 第一个 p 标签
# print(soup.find_all('p'))  # 所有 p 标签
#
# # p 的 calss 属性值
# print(soup.p['class'])
# print(soup.p.string)
# print(soup.p.b)
#
# # 找到 a 标签
# print(soup.a)
#
# # 找到所有 a 标签
# print(soup.find_all('a'))   # 返回一个 list
#
# # 找到第一个 id 值等于 2 的 a 标签
# print(soup.find(id='link2'))  # 第一个
# print(soup.find_all(id='link2'))  # 所有
#
#


#####
# 高级用法
#####

# 找到所有 <a> 标签的链接

for link in soup.find_all('a'):
    print(link.get('href'))
    print(link['href'])

# 从文档中获取所有文字内容
print(soup.get_text())      # 所有内容，一条字符串
print(type(soup.get_text()))    # <class 'str'>

