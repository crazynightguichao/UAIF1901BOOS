# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BoosspiderPipeline(object):
    def process_item(self, item, spider):
        with open('boos.txt', 'a', encoding="utf-8") as f:
            f.write("%s %s %s %s %s %s %s %s %s" % (item['title'], item['price'],item['address'],item['experience'], item['demand'], item['company'], item['detail'], item['recruiter'],item['job']))
            f.write("\n")
        return item
