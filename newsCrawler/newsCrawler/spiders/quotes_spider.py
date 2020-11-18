import scrapy
from ..items import NewscrawlerItem

class QuoteSpider(scrapy.Spider):
    name = 'firstTry'
    start_urls = [
        'https://www.truthorfiction.com/',
    ]

    def _parse(self, response, **kwargs):
        items = NewscrawlerItem()

        titles = response.css('.entry-title a::text').extract()
        authors = response.css('.author-name::text').extract()
        dates = response.css('.published::text').extract()

        items[titles] = titles
        items[authors] = authors
        items[dates] = dates
        yield items
      #  for i in range(len(titles)):
      #      yield {
      #          'title': titles[i],
      #          'author': authors[i],
      #          'date': dates[i]
      #      }
