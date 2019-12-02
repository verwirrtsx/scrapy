# -*- coding: utf-8 -*-
import scrapy
from bz.items import BzItem

class MvbzSpider(scrapy.Spider):
    name = 'mvbz'
    allowed_domains = ['www.win4000.com']
    start_urls = ['http://www.win4000.com/wallpaper_2285_0_0_1.html']

    def parse(self, response):
        urls = response.xpath('//div[@class="tab_box"]/div/ul[@class="clearfix"]/li/a')[0:24]
        imgurls=[]
        for url in urls :
            title = url.xpath('p/text()').extract_first()
            url = url.xpath('@href').extract_first()
            yield scrapy.Request(url,callback=self.detail,meta={'title':title,'imgurls':imgurls})
        next_page1 = response.xpath('//div[@class="pages"]/div/a[@class="next"]/@href').extract_first()
        if next_page1 is not None :
        	yield scrapy.Request(next_page1,callback=self.parse)

    def detail(self,response):
        item = BzItem()
        title  = response.meta['title']
        imgurls  = response.meta['imgurls']
        # if response.meta['title'] is not None:
        #     title  = response.meta['title']
        # else :
        #     title = []
        imgurl = response.xpath('//div[@class="pic-meinv"]/a/img/@src').extract_first()
        print(title)
        # item['title'] = title
        # imgurl =response.xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[1]/div[1]/a/img/@src').extract_frist()
        imgurls.append(imgurl)
        page_num = response.xpath('//div[@class="ptitle"]/em/text()').extract_first()
        in_page = response.xpath('//div[@class="ptitle"]/span/text()').extract_first()

        next_page = response.xpath('//div[@class="pic-next-img"]/a/@href').extract_first()
        if int(page_num) != int(in_page):
            yield scrapy.Request(next_page,callback=self.detail,meta={'title':title,'imgurls':imgurls})
        else:
            item['title'] = title
            item['imgurls'] = imgurls
            yield item
        # imgurl = response.xpath('//div[@class="pic-meinv"]/a/img/@src').extract_first()
        # item['imgurl'] = imgurl
        # yield item

