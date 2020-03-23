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
        for article in response.xpath('//article'):
            article_url = article.xpath(
                './/a[contains(@href,\'/status\')]/@href').extract()[0]
            article_id = re.search('\/status\/(\d+)', article_url).group(1)
            text = article.xpath('normalize-space(string(.))').extract()
            item = ArticleItem()
            item['article_id'] = article_id
            item['text'] = text
            item['image'] = article.xpath('.//img[contains(@src,''media'')]/@src').extract()
            yield item
