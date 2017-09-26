# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import mysql.connector
db = mysql.connector.connect(host='127.0.0.1',port=3306,user='root',password='root',db='gu')
cursor = db.cursor()
from gupiao.items import *
class GupiaoPipeline(object):
    def process_item(self, item, spider):
        return item
        if isinstance(item,GupiaoItem):
            a=item['a']
            b=item['b']
            c=item['c']
            d=item['d']
            e=item['e']
            f=item['f']
            g=item['g']
            h=item['h']
            sql = "insert into piao(a,b,`c`,d,e,f,g,h) VALUES ('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"','"+g+"','"+h+"')"
            cursor.execute(sql)
        db.commit()
        return item

class MongoPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,ComItem):
            db = pymongo.MongoClient()
            biao = db['gu']['piao']
            biao.insert(dict(item))

        return item
