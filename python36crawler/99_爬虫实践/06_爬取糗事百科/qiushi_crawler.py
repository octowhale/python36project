#!/usr/bin/env python
# encoding: utf-8
#

"""
@python ver: Python 3.6
@FILE: qiushi_crawler.py
@time: 2017/8/21 21:09
"""

import os
import sys
import requests
from bs4 import BeautifulSoup
import time
import threading
from random import randint
import queue

s = requests.Session()
q = queue.Queue()


def crawler(url):
    time.sleep(1)
    r = s.get(url)
    r.raise_for_status()
    # print(r.apparent_encoding)
    # r.encoding = r.apparent_encoding
    r.encoding = 'utf-8'
    html = r.text

    # return html

    # nextpage_crawler(html)
    # content_crawler(html)

    # t = threading.Thread(target=nextpage_crawler, args=(html,))
    # t.start()

    # t1 = threading.Thread(target=content_crawler, args=(html,))
    # t1.start()

    tn = threading.Thread(target=get_content, args=(html,))
    tn.start()


def nextpage_crawler(html):
    soup = BeautifulSoup(html, 'lxml')

    ul_tag = soup.find('ul', class_="pagination")
    li_tags = ul_tag.find_all('li')[-1]

    # print(li_tags.find('a')['href'].string.strip())

    uri = li_tags.a['href'].strip()
    next_url = '{}{}'.format('https://www.qiushibaike.com', uri)
    # print(next_url)
    q.put(next_url)
    # print(li_tags.a['href'].strip())


def content_crawler(html):
    soup = BeautifulSoup(html, 'lxml')

    contents = soup.find_all('div', class_='content')

    for content in contents:
        """
        <div class="content">
        <span>
        念大学时候....他也上去踹了两脚，结果，扭到脚了，扭，扭到脚了？
        </span>
        </div>
        """
        # print(content)

        print(content.find('span').text.strip())
        # exit(0)
        # return (0)


def main():
    while True:
        qb_url = q.get(timeout=10)

        print(qb_url)
        # threading.Thread(crawler, args=(qb_url,))

        crawler(qb_url)


def get_content(html):
    # p=threading.Thread(target=)

    nextpage_crawler(html)
    content_crawler(html)
    pass


if __name__ == "__main__":
    url = 'https://www.qiushibaike.com/'
    q.put(url)
    # crawler(url)

    main()
