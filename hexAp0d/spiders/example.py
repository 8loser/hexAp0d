# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class ExampleSpider(scrapy.Spider):
    # 唯一名稱，不可跟其他spider重複
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']


    def start_requests(self):
        for url in self.start_urls:
            lua_script = """
            function main(splash, args)
                assert(splash:go(args.url))
                assert(splash:wait(3))
                return {
                    html = splash:html(),
                }
            end
            """
            yield SplashRequest(url=url, endpoint="execute", callback=self.parse, args={"lua_source": lua_script, "wait": 2})

    # response 進來的位置
    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
