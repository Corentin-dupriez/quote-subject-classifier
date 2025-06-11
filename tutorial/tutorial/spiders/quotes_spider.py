import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.goodreads.com/quotes?page=1'
    ]

    def parse(self, response: scrapy.http.Response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('div.quoteText::text').get().replace('\n', '').replace('“', '').replace('”', '').strip(),
                'author': quote.css('span.authorOrTitle::text').get().replace('\n', '').replace(',', '').strip(),
                'tags': quote.css('div.greyText a::text').getall(),
            }

        next_page = response.css('a.next_page::attr(href)').get()
        if next_page is not None:
            yield response.follow(url=next_page, callback=self.parse)