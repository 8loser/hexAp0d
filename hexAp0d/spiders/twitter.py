# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy_splash import SplashRequest
from hexAp0d.items import ArticleItem


class TwitterSpider(scrapy.Spider):
    # 唯一名稱，不可跟其他spider重複
    name = 'twitter'
    allowed_domains = ['twitter.com']
    start_urls = ['https://twitter.com/twitter']

    def start_requests(self):
        # 解析時使用lua腳本
        lua_script = """
            function main(splash, args)
                assert(splash:go(args.url))
                assert(splash:wait(3))
                return {
                    html = splash:html(),
                }
            end
            """
        # splash 參數
        splash_args = {
            "lua_source": lua_script,
            "wait": 0.5
        }
        for url in self.start_urls:
            yield SplashRequest(url=url, endpoint="execute", callback=self.parse, args=splash_args)

    # response 進來的位置
    def parse(self, response):
        # 測試用
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        # 輪詢每個推文、轉推
        for article in response.xpath('//article'):
            # 抓取推文網址後面數字當成ID
            # https://twitter.com/帳號/status/1242116348970336261
            article_url = article.xpath(
                './/a[contains(@href,\'/status\')]/@href').extract()[0]
            article_id = re.search('\/status\/(\d+)', article_url).group(1)
            # 解析推文內容
            text = article.xpath(
                './div/div/div/div/div[2]').xpath('normalize-space(string(.))').extract()
            # 解析推文內圖片
            image = article.xpath(
                './/img[contains(@src,\'media\')]/@src').extract()
            # 存入item
            item = ArticleItem()
            item['article_id'] = article_id
            item['text'] = text
            item['image'] = image
            yield item
