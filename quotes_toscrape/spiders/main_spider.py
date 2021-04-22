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
            author = quote.xpath('.//small[@class="author"]/text()').extract_first()
            tags = quote.xpath('.//div[@class="tags"]/a/text()').extract()

            yield {
                'Quote': text,
                'Author': author,
                'Tags': tags
            }
