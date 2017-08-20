# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem


class SztianqiSpider(scrapy.Spider):
    name = 'SZtianqi'
    # allowed_domains = ['suzhou.tianqi.com']
    allowed_domains = ['tianqi.com']
    # start_urls = ['http://suzhou.tianqi.com/']

    ## 建立需要爬区的信息的 url 列表
    start_urls = []

    # citys = ['nanjing', 'suzhou', 'shanghai']
    citys = ['chengdu']

    for city in citys:
        start_urls.append('http://{}.tianqi.com'.format(city))

    def parse(self, response):
        """
        筛选信息的函数

        date: 今日日期
        week: 星期几
        img: 天气图片
        temperature: 温度
        weather: 天气
        wind: 风向

        :param response: 网页结果
        :return: items 过滤信息
        """

        ## 建立一个列表，用来保存当天的信息
        items = []

        # 找到包裹着当天信息的div
        sixday = response.xpath('//div[@class="tqshow1"]')

        # 循环赛选出每天的信息

        for day in sixday:
            # 先申请一个 weatheritem 的类型来把保存结果
            item = WeatherItem()

            # 观察网页，知道 h3 标签下的不单单是一行 string。我们用 trick 的方式将他链接起来
            date = ''

            for datetitle in day.xpath('./h3//text()').extract():
                date += datetitle

                item['date'] = date

                item['week'] = day.xpath('./p//text()').extract()[0]
                item['img'] = day.xpath(
                    './ul/li[@class="tqpng"]/img/@src').extract()[0]
                tq = day.xpath('./ul/li[2]//text()').extract()
                # 我们用第二种取巧的方式，将tq里找到的str连接
                item['temperature'] = ''.join(tq)
                item['weather'] = day.xpath('./ul/li[3]/text()').extract()[0]
                item['wind'] = day.xpath('./ul/li[4]/text()').extract()[0]
                items.append(item)

            return item
