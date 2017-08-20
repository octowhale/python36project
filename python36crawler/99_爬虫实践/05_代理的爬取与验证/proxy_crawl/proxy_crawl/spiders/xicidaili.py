# -*- coding: utf-8 -*-
import scrapy
from proxy_crawl.items import ProxyCrawlItem
import sys

import time

time.sleep(2)


class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'
    allowed_domains = ['www.xicidaili.com']
    # start_urls = ['http://www.xicidaili.com/nn/']

    start_urls = []
    start_uri = ['nn', 'nt', 'wn', 'wt']
    # start_uri = ['nn']

    items = []

    for uri in start_uri:
        start_urls.append('{}/{}/'.format('http://www.xicidaili.com', uri))

    #
    # start_urls = ['xicidl.html']

    def parse(self, response):

        # print("========================")
        # print(type(response))
        # print("========================")
        # items = []
        proxys_odd = response.xpath('//tr[@class="odd"]')
        proxys = response.xpath('//tr[@class]')

        # print("========================")
        # print(type(proxys))
        # for proxy in proxys:
        #     print(proxy)
        #     print(type(proxy))
        # print("========================")

        # print(type(proxys))
        # print(len(proxys))
        # print(proxy_class)
        for proxy in proxys:
            self.add_item(proxy)

        for proxy in proxys_odd:
            self.add_item(proxy)
            # print(proxy)
            # try:
            #     item = ProxyCrawlItem()
            #
            #     item['country'] = proxy.xpath('./td[@class="country"]/img/@alt').extract()[0]
            #     item['addr'] = proxy.xpath('./td//text()')[0].extract()
            #     item['port'] = proxy.xpath('./td//text()')[1].extract()
            #     item['anonymous'] = proxy.xpath('./td//text()')[5].extract()
            #     item['protocol'] = proxy.xpath('./td//text()')[6].extract()
            #
            #     items.append(item)
            #
            #     # print("*************************")
            #     # print(proxy.xpath('./td//text()'))
            #     # print(proxy.xpath('./td//text()')[0].extract())
            #     # print(proxy.xpath('./td//text()')[1].extract())
            #     # print(proxy.xpath('./td//text()')[5].extract())
            #     # print(proxy.xpath('./td//text()')[6].extract())
            #     # print("*************************")
            #     #
            #     # print("@" * 20)
            #     # print(proxy.xpath('./td[@class="country"]/img/@alt'))
            #     # print(proxy.xpath('./td[@class="country"]/img/@alt').extract()[0])
            #     # print("@" * 20)
            #     # return items
            # except:
            #     print(proxy.xpath('./td[@class="country"]/img/@alt'))
            #     pass

        # print('# @ ' * 10)
        # print(len(self.items))
        # print(len(set(self.items)))
        return set(self.items)

    def add_item(self, proxy):
        try:
            item = ProxyCrawlItem()

            item['country'] = proxy.xpath('./td[@class="country"]/img/@alt').extract()[0]
            item['addr'] = proxy.xpath('./td//text()')[0].extract()
            item['port'] = proxy.xpath('./td//text()')[1].extract()
            item['anonymous'] = proxy.xpath('./td//text()')[5].extract()
            item['protocol'] = proxy.xpath('./td//text()')[6].extract()

            self.items.append(item)

            # print("*************************")
            # print(proxy.xpath('./td//text()'))
            # print(proxy.xpath('./td//text()')[0].extract())
            # print(proxy.xpath('./td//text()')[1].extract())
            # print(proxy.xpath('./td//text()')[5].extract())
            # print(proxy.xpath('./td//text()')[6].extract())
            # print("*************************")
            #
            # print("@" * 20)
            # print(proxy.xpath('./td[@class="country"]/img/@alt'))
            # print(proxy.xpath('./td[@class="country"]/img/@alt').extract()[0])
            # print("@" * 20)
            # return items
        except:
            # print(proxy.xpath('./td[@class="country"]/img/@alt'))
            pass
