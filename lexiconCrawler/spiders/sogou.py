# -*- coding: utf-8 -*-
import scrapy


class SogouSpider(scrapy.Spider):
    name = "sogou"
    allowed_domains = ["pinyin.sogou.com"]
    start_urls = ['http://pinyin.sogou.com/']

    def parse(self, response):
        pass
