# -*- coding: utf-8 -*-
import scrapy


class QqSpider(scrapy.Spider):
    name = "qq"
    allowed_domains = ["dict.qq.pinyin.cn"]
    start_urls = ['http://dict.qq.pinyin.cn/']

    def parse(self, response):
        for url in response.css('.cikuCategory a::attr(href),.subCategory a::attr(href)').extract():
            yield scrapy.Request('http://dict.qq.pinyin.cn%s' % url, callback=self.files_list)

    def files_list(self, response):
        for url in response.css('a.downloadICO::attr(href)').extract():
            # TODO
            print url
        for url in response.css('.page-bottom a::attr(href)').extract():
            yield scrapy.Request('http://dict.qq.pinyin.cn%s' % url, callback=self.files_list)




