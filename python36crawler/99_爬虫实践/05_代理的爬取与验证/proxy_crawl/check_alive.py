#!/usr/bin/env python
# encoding: utf-8
#

"""
@python ver: Python 3.6
@FILE: check_alive.py
@time: 2017/8/20 17:04
"""

import os
import sys
import requests
import threading


def checking(line):
    # print("checking ... ", line)
    with open('alive_proxy2.txt', 'a', encoding='utf-8') as fa:
        try:
            addr, port, protocol = line.split()[1:4]
            proxies = {
                "http": "{}://{}:{}".format(protocol, addr, port),
                "https": "{}://{}:{}".format(protocol, addr, port),
            }
            # print(proxies)
            url = 'https://www.baidu.com/'
            r = requests.get(url, proxies=proxies, timeout=1)
            if r.status_code == 200:
                fa.write(line)
        except:
            pass


def main():
    with open('proxy.txt', 'r', encoding='utf-8') as f:
        for line in f:
            # print(line)
            t = threading.Thread(target=checking, args=(line,))
            t.start()

            # addr, port, protocol = line.split()[1:4]
            # print(addr, port, protocol)

            # exit(0)


def proxy_req():
    """61.143.228.162 3128"""
    proxies = {
        'http': 'HTTPS://61.143.228.162:3128',
        'https': 'HTTPS://61.143.228.162:3128',
    }

    r = requests.get('https://www.baidu.com', proxies=proxies, timeout=3)

    r.raise_for_status()
    r.encoding = r.apparent_encoding

    print(r.text)
    if r.status_code == 200:
        print("ok")
    else:
        print("not ok")


if __name__ == "__main__":
    # main()
    proxy_req()
