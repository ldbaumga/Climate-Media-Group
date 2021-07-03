import scrapy
from scrapy.http import FormRequest


class QuotesSpider(scrapy.Spider):
    name = "login2"
    start_urls = [
        'https://www.proquest.com/globalnews/index?accountid=13360',
        'https://www.proquest.com/globalnews/index?accountid=13360'
    ]

    def parse(self, response):
        return FormRequest.from_response(response, formdata={
            'username': 'ldbaumga',
            'password': '1519,141666'
            }, callback=self.start_scraping)

    def start_scraping(self, response):
        p = 0
        filename = f'pages{p}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
        p += 1
