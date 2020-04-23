# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Hexap0DItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ArticleItem(scrapy.Item):
    collection = table = 'article'
    url = scrapy.Field()  # 資料來源網址
    title = scrapy.Field()  # 文章標題
    context = scrapy.Field()  # 文章內容
    post_time = scrapy.Field()  # 文章發布時間
    create_time = scrapy.Field()  # 資料抓取時間
