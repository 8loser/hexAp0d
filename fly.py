import config  # 載入設定檔
import pymongo

# 執行多個spider
# https://docs.scrapy.org/en/latest/topics/practices.html
# https://stackoverflow.com/questions/15564844/locally-run-all-of-the-spiders-in-scrapy
# https://botproxy.net/docs/how-to/scrapy-crawl-multiple-spiders-sharing-same-items-pipeline-and-settings-but-with-separa/

client = pymongo.MongoClient(config.mongoDBUrl)
db = client['lair']
collection = db.pheromone

# 找出未處理的 state=0
for post in collection.find({'state': 0}):
    print(post)
