# -*- coding: utf-8 -*-
import scrapy


class GuansuSpider(scrapy.Spider):
    name = "guansu"
    allowed_domains = ["www.guangsu.cn"]
    start_urls = ['http://www.guangsu.cn/word.html']

    def parse(self, response):
        pass
