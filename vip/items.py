# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VipItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    brandslug=scrapy.Field()
    infourl=scrapy.Field()
    adurl=scrapy.Field()
    picurl=scrapy.Field()
    price=scrapy.Field()
    content=scrapy.Field()
    minicontent=scrapy.Field()
    cat1=scrapy.Field()
    cat2=scrapy.Field()
    cat3=scrapy.Field()
    cat4=scrapy.Field()
