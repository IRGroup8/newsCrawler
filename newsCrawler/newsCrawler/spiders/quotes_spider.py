import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'firstTry'
    start_urls = [
        'https://www.truthorfiction.com/',
    ]

    def _parse(self, response, **kwargs):
        titles = response.css('.entry-title a::text').extract()
        authors = response.css('.author-name::text').extract()
        dates = response.css('.published::text').extract()

        for i in range(len(titles)):
            yield {
                'title': titles[i],
                'author': authors[i],
                'date': dates[i]
            }
