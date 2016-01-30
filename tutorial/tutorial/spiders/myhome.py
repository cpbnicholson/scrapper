import re
import scrapy
# from tutorial.items import myhomeItem


class myhomeItem(scrapy.Item):
    price = scrapy.Field()
    size = scrapy.Field()
    ber = scrapy.Field()
    address = scrapy.Field()
    description = scrapy.Field()
    beds = scrapy.Field()
    url = scrapy.Field()


class MyHomeSpider(scrapy.Spider):
    name = "myhome"
    allowed_domains = ["myhome.ie"]
    start_urls = [
        "http://www.myhome.ie/residential/dublin/apartment-for-sale-in-dublin-2?page=1&maxprice=300000&minbeds=1&maxbeds=2&sort=price",
        "http://www.myhome.ie/residential/dublin/apartment-for-sale-in-dublin-2?page=2&maxprice=300000&minbeds=1&maxbeds=2&sort=price",
        "http://www.myhome.ie/residential/dublin/apartment-for-sale-in-dublin-2?page=3&maxprice=300000&minbeds=1&maxbeds=2&sort=price"
    ]

    def parse(self, response):
        x_pages = response.xpath('//*[@id="resultItem"]/div[1]/div[1]/a')

        for page in x_pages:
            url = 'http://www.myhome.ie' + page.xpath('.//@href').extract()[0]
            yield scrapy.Request(url, callback=self.parse_brochure)

    def parse_brochure(self, response):
        itm = myhomeItem()

        itm['address'] = response.css('div.brochureAddress::text').extract()[0].strip()
        description = response.css('h2.brochureDescription > span::text').extract()[0].strip()
        match = re.search('-\s(.+)(\s\d*\sm)', description)
        if match:
            itm['description'] = match.group(1)
            itm['size'] = re.search('\s(\d+)', match.group(2)).group(1)
            itm['beds'] = re.search('(\d)', match.group(1)).group(1)
        price = response.css('div.brochurePrice::text').extract()[0].strip()
        price = price[1:].replace(",", "")
        itm['price'] = price
        itm['url'] = response.url
        itm['ber'] = response.css('#BER').xpath('@alt').extract()[0].strip()
        yield itm
