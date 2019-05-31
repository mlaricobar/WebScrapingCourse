# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class ExampleSpider(scrapy.Spider):
    name = 'linio_spider_v4'
    allowed_domains = ['linio.com.pe']
    start_urls = ['https://www.linio.com.pe/c/celulares-y-tablets/']
    #start_urls = ["https://www.linio.com.pe/c/celulares-y-tablets?page={0}".format(i) for i in range(1,18)]

    def parse(self, response):
        product_list = response.xpath("//div[@id='catalogue-product-container']//div[@class='catalogue-product row']")#.extract()

        for product_selector in product_list:
            #product_selector = Selector(text=product)
            yield {
            "title": product_selector.xpath(".//span[@class='title-section']/text()").extract_first(),
            "img_url": product_selector.xpath(".//div[@class='image-container']//img/@data-lazy").extract_first(),
            "product_price": product_selector.xpath(".//div[@class='detail-container']//span[@class='price-main']/text()").extract_first(),
            "product_discount": product_selector.xpath(".//div[@class='detail-container']//span[@class='discount']/text()").extract_first()
            }

        next_page = response.xpath("//nav[@class='pagination-container']//a[@class='page-link page-link-icon']/@href").extract()[-2]  #Obtiene la url del paginado
        if next_page is not None:
            next_page_link= response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)