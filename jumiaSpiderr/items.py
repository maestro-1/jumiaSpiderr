# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JumiaspiderrItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    item_name = scrapy.Field()
    discount_price = scrapy.Field()
    actual_price = scrapy.Field()
    number_of_ratings = scrapy.Field()
    ratings = scrapy.Field()
    all_details = scrapy.Field()
