import scrapy
from ..items import NewscrawlerItem


class QuoteSpider(scrapy.Spider):
    name = 'firstTry'
    page_number = 2
    start_urls = [
        'https://www.truthorfiction.com/page/1/',
    ]

    def parse(self, response, **kwargs):
        items = NewscrawlerItem()

        titles = response.css('.entry-title a::text').extract()
        authors = response.css('.author-name::text').extract()
        dates = response.css('.published::text').extract()
        for i in range(len(titles)):
            items['titles'] = titles[i]
            items['authors'] = authors[i]
            items['dates'] = dates[i]
            yield items

        next_page = 'https://www.truthorfiction.com/page/'+str(QuoteSpider.page_number)+'/'
        if QuoteSpider.page_number < 515:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

      #  for i in range(len(titles)):
      #      yield {
      #          'title': titles[i],
      #          'author': authors[i],
      #          'date': dates[i]
      #      }
