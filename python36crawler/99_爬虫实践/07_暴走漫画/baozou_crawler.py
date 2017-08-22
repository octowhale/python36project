#!/usr/bin/env python
# encoding: utf-8

# python 3.6

import os
import sys
import requests
from bs4 import BeautifulSoup
import queue
import threading

s = requests.Session()
q_img = queue.Queue()

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}


def crawler(url):
    # r = s.get(url, timeout=10, headers=headers)
    r = s.get(url, timeout=10)

    r.raise_for_status()
    r.encoding = r.apparent_encoding

    html = r.text

    # return html

    # print(html)

    open('bz.html', 'w', encoding='utf-8').write(html)
    get_img(html)


def get_img(html):
    # html = open('baozou.html', 'r', encoding='utf-8').read()

    soup = BeautifulSoup(html, 'lxml')

    contents = soup.find_all('div', class_="article-content")
    print(contents)
    for content in contents:
        print("helll")
        title = content.a.text.strip()
        img_url = content.img['data-original-image-url'].strip()

        # download_img(title, img_url)

        # return title, img_url

        q_img.put((title, img_url))

        threading.Thread(target=download_img).start()


def download_img():
    """
    下载图片
    二进制的内容需要使用 content。而不在使用 text
    """

    try:
        title, img_url = q_img.get(timeout=10)
        img_b = s.get(img_url).content

        # print(img_b.content)
        # print(img_b.text)
        #

        postfix = img_url.split('.')[-1]

        filename = os.path.join('download', '{}.{}'.format(title, postfix))
        with open(filename, 'wb') as f:
            f.write(img_b)
    except:
        print("所有图片下载完成")


if __name__ == '__main__':
    # main()
    url = 'http://baozoumanhua.com/qutu'
    crawler(url)
    s.close()
