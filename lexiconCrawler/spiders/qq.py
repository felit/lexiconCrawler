# -*- coding: utf-8 -*-
import scrapy


class QqSpider(scrapy.Spider):
    name = "qq"
    allowed_domains = ["dict.qq.pinyin.cn"]
    start_urls = ['http://dict.qq.pinyin.cn/']

    def parse(self, response):
        pass
