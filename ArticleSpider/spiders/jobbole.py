# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobble.com']
    start_urls = ['http://blog.jobbole.com/100327/']

    def parse(self, response):
        re_selector = response.xpath('//*[@id="post-100327"]/div[1]/h1/text()')
        re_selector1 = response.xpath('//*[@id="sidebar"]/h3[1]/a/text()')
        re_selector3 = response.xpath('//*[@class="post-adds"]//span/text()')
        pass
