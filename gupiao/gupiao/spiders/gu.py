# -*- coding: utf-8 -*-
import scrapy
import random
import re
from scrapy.http import Request
from gupiao.items import *
class GuSpider(scrapy.Spider):
    name = "gu"
    start_urls = ['http://www.szse.cn/main/marketdata/jypz/colist/']
    def parse(self, response):
        for i in range(1,3):
            num = random.random()
            begin_url = 'http://www.szse.cn/szseWeb/FrontController.szse?randnum=' + str(num)
            formdate = {
                'ACTIONID': '7',
                'AJAX': 'AJAX - TRUE',
                'CATALOGID': '1110',
                'TABKEY': 'tab1',
                'tab1PAGENO': str(i),
                'tab1PAGECOUNT': '203',
                'tab1RECORDCOUNT': '2029',
                'REPORT_ACTION': 'navigate'

            }
            yield scrapy.FormRequest(
                url= begin_url,
                formdata=formdate,
                callback=self.second,
            )


    def second(self,response):
        demo = response.xpath('//*[@id="REPORTID_tab1"]/tr')[1:]
        items = ComItem()
        for i in demo:
            id = i.xpath('td[1]/a/u/text()').extract_first()
            name = i.xpath('td[2]/a/u/text()').extract_first()
            all_name = i.xpath('td[3]/text()').extract_first()
            type = i.xpath('td[4]/text()').extract_first()
            web = i.xpath('td[5]/text()').extract_first()
            print(id,name)
            items['id'] = id
            items['name'] = name
            items['all_name'] = all_name
            items['type'] = type
            items['web'] = web
            yield items
            formdate = {
                'ACTIONID': '7',
                'CATALOGID': '1815_stock_child',
                    'TABKEY':'tab1',
            'SOURCEURL': '/ szseWeb / FrontController.szse * _QUESTION_ * ACTIONID = 7 * _AND_ * AJAX = AJAX - TRUE * _AND_ * CATALOGID = 1110 * _AND_ * TABKEY = tab1 * _AND_ * tab1PAGENO = 2 * _AND_ * tab1PAGECOUNT = 203 * _AND_ * tab1RECORDCOUNT = 2029',
            'SOURCECATALOGID':'1110',
            'txtDm':id,
            }
            num = random.random()
            begin_url = 'http://www.szse.cn/szseWeb/FrontController.szse?randnum=' + str(num)
            yield scrapy.FormRequest(
                url=begin_url,
                formdata=formdate,
                callback=self.third,
            )

    def third(self,response):
        items = GupiaoItem()
        page = response.xpath('//*[@id="REPORTID_tab1"]/tr/td/text()').extract()
        # print(page)
        yuan = ()
        lists=[]
        listss = []
        for i in range(len(page)):
            n = i+1
            if n%8!=0:
                # print(n)
                lists.append(page[i])
                # print(lists)
            else:
                lists.append(page[i])
                listss.append(lists)
                lists = []
        for a,b,c,d,e,f,g,h in listss:
            items['a'] = a
            items['b'] = b
            items['c'] = c
            items['d'] = d
            items['e'] = e
            items['f'] = f
            items['g'] = g
            items['h'] = h
            yield items







#         print(response.text)
# //*[@id="REPORTID_tab1"]/tbody/tr[2]/td[1]/a/u
# //*[@id="REPORTID_tab1"]/tbody/tr[2]/td[2]/a/u
# //*[@id="REPORTID_tab1"]/tbody/tr[2]/td[3]
# //*[@id="REPORTID_tab1"]/tbody/tr[2]/td[4]
# //*[@id="REPORTID_tab1"]/tbody/tr[2]/td[5]


