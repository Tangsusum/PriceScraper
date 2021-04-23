import scrapy
from datetime import date
from numpy import genfromtxt
import pandas



class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    # start_urls = ['https://www.amazon.com.au/Philips-Play-Extension-Cable-Black/dp/B07FXT49KF/ref=sr_1_1?keywords=8718696171189&amp%3Bqid=1571943620&amp%3Bsr=8-1&fbclid=IwAR3oN1ksOpbwZtTzVSO-kUIc5YjYffiYAaoEWihfqoWDo6RQvfLIkp_n9rQ', 'https://www.amazon.com.au/dp/B084NTF5ZY/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B084NTF5ZY&pd_rd_w=lxbSa&pf_rd_p=ea20208d-137b-46cb-8ff4-3f2183f0cd6f&pd_rd_wg=tw0cL&pf_rd_r=VYTJM25MNF4FH9PFQYEJ&pd_rd_r=5daeb1f6-5c5c-4406-8949-2e5ef39547b9&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE1STEySUk0SlJKOFQmZW5jcnlwdGVkSWQ9QTA1NTM3NTUxT0MwTzZaMFRJSEdaJmVuY3J5cHRlZEFkSWQ9QVhQNTNKNE03V1BFJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==']
    # start_urls = ['https://www.amazon.com.au/dp/B084NTF5ZY/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B084NTF5ZY&pd_rd_w=lxbSa&pf_rd_p=ea20208d-137b-46cb-8ff4-3f2183f0cd6f&pd_rd_wg=tw0cL&pf_rd_r=VYTJM25MNF4FH9PFQYEJ&pd_rd_r=5daeb1f6-5c5c-4406-8949-2e5ef39547b9&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE1STEySUk0SlJKOFQmZW5jcnlwdGVkSWQ9QTA1NTM3NTUxT0MwTzZaMFRJSEdaJmVuY3J5cHRlZEFkSWQ9QVhQNTNKNE03V1BFJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==']
    df = pandas.read_csv('./InputURLs.csv')
    start_urls = list(df['URLs'].values)

    def parse(self, response):
        # product = response.css('div.a-section.a-spacing-micro')
        price = response.css('div.a-section.a-spacing-micro').css('span.a-size-medium.a-color-price::text').get().strip()
        name = response.css('div.a-section.a-spacing-none').css('h1.a-size-large.a-spacing-none').css('span.a-size-large.product-title-word-break::text').get().strip() 
        print('price??????????????????????????????????????????????????')
        print(type(name))
        print(price)
        print(name.strip())
        yield {
            'Date': date.today(),
            'Product Name': name,
            'Price': price
        }
        

    # def parse_detail_page(self, response):
    #     # item = PriceScraperItem()
    #     # item['name'] = response.css('div h1.shelfProductTile-title heading3::text').extract()
    #     # yield item
    #     product = response.css('div.a-section.a-spacing-micro')
    #     price = product.css('span.a-size-medium.a-color-price::text').get()
    #     print('price??????????????????????????????????????????????????')
    #     print(price)

       


