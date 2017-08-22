#!/usr/bin/env python
# encoding: utf-8

# python 3.6

import os
import sys
from pypinyin import lazy_pinyin
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64);"}


def main(city):
    s = requests.Session()

    city_str = ''.join(lazy_pinyin(city))

    r = s.get('http://{}.{}'.format(city_str, 'tianqi.com'), headers=headers, timeout=3)

    # print(r.apparent_encoding)

    r.encoding = 'GB2312'

    html = r.text

    soup = BeautifulSoup(html, 'lxml')
    today_info = soup.find('div', attrs={"class": "tqshow", "id": "today"})

    title = today_info.find('h3', attrs={"style": "padding-bottom:0px;"}).text
    time = today_info.find('li', class_="time").text
    temperature = today_info.find('li', class_="fon14 fB").span.text
    weather_info = today_info.find('li', class_="cDRed").text
    wind = today_info.find('li', attrs={"style": "height:18px;overflow:hidden"}).text

    print(title)
    print(time)
    print(temperature)
    print(weather_info)
    print(wind)
    print("\n")

    print("{} {}\n{}\n{}\n{}\n".format(title, time, temperature, weather_info, wind))


if __name__ == '__main__':
    # main('chengdu')
    # main('nanjing')

    # main('成都')
    # main('chengdu')
    # main('chengde')
    main('daying')
