# -*- coding: utf-8 -*-

import scrapy
class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
"""
class BaidustocksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
"""