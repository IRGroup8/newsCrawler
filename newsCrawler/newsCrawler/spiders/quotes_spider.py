import scrapy
from ..items import NewscrawlerItem


class QuoteSpider(scrapy.Spider):

    name = 'newsCrawler'
    page_no = 2
    start_urls = ['https://www.politifact.com/article/list/', 'https://www.truthorfiction.com', 'https://www.snopes.com/fact-check/']


    def set_url(self, url, page_no):

        if url == self.start_urls[0]:            # www.politifact.com
            return url + "?page=" + str(page_no)

        elif url == self.start_urls[1]:          # www.truthorfiction.com
            return url + "/page/" + str(page_no) + '/'

        elif url == self.start_urls[1]:          # www.snopes.com
            return url + "page/" + str(page_no) + '/'


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

        next_page = self.set_url(url=self.start_urls[0], page_no=self.page_no)
        if self.page_no < 515:
            self.page_no += 1
            yield response.follow(next_page, callback=self.parse)



      #  for i in range(len(titles)):
      #      yield {
      #          'title': titles[i],
      #          'author': authors[i],
      #          'date': dates[i]
      #      }
