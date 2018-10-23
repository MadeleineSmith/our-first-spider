# -*- coding: utf-8 -*-
import scrapy                                       


class MainSpiderSpider(scrapy.Spider):                  
    name = 'main_spider'                                
    allowed_domains = ['quotes.toscrape.com']           
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')

        for quote in quotes:
            text = quote.xpath('./span[@class="text"]/text()').extract_first()
            author = quotes.xpath('.//small[@class="author"]/text()').extract_first()
            tags = quote.xpath('.//div[@class="tags"]/a/text()').extract()

            yield {
                'Quote': text,
                'Author': author,
                'Tags': tags
            }

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()   # Store the @href value of the 'next' button
        if next_page_url:                                                               # If next_page_url exists...
            next_page_absolute_url = 'http://quotes.toscrape.com/' + next_page_url                    # Join 'quotes.toscrape.com' and relative path
            yield scrapy.Request(next_page_absolute_url, self.parse)                    # Make a request to the server for the next page
