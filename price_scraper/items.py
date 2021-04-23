# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PriceScraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    original_price = scrapy.Field()
    discounted_price = scrapy.Field()
    url = scrapy.Field()
    pass
