# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


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
        for article in response.xpath('//article'):
            text = article.xpath('normalize-space(string(.))')
            for image in article.xpath('.//img[contains(@src,''media'')]/@src'):
                print(image)
            print(text)