#!/usr/bin/env python
# encoding: utf-8
#

"""
@license: Apache Licence
@python ver: Python 2.7.12
@python ver: Python 3.6
@FILE: xicidaili.py
@time: 2017/8/20 14:41
"""

import os
import sys
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0;"}


def get_proxy():
    url = 'http://www.xicidaili.com/nn/'
    s = requests.Session()
    r = s.get(url, headers=headers)

    reponse = r.text

    # print(reponse)


    with open('xicidl.html', 'w', encoding='utf-8') as f:
        f.write(reponse)


if __name__ == "__main__":
    get_proxy()
