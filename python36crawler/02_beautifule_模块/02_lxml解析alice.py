#!/usr/bin/env python
# encoding: utf-8

import bs4

# 使用 lxml 解析

"""
from_encoding='编码格式' 可以手动设置来源编码
"""

# soup = bs4.BeautifulSoup(open('alice.html', 'r').read(), 'lxml')
# soup = bs4.BeautifulSoup(open('alice_big5.html'), 'lxml')    # 可以直接传入 fileobj 代替字符串
soup = bs4.BeautifulSoup(open('alice.html'), 'lxml', from_encoding='utf-8')  # 手动设置来源编码

# print(soup.title)



"""
子节点：tag的.contents属性可以将tag的子节点以列表的方式输出
"""
# head_tag = soup.head
# print(head_tag.contents)
# title_tag = head_tag.contents[0]
# print(title_tag.contents)

""" 子节点
tag 的 .children 生成器，可以对tag 的子节点进行循环
"""
# for child in title_tag.children:
#     print(child)

""" 子节点和孙节点
子孙节点： tag 的 .descendants 属性可以将 tag 的子孙记得点一列表方式输出
"""
# for child in head_tag.descendants:
#     print(child)


""" 找到 tag 下的所有文本内容
1. 如果该 tag 只有一个子节点（ NavigableString 类型 ）： 直接使用 `tag.string` 就能找到。
2. 如果 tag 有很多个子、孙节点，并且每个节点里都有 sting，我肯可以使用迭代的方式将其全部找出
"""

for string in soup.strings:
    print(repr(string))


""" Beautiful Soup 4.2.0 中文文档
https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
"""