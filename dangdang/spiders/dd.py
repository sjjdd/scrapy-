# -*- coding: utf-8 -*-
import scrapy
#所有的导入都是从核心目录开始定位
from dangdang.items import DangdangItem
from scrapy.http import Request#这个别忘了
class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4008154.html']

    def parse(self, response):
        #使用item下的目标
        item=DangdangItem()
        item["title"]=response.xpath("//a[@name='itemlist-picture']/@title").extract()
        item["link"]=response.xpath("//a[@name='itemlist-picture']/@href").extract()
        item["comment"]=response.xpath("//a[@name='itemlist-review']/text()").extract()
        # print(item["title"])
        # print(item["link"])
        #每爬一页就将数据提取到pipelines中
        yield item
        #在这里写写入数据库的话也可以，但是效率慢
        for i in range(2,81):
            url="http://category.dangdang.com/pg"+str(i)+"-cid4008154.html"
            yield Request(url,callback=self.parse)

