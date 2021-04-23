# PriceScraper

The following project aims to scrap prices from online shopping websites. In the InputURLs.csv, users can specify the URL links that they wish to crawl. Scrapped prices will be
output in results.csv where the file contains the scrapping date, product name and product price of the each item. Currently, this project only supports web price scrapping from
Amazon. 


SETUP
------------
To run the project, go into the price_scraper directory and enter the following in the command shell. 

```
scrapy crawl amazon -O results.csv  
```
