# -*- coding: utf-8 -*-
import scrapy


class SogouSpider(scrapy.Spider):
    name = "sogou"
    allowed_domains = ["pinyin.sogou.com"]
    start_urls = ['http://pinyin.sogou.com/dict/']

    def parse(self, response):
        for url in response.css('.dict_category_list_title a::attr(href)').extract():
            yield scrapy.Request('http://pinyin.sogou.com%s' % url, callback=self.files_list)
        for url in response.css('.catewords a::attr(href)').extract():
            yield scrapy.Request('http://pinyin.sogou.com%s' % url, callback=self.files_list)


    def files_list(self, response):
        for url in response.css('.dict_dl_btn a').extract():
            # yield scrapy.Request(url, callback=self.download_files)
            print url
        for url in response.css('#dict_page_list a::attr(href)').extract():
            yield scrapy.Request('http://pinyin.sogou.com%s' % url, callback=self.files_list)

    def download_files(self, response):
        pass

