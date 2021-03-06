import scrapy
from ..items import NewscrawlerItem


class QuoteSpider(scrapy.Spider):
    name = 'newsCrawler'
    allowed_domains = ['truthorfiction.com']
    start_urls = ['https://www.truthorfiction.com/page/1/', ]


    def parse_news(self, response):
        items = NewscrawlerItem()
        titles = response.css('.entry-title::text').extract()
        authors = response.css('.author-name::text').extract()
        dates = response.css('.published::text').extract()
        url = response.request.url
        tags = response.css(".rating-description span::text").extract()
        content = response.css(".entry-content p::text").extract()
        cats = response.css('.cat-links a::text').extract()

        # adding to item
        items['titles'] = titles
        items['authors'] = authors
        items['dates'] = dates
        items['page_Url'] = url
        items['tags'] = tags
        items['content'] = content
        items['cats'] = cats

        yield items

    page_number = 2
    def parse(self, response):
        page_Urls = response.css('.entry-title a').xpath("@href").extract()
        for i in range(len(page_Urls)):
            yield response.follow(page_Urls[i], callback=self.parse_news)

        next_page = 'https://www.truthorfiction.com/page/' + str(self.page_number) + '/'
        if self.page_number < 12:
            self.page_number += 1
            yield response.follow(next_page, callback=self.parse)

