# Article Analysis Tool
#### By Marc Schmitt

## Usage Requirements
* Python 3.6
* Scrapy

## Setup Instructions

## Usage

### Scraping a Website
1. Collect Links and Articles
* Run the following commands:
* `cd lexProject`
* `scrapy crawl LinkSpider -o links.json`
* `scrapy crawl ArticleSpider -o all_articles.json`
2. Filter Collected Articles
* Run the following commands:
* `cd ..`
* `python filter_script.py`
3. Search for Keywords
* Run the following commands:
* `python query_script.py`
* Enter your keyword to search for
* The result of the search will be in the file "<<YOUR KEYWORD>>.csv"