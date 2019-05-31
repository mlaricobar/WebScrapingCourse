# -*- coding: utf-8 -*-
import scrapy

class LinioSpider(scrapy.Spider):
	name = 'linio_spider'
	allowed_domains = ['linio.com.pe']
	start_urls = ['https://www.linio.com.pe/c/celulares-y-tablets/']

	def parse(self, response):
		product_titles = response.xpath("//div[@id='catalogue-product-container']//div[@class='detail-container']//span[@class='title-section']/text()").extract()
		yield {'product_titles': product_titles}