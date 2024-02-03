from quotes_scraper.spiders.quotes_spider import QuotesSpider
from quotes_scraper.spiders.authors_spider import AuthorsSpider
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess()

process.crawl(QuotesSpider)
process.crawl(AuthorsSpider)

process.start()
