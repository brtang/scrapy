import scrapy

from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.contrib.linkextractors import LinkExtractor
from sample.items import SampleItem

class TwitterSpider(scrapy.Spider):
	name = 'twitter'
	allowed_domains=['twitter.com']
	start_urls = ['http://www.twitter.com/uber']
	#rules = [Rule(LinkExtractor(allow=['/gallery/,*']), 'parse_twitter')]
	
	def parse_twitter(self, response):
		item = SampleItem()
		item['time'] = response.xpath('//*[@id="stream-item-tweet-743942908877770755"]/div/div[2]/div[1]/small/a/text()').extract()
		item['title'] = response.xpath('//*[@id="stream-item-tweet-743942908877770755"]/div/div[2]/div[2]/p/text()').extract()
		
		return item