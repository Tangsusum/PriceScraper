import scrapy
from datetime import date
import pandas



class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    df = pandas.read_csv('./InputURLs.csv')
    start_urls = list(df['URLs'].values)

    def parse(self, response):
        price = response.css('div.a-section.a-spacing-micro').css('span.a-size-medium.a-color-price::text').get().strip()
        name = response.css('div.a-section.a-spacing-none').css('h1.a-size-large.a-spacing-none').css('span.a-size-large.product-title-word-break::text').get().strip() 

        yield {
            'Date': date.today(),
            'Product Name': name,
            'Price': price
        }
       


