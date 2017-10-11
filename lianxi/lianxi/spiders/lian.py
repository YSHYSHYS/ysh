# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from lianxi.items import LianxiItem
import re

class LianSpider(scrapy.Spider):
    name = "lian"
    # allowed_domains = ["www.qiushibaike.com/"]
    start_urls = ['https://www.qiushibaike.com/']

    def parse(self, response):
        lists = ['8hr/','hot/','text/','history/']
        for i in lists:
            types_url = 'https://www.qiushibaike.com/'+i
            # print(types_url)
            yield Request(types_url,self.every_page)
    def every_page(self,response):
        # print(response.url)
        max_page = response.xpath('//ul[@class="pagination"]/li[7]/a/span/text()').extract()[0]
        for ii in range(1,int(max_page)+1):
            every_url = response.url+'page/'+str(ii)
            # print(every_url)
            yield Request(every_url,self.every_contents)
    def every_contents(self,response):
        item = LianxiItem()
        demo = re.compile('<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?</div>',re.S)
        author = demo.findall(response.text)
        print(author)
        for authors,contents in author:
            item['authors'] = authors
            item['contents'] = contents
        return item