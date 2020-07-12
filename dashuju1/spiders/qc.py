# -*- coding: utf-8 -*-
import scrapy
from dashuju1.items import Dashuju1Item


class QcSpider(scrapy.Spider):
    name = 'qc'
    allowed_domains = ['search.51job.com/']
    start_urls = ['https://jobs.51job.com/all/']

    def parse(self, response):
        items = Dashuju1Item()
        es = response.xpath("//div[contains(@class,'gbox')]/div[contains(@class,'e')]")
        for e in es:
            # 岗位名字
            job_name = e.xpath(".//p[@class='info']/span[@class='title']/a[1]/@title").get()
            items['job_name'] = job_name

            # 公司名字
            com_name = e.xpath(".//p[@class='info']/a/@title").get()
            items['com_name'] = com_name

            # 地点
            address = e.xpath(".//p[@class='info']/span[contains(@class,'name')]/text()").get()
            items['address'] = address

            # 薪资
            money = e.xpath(".//p[@class='info']/span[@class='location']/text()").get()
            items['money'] = money

            # 时间
            time = e.xpath(".//p[@class='info']/span[@class='time']/text()").get()
            items['time'] = time

            order = e.xpath(".//p[@class='order']/text()").getall()
            educational = None
            com_nature = None
            experience = None
            com_insize = None
            if len(order) >= 4:
                educational = order[0]  # 学历
                experience = order[1]  # 经验
                com_nature = order[2]  # 公司性质
                com_insize = order[3]  # 公司规模

            items['educational'] = educational
            items['experience'] = experience
            items['com_nature'] = com_nature
            items['com_insize'] = com_insize

            about = str(e.xpath(".//p[@class='text']/@title").get()).strip().replace("\xa0", '') \
                .replace("\n", '')
            # 职责相关
            items['about'] = about

            yield items

        # 下一页
        next_url = response.xpath("//div[@class='p_in']/ul/li[last()]/a/@href").get()
        if next_url:
            yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
