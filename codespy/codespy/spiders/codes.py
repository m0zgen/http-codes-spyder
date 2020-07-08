import scrapy, csv


class CodesSpider(scrapy.Spider):
    name = 'codes'
    allowed_domains = ['httpstatuses.com']
    start_urls = ['http://httpstatuses.com/']
    base_url = 'http://httpstatuses.com'

    # Custom csv writer
    def __init__(self):
        self.outfile = open("output.csv", "w", newline="")
        self.writer = csv.writer(self.outfile)

    # Parse web data
    def parse(self, response):
        links = response.xpath('//ul/li/a/@href').extract()

        for link in links:
            absolute_url = self.base_url + link
            yield scrapy.Request(absolute_url, callback=self.parse_attr)

    # Bind object items
    def parse_attr(self, response):
        # Custom data to csv
        code = response.xpath('//article/h1/span/text()').extract_first()
        code_class = str(response.xpath('//article/h2/text()').extract())
        code_short_desc = response.xpath('//article/h1/text()').extract_first()
        code_full_desc = response.xpath('//article/p/text()').extract_first()

        code_full_desc = code_full_desc.replace('\n', '')
        self.writer.writerow([code, code_short_desc, code_class, code_full_desc])

    def closed(self,reason):
        self.outfile.close()
        print("***"*20,"closed")