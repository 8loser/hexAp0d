import config  # 載入設定檔
import scrapy
from scrapy.crawler import CrawlerProcess
from hexAp0d.spiders import simple
from scrapy.utils.project import get_project_settings
import pymongo
# 執行多個spider
# https://docs.scrapy.org/en/latest/topics/practices.html
# https://stackoverflow.com/questions/15564844/locally-run-all-of-the-spiders-in-scrapy
# https://botproxy.net/docs/how-to/scrapy-crawl-multiple-spiders-sharing-same-items-pipeline-and-settings-but-with-separa/


def fly():
    client = pymongo.MongoClient(config.mongoDBUrl)
    db = client['lair']
    collection = db.pheromone

    # 找出未處理的 state=0
    for post in collection.find({'state': 0}):
        print(post)
        s = Setting()
        process = CrawlerProcess(s)
        process.crawl(simple.SimpleSpider)
        process.start()


def Setting():
    '''
    加載設定
    '''
    s = get_project_settings()
    # Log設定
    s.update({
        'LOG_FILE': 'log.txt',
        'LOG_LEVEL': 'ERROR'
    })
    # slpash設定
    if (hasattr(config, 'splashServer') and (config.splashServer)):
        s.update({
            'SPLASH_URL': config.splashServer,
            'DOWNLOADER_MIDDLEWARES': {
                'scrapy_splash.SplashCookiesMiddleware': 723,
                'scrapy_splash.SplashMiddleware': 725,
                'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
            },
            'DUPEFILTER_CLASS': 'scrapy_splash.SplashAwareDupeFilter',
            'HTTPCACHE_STORAGE': 'scrapy_splash.SplashAwareFSCacheStorage',
            'SPIDER_MIDDLEWARES': {
                'scrapy_splash.SplashDeduplicateArgsMiddleware': 100}
        })
    # mongoDB設置
    if (hasattr(config, 'mongoDBUrl') and (config.mongoDBUrl)):
        s.update({
            'MONGO_URI': config.mongoDBUrl,
            'MONGO_DB': 'lair'
        })
    return s


if __name__ == "__main__":
    fly()
    print('done')
