# -*- coding: utf-8 -*-
import scrapy


class BaiduMimeSpider(scrapy.Spider):
    name = "baidu_mime"
    allowed_domains = ["mime.baidu.com"]
    start_urls = ['http://mime.baidu.com/']

    def parse(self, response):
        pass
