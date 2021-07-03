import scrapy
from scrapy.http import FormRequest


class QuotesSpider(scrapy.Spider):
    name = "login"
    start_urls = [
        'http://quotes.toscrape.com/login',
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={'csrf_token': token,'username': 'adaaa', 'password': 'ADFAF'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        filename = f'pages.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
