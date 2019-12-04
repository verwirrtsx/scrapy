# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class CaipPipeline(object):
    def process_item(self, item, spider):
        res = item['res']
        res_s = item['res_s']
        res_time = item['res_time']
        first_prize_num = item['first_prize_num']
        first_prize_get = item['first_prize_get']
        two_prize_num = item['two_prize_num']
        two_prize_get = item['two_prize_get']

        conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',database='lottery',charset='utf8')
        cursor=conn.cursor()
        inster = "insert into heihei (res,res_s,res_time,first_prize_num,first_prize_get,two_prize_num,two_prize_get) values ('%s' ,'%s' ,'%s','%s' ,'%s','%s' ,'%s');" \
         % ( res , res_s, res_time,first_prize_num, first_prize_get,two_prize_num,two_prize_get)
        cursor.execute(inster)
        cursor.close()
        conn.close() 
        return item
