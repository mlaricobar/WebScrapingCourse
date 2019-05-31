# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader.processors import MapCompose, TakeFirst


def remove_whitespace(value):
    return value.strip()

def set_prefix_url(value):
    return 'https' + value

def clean_price_value(value):
    return float(re.search(r'S/\s(.+)', value).group(1).replace(",", ""))

def clean_discount_value(value):
    return int(re.search(r'\d+', value).group())



class MiSegundoSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field(
        input_processor = MapCompose(remove_whitespace, set_prefix_url), 
        output_processor=TakeFirst()
        )

    img_url = scrapy.Field(output_processor=TakeFirst())
    product_price = scrapy.Field(input_processor=MapCompose(remove_whitespace, clean_price_value), output_processor=TakeFirst())
    product_discount = scrapy.Field(input_processor=MapCompose(remove_whitespace, clean_discount_value), output_processor=TakeFirst())
    url_pagination = scrapy.Field(output_processor=TakeFirst())
