# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Dashuju1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()
    com_name = scrapy.Field()
    address = scrapy.Field()
    money = scrapy.Field()
    time = scrapy.Field()
    educational = scrapy.Field()
    experience = scrapy.Field()
    com_nature = scrapy.Field()
    com_insize = scrapy.Field()
    about = scrapy.Field()
