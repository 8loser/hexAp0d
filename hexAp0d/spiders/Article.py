# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from hexAp0d.items import ArticleItem
import datetime


class ArticleSpider(scrapy.Spider):
    # 唯一名稱，不可跟其他spider重複
    name = 'Article'

    def __init__(self, urls=None, foraging=None):
        self.start_urls = urls
        self.foraging = foraging

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
        # 產生的 Item
        item = ArticleItem()
        # 抓取的網址
        item['url'] = response.request._original_url
        # item['url'] = response.request.url
        # foraging 內有設定的元素才抓取
        for element, feature in self.foraging.items():
            item[element] = response.xpath(feature).get()
        # 建立時間
        item['create_time'] = datetime.datetime.now()
        # 存入資料庫
        yield item
