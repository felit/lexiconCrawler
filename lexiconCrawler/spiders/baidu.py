# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["shurufa.baidu.com/dict"]
    start_urls = ['http://shurufa.baidu.com/dict/']

    def parse(self, response):
        pass
