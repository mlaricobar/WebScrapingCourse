# -*- coding: utf-8 -*-
import scrapy
from mi_primer_spider.items import MiPrimerSpiderItem
from scrapy.loader import ItemLoader

class ExampleSpider(scrapy.Spider):
    name = 'linio_spider_v2'
    allowed_domains = ['linio.com.pe']
    start_urls = ['https://www.linio.com.pe/']

    def parse(self, response):
        for href in response.xpath("//li[@class='nav-item']/a/@href"):
            url_category = "https://www.linio.com.pe" + href.extract()
            yield scrapy.Request(url_category, callback=self.parse_category)

    def parse_category(self, response):
        for href in response.xpath("//div[@id='catalogue-product-container']//div[@class='catalogue-product row']/a/@href"):
            url_product = "https://www.linio.com.pe" + href.extract()
            yield scrapy.Request(url_product, callback=self.parse_product)

        next_page = response.xpath("//nav[@class='pagination-container']//a[@class='page-link page-link-icon']/@href").extract()[-2]
        if next_page is not None:
            next_page_link= response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse_category)

    def parse_product(self, response):

        item = MiPrimerSpiderItem()
        item["title"] = response.xpath("//meta[@itemprop='name']/@content").extract_first()
        item["sku"] = response.xpath("//meta[@itemprop='sku']/@content").extract_first()
        item["price"] = response.xpath("//meta[@itemprop='price']/@content").extract_first()
        item["priceCurrency"] = response.xpath("//meta[@itemprop='priceCurrency']/@content").extract_first()
        item["brand"] = response.xpath("//meta[@itemprop='brand']/@content").extract_first()
        item["model"] = response.xpath("//meta[@itemprop='model']/@content").extract_first()
        item["category"] = response.xpath("//meta[@itemprop='category']/@content").extract_first()
        item["image"] = response.xpath("//meta[@itemprop='image']/@content").extract_first()
        item["availability"] = response.xpath("//meta[@itemprop='availability']/@content").extract_first()
        item["url"] = response.xpath("//meta[@itemprop='url']/@content").extract_first()

        yield item