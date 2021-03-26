# -*- coding: utf-8 -*-
import scrapy


class VipshopSpider(scrapy.Spider):
    name = 'vipshop'
    allowed_domains = ['vip.com']
    start_urls = ['https://www.vip.com/']
    redis_key='vipshop:start_urls'

    def parse(self, response):
        print(response.url)
        
