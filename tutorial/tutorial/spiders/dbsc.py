import re
import scrapy

class MyDbscSpider(scrapy.Spider):
    name = "dbsc"
    allowed_domains = ["dbsc.org"]
    start_urls = [
        "http://95.45.235.62/dbsc/Racing/RaceResults.asp?Category=&ClassList=CRUISERS 3 A&RaceId=D31D6050"
        # "http://95.45.235.62/dbsc/Racing/RaceResults.asp?Category=&ClassList=CRUISERS 1&RaceId=D3AB7260",
        # "http://95.45.235.62/dbsc/Racing/RaceResults.asp?Category=&ClassList=CRUISERS%202&RaceId=D3BC9270",
        #"http://95.45.235.62/dbsc/Racing/RaceResults.asp?Category=&ClassList=CRUISERS%202&RaceId=D31C4240"
    ]

    def parse(self, response):
        print '*****'
        # b = response.xpath('//*[@id="RESULT"]//@src').extract()
        rtn = []
        b = response.selector.xpath('//td')
        for each in reversed(b):
            c = each.xpath('text() | a/text()').extract()
            rtn.append(c[0]) if c else rtn.append(None)

        bling = chunks(rtn, 11)

        munks = []
        for i in bling:
            munks.append(i)
            if i[-1] == '1':
                break
        print munks

        rtn = []
        boat_details = []
        for each in reversed(munks):
            rtn.append([each[8], each[6], 'cruisers3'])
            boat_details.append(['cruisers3', str(each[9]), str(each[8]), 'RIYC', str(each[7])])

        print rtn
        print boat_details


class MyDbscOverallSpider(scrapy.Spider):
    name = "dbscoverall"
    allowed_domains = ["dbsc.org"]
    start_urls = [
        "http://95.45.235.62/dbsc/Racing/RaceResults.asp?Category=&ClassList=Overall%20CRUISERS%201&RaceId=D37BXXXX"
        # "http://95.45.235.62/dbsc/Racing/RaceResults.asp?Category=&ClassList=CRUISERS 1&RaceId=D3AB7260",
        # "http://95.45.235.62/dbsc/Racing/RaceResults.asp?Category=&ClassList=CRUISERS%202&RaceId=D3BC9270",
        #"http://95.45.235.62/dbsc/Racing/RaceResults.asp?Category=&ClassList=CRUISERS%202&RaceId=D31C4240"
    ]

    def parse(self, response):
        print '*****'
        # b = response.xpath('//*[@id="RESULT"]//@src').extract()
        rtn = []
        b = response.selector.xpath('//td')
        for each in reversed(b):
            c = each.xpath('text() | a/text()').extract()
            rtn.append(c[0]) if c else rtn.append(None)

        bling = chunks(rtn, 22)

        munks = []
        for i in bling:
            munks.append(i)
            if i[-1] == '1':
                break
        print munks

        rtn = []
        boat_details = []
        for each in reversed(munks):
            rtn.append(list(reversed(each)))

        print rtn



def chunks(l, n):
    """ Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i+n]




