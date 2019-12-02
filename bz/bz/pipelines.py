# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import scrapy

class BzPipeline(ImagesPipeline):
    def get_media_requests(self, item, spider):
        title = item['title']
        imgurls = item['imgurls']
        for imgurl in imgurls:
            yield scrapy.Request(imgurl,meta={'item':item})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
            #item['image_paths'] = image_paths
        return item

    def file_path(self, request, response=None, info=None):#自定义存储路径
        item = request.meta['item']  # 通过上面的meta传递过来item
        image_guid = request.url.split('/')[-1]
        filename = u'full/{0}/{1}'.format(item['title'], image_guid)#title为二级目录
        return filename
