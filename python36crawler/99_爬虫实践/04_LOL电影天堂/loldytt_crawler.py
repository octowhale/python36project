#!/usr/bin/env python
# encoding: utf-8
#

"""
@python ver: Python 3.6
@FILE: loldytt_crawler.py
@time: 2017/8/19 12:58
"""

import os
import sys
import requests
from bs4 import BeautifulSoup


def get_html(url):
    s = requests.Session()
    r = s.get(url)

    r.raise_for_status()

    # print(r.encoding, r.apparent_encoding)
    r.encoding = r.apparent_encoding

    return r.text


def get_downurl(url):
    html = get_html(url)

    soup = BeautifulSoup(html, 'lxml')

    title = soup.find('h1').text.strip()

    print(title.split('>')[1].strip())

    ultag = soup.find('ul', attrs={'class': 'downurl'})

    downurls = ultag.find_all('a', attrs={'target': "_self"})
    # downurl = ultag.find_all('a', target_='_self')

    for downurl in downurls:
        # print(downurl)

        # print(downurl.text.strip())
        # print(downurl['href'].strip())
        #
        # title=downurl.text.strip()
        # dlurl=downurl['href'].strip()

        # print(repr('{} : {}'.format(downurl.text.strip(), downurl['href'].strip())))
        print('{} : {}'.format(downurl.text.strip(), downurl['href'].strip()))

        # sys.exit(0)
        #
        # print(ultag)


if __name__ == "__main__":
    # url = 'http://www.loldytt.com/Dianshiju/SSC/'

    url = 'http://www.loldytt.com/Zuixinhanju/CWHJ/'
    get_downurl(url)
