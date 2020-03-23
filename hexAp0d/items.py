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
    article_id = scrapy.Field()
    text = scrapy.Field()
    image = scrapy.Field()
    # update_time = scrapy.Field(serializer=str)
