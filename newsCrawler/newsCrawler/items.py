# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewscrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    titles = scrapy.Field()
    authors = scrapy.Field()
    dates = scrapy.Field()
    page_Url = scrapy.Field()
    # name = scrapy.Field()
    #pass
