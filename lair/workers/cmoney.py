# -*- coding: utf-8 -*-
import scrapy


class CMoneySpider(scrapy.Spider):
    name = 'cmoney'
    allowed_domains = ['www.cmoney.tw']
    # start_urls = ['https://www.cmoney.tw/follow/channel/hot-stock']
    start_urls = ['https://www.cmoney.tw/follow/channel/getdata/channellisthotstock?mainId=9&subId=0&size=10']

    def parse(self, response):
        f = open(self.name+'.txt', 'wb')
        f.write(response.body)
        f.close()
        # pass