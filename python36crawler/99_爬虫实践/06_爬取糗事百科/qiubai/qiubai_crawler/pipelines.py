# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

if os.path.exists('content.txt'):
    os.remove('content.txt')


class QiubaiCrawlerPipeline(object):
    def process_item(self, item, spider):
        with open('content.txt', 'a', encoding='utf-8') as f:
            f.write(item['content'].strip() + '\n')
        return item
