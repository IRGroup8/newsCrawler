import scrapy
from ..items import NewscrawlerItem


class QuoteSpider(scrapy.Spider):
    name = 'firstTry'
    page_number = 2
    allowed_domains = ['truthorfiction.com']
    start_urls = [
        'https://www.truthorfiction.com/page/1/',
    ]

    def parse_news(self, response):
        items = NewscrawlerItem()
        titles = response.css('.entry-title::text').extract()
        authors = response.css('.author-name::text').extract()
        dates = response.css('.published::text').extract()
        url = response.request.url
        items['titles'] = titles
        items['authors'] = authors
        items['dates'] = dates
        items['page_Url'] = url
        yield items

    def parse(self, response):
        page_Urls = response.css('.entry-title a').xpath("@href").extract()
        for i in range(len(page_Urls)):
            yield response.follow(page_Urls[i],callback=self.parse_news)

        next_page = 'https://www.truthorfiction.com/page/%27+str(QuoteSpider.page_number)+%27/'
        if QuoteSpider.page_number < 5:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

      #  for i in range(len(titles)):
      #      yield {
      #          'title': titles[i],
      #          'author': authors[i],
      #          'date': dates[i]
      #      }