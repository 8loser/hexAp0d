# -*- coding: utf-8 -*-
import pymongo

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Hexap0DPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            # 從 settings.py 取得 MongoDB 參數設置
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    # spider開啟時執行
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    # 資料儲存方法，資料庫或者JSON
    def process_item(self, item, spider):
        '''
        TODO 這邊可以加log
        加上篩選資料條件、過濾重複資料
        '''
        # 可以改成update動作
        self.db[item.collection].insert(dict(item))
        return item

    # spider關閉時執行
    def close_spider(self, spider):
        self.client.close()
