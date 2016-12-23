import scrapy
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy.exporters import CsvItemExporter
from sample.items import SampleItem
from scrapy.selector import Selector


class TwitterSpider(scrapy.Spider):
   name = 'twitter'
   allowed_domains=['twitter.com']
   start_urls = ['http://www.twitter.com/uber']
	
   def parse(self, response):
      		  
      self.driver = webdriver.Firefox()
      self.driver.get(response.url)
      element = self.driver.find_element_by_tag_name('body')
      loop = 14100
      while loop > 0:
         element.send_keys(Keys.PAGE_DOWN)
         time.sleep(0.2)
         loop -= 1
		
      tweets = self.driver.find_elements_by_xpath('//div[@class="content"]') 
      likes_retweets = self.driver.find_elements_by_xpath('//div[@class="IconTextContainer"]/span[@class="ProfileTweet-actionCount"]/span[@class="ProfileTweet-actionCountForPresentation"]')	  
      count = 0
      count2=0
      count3=2      
      for tweet in tweets:
         item = SampleItem()			
         item['time'] = tweet.find_elements_by_xpath('//small[@class="time"]/a')[count].text
		#item['time'] =  item['time'][104:126]
         item['number'] = str(count)
         item['title'] = tweet.find_elements_by_xpath('//div[@class="content"]/div[@class="js-tweet-text-container"]/p')[count].text
         #item['retweets'] = tweet.find_elements_by_xpath('//div[@class="IconTextContainer"]/span[@class="ProfileTweet-actionCount"]/span[@class="ProfileTweet-actionCountForPresentation"]')[count2].text         
		 #item['retweets']= tweet.find_elements_by_xpath('//*[contains(@data-modal, "ProfileTweet-retweet")]')[count2].text			
         #item['likes'] = tweet.find_elements_by_xpath('//div[@class="IconTextContainer"]/span[@class="ProfileTweet-actionCount"]/span[@class="ProfileTweet-actionCountForPresentation"]')[count3].text
         item['retweets'] = likes_retweets[count2].text   
         item['likes'] = likes_retweets[count3].text
         count += 1
         count2 += 4
         count3 += 4		 
         yield item		
	
        
      
      