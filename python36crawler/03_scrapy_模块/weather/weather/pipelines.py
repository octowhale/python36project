# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests
import json

"""
一些初始化的操作可以写在 class 外面，比如说删除过期的记录
这里的语句只会被调用一次
"""

base_dir = os.getcwd()
# filename_json = base_dir + '/data/weather.json'
# filename_txt = base_dir + '/data/weather.txt'
filename_txt = os.path.join(base_dir, r'data\weather.txt')
filename_json = os.path.join(base_dir, r'data\weather.json')

if os.path.exists(filename_json):
    os.remove(filename_json)

if os.path.exists(filename_txt):
    os.remove(filename_txt)


class WeatherPipeline(object):
    def process_item(self, item, spider):
        '''
        处理每一个从SZtianqi传过来的
        item
        '''
        # 获取当前工作目录
        # base_dir = os.getcwd()
        # 文件存在data目录下的weather.txt文件内
        # fiename = base_dir + '/data/weather.txt'
        # filename_txt = os.path.join(base_dir, r'data/weather.txt')

        # if os.path.exists(filename):
        #     os.remove(filename)
        # 从内存以追加的方式打开文件，并写入对应的数据
        with open(filename_txt, 'a', encoding='utf-8') as f:
            f.write(item['date'] + '\n')
            f.write(item['week'] + '\n')
            f.write(item['temperature'] + '\n')
            f.write(item['weather'] + '\n')

            f.write(item['wind'] + '\n\n')

        # 下载图片
        with open(base_dir + '/data/' + item['date'] + '.png', 'wb') as f:
            f.write(requests.get(item['img']).content)

        return item


class W2json(object):
    def process_item(self, item, spider):
        '''
        讲爬取的信息保存到json
        方便其他程序员调用
        '''
        # base_dir = os.getcwd()
        # filename_json = base_dir + '/data/weather.json'

        # if os.path.exists(filename):
        #     os.remove(filename)

        # 打开json文件，向里面以dumps的方式吸入数据
        # 注意需要有一个参数ensure_ascii=False ，不然数据会直接为utf编码的方式存入比如:“/xe15”
        # with codecs.open(filename, 'a') as f:
        with open(filename_json, 'a', encoding='utf-8') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)

        return item
