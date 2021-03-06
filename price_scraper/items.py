# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemLoader.processors import TakeFirst, MapCompose


class PriceScraperItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
