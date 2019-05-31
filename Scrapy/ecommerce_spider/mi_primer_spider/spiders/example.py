# -*- coding: utf-8 -*-
import scrapy
from mi_primer_spider.items import MiPrimerSpiderItem
from scrapy.loader import ItemLoader

class ExampleSpider(scrapy.Spider):
    name = 'linio_spider'
    allowed_domains = ['linio.com.pe']
    start_urls = ['https://www.linio.com.pe/c/celulares-y-tablets/', 'https://www.linio.com.pe/c/tv-audio-y-video', 'https://www.linio.com.pe/c/consolas-y-videojuegos']
    #start_urls = ["https://www.linio.com.pe/c/celulares-y-tablets?page={0}".format(i) for i in range(1,18)]

    def parse(self, response):


    	product_list = response.xpath("//div[@id='catalogue-product-container']//div[@class='catalogue-product row']")#.extract()

    	for product_selector in product_list:
    		#product_selector = Selector(text=product)
    		l = ItemLoader(item=MiPrimerSpiderItem(), selector=product_selector)
    		l.add_xpath("title", ".//span[@class='title-section']/text()")
    		l.add_xpath("img_url", ".//div[@class='image-container']//img/@data-lazy")
    		l.add_xpath("product_price", ".//div[@class='detail-container']//span[@class='price-main']/text()")
    		l.add_xpath("product_discount", ".//div[@class='detail-container']//span[@class='discount']/text()")
    		l.add_value("url_pagination", response.request.url)
    		yield l.load_item()

    	next_page = response.xpath("//nav[@class='pagination-container']//a[@class='page-link page-link-icon']/@href").extract()[-2]
    	if next_page is not None:
    		next_page_link= response.urljoin(next_page)
    		yield scrapy.Request(url=next_page_link, callback=self.parse)

    		#data_list.append(data_row)
    	#yield {"data": data_list}