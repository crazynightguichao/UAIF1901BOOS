# -*- coding: utf-8 -*-
import scrapy
from boosspider.items import BoosspiderItem

class BoosSpider(scrapy.Spider):
    name = 'boos'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['http://www.zhipin.com/']

    def parse(self, response):
        categorys = response.xpath("//div[@class='search-hot']/a/text()").extract()
        links = response.xpath("//div[@class='search-hot']/a/@href").extract()
        # print(categorys, links)
        for category,link in zip(categorys,links):
            # 记录  标题 以及 标题链接
            link = 'https://www.zhipin.com'+link+ '&ka=hot-position-1'
            data = {'category': category, 'link': link}
            print(data)
            #请求分类页面
            yield scrapy.Request(link,meta={'data':data},callback=self.getNewList)
    def getNewList(self,response):
        data = response.meta['data']        # 通过meta得到item
        category = data["category"]
        link = data["link"]
        titles = []
        prices = []
        addresss = []
        experiences = []
        demands = []
        companys = []
        details = []
        recruiters = []
        jobs = []
        if category == "Java":
            titles += response.xpath("//div[@class='info-primary']/h3/a/div[@class='job-title']/text()").extract()
            prices += response.xpath("//div[@class='info-primary']/h3/a/span[@class='red']/text()").extract()
            addresss += response.xpath("//div[@class='info-primary']/p/text()[1]").extract()
            experiences += response.xpath("//div[@class='info-primary']/p/text()[2]").extract()
            demands += response.xpath("//div[@class='info-primary']/p/text()[3]").extract()
            companys += response.xpath("//div[@class='info-company']/div[@class='company-text']/h3/a/text()").extract()
            details += response.xpath("//div[@class='info-company']/div[@class='company-text']/p/text()[1]").extract()
            recruiters += response.xpath("//div[@class='info-publis']/h3/text()[1]").extract()
            jobs += response.xpath("//div[@class='info-publis']/h3/text()[2]").extract()
        if category == "PHP":
            titles += response.xpath("//div[@class='info-primary']/h3/a/div[@class='job-title']/text()").extract()
            prices += response.xpath("//div[@class='info-primary']/h3/a/span[@class='red']/text()").extract()
            addresss += response.xpath("//div[@class='info-primary']/p/text()[1]").extract()
            experiences += response.xpath("//div[@class='info-primary']/p/text()[2]").extract()
            demands += response.xpath("//div[@class='info-primary']/p/text()[3]").extract()
            companys += response.xpath("//div[@class='info-company']/div[@class='company-text']/h3/a/text()").extract()
            details += response.xpath("//div[@class='info-company']/div[@class='company-text']/p/text()[1]").extract()
            recruiters += response.xpath("//div[@class='info-publis']/h3/text()[1]").extract()
            jobs += response.xpath("//div[@class='info-publis']/h3/text()[2]").extract()
        if category == "C++":
            titles += response.xpath("//div[@class='info-primary']/h3/a/div[@class='job-title']/text()").extract()
            prices += response.xpath("//div[@class='info-primary']/h3/a/span[@class='red']/text()").extract()
            addresss += response.xpath("//div[@class='info-primary']/p/text()[1]").extract()
            experiences += response.xpath("//div[@class='info-primary']/p/text()[2]").extract()
            demands += response.xpath("//div[@class='info-primary']/p/text()[3]").extract()
            companys += response.xpath("//div[@class='info-company']/div[@class='company-text']/h3/a/text()").extract()
            details += response.xpath("//div[@class='info-company']/div[@class='company-text']/p/text()[1]").extract()
            recruiters += response.xpath("//div[@class='info-publis']/h3/text()[1]").extract()
            jobs += response.xpath("//div[@class='info-publis']/h3/text()[2]").extract()
        if category == "web前端":
            titles += response.xpath("//div[@class='info-primary']/h3/a/div[@class='job-title']/text()").extract()
            prices += response.xpath("//div[@class='info-primary']/h3/a/span[@class='red']/text()").extract()
            addresss += response.xpath("//div[@class='info-primary']/p/text()[1]").extract()
            experiences += response.xpath("//div[@class='info-primary']/p/text()[2]").extract()
            demands += response.xpath("//div[@class='info-primary']/p/text()[3]").extract()
            companys += response.xpath("//div[@class='info-company']/div[@class='company-text']/h3/a/text()").extract()
            details += response.xpath("//div[@class='info-company']/div[@class='company-text']/p/text()[1]").extract()
            recruiters += response.xpath("//div[@class='info-publis']/h3/text()[1]").extract()
            jobs += response.xpath("//div[@class='info-publis']/h3/text()[2]").extract()
        if category == "iOS":
            titles += response.xpath("//div[@class='info-primary']/h3/a/div[@class='job-title']/text()").extract()
            prices += response.xpath("//div[@class='info-primary']/h3/a/span[@class='red']/text()").extract()
            addresss += response.xpath("//div[@class='info-primary']/p/text()[1]").extract()
            experiences += response.xpath("//div[@class='info-primary']/p/text()[2]").extract()
            demands += response.xpath("//div[@class='info-primary']/p/text()[3]").extract()
            companys += response.xpath("//div[@class='info-company']/div[@class='company-text']/h3/a/text()").extract()
            details += response.xpath("//div[@class='info-company']/div[@class='company-text']/p/text()[1]").extract()
            recruiters += response.xpath("//div[@class='info-publis']/h3/text()[1]").extract()
            jobs += response.xpath("//div[@class='info-publis']/h3/text()[2]").extract()
        if category == "Android":
            titles += response.xpath("//div[@class='info-primary']/h3/a/div[@class='job-title']/text()").extract()
            prices += response.xpath("//div[@class='info-primary']/h3/a/span[@class='red']/text()").extract()
            addresss += response.xpath("//div[@class='info-primary']/p/text()[1]").extract()
            experiences += response.xpath("//div[@class='info-primary']/p/text()[2]").extract()
            demands += response.xpath("//div[@class='info-primary']/p/text()[3]").extract()
            companys += response.xpath("//div[@class='info-company']/div[@class='company-text']/h3/a/text()").extract()
            details += response.xpath("//div[@class='info-company']/div[@class='company-text']/p/text()[1]").extract()
            recruiters += response.xpath("//div[@class='info-publis']/h3/text()[1]").extract()
            jobs += response.xpath("//div[@class='info-publis']/h3/text()[2]").extract()
        if category == "产品经理":
            titles += response.xpath("//div[@class='info-primary']/h3/a/div[@class='job-title']/text()").extract()
            prices += response.xpath("//div[@class='info-primary']/h3/a/span[@class='red']/text()").extract()
            addresss += response.xpath("//div[@class='info-primary']/p/text()[1]").extract()
            experiences += response.xpath("//div[@class='info-primary']/p/text()[2]").extract()
            demands += response.xpath("//div[@class='info-primary']/p/text()[3]").extract()
            companys += response.xpath("//div[@class='info-company']/div[@class='company-text']/h3/a/text()").extract()
            details += response.xpath("//div[@class='info-company']/div[@class='company-text']/p/text()[1]").extract()
            recruiters += response.xpath("//div[@class='info-publis']/h3/text()[1]").extract()
            jobs += response.xpath("//div[@class='info-publis']/h3/text()[2]").extract()
        if category == "UI设计师":
            titles += response.xpath("//div[@class='info-primary']/h3/a/div[@class='job-title']/text()").extract()
            prices += response.xpath("//div[@class='info-primary']/h3/a/span[@class='red']/text()").extract()
            addresss += response.xpath("//div[@class='info-primary']/p/text()[1]").extract()
            experiences += response.xpath("//div[@class='info-primary']/p/text()[2]").extract()
            demands += response.xpath("//div[@class='info-primary']/p/text()[3]").extract()
            companys += response.xpath("//div[@class='info-company']/div[@class='company-text']/h3/a/text()").extract()
            details += response.xpath("//div[@class='info-company']/div[@class='company-text']/p/text()[1]").extract()
            recruiters += response.xpath("//div[@class='info-publis']/h3/text()[1]").extract()
            jobs += response.xpath("//div[@class='info-publis']/h3/text()[2]").extract()
        if category == "产品运营":
            titles += response.xpath("//div[@class='info-primary']/h3/a/div[@class='job-title']/text()").extract()
            prices += response.xpath("//div[@class='info-primary']/h3/a/span[@class='red']/text()").extract()
            addresss += response.xpath("//div[@class='info-primary']/p/text()[1]").extract()
            experiences += response.xpath("//div[@class='info-primary']/p/text()[2]").extract()
            demands += response.xpath("//div[@class='info-primary']/p/text()[3]").extract()
            companys += response.xpath("//div[@class='info-company']/div[@class='company-text']/h3/a/text()").extract()
            details += response.xpath("//div[@class='info-company']/div[@class='company-text']/p/text()[1]").extract()
            recruiters += response.xpath("//div[@class='info-publis']/h3/text()[1]").extract()
            jobs += response.xpath("//div[@class='info-publis']/h3/text()[2]").extract()
        if titles and prices and demands and companys and details and recruiters:
            for title,price,address,experience,demand,company,detail,recruiter,job in zip(titles,prices,addresss,experiences,demands,companys,details,recruiters,jobs):
                item = BoosspiderItem()
                item['category'] = category
                item['link'] = link
                item['title'] = title
                item['price'] = price
                item['address'] = address
                item['experience'] = experience
                item['demand'] = demand
                item['company'] = company
                item['detail'] = detail
                item['recruiter'] = recruiter
                item['job'] = job
                yield item


