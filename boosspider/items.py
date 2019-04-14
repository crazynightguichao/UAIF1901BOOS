# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BoosspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 第一级信息
    category = scrapy.Field()  # 分类
    link = scrapy.Field()  # 分类链接

    # 第二级信息
    title = scrapy.Field()  # 职位
    price = scrapy.Field()  # 薪资
    address = scrapy.Field() # 地址
    experience = scrapy.Field()  # 工作经验
    demand= scrapy.Field()  # 学历要求
    company = scrapy.Field()  # 公司
    detail = scrapy.Field()  # 公司情况
    recruiter = scrapy.Field()  # 招聘人
    job = scrapy.Field()    # 招聘人职位

