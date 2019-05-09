# -*- coding: utf-8 -*-
import scrapy
import json
from mySpider.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # filename="teacher.html"
        # open(filename,'wb').write(response.body)
        #
        #/html/body/div[1]/div[5]/div[2]/div[1]/ul/li[1]/div[2]/h3
        path0="/html/body/div[1]/div[5]/div[2]/div[1]/ul/li"
        path1 = "/html/body/div[1]/div[5]/div[2]/div"
        context = response.xpath(path1)
        items=[]
        items2=[]
        for divlist in context:
            #print("======")
            #print(divlist)
            eachDiv = divlist.xpath("ul/li")
            for each in eachDiv:
                #print("===")
                #print(each)
                item = ItcastItem()
                item['name']=each.xpath("div[2]/h3/text()").extract_first().strip()
                item['title']=each.xpath("div[2]/h4/text()").extract_first().strip()
                item['info']=each.xpath("div[2]/p/text()").extract_first().strip()
                items.append(item.__dict__)
                items2.append(item)
                yield item
                #print(item)

                txt0 = json.dumps(item.__dict__,ensure_ascii=False)
                try:
                    open('teacher0.txt','a').write(txt0)
                    open('teacher0.txt','a').write("\n")
                except:
                    #print("失败")
                    None
                else:
                    #print('写入成功')
                    None
        txt1 = json.dumps(items,ensure_ascii=False)
        txt2 = json.dumps(context.extract(),ensure_ascii=False)
        #open('teacher.txt','w').write(txt2)
        #yield items2[0]
