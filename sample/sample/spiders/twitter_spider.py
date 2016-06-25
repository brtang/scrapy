import scrapy
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from scrapy.contrib.spiders import Rule, CrawlSpider
#from scrapy.contrib.linkextractors import LinkExtractor
from sample.items import SampleItem
from scrapy.selector import Selector

#from scrapy.spider import BaseSpider

class TwitterSpider(scrapy.Spider):
	name = 'twitter'
	allowed_domains=['twitter.com']
	start_urls = ['http://www.twitter.com/uber']
	#rules = [Rule(LinkExtractor(allow=['/gallery/,*']), 'parse_twitter')]
	
	
	
	
	def parse(self, response):
		
		self.driver = webdriver.Firefox()
		
		self.driver.get(response.url)
		element = self.driver.find_element_by_tag_name('body')
		loop = 100
		while loop > 0:
			element.send_keys(Keys.PAGE_DOWN)
			time.sleep(0.2)
			loop -= 1
		
		#timelines = response.selector.xpath('//div[@class="content"]')
		#i = 0;
		#for timeline in timelines:
		
		tweets = self.driver.find_elements_by_xpath('//div[@class="js-tweet-text-container"]')
		
		for tweet in tweets:
			item = SampleItem()
		#item['time'] = response.xpath('//small[@class="time"]/a').extract()#[i]
		#item['time'] =  item['time'][104:126]
			item['title'] = tweet.find_element_by_tag_name('p').text#.extract()[i]
		#item['likes'] = response.xpath('//div[@class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState"]/button/div[@class="IconTextContainer"]/span/span/text()').extract()#[i]
		#item['retweets'] = response.xpath('//div[@class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt"]/button/div[@class="IconTextContainer"]/span/span/text()').extract()#[i]
			#i += 1
			yield item
			
		#self.driver.close()