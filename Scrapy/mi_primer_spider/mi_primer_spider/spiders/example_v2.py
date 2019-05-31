# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'linio_spider_v2'
    allowed_domains = ['linio.com.pe']
    start_urls = ['https://www.linio.com.pe/c/celulares-y-tablets/']
    #start_urls = ["https://www.linio.com.pe/c/celulares-y-tablets?page={0}".format(i) for i in range(1,18)]

    def parse(self, response):
    	product_titles = response.xpath("//div[@id='catalogue-product-container']//div[@class='detail-container']//span[@class='title-section']/text()").extract()
    	img_urls = response.xpath("//div[@id='catalogue-product-container']//div[@class='image-container']//img/@data-lazy").extract()
    	product_prices = response.xpath("//div[@id='catalogue-product-container']//div[@class='detail-container']//span[@class='price-main']/text()").extract()
    	product_discounts = response.xpath("//div[@id='catalogue-product-container']//div[@class='detail-container']//span[@class='discount']/text()").extract()
    	yield {'product_titles': product_titles, 'img_urls': img_urls, 'product_prices': product_prices, 'product_discounts': product_discounts, 'len_products': len(product_titles)}