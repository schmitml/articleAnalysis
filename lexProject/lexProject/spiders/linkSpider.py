import scrapy


class LinkSpider(scrapy.Spider):
    name = "linkSpider"
    start_urls = [
        'https://www.state.gov/r/pa/prs/ps/2018/index.htm'
    ]
    

    def parse(self, response):
        # Links Pages
        for link in response.css('a'):
            yield {
                'link':link.css('a:text').extract_first()
            }