# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class CaipItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    res = scrapy.Field()
    res_s = scrapy.Field()
    res_time = scrapy.Field()
    first_prize_num = scrapy.Field()
    first_prize_get = scrapy.Field()
    two_prize_num = scrapy.Field()
    two_prize_get = scrapy.Field()