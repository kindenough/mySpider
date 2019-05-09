# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
class MyspiderPipeline(object):
    def process_item(self, item, spider):
        print("===db start")
        db = pymysql.Connect(host="localhost", port=3307, user="root", password="usbw", charset="utf8", db="test")
        cursor=db.cursor()
        sql="insert into spider(name,title,info) values(\'{0}\',\'{1}\',\'{2}\')".format(item["name"],item["title"],item["info"])
        print("===db execute start")
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            print("sql ERROR...")
        db.close()
        print("===db end")
        # txt0 = json.dumps(item.__dict__, ensure_ascii=False)
        # open('pipeline.txt', 'a').write(txt0)
        return item
