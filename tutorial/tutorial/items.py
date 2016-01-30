# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class myhomeItem(scrapy.Item):
    price = scrapy.Field()
    size = scrapy.Field()
    ber = scrapy.Field()
    address = scrapy.Field()
    description = scrapy.Field()
    beds = scrapy.Field()
    url = scrapy.Field()


class dbscItem(scrapy.Item):
    name = scrapy.Field()
    sail_number = scrapy.Field()

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
