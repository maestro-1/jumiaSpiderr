# -*- coding: utf-8 -*-
import scrapy
from ..items import JumiaspiderrItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class JumiaSpider(CrawlSpider):
    name = 'jumia'
    allowed_domains = ['www.jumia.com.ng']
    start_urls = ['http://www.jumia.com.ng/']

    rules = (
        Rule(
            LinkExtractor(
                allow=("/\w+/(\?page)?"), deny=(".html")), follow=True
        ),
        Rule(
            LinkExtractor(
                allow=("[-]\w+\.html$"), deny=("/\w+/")),
            callback="parse_extract_items"
        )
    )

    def parse_extract_items(self, response):

        properties = {}

        properties["item_name"] = response.css("h1.-fs20::text").get()
        properties["discount_price"] = response.css(".-fs24::text").get()
        try:
            properties["actual_price"] = response.css(".-mtxs > div:nth-child(2) > span:nth-child(1)::text").get()
        except Exception:
            pass

        properties["number_of_ratings"] = response.css("p.-fs16::text").get()
        properties["ratings"] = response.css(".-fs29 > span:nth-child(1)::text").get()
        properties["all_details"] = response.url

        JumiaspiderrItem(**properties)
