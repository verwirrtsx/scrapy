# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
class StoryPipeline(object):
    def process_item(self, item, spider):
        # db = pymysql.connect("localhost","root","root","stroy")
        sid = 'id'
        title = item['title']
        content = ','.join(item['content'])
        chapter = item['chapter']
        conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',database='story',charset='utf8')
        cursor=conn.cursor()
        verify = "select %s from s_name where story_name = '%s' ;" %(sid,title)
        # print(verify)
        cursor.execute(verify)
        ret = cursor.fetchone()
        inster = "insert into s_body (chapter,content,sid) values ('%s' ,'%s' ,'%s');" % ( chapter , content, ret[0] )
        cursor.execute(inster)
        cursor.close()
        conn.close() 


    	# cursor = db.cursor()
  #       sql = "INSERT INTO s_body(sid,chapter, content) VALUES ('%d', '%s', '%s' )" %(1,chapter,content)
  #       try:
  # # 执行sql语句
  #           cursor.execute(sql)
  #             # 执行sql语句
  #           db.commit()
  #           print("insert ok")
  #       except:
  # # 发生错误时回滚
  #           db.rollback()
# 关闭数据库连接
    	# sql = "SELECT id FROM s_name WHERE stroy_name = "+title
    	# try:
    	# 	cursor.execute(sql)
    	# 	results = cursor.fetchone()
    	# 	print(results)
    	# except:
    	# 	print('123')
    	# cur = conn.cursor()
    	# conn.close()
    	# sqli="insert into s_body values(%s,%s,%s)"
