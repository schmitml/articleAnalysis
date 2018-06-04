import scrapy
import json

class ArticleSpider(scrapy.Spider):
    name = "ArticleSpider"
    output = []
    start_urls = []
    # with open('test_links.json') as f:
    #     data = json.load(f)
    # for addr in data:
    #     print(addr)
    #     start_urls.append(addr['link'])
    start_urls.append('https://www.state.gov/secretary/20172018tillerson/remarks/2018/01/276814.htm') 
    

    def parse(self, response):
        # Individual Statement
        art = {
            'title':response.css('title::text').extract_first(),
            'official_name':response.css('span.officials-name::text').extract_first(),
            'official_title':response.css('span.officials-title::text').extract_first(),
            'date':response.xpath('//div[@id="date_long"]/text()').extract_first(),
            'text':response.xpath('//div[@id="centerblock"]').extract(),
        }

        # with open('comparison.json','r') as outFile:
        #     json.load(outFile)
        #     for article in outFile: 
        #         print('\n\n\n' + art['title'] + article['title'])
        #         if(art['title'] == article['title']):
        #             print('Already added file\n\n\n\n')
        #             return
        #     print("Added\n\n\n")
        yield {
            'title':response.css('title::text').extract_first(),
            'official_name':response.css('span.officials-name::text').extract_first(),
            'official_title':response.css('span.officials-title::text').extract_first(),
            'date':response.xpath('//div[@id="date_long"]/text()').extract_first(),
            'text':response.xpath('//div[@id="centerblock"]').extract(),
        }

        # with open('comparison.json','w') as outFile:
        #     json.dump(art,outFile,indent=4)
    