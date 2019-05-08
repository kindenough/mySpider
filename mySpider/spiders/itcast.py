# -*- coding: utf-8 -*-
import scrapy
import json
from mySpider.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        filename="teacher.html"
        open(filename,'wb').write(response.body)

#/html/body/div[1]/div[5]/div[2]/div[1]/ul/li[1]/div[2]/h3
        context = response.xpath("/html/body/div[1]/div[5]/div[2]/div[1]/ul")
        items=[]
        for each in context:
            item = ItcastItem()
            item['name']=each.xpath("li[1]/div[2]/h3/text()").extract_first()
            item['title']=each.xpath("li[1]/div[2]/h4/text()").extract_first()
            item['info']=each.xpath("li[1]/div[2]/p/text()").extract_first()
            items.append(item.__dict__)

            txt0 = json.dumps(item.__dict__,ensure_ascii=False)
            open('teacher0.txt','a').write(txt0)
            open('teacher0.txt','a').write("\n===\n")


        txt1 = json.dumps(items,ensure_ascii=False)
        txt2 = json.dumps(context.extract(),ensure_ascii=False)
        open('teacher.txt','a').write(txt2)
