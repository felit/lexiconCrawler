# -*- coding: utf-8 -*-
import scrapy


class SogouWubiSpider(scrapy.Spider):
    name = "sogou_wubi"
    allowed_domains = ["wubi.sogou.com"]
    start_urls = ['http://wubi.sogou.com/']

    def parse(self, response):
        pass
