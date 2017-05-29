# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["scDemo.io"]
    start_urls = ['http://scDemo.io/']

    def parse(self, response):
        pass
