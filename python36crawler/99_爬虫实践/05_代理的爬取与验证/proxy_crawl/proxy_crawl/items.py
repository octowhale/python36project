# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    addr = scrapy.Field()
    port = scrapy.Field()
    protocol = scrapy.Field()
    country = scrapy.Field()
    anonymous = scrapy.Field()


