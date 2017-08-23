#!/usr/bin/env python
# encoding: utf-8
#

"""
@python ver: Python 3.6
@FILE: zimuvu_crawler.py
@time: 2017/8/19 16:00
"""

import os
import sys
import requests
import json
from bs4 import BeautifulSoup

fakeheader = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
    # 'X-Forwarded-For': '8.8.8.8',  # 伪装IP地址
    'Accept': 'image/webp,image/*,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, sdch',  # 使用后压缩结果
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Content-Type': 'application/html',
}

s = requests.Session()


def login(url):
    """
    登录
    :param url:
    :return: s
    """

    # login_url = '${}/user/login'.format(url)
    """
    字母组的登录页面并不是真正的登录页面。如果使用 /user/login 去尝试登录，会一直提示页面不存在
    这种情况下，可以使用 fiddle 抓取浏览器登录的链接。获取真相的登录 url = /User/Login/ajaxLogin
    """
    login_url = '{}/User/Login/ajaxLogin'.format(url)
    # login_url = 'http://www.zimuzu.tv/user/sign'
    userinfo = json.load(open('user.json'))
    # print(userinfo)

    r = s.post(login_url, data=userinfo, headers=headers)
    # r = s.post(login_url, data=userinfo)

    # print(r.headers)
    # r = s.get(login_url, timeout=3, headers=headers)
    r.raise_for_status()

    result = json.loads(r.text)
    # for k in result:
    #     print(k, result[k])

    return s


def get_today():
    # s = login(url)
    today_url = '{}/today'.format(url)

    r = s.get(today_url)
    r.raise_for_status()

    r.encoding = r.apparent_encoding

    # print(r.text)

    html = r.text

    open('today.html', 'w', encoding='utf-8').write(html)


def get_res():
    items = []

    html = open('today.html', 'r', encoding='utf-8').read()

    soup = BeautifulSoup(html, 'lxml')

    res_list = soup.find('table', class_="d_r_t")

    movies = res_list.find_all('tr', attrs={"day": "08-22"})

    print(len(movies))

    for movie in movies:
        m_dict = {}
        """
        使用选择器，可行
        # m_type = movie.select('td.d1')[0].string
        # m_format = movie.select('td.d2')[0].text
        """
        m_area = movie['area']
        m_type = movie.find('td', class_="d1").text
        m_format = movie.find('td', class_="d2").text

        m_title = movie.find('a', attrs={"target": "_blank"}).text
        m_detail = movie.find('a', attrs={"target": "_blank"})['href']

        m_dict['area'] = m_area
        m_dict['m_type'] = m_type
        m_dict['m_format'] = m_format
        m_dict['m_title'] = m_title
        m_dict['m_detail'] = m_detail

        # print(m_area)
        # print(m_type, m_format)
        # print(m_title, m_detail)

        m_dict['dl'] = []
        for dl in movie.find('td', class_="dr_ico").find_all('a'):
            try:
                # print("{} : {}".format(dl.text, dl['href']))

                m_dict['dl'].append({'dl_name': dl.text, 'dl_url': dl['href']})
                # print(dl)

                if dl.text == '驴':
                    print(m_title)
                    print(dl['href'])
            except:
                pass

        # print(json.dumps(m_dict))
        print("\n")

        items.append(m_dict)


if __name__ == "__main__":
    url = 'http://www.zimuzu.tv'
    # s = login(url)

    get_res()
