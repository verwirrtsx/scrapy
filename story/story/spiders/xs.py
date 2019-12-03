# -*- coding: utf-8 -*-
import scrapy
import pymysql
from story.items import StoryItem
class XsSpider(scrapy.Spider):
    name = 'xs'
    allowed_domains = ['www.xiaoshuo530.com']
    start_urls = ['https://www.xiaoshuo530.com/files/article/info/1/1575.html']

    def parse(self, response):
        story_name = response.xpath('//*[@id="info"]/h1/text()').extract_first()
        author = response.xpath('//*[@id="info"]/p[1]/a/text()').extract_first()
        detail = response.xpath('//*[@id="intro"]/text()').extract_first()
        # print(story_name+author+detail)

        conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',database='story',charset='utf8')
        cursor=conn.cursor()

        inster = "insert into s_name (story_name , author , detail) values('%s','%s','%s');"%(story_name,author,detail)
        cursor.execute(inster)
        cursor.close() #关闭游标
        conn.close() #关闭连接

        urls = response.xpath('//*[@id="list"]/dl/dd/a/@href')[14:-1].extract()
        # print(urls)
        for url in urls:
            url = 'https://www.xiaoshuo530.com'+ url
            yield scrapy.Request(url,callback=self.detail,meta={'title':story_name})

    def detail(self, response):
        item = StoryItem()
        item['title'] = response.meta['title']
        arr = response.xpath('//div[@id="content"]/text()').extract()
        item['content'] =','.join(arr)
        item['chapter'] = response.xpath('//*[@id="main"]/div/div/div[2]/h1/text()').extract_first()
        # print(item)
        yield item
