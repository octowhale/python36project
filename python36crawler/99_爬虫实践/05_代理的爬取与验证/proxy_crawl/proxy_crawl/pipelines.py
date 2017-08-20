# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests

if os.path.exists('proxy.txt'):
    os.remove('proxy.txt')
if os.path.exists('alive_proxy.txt'):
    os.remove('alive_proxy.txt')


class ProxyCrawlPipeline(object):
    def process_item(self, item, spider):
        with open('proxy.txt', 'a', encoding='utf-8') as f:
            f.write('{} {} {} {} {} \n'.format(item['country'],
                                               item['addr'],
                                               item['port'],
                                               item['protocol'],
                                               item['anonymous']))
        return item


class AliveProxyPipeline(object):
    def process_item(self, item, spider):
        proxies = {
            "http": "{}://{}:{}".format(item['protocol'], item['addr'], item['port']),
            "https": "{}://{}:{}".format(item['protocol'], item['addr'], item['port']),
        }

        r = requests.get('https://www.baidu.com/', proxies=proxies, timeout=3)

        if r.status_code == 200:
            with open('alive_proxy.txt', 'a', encoding='utf-8') as fa:
                fa.write('{} {} {} {} {} \n'.format(item['country'],
                                                    item['addr'],
                                                    item['port'],
                                                    item['protocol'],
                                                    item['anonymous']))
