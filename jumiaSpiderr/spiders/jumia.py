# -*- coding: utf-8 -*-
import scrapy


class JumiaSpider(scrapy.Spider):
    name = 'jumia'
    allowed_domains = ['www.jumia.com.ng']
    start_urls = ['http://www.jumia.com.ng/']

    def parse(self, response):
        pass
