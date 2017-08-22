# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class QbCrawlerSpider(scrapy.Spider):
    name = 'qb_crawler'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    def parse(self, response):
        contents = response.xpath('//div[@class="content"]')

        # print("# " * 20)
        # print(contents)
        # print("# " * 20)

        items = []
        for content in contents:
            item = {}
            # print(" $ @" * 10)
            # print(content.xpath('./span//text()').extract()[0].strip())
            # print(" $ @" * 10)


            # item['content'] = content.xpath('./span//text()').extract()[0].strip()
            # exit(0)


            item['content'] = ''.join(content.xpath('./span//text()').extract())
            # print(content.xpath('./span//text()').extract())

            # print(item['content'])
            items.append(item)

        return items

    def usage(self):
        print('scrapy crawl qb_crawler --loglevel=ERROR')
