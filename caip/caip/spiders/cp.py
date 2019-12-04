# -*- coding: utf-8 -*-
import scrapy
from caip.items import CaipItem

class CpSpider(scrapy.Spider):
    name = 'cp'
    allowed_domains = ['kaijiang.500.com']
    start_urls = ['http://kaijiang.500.com/']

    def parse(self, response):
    # 出球顺序 -  //table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]
    # 期号 -   //*[@id="link2999"]/font/strong
    # 开奖日期 -   //table[1]/tbody/tr[1]/td/span[2]
    # 一等奖  中奖注数-   //table[2]/tbody/tr[3]/td[2]
    # 一等奖  单注奖金（元）-   //table[2]/tbody/tr[3]/td[3]
    # 二等奖  中奖注数-   ///table[2]/tbody/tr[4]/td[2]
    # 二等奖  单注奖金（元）-   //table[2]/tbody/tr[4]/td[3]
    	num =3000
    	while int(num) < 19138:
    		num = int(num) + 1
    		num = str(num).rjust(5,'0')
    		page = 'shtml/ssq/'+num+'.shtml'
    		w_page = self.start_urls[0]+page
    		yield scrapy.Request(w_page,callback=self.work)

    def work(self, response):
    	item = CaipItem()
    	item['res'] = response.xpath('//div[@class="kjxq_box02"]/div[2]/table[1]/tr[2]/td/table/tr[2]/td[2]/text()').extract_first().replace('\r','').replace('\n','').replace('\t','')
    	item['res_s'] = response.xpath('//span[@class="span_left"]/a/font/strong/text()').extract_first()
    	item['res_time'] = response.xpath('//span[@class="span_right"]/text()').extract_first()
    	item['first_prize_num']  = response.xpath('//div[@class="kjxq_box02"]/div[2]/table/tr[3]/td[2]/text()').extract_first().replace('\r','').replace('\n','').replace('\t','')
    	item['first_prize_get']  = response.xpath('//div[@class="kjxq_box02"]/div[2]/table/tr[3]/td[3]/text()').extract_first().replace('\r','').replace('\n','').replace('\t','')
    	item['two_prize_num']  = response.xpath('//div[@class="kjxq_box02"]/div[2]/table/tr[4]/td[2]/text()').extract_first().replace('\r','').replace('\n','').replace('\t','')
    	item['two_prize_get']  = response.xpath('//div[@class="kjxq_box02"]/div[2]/table/tr[4]/td[3]/text()').extract_first().replace('\r','').replace('\n','').replace('\t','')
    	# print(item)
    	yield item