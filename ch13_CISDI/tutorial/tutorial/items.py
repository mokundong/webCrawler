# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field
import scrapy

class DmozItem(scrapy.Item):
    name = scrapy.Field()
    location = scrapy.Field()
    company = scrapy.Field()
    Overview = scrapy.Field()
    publishtime = scrapy.Field()
"""
class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

"""
