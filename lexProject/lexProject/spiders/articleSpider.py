import scrapy


class ArticleSpider(scrapy.Spider):
    name = "ArticleSpider"
    start_urls = [
        'https://www.state.gov/r/pa/prs/ps/2018/index.htm'
    ]
    

    def parse(self, response):
        # Individual Statement
        # yield {
        #     'title':response.css('title::text').extract_first(),
        #     'official_name':response.css('span.officials-name::text').extract_first(),
        #     'official_title':response.css('span.officials-title::text').extract_first(),
        #     'date':response.xpath('//div[@id="date_long"]/text()').extract_first(),
        #     'text':response.xpath('//div[@id="centerblock"]').extract_first(),
        # }

        # Links Pages
        for link in response.css('a'):
            yield {
                'link':link.css('a:text').extract_first()
            }