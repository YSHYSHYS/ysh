# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class LianxiPipeline(object):
    def __init__(self, mongo_db, mongo_table):
        self.monge_db = mongo_db
        self.monge_table = mongo_table

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_db=crawler.settings.get('MONGO_DB'), mongo_table=crawler.settings.get('MONGO_TABLE'))

    def open_spider(self, spider):
        self.mg = pymongo.MongoClient()[self.monge_db][self.monge_table]

    def process_item(self, item, spider):
        self.mg.insert(dict(item))
        return item

    def close_spider(self, spider):
        self.mg.close()
