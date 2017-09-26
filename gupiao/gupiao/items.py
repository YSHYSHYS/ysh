# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GupiaoItem(scrapy.Item):
    # define the fields for your item here like:
    b = scrapy.Field()
    a = scrapy.Field()
    c = scrapy.Field()
    d = scrapy.Field()
    e = scrapy.Field()
    f = scrapy.Field()
    g = scrapy.Field()
    h = scrapy.Field()

class ComItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    name = scrapy.Field()
    all_name = scrapy.Field()
    type = scrapy.Field()
    web = scrapy.Field()



