# -*- coding: utf-8 -*-
import scrapy


class PortraitSpider(scrapy.Spider):
    name = 'portrait'
    allowed_domains = ['commons.wikimedia.org/wiki/Category:17th-century_oil_portraits_of_standing_women_at_three-quarter_length']
    start_urls = ['http://commons.wikimedia.org/wiki/Category:17th-century_oil_portraits_of_standing_women_at_three-quarter_length/']

    def parse(self, response):
        pass
