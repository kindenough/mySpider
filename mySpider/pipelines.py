# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
import traceback
import mySpider.items
class MyspiderPipeline(object):
    def process_item(self, item, spider):

        print("-*-*-*{0},{1}[{2}]".format(type(item)==mySpider.items.newsItem(),
                                          type(mySpider.items.newsItem()),
                                     isinstance(item,mySpider.items.newsItem)))
        db = pymysql.Connect(host="localhost", port=3307, user="root", password="usbw", charset="utf8", db="test")
        cursor=db.cursor()
        sql="insert into spider(name,title,info) values(\'{0}\',\'{1}\',\'{2}\')".format(item["name"],item["title"],item["info"])
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            traceback.print_exc()
            db.rollback()
            print("sql ERROR...")
        db.close()
        # txt0 = json.dumps(item.__dict__, ensure_ascii=False)
        # open('pipeline.txt', 'a').write(txt0)
        return item
    
# CREATE TABLE `spider` (
#  `id` int(11) NOT NULL AUTO_INCREMENT,
#  PRIMARY KEY (`id`),
#  `name` text NOT NULL,
#  `title` text NOT NULL,
#  `info` text NOT NULL
# ) ENGINE=InnoDB AUTO_INCREMENT=288 DEFAULT CHARSET=utf8