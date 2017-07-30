# -*- coding: utf-8 -*-
import scrapy


class EastdaySpider(scrapy.Spider):
    name = "eastday"
    allowed_domains = ["shurufa.eastday.com"]
    start_urls = ['http://shurufa.eastday.com/']

    def parse(self, response):
        pass
