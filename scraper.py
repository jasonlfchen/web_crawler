import scrapy

class ShoeSpider(scrapy.Spider):
    name = "shoe_spider"
    start_urls = ['https://kithnyc.com/collections/footwear']

    def parse(self, response):
        SET_SELECTOR = '.product-card-info'
        for shoe_spider in response.css(SET_SELECTOR):
            NAME_SELECTOR = '.product-card-title span ::text'
            #ALT_SELECTOR = '.product-card-variant ::text'
            URL_SELECTOR = 'a::attr(href)'
            yield {
                'name': shoe_spider.css(NAME_SELECTOR).extract(),
                #'alt': shoe_spider.css(ALT_SELECTOR).extract(),
                'url': shoe_spider.css(URL_SELECTOR).extract(),
            }
       
        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
