# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class SimpleSpider(scrapy.Spider):
    # 唯一名稱，不可跟其他spider重複
    name = 'simple'

    def __init__(self, urls=None):
        self.start_urls = urls

    # 這邊參考
    # https://scrapy-cookbook.readthedocs.io/zh_CN/latest/scrapy-10.html
    def start_requests(self):
        # 解析時使用lua腳本
        lua_script = """
            function main(splash, args)
                assert(splash:go(args.url))
                assert(splash:wait(5))
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
        filename = response.xpath('//title/text()').get()
        print(filename)
