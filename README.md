# 環境

- Python 3.7.4 32-bit

- Scrapy 2.0.1

- Visual Studio Code

# TODO

- [x] ~~自動建立資料庫~~ 設定好資料資料庫與 collection 後，yield 時會自動建立
- [ ] 判斷已是最新資料/不 insert 重複
- [ ] 排程自動執行
- [ ] 加上執行 log
- [ ] 寬度擴散 (path)
- [ ] 偽裝 使用隨機 User-Agent

# 備忘

- 執行 `python fly.py`

- 執行爬蟲，只顯示錯誤 `scrapy crawl 爬蟲名稱 -L ERROR`

- 產生爬蟲 `scrapy genspider 爬蟲名稱 爬蟲網址`

# 備註

## Twitter 爬取問題

有些推特帳號直接用 slpash 頁面 render，頁面會出現 "Something went wrong, but don't fret - it's not your falut." 的訊息。實際爬取頁面時也抓不到資料，建議使用呼叫 API 的方式。

# 參考

https://piaosanlang.gitbooks.io/spiders

https://docs.scrapy.org
