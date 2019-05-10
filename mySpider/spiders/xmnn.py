# -*- coding: utf-8 -*-
import scrapy
import json
import traceback
import datetime

from mySpider.items import newsItem,ItcastItem

class XmnnSpider(scrapy.Spider):
    name = 'xmnn'
    allowed_domains = ['news.xmnn.cn']
    # start_urls = ['http://www.itcast.cn/channel/teacher.shtml']
    start_urls = ['http://news.xmnn.cn/']
    count=1

    def parse(self, response):
        # print("bdnews.html===")
        # filename="bdnews.html"
        # open(filename,'wb').write(response.body)
        print("---")
        try:
            path1 = '//*[@id="xhead"]/div[2]/div/span/p/em/a'
            path2 = "@href"
            path3 = "text()"
            context = response.xpath(path1)
            print(len(context))
            for each in context:
                hrefs = each.xpath(path2)
                text = each.xpath(path3).extract_first()
                print("==={0}".format(self.count))
                print(text)
                print("+++")
                url2=hrefs.extract_first()
                print(url2)
                self.count+=1

                item = newsItem()
                item['name']=text
                item['title']=text
                item['info']=url2
                yield item

                # yield scrapy.Request(url2,self.parse)
                yield scrapy.Request(url="http:"+url2, callback=self.parse2)
        except Exception as e:
            print("=-=-=")
            traceback.print_exc()
    def parse2(self,response):
        # filename="bdnews.html"
        # open(filename,'wb').write(response.body)
        print("{1}.***.{0}".format(datetime.datetime.now(),self.count))
        # print(response.body)
        item = ItcastItem()
        item['name']='a'
        item['title']='b'
        item['info']='c'
        yield item