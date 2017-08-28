#!/usr/bin/env python
# encoding: utf-8

# python 3.6

import os
import sys
import requests
import json
from bs4 import BeautifulSoup
import pymongo


class Zimuzu(object):
    def __init__(self, auth):
        self.auth = auth
        self.setting = json.load(open(self.auth, 'r', encoding='utf-8'))
        self.s = requests.Session()

    def login(self):
        headers = headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
            'X-Forwarded-For': '8.8.8.8',  # 伪装IP地址
            'Accept': 'image/webp,image/*,*/*;q=0.8',
            # 'Accept-Encoding': 'gzip, deflate, sdch',  # 使用后压缩结果
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Content-Type': 'application/html',
        }
        userinfo = {"account": self.setting['account'], "password": self.setting['password']}
        # account = setting['account']
        # password = setting['password']
        login_url = "{}/User/Login/ajaxLogin".format(self.setting['site_url'])

        try:
            r = self.s.post(login_url,
                            data=userinfo,
                            headers=headers)

            # print('登录成功')
            signin_info = json.loads(r.text)
            for k in signin_info:
                print(signin_info[k])
            return self.s
        except:
            print('登录失败')
            sys.exit(1)

    def top24(self):
        pass

    def movie_breaf(self):
        """资源简介页面"""
        """/resource/id"""
        pass

    def moive_detail(self, uri):
        """资源详细下载页面"""

        """/resource/list/id"""

        url = "{}{}".format(self.setting['site_url'], uri)

        # print(url)
        r = self.s.get(url)

        with open('de.html', 'w', encoding='utf-8') as f:
            f.write(r.text)

        items = {}

        with open('de.html', 'r', encoding='utf-8') as f:
            html = f.read()

        soup = BeautifulSoup(html, 'lxml')

        movie_name = soup.find('h2').text.strip("返回详情介绍页")
        items['movie_name'] = movie_name
        # print(movie_name)
        #
        # exit(0)

        # fmts = soup.find('div', class_="download-filter").find_all('a')

        fmts_list = ['MP4', 'HDTV']
        # fmts = ['MP4', 'HDTV', '720P', 'WEB-DL']

        fmts = {}
        seasons = {}
        # li_tags = soup.find_all('li', class_='clearfix')
        for fmt in fmts_list:
            # li_tags = soup.find_all('li', class_='clearfix', format_='MP4')
            li_tags = soup.find_all('li', attrs={"class": "clearfix", "format": fmt})

            # print(len(li_tags))
            for li_tag in li_tags:

                fmt = li_tag['format']
                season = li_tag['season']
                episode = li_tag['episode']

                a_tags = li_tag.find('div', class_='fr').find_all('a')

                episodes = {}

                fmts["第_{}_集".format(episode)] = episodes

                seasons[fmt] = fmts
                items["第_{}_季".format(season)] = seasons

                for a_tag in a_tags:

                    dl_app = a_tag.text.strip()

                    try:
                        if dl_app == '小米路由下载':
                            dl_url = a_tag['xmhref']
                        else:
                            dl_url = a_tag['href']
                    except:
                        dl_url = 'None'

                    episodes[dl_app] = dl_url

        """记录在本地文件中"""
        filename = '_'.join(uri.split('/')) + '.json'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(items, indent=4, ensure_ascii=False))

        """记录在 mongodb 中"""
        mongo_auth = os.path.join('auth', 'mongo_auth.json')
        mongo_info = json.load(open(mongo_auth, 'r'))
        host, port = mongo_info['host'], mongo_info['port']
        with pymongo.MongoClient(host, port) as client:
            db = client.zimuzu

            db.detail.insert(items)


if __name__ == "__main__":
    z = Zimuzu('auth/setting.json')

    z.login()
    z.moive_detail('/resource/list/35324')
